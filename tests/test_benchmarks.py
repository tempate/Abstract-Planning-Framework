import json
import os
import shlex
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.collect_benchmarks import collect
from scripts.run_benchmark import (
    DEFAULT_TIMEOUT,
    NO_SYMMETRIES_MESSAGE,
    PROJECT_ROOT,
    _argument_parser as _benchmark_argument_parser,
    _human_status,
    _planner_command,
    _run_task,
)
from scripts.run_benchmarks import DEFAULT_MEMORY_LIMIT, _argument_parser, _benchmark_tasks, _write_copperbench_config


class BenchmarkTests(unittest.TestCase):
    def test_cluster_resource_defaults(self):
        args = _argument_parser().parse_args([])

        self.assertEqual(args.timeout, 30 * 60)
        self.assertEqual(args.memory_limit, 8 * 1024)
        self.assertEqual(args.timeout, DEFAULT_TIMEOUT)
        self.assertEqual(args.memory_limit, DEFAULT_MEMORY_LIMIT)

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

    def test_separate_mode_runs_are_collected_as_one_comparison(self):
        abstract_output = "Horizon: 4\nPlan found: yes\nRefinement iterations: 1\nDecrements: 2\nTotal time: 1.250s\n"
        concrete_output = "Horizon: 6\nPlan found: yes\nTotal time: 2.500s\n"
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
        self.assertEqual(abstract["return_code"], 0)
        self.assertNotIn("concrete", abstract)
        self.assertEqual(concrete["mode"], "concrete")
        self.assertEqual(concrete["return_code"], 0)
        self.assertEqual(rows[0]["status"], "success")
        self.assertEqual(rows[0]["horizon"], 4)
        self.assertEqual(rows[0]["decrements"], 2)
        self.assertEqual(rows[0]["planner_time_seconds"], 1.25)
        self.assertEqual(rows[0]["concrete_status"], "success")
        self.assertEqual(rows[0]["concrete_horizon"], 6)
        self.assertEqual(rows[0]["concrete_planner_time_seconds"], 2.5)
        self.assertEqual(run.call_count, 2)
        self.assertEqual(
            run.call_args_list[0].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "abstract")
        )
        self.assertEqual(
            run.call_args_list[1].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "concrete")
        )

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
        self.assertEqual(rows[0]["concrete_status"], "success")
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

        self.assertEqual(rows[0]["horizon"], 4)
        self.assertEqual(rows[0]["concrete_horizon"], 6)


if __name__ == "__main__":
    unittest.main()
