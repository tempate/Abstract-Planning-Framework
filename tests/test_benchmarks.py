import json
import os
import shlex
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from benchmarks.suite import NON_SYMMETRIC_DOMAINS, SUITE, SYMMETRIC_DOMAINS
from scripts.collect_benchmarks import FIELDS, collect
from scripts.run_benchmark import (
    DEFAULT_TIMEOUT,
    NO_SYMMETRIES_MESSAGE,
    PROJECT_ROOT,
    _argument_parser as _benchmark_argument_parser,
    _human_status,
    _planner_command,
    _run_pipeline,
    _run_task,
)
from scripts.run_benchmarks import (
    DEFAULT_MEMORY_LIMIT,
    MANIFEST_NAME,
    _argument_parser,
    _benchmark_tasks,
    _reset_results_dir,
    _write_copperbench_config,
    _write_manifest,
)


class BenchmarkTests(unittest.TestCase):
    @staticmethod
    def _write_result(directory, mode, status="success"):
        result = {
            "domain": "example",
            "problem": "p01.pddl",
            "mode": mode,
            "status": status,
            "return_code": 0,
            "timed_out": False,
            "wall_time_seconds": 1.0,
            "output": "Plan found: yes\n",
        }
        path = Path(directory) / "example" / "p01" / f"{mode}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result), encoding="utf-8")

    def test_suite_groups_domains_by_confirmed_symmetries(self):
        self.assertEqual(len(SYMMETRIC_DOMAINS), 26)
        self.assertEqual(len(NON_SYMMETRIC_DOMAINS), 23)
        self.assertEqual(SUITE, SYMMETRIC_DOMAINS + NON_SYMMETRIC_DOMAINS)
        self.assertFalse(set(SYMMETRIC_DOMAINS) & set(NON_SYMMETRIC_DOMAINS))
        self.assertIn("gripper", SYMMETRIC_DOMAINS)
        self.assertIn("blocks", NON_SYMMETRIC_DOMAINS)

    def test_benchmark_runner_defaults_to_symmetric_domains(self):
        self.assertIs(_benchmark_tasks.__defaults__[1], SYMMETRIC_DOMAINS)

    def test_cluster_resource_defaults(self):
        args = _argument_parser().parse_args([])

        self.assertEqual(args.timeout, 30 * 60)
        self.assertEqual(args.memory_limit, 8 * 1024)
        self.assertEqual(args.timeout, DEFAULT_TIMEOUT)
        self.assertEqual(args.memory_limit, DEFAULT_MEMORY_LIMIT)

    def test_new_suite_run_removes_previous_results(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "benchmark-results"
            old_run = results / "old-run" / "result.json"
            old_run.parent.mkdir(parents=True)
            old_run.write_text("old result\n", encoding="utf-8")

            _reset_results_dir(results)

            self.assertTrue(results.is_dir())
            self.assertEqual(list(results.iterdir()), [])

    def test_single_benchmark_selects_one_mode(self):
        common = ["--domain-name", "example", "--domain", "domain.pddl", "--problem", "p01.pddl"]

        abstract = _benchmark_argument_parser().parse_args(["abstract", *common])
        concrete = _benchmark_argument_parser().parse_args(["concrete", *common])

        self.assertEqual(abstract.mode, "abstract")
        self.assertEqual(concrete.mode, "concrete")
        self.assertEqual(abstract.timeout, 30 * 60)
        self.assertEqual(concrete.timeout, 30 * 60)

    def test_prepares_one_copperbench_job_per_mode_and_problem(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            project.mkdir()
            domain = project / "domain.pddl"
            problem = project / "p01.pddl"
            domain.touch()
            problem.touch()
            definition_dir = root / "definition"
            definition_dir.mkdir()

            config_file = _write_copperbench_config(
                [("abstract", "example", domain, problem), ("concrete", "example", domain, problem)],
                definition_dir=definition_dir,
                timeout=1800,
                memory_limit=4096,
                max_parallel_jobs=12,
            )
            config = json.loads(config_file.read_text(encoding="utf-8"))
            worker = shlex.split((definition_dir / "configs.txt").read_text(encoding="utf-8"))
            instances = (definition_dir / "instances.txt").read_text(encoding="utf-8").splitlines()

        self.assertTrue(config["name"].startswith("run-"))
        self.assertEqual(config["timeout"], 1800)
        self.assertEqual(config["mem_limit"], 4096)
        self.assertEqual(config["request_cpus"], 1)
        self.assertNotIn("runs", config)
        self.assertTrue(config["instances_are_parameters"])
        self.assertNotIn("exclusive", config)
        self.assertEqual(config["max_parallel_jobs"], 12)
        self.assertEqual(config["working_dir"], os.path.relpath(PROJECT_ROOT, definition_dir))
        self.assertEqual(
            worker[1:],
            [
                "-m",
                "scripts.run_benchmark",
                "$1",
                "--domain-name",
                "$2",
                "--domain",
                "$3",
                "--problem",
                "$4",
                "--timeout",
                "$timeout",
            ],
        )
        self.assertEqual(
            instances,
            [
                f"abstract example {domain.resolve()} {problem.resolve()}",
                f"concrete example {domain.resolve()} {problem.resolve()}",
            ],
        )

    def test_discovers_both_modes_for_problem_and_its_domain(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            domain = benchmark / "domain.pddl"
            problem = benchmark / "p01.pddl"
            domain.touch()
            problem.touch()

            self.assertEqual(
                list(_benchmark_tasks(root, ["example"])),
                [("abstract", "example", domain, problem), ("concrete", "example", domain, problem)],
            )

    def test_planner_gets_only_the_mode_problem_and_domain(self):
        command = _planner_command(Path("domain.pddl"), Path("problem.pddl"), "abstract")
        concrete_command = _planner_command(Path("domain.pddl"), Path("problem.pddl"), "concrete")

        self.assertEqual(
            command[1:], ["-m", "scripts.planner", "abstract", "--problem", "problem.pddl", "--domain", "domain.pddl"]
        )
        self.assertEqual(
            concrete_command[1:],
            ["-m", "scripts.planner", "concrete", "--problem", "problem.pddl", "--domain", "domain.pddl"],
        )

    def test_existing_result_does_not_exclude_problem_from_new_run(self):
        with tempfile.TemporaryDirectory() as benchmarks, tempfile.TemporaryDirectory() as results:
            benchmark = Path(benchmarks) / "example"
            benchmark.mkdir()
            domain = benchmark / "domain.pddl"
            problem = benchmark / "p01.pddl"
            domain.touch()
            problem.touch()
            result = Path(results) / "example" / "p01" / "abstract.json"
            result.parent.mkdir(parents=True)
            result.touch()

            self.assertEqual(
                list(_benchmark_tasks(benchmarks, ["example"])),
                [("abstract", "example", domain, problem), ("concrete", "example", domain, problem)],
            )

    def test_collector_ignores_copperbench_metadata_next_to_results(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory) / "run-1"
            run_dir.mkdir()
            (run_dir / "metadata.json").write_text('{"instances": {}, "configs": {}}\n', encoding="utf-8")

            self.assertEqual(collect(directory), [])

    def test_separate_mode_runs_are_collected_as_separate_rows(self):
        abstract_output = (
            "Collapsed ['package1', 'package2'] into package_abs (type=package)\n"
            "Horizon: 4\nPlan found: yes\nDecrements: 2\nIncrements: 1\n"
            "Plan:\n  occurs(action(abstract),1)\n  occurs(action(refine),2)\n"
        )
        concrete_output = (
            "Horizon: 6\nPlan found: yes\n"
            "Plan:\n  occurs(action(first),1)\n  occurs(action(second),1)\n  occurs(action(third),2)\n"
        )
        completed = [
            subprocess.CompletedProcess([], 0, stdout=abstract_output),
            subprocess.CompletedProcess([], 0, stdout=concrete_output),
        ]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmark.subprocess.run", side_effect=completed) as run,
        ):
            _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            _run_task("concrete", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)
            abstract = json.loads((Path(directory) / "example" / "p01" / "abstract.json").read_text())
            concrete = json.loads((Path(directory) / "example" / "p01" / "concrete.json").read_text())

        self.assertEqual(abstract["mode"], "abstract")
        self.assertEqual(abstract["status"], "success")
        self.assertEqual(abstract["return_code"], 0)
        self.assertNotIn("concrete", abstract)
        self.assertEqual(concrete["mode"], "concrete")
        self.assertEqual(concrete["return_code"], 0)
        self.assertEqual(len(rows), 2)
        self.assertEqual(
            FIELDS,
            (
                "domain",
                "problem",
                "mode",
                "status",
                "wall_time_seconds",
                "horizon",
                "plan_length",
                "decrements",
                "increments",
                "abstracted_object_count",
                "abstracted_object_type",
                "error_message",
            ),
        )
        self.assertEqual(rows[0]["mode"], "abstract")
        self.assertEqual(rows[0]["status"], "success")
        self.assertEqual(rows[0]["horizon"], 4)
        self.assertEqual(rows[0]["plan_length"], 2)
        self.assertEqual(rows[0]["decrements"], 2)
        self.assertEqual(rows[0]["increments"], 1)
        self.assertEqual(rows[0]["abstracted_object_count"], 2)
        self.assertEqual(rows[0]["abstracted_object_type"], "package")
        self.assertEqual(rows[1]["mode"], "concrete")
        self.assertEqual(rows[1]["status"], "success")
        self.assertEqual(rows[1]["horizon"], 6)
        self.assertEqual(rows[1]["plan_length"], 3)
        self.assertEqual(rows[1]["abstracted_object_count"], "")
        self.assertEqual(rows[1]["abstracted_object_type"], "")
        self.assertEqual(run.call_count, 2)
        self.assertEqual(
            run.call_args_list[0].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "abstract")
        )
        self.assertEqual(
            run.call_args_list[1].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "concrete")
        )

    def test_collector_preserves_concise_error_message(self):
        failed = subprocess.CompletedProcess(
            [], 2, stdout="usage: planner.py [-h]\nplanner.py: error: Unsupported quality metric\nStarting\n"
        )
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmark.subprocess.run", return_value=failed),
        ):
            _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(rows[0]["status"], "error (exit code 2)")
        self.assertEqual(rows[0]["error_message"], "Unsupported quality metric")

    def test_each_mode_receives_the_complete_timeout(self):
        timeouts = [
            subprocess.TimeoutExpired([], 1800, output="Starting abstract\n"),
            subprocess.TimeoutExpired([], 1800, output=b"Starting concrete\n"),
        ]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmark.subprocess.run", side_effect=timeouts) as run,
        ):
            abstract = _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=1800)
            concrete = _run_task("concrete", "example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=1800)

        self.assertTrue(abstract["timed_out"])
        self.assertEqual(abstract["output"], "Starting abstract\n")
        self.assertTrue(concrete["timed_out"])
        self.assertEqual(concrete["output"], "Starting concrete\n")
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args_list[0].kwargs["timeout"], 1800)
        self.assertEqual(run.call_args_list[1].kwargs["timeout"], 1800)

    def test_benchmark_status_is_human_readable(self):
        self.assertEqual(_human_status({"timed_out": False, "return_code": 0, "output": ""}), "success")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 1, "output": ""}), "no plan found")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 2, "output": ""}), "error (exit code 2)")
        self.assertEqual(_human_status({"timed_out": True, "return_code": None, "output": ""}), "timed out")
        self.assertEqual(_human_status({"status": "symmetry_timeout"}), "symmetry timeout")
        self.assertEqual(_human_status({"status": "killed", "signal": 9}), "killed (signal 9)")

    def test_pipeline_records_every_machine_readable_outcome(self):
        completed = [
            subprocess.CompletedProcess([], 0, stdout=""),
            subprocess.CompletedProcess([], 1, stdout=""),
            subprocess.CompletedProcess([], 4, stdout=""),
            subprocess.CompletedProcess([], 3, stdout=""),
            subprocess.CompletedProcess([], -9, stdout=""),
            subprocess.CompletedProcess([], 2, stdout=""),
            subprocess.TimeoutExpired([], 10, output="partial output"),
        ]
        with patch("scripts.run_benchmark.subprocess.run", side_effect=completed):
            results = [_run_pipeline([], 10) for _ in completed]

        self.assertEqual(
            [result["status"] for result in results],
            ["success", "no_plan", "no_symmetries", "symmetry_timeout", "killed", "error", "timed_out"],
        )
        self.assertEqual(results[4]["return_code"], -9)
        self.assertEqual(results[4]["signal"], 9)
        self.assertNotIn("signal", results[5])

    def test_no_symmetries_does_not_prevent_the_separate_concrete_run(self):
        no_symmetries = subprocess.CompletedProcess([], 2, stdout=f"planner.py: error: {NO_SYMMETRIES_MESSAGE}\n")
        concrete_completed = subprocess.CompletedProcess([], 0, stdout="Plan found: yes\n")
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmark.subprocess.run", side_effect=[no_symmetries, concrete_completed]) as run,
        ):
            abstract = _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            concrete = _run_task("concrete", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(_human_status(abstract), "no symmetries")
        self.assertEqual(_human_status(concrete), "success")
        self.assertEqual(rows[0]["status"], "no symmetries")
        self.assertEqual(rows[1]["status"], "success")
        self.assertEqual(run.call_count, 2)

    def test_collector_reads_legacy_combined_result(self):
        legacy = {
            "domain": "example",
            "problem": "p01.pddl",
            "return_code": 0,
            "timed_out": False,
            "wall_time_seconds": 1.0,
            "output": "Horizon: 4\nPlan found: yes\n",
            "concrete": {
                "return_code": 0,
                "timed_out": False,
                "wall_time_seconds": 2.0,
                "output": "Horizon: 6\nPlan found: yes\n",
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            result_file = Path(directory) / "example" / "p01.json"
            result_file.parent.mkdir()
            result_file.write_text(json.dumps(legacy), encoding="utf-8")

            rows = collect(directory)

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["mode"], "abstract")
        self.assertEqual(rows[0]["horizon"], 4)
        self.assertEqual(rows[1]["mode"], "concrete")
        self.assertEqual(rows[1]["horizon"], 6)

    def test_manifest_marks_one_missing_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            problem = Path("p01.pddl")
            tasks = [
                ("abstract", "example", Path("domain.pddl"), problem),
                ("concrete", "example", Path("domain.pddl"), problem),
            ]
            _write_manifest(tasks, directory)
            self._write_result(directory, "abstract")

            rows = collect(directory)

        self.assertEqual(
            [(row["mode"], row["status"]) for row in rows], [("abstract", "success"), ("concrete", "missing")]
        )

    def test_manifest_marks_both_modes_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            problem = Path("p01.pddl")
            tasks = [
                ("abstract", "example", Path("domain.pddl"), problem),
                ("concrete", "example", Path("domain.pddl"), problem),
            ]
            manifest = _write_manifest(tasks, directory)

            rows = collect(directory)

        self.assertEqual(manifest.name, MANIFEST_NAME)
        self.assertEqual([row["status"] for row in rows], ["missing", "missing"])

    def test_complete_manifest_has_no_missing_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            problem = Path("p01.pddl")
            tasks = [
                ("abstract", "example", Path("domain.pddl"), problem),
                ("concrete", "example", Path("domain.pddl"), problem),
            ]
            _write_manifest(tasks, directory)
            self._write_result(directory, "abstract")
            self._write_result(directory, "concrete")

            rows = collect(directory)

        self.assertEqual(len(rows), 2)
        self.assertNotIn("missing", {row["status"] for row in rows})


if __name__ == "__main__":
    unittest.main()
