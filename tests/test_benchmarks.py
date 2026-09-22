import contextlib
import csv
import io
import json
import os
import shlex
import subprocess
import sys
import tempfile
import time
import re
import unittest
from pathlib import Path
from unittest.mock import patch

from experiments.plan.suite import SUITE
from experiments.tracks import DEFAULT_TRACK, TRACKS
from experiments.submit import _find_domain
from core.metrics import COUNTER_LABELS, DURATION_LABELS
from experiments.collect import FIELDS, _preserved_rows, collect
from scripts.utils.reporting import update_result_progress
from experiments.run import (
    DEFAULT_TIMEOUT,
    NO_SYMMETRIES_MESSAGE,
    PROJECT_ROOT,
    _argument_parser as _benchmark_argument_parser,
    _human_status,
    _planner_command,
    _run_pipeline,
    _run_task,
)
import experiments.report
import experiments.submit
from experiments.report import _coverage, _finished_problems, _head_to_head
from experiments.submit import (
    DEFAULT_MEMORY_LIMIT,
    MANIFEST_NAME,
    REQUIRED_ARTIFACTS,
    _argument_parser,
    _benchmark_tasks,
    _check_worktree_is_built,
    _reset_results_dir,
    _write_copperbench_config,
    _write_manifest,
)


class _FakeProcess:
    """One recorded outcome, shaped like the Popen the worker waits on."""

    def __init__(self, command, outcome):
        self.args = command
        # Never a real group: the worker signals this pid on a timeout.
        self.pid = -1
        self.returncode = None
        self.timeouts = []
        self._outcome = outcome

    def communicate(self, timeout=None):
        # The kill path waits a second time, so every wait is recorded.
        self.timeouts.append(timeout)
        outcome = self._outcome
        if isinstance(outcome, BaseException):
            # The worker kills the group and reads what the process had left.
            left = getattr(outcome, "output", "") or ""
            if isinstance(left, bytes):
                left = left.decode()
            self._outcome = subprocess.CompletedProcess(self.args, None, stdout=left)
            raise outcome
        self.returncode = outcome.returncode
        return outcome.stdout, None

    def kill(self):
        pass


@contextlib.contextmanager
def _fake_planner(outcomes):
    """Replace the planner subprocess with recorded outcomes.

    `outcomes` is one CompletedProcess, a sequence of them, or a callable taking
    the command and the spawn arguments. os.killpg goes too, so that the fake
    pid cannot reach a group this test may signal.
    """
    pending = iter(outcomes if isinstance(outcomes, (list, tuple)) else [outcomes])

    def spawn(command, **kwargs):
        try:
            outcome = outcomes(command, **kwargs) if callable(outcomes) else next(pending)
        except BaseException as error:  # noqa: BLE001 - replayed where the worker expects it
            outcome = error
        process = _FakeProcess(command, outcome)
        spawned.append(process)
        return process

    spawned = []
    with patch("experiments.run.subprocess.Popen", side_effect=spawn) as popen, patch("experiments.run.os.killpg"):
        popen.processes = spawned
        yield popen


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

    def test_every_mode_becomes_its_own_row(self):
        """A mode the collector does not know is filed as an abstract result and
        then dropped, silently, because the real abstract result sorts first."""
        with tempfile.TemporaryDirectory() as directory:
            for mode in ("abstract", "concrete", "lama"):
                self._write_result(directory, mode)

            rows = collect(directory)

        self.assertEqual({row["mode"] for row in rows}, {"abstract", "concrete", "lama"})

    def test_the_default_track_runs_the_whole_symmetry_suite_through_the_planner(self):
        track = TRACKS[DEFAULT_TRACK]

        self.assertIs(track.suite.SUITE, SUITE)
        self.assertEqual(track.pipeline, "plan")

    def test_the_run_names_the_partition_every_task_goes_to(self):
        with tempfile.TemporaryDirectory() as directory:
            definition_dir = Path(directory)

            config_file = _write_copperbench_config([], definition_dir=definition_dir, partition="sunnycove")
            config = json.loads(config_file.read_text(encoding="utf-8"))

        self.assertEqual(config["partition"], "sunnycove")

    def test_the_project_root_is_the_repository_root(self):
        """Guards the parents[N] depth, which moving the runner has broken twice."""
        self.assertTrue((PROJECT_ROOT / "pyproject.toml").is_file(), f"{PROJECT_ROOT} is not the repository root")

    def test_cluster_resource_defaults(self):
        args = _argument_parser().parse_args([])

        self.assertEqual(args.timeout, DEFAULT_TIMEOUT)
        self.assertEqual(args.memory_limit, DEFAULT_MEMORY_LIMIT)
        self.assertEqual(args.partition, "sunnycove")

    def test_new_suite_run_removes_previous_results(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "runs"
            old_run = results / "old-run" / "result.json"
            old_run.parent.mkdir(parents=True)
            old_run.write_text("old result\n", encoding="utf-8")

            _reset_results_dir(results)

            self.assertTrue(results.is_dir())
            self.assertEqual(list(results.iterdir()), [])

    def test_a_dry_run_submits_nothing_and_leaves_the_results_alone(self):
        argv = ["submit", "--dry-run", "--domains", "driverlog", "--problems", "p07"]
        with (
            patch("sys.argv", argv),
            patch.object(experiments.submit, "_check_worktree_is_built"),
            patch.object(experiments.submit, "_reset_results_dir") as reset,
            patch.object(experiments.submit, "_write_manifest") as manifest,
            patch.object(experiments.submit, "subprocess") as subprocesses,
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            experiments.submit.main()

        reset.assert_not_called()
        manifest.assert_not_called()
        subprocesses.run.assert_not_called()
        self.assertIn("driverlog", output.getvalue())

    def test_an_unbuilt_worktree_is_refused_before_anything_is_submitted(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(SystemExit) as refusal:
                _check_worktree_is_built(project_root=Path(directory))

        self.assertIn("plasp", str(refusal.exception))

    def test_a_built_worktree_submits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for artifact in REQUIRED_ARTIFACTS:
                path = root / artifact
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()

            _check_worktree_is_built(project_root=root)

    def test_single_benchmark_selects_one_mode(self):
        common = ["--domain-name", "example", "--domain", "domain.pddl", "--problem", "p01.pddl"]

        abstract = _benchmark_argument_parser().parse_args(["abstract", *common])
        concrete = _benchmark_argument_parser().parse_args(["concrete", *common])

        self.assertEqual(abstract.mode, "abstract")
        self.assertEqual(concrete.mode, "concrete")
        self.assertEqual(abstract.timeout, DEFAULT_TIMEOUT)
        self.assertEqual(concrete.timeout, DEFAULT_TIMEOUT)

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
        self.assertIn("experiments.run", worker)
        for placeholder in ("$1", "$2", "$3", "$4", "$timeout"):
            self.assertIn(placeholder, worker)
        self.assertEqual(
            instances,
            [
                f"abstract example {domain.resolve()} {problem.resolve()}",
                f"concrete example {domain.resolve()} {problem.resolve()}",
            ],
        )

    def test_discovers_the_problem_and_its_domain(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            domain = benchmark / "domain.pddl"
            problem = benchmark / "p01.pddl"
            domain.touch()
            problem.touch()

            runnable = {("example", "p01.pddl")}
            self.assertEqual(
                list(_benchmark_tasks(root, ["example"], runnable)), [("abstract", "example", domain, problem)]
            )
            self.assertEqual(
                list(_benchmark_tasks(root, ["example"], runnable, modes=("abstract", "concrete", "lama"))),
                [
                    ("abstract", "example", domain, problem),
                    ("concrete", "example", domain, problem),
                    ("lama", "example", domain, problem),
                ],
            )

    def test_only_problems_with_an_abstraction_class_are_submitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            (benchmark / "p02.pddl").touch()

            tasks = list(_benchmark_tasks(root, ["example"], runnable={("example", "p02.pddl")}))

            self.assertEqual([problem.name for _mode, _name, _domain, problem in tasks], ["p02.pddl"])

    def test_a_subset_run_names_its_domains_and_problems(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for domain_name in ("one", "two"):
                benchmark = root / domain_name
                benchmark.mkdir()
                (benchmark / "domain.pddl").touch()
                (benchmark / "p01.pddl").touch()
                (benchmark / "p02.pddl").touch()
            suite = ["one", "two"]

            by_domain = _benchmark_tasks(root, suite, runnable=None, domains=["two"])
            by_problem = _benchmark_tasks(root, suite, runnable=None, domains=["two"], problems=["p02"])
            by_file_name = _benchmark_tasks(root, suite, runnable=None, problems=["p02.pddl"])

            self.assertEqual({name for _m, name, _d, _p in by_domain}, {"two"})
            self.assertEqual([(n, p.name) for _m, n, _d, p in by_problem], [("two", "p02.pddl")])
            self.assertEqual({p.name for _m, _n, _d, p in by_file_name}, {"p02.pddl"})

    def test_a_misspelled_domain_is_refused_rather_than_submitting_nothing(self):
        with self.assertRaises(SystemExit) as refusal:
            list(_benchmark_tasks(Path("/nowhere"), ["driverlog"], runnable=None, domains=["driverlgo"]))

        self.assertIn("driverlgo", str(refusal.exception))

    def test_only_the_problems_known_unsolvable_are_submitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "example").mkdir()
            names = ("dom01.pddl", "prob01.pddl", "satdom01.pddl", "satprob01.pddl", "unknownprob01.pddl")
            for name in names:
                (root / "example" / name).touch()

            tasks = list(_benchmark_tasks(root, ["example"], runnable=None))

        self.assertEqual([task[3].name for task in tasks], ["prob01.pddl"])

    def test_the_decide_pipeline_runs_the_unsolvability_script(self):
        command = _planner_command(Path("domain.pddl"), Path("problem.pddl"), "abstract", "decide")

        self.assertIn("scripts.unsolvability", command)
        self.assertIn("abstract", command)

    def test_every_problem_runs_when_no_symmetry_class_is_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "example").mkdir()
            (root / "example" / "domain.pddl").touch()
            (root / "example" / "p01.pddl").touch()
            (root / "example" / "p02.pddl").touch()

            tasks = list(_benchmark_tasks(root, ["example"], runnable=None))

        self.assertEqual([task[3].name for task in tasks], ["p01.pddl", "p02.pddl"])

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
                list(_benchmark_tasks(benchmarks, ["example"], {("example", "p01.pddl")})),
                [("abstract", "example", domain, problem)],
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
            "Horizon: 4\nPlan found: yes\n"
            "Metrics:\n"
            "  Durations (seconds):\n"
            "    Total                  1.250000\n"
            "    Abstract plan solving  0.500000\n"
            "  Solver activity:\n"
            "    Refinement decrements  2\n"
            "    Horizon increments     1\n"
            "    Abstract plan length    3\n"
            "    Final horizon          4\n"
            "    Abstract solver calls  1\n"
            "    Concrete solver calls  4\n"
            "Plan:\n  occurs(action(abstract),1)\n  occurs(action(refine),2)\n"
        )
        concrete_output = (
            "Horizon: 6\nPlan found: yes\n"
            "Metrics:\n"
            "  Durations (seconds):\n"
            "    Total                   2.500000\n"
            "    Concrete Fast Downward  1.000000\n"
            "  Solver activity:\n"
            "    Final horizon          6\n"
            "    Concrete solver calls  1\n"
            "Plan:\n  occurs(action(first),1)\n  occurs(action(second),1)\n  occurs(action(third),2)\n"
        )
        completed = [
            subprocess.CompletedProcess([], 0, stdout=abstract_output),
            subprocess.CompletedProcess([], 0, stdout=concrete_output),
        ]
        with tempfile.TemporaryDirectory() as directory, _fake_planner(completed) as run:
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
        self.assertEqual(FIELDS[:4], ("domain", "problem", "mode", "status"))
        for name in (*(f"{name}_seconds" for name in DURATION_LABELS), *COUNTER_LABELS):
            self.assertIn(name, FIELDS)
        self.assertEqual(rows[0]["mode"], "abstract")
        self.assertEqual(rows[0]["status"], "success")
        self.assertEqual(rows[0]["plan_length"], 2)
        self.assertEqual(rows[0]["decrements"], 2)
        self.assertEqual(rows[0]["increments"], 1)
        self.assertEqual(rows[0]["total_seconds"], 1.25)
        self.assertEqual(rows[0]["abstract_solving_seconds"], 0.5)
        self.assertEqual(rows[0]["abstract_plan_length"], 3)
        self.assertEqual(rows[0]["concrete_solve_calls"], 4)
        self.assertEqual(rows[0]["abstracted_object_count"], 2)
        self.assertEqual(rows[0]["abstracted_object_type"], "package")
        self.assertEqual(rows[1]["mode"], "concrete")
        self.assertEqual(rows[1]["status"], "success")
        self.assertEqual(rows[1]["plan_length"], 3)
        self.assertEqual(rows[1]["total_seconds"], 2.5)
        self.assertEqual(rows[1]["concrete_fd_seconds"], 1.0)
        self.assertEqual(rows[1]["abstracted_object_count"], "")
        self.assertEqual(rows[1]["abstracted_object_type"], "")
        self.assertEqual(run.call_count, 2)
        self.assertEqual(
            run.call_args_list[0].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "abstract")
        )
        self.assertEqual(
            run.call_args_list[1].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "concrete")
        )

    def test_worker_preserves_phase_progress_in_the_result(self):
        metrics = {"durations": {"concrete_fd": 2.5}, "counters": {}}

        def complete(command, **_kwargs):
            result_file = Path(_kwargs["env"]["APF_BENCHMARK_RESULT_FILE"])
            running = json.loads(result_file.read_text(encoding="utf-8"))
            self.assertEqual(running["status"], "running")
            self.assertIsNone(running["progress"]["last_completed_phase"])
            update_result_progress(result_file, {"kind": "phase_completed", "phase": "concrete_fd"}, metrics)
            return subprocess.CompletedProcess(command, 2, stdout="planner failed before final metrics\n")

        with tempfile.TemporaryDirectory() as directory, _fake_planner(complete):
            result = _run_task("concrete", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(result["progress"]["last_completed_phase"], "concrete_fd")
        self.assertEqual(result["progress"]["last_update"]["kind"], "phase_completed")
        self.assertEqual(rows[0]["concrete_fd_seconds"], 2.5)
        self.assertEqual(rows[0]["last_completed_phase"], "concrete_fd")

    def test_a_run_the_memory_limit_interrupts_is_recorded_with_its_phase(self):
        metrics = {"durations": {"symmetry_discovery": 1.5}, "counters": {}}

        def interrupt(command, **_kwargs):
            result_file = Path(_kwargs["env"]["APF_BENCHMARK_RESULT_FILE"])
            update_result_progress(result_file, {"kind": "phase_completed", "phase": "symmetry_discovery"}, metrics)
            # runsolver sends SIGINT when the job outgrows its memory limit.
            raise KeyboardInterrupt

        with tempfile.TemporaryDirectory() as directory, _fake_planner(interrupt):
            result = _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(result["status"], "interrupted")
        self.assertEqual(rows[0]["last_completed_phase"], "symmetry_discovery")
        self.assertNotEqual(rows[0]["status"], "running")

    def test_timed_out_run_still_records_the_collapsed_class(self):
        metrics = {
            "durations": {},
            "counters": {},
            "abstraction": {"objects": ["ball1", "ball2", "ball3"], "object_type": "ball"},
        }

        def selected_then_killed(command, **kwargs):
            result_file = Path(kwargs["env"]["APF_BENCHMARK_RESULT_FILE"])
            update_result_progress(result_file, {"kind": "abstraction_selected"}, metrics)
            raise subprocess.TimeoutExpired(command, 10, output="Starting\n")

        with tempfile.TemporaryDirectory() as directory, _fake_planner(selected_then_killed):
            _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=10)
            rows = collect(directory)

        # Nothing the killed run printed reaches the collector, so the class can
        # only come from the result file.
        self.assertEqual(rows[0]["status"], "timed out")
        self.assertEqual(rows[0]["abstracted_object_count"], 3)
        self.assertEqual(rows[0]["abstracted_object_type"], "ball")

    def test_collector_preserves_concise_error_message(self):
        failed = subprocess.CompletedProcess(
            [], 2, stdout="usage: planner.py [-h]\nplanner.py: error: Unsupported quality metric\nStarting\n"
        )
        with tempfile.TemporaryDirectory() as directory, _fake_planner(failed):
            _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(rows[0]["status"], "error (exit code 2)")
        self.assertEqual(rows[0]["error_message"], "Unsupported quality metric")

    def test_collector_reads_an_error_the_planner_capitalized(self):
        # Fast Downward reports its failure, then keeps printing; the message is
        # not the last thing on stdout.
        failed = subprocess.CompletedProcess(
            [],
            2,
            stdout=(
                "Starting\n"
                "Error: Fast Downward (abstract) failed with exit code 31\n"
                "Driver aborting after translate\n"
                "INFO     Planner time: 0.14s\n"
            ),
        )
        with tempfile.TemporaryDirectory() as directory, _fake_planner(failed):
            _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(rows[0]["error_message"], "Fast Downward (abstract) failed with exit code 31")

    def test_each_mode_receives_the_complete_timeout(self):
        timeouts = [
            subprocess.TimeoutExpired([], 1800, output="Starting abstract\n"),
            subprocess.TimeoutExpired([], 1800, output=b"Starting concrete\n"),
        ]
        with tempfile.TemporaryDirectory() as directory, _fake_planner(timeouts) as run:
            abstract = _run_task("abstract", "example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=1800)
            concrete = _run_task("concrete", "example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=1800)

        self.assertTrue(abstract["timed_out"])
        self.assertEqual(abstract["output"], "Starting abstract\n")
        self.assertTrue(concrete["timed_out"])
        self.assertEqual(concrete["output"], "Starting concrete\n")
        self.assertEqual([process.timeouts[0] for process in run.processes], [1800, 1800])

    def test_a_timeout_takes_down_what_the_pipeline_spawned(self):
        # No mocks: what outlives a timeout is the planner's own children, and
        # only a real process tree shows whether they were reaped.
        with tempfile.TemporaryDirectory() as directory:
            survivor = Path(directory) / "survivor.txt"
            outlives_its_parent = f"import time; time.sleep(1.5); open({str(survivor)!r}, 'w').write('alive')"
            spawns_it = (
                f"import subprocess, sys, time;"
                f" subprocess.Popen([sys.executable, '-c', {outlives_its_parent!r}]);"
                f" time.sleep(1.5)"
            )

            result = _run_pipeline([sys.executable, "-c", spawns_it], timeout=0.5)

            self.assertTrue(result["timed_out"])
            time.sleep(2)
            self.assertFalse(survivor.exists(), "a grandchild outlived the timeout")

    def test_benchmark_status_is_human_readable(self):
        self.assertEqual(_human_status({"timed_out": False, "return_code": 0, "output": ""}), "success")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 1, "output": ""}), "no plan found")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 2, "output": ""}), "error (exit code 2)")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 5, "output": ""}), "out of memory")
        self.assertEqual(_human_status({"timed_out": True, "return_code": None, "output": ""}), "timed out")
        self.assertEqual(_human_status({"status": "symmetry_timeout"}), "symmetry timeout")
        self.assertEqual(_human_status({"status": "killed", "signal": 9}), "killed (signal 9)")
        self.assertEqual(_human_status({"status": "running"}), "running")

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
        with _fake_planner(completed):
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
        with tempfile.TemporaryDirectory() as directory, _fake_planner([no_symmetries, concrete_completed]) as run:
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
        self.assertEqual(rows[1]["mode"], "concrete")

    def test_the_manifest_marks_every_mode_that_produced_no_result(self):
        expected_statuses = {
            (): ["missing", "missing"],
            ("abstract",): ["success", "missing"],
            ("abstract", "concrete"): ["success", "success"],
        }
        for completed, statuses in expected_statuses.items():
            with self.subTest(completed=completed), tempfile.TemporaryDirectory() as directory:
                problem = Path("p01.pddl")
                tasks = [
                    ("abstract", "example", Path("domain.pddl"), problem),
                    ("concrete", "example", Path("domain.pddl"), problem),
                ]
                manifest = _write_manifest(tasks, directory)
                for mode in completed:
                    self._write_result(directory, mode)

                rows = collect(directory)

                self.assertEqual(manifest.name, MANIFEST_NAME)
                self.assertEqual([row["mode"] for row in rows], ["abstract", "concrete"])
                self.assertEqual([row["status"] for row in rows], statuses)


class CollectedCsvTests(unittest.TestCase):
    @staticmethod
    def _write_csv(directory, rows):
        path = Path(directory) / "results.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            for domain, problem, mode, status in rows:
                writer.writerow({"domain": domain, "problem": problem, "mode": mode, "status": status})
        return path

    @staticmethod
    def _collected(rows):
        collected = []
        for domain, problem, mode, status in rows:
            collected.append({"domain": domain, "problem": problem, "mode": mode, "status": status})
        return collected

    def test_a_run_without_concrete_results_keeps_the_ones_already_collected(self):
        with tempfile.TemporaryDirectory() as directory:
            csv_file = self._write_csv(directory, [("example", "p01.pddl", "concrete", "success")])
            collected = self._collected([("example", "p01.pddl", "abstract", "success")])

            preserved = _preserved_rows(collected, csv_file)

        self.assertEqual([row["mode"] for row in preserved], ["concrete"])
        self.assertEqual(preserved[0]["status"], "success")

    def test_a_collected_result_replaces_the_one_already_in_the_csv(self):
        rows = [("example", "p01.pddl", "concrete", "success")]
        for status in ("timed out", "missing"):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as directory:
                csv_file = self._write_csv(directory, rows)
                collected = self._collected([("example", "p01.pddl", "concrete", status)])

                preserved = _preserved_rows(collected, csv_file)

                self.assertEqual(preserved, [])

    def test_a_mode_the_run_submitted_does_not_keep_its_old_results(self):
        """Otherwise a problem dropped from the suite would keep reporting the
        result of an encoding that is no longer the one being measured."""
        with tempfile.TemporaryDirectory() as directory:
            csv_file = self._write_csv(directory, [("example", "p01.pddl", "abstract", "success")])
            collected = self._collected([("example", "p02.pddl", "abstract", "success")])

            preserved = _preserved_rows(collected, csv_file)

        self.assertEqual(preserved, [])

    def test_the_modes_the_run_left_alone_keep_their_results(self):
        """A baseline can be measured on its own without erasing the pipelines
        it is there to be compared against."""
        with tempfile.TemporaryDirectory() as directory:
            csv_file = self._write_csv(
                directory,
                [
                    ("example", "p01.pddl", "abstract", "success"),
                    ("example", "p01.pddl", "concrete", "success"),
                    ("example", "p01.pddl", "lama", "timed out"),
                ],
            )
            collected = self._collected([("example", "p01.pddl", "lama", "success")])

            preserved = _preserved_rows(collected, csv_file)

        self.assertEqual({row["mode"] for row in preserved}, {"abstract", "concrete"})

    def test_a_first_run_has_nothing_to_keep(self):
        with tempfile.TemporaryDirectory() as directory:
            preserved = _preserved_rows(self._collected([]), Path(directory) / "results.csv")

        self.assertEqual(preserved, [])


class ReportTests(unittest.TestCase):
    def test_running_the_report_writes_it_beside_the_results(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                for mode in ("abstract", "concrete"):
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {
                            "domain": "example",
                            "problem": "p01.pddl",
                            "mode": mode,
                            "status": "success",
                            "wall_time_seconds": "1.0",
                            "decrements": "0",
                            "increments": "0",
                            "relaxed_deletes": "0",
                        }
                    )

            with patch("sys.argv", ["report", str(results)]), contextlib.redirect_stdout(io.StringIO()):
                experiments.report.main()

            self.assertTrue((Path(directory) / "reports.md").is_file())

    def test_the_report_survives_a_run_with_no_shared_solves(self):
        problems = [
            {
                "abstract": {"status": "timed out", "wall_time_seconds": "1800.0"},
                "concrete": {"status": "success", "wall_time_seconds": "12.0"},
            }
        ]

        _title, lines = _head_to_head(problems, "concrete")

        median = next(line for line in lines if line.startswith("Median runtime"))
        self.assertNotIn(" s", median)

    def test_every_problem_is_accounted_for_in_the_coverage_table(self):
        """The rows have to add up, or a reader cannot tell what became of the
        problems that neither solved nor timed out."""
        modes = ("abstract", "concrete", "lama")
        statuses = (
            ("success", "timed out", "success"),
            ("timed out", "success", "no plan found"),
            ("error (exit code 2)", "interrupted", "success"),
            ("no plan found", "killed (signal 9)", "out of memory"),
        )
        problems = [dict(zip(modes, ({"status": status} for status in row))) for row in statuses]

        _title, lines = _coverage(problems, modes)

        counted = [0] * len(modes)
        for label in ("Plans found", "Timeouts", "Out of memory", "Others"):
            line = next(line for line in lines if line.startswith(label))
            for index, count in enumerate(re.findall(r"(\d+) \(", line)):
                counted[index] += int(count)

        self.assertEqual(counted, [len(problems)] * len(modes))

    def test_a_baseline_is_compared_against_the_abstract_pipeline_alone(self):
        """Intersecting all three would drop the problems one baseline missed out
        of the others' comparison, moving numbers for an unrelated reason."""
        problems = [
            {
                "abstract": {"status": "success", "wall_time_seconds": "1.0"},
                "concrete": {"status": "success", "wall_time_seconds": "2.0"},
                "lama": {"status": "success", "wall_time_seconds": "3.0"},
            },
            {
                "abstract": {"status": "success", "wall_time_seconds": "1.0"},
                "concrete": {"status": "success", "wall_time_seconds": "2.0"},
                "lama": {"status": "timed out", "wall_time_seconds": "1800.0"},
            },
        ]

        _title, concrete = _head_to_head(problems, "concrete")
        _title, lama = _head_to_head(problems, "lama")

        self.assertIn("2", next(line for line in concrete if line.startswith("Plans found by both")))
        self.assertIn("1", next(line for line in lama if line.startswith("Plans found by both")))

    def test_the_report_covers_the_modes_the_results_hold(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                rows = [("p01.pddl", "abstract"), ("p01.pddl", "concrete"), ("p01.pddl", "lama")]
                # p02 never ran the baseline, so no mode can be compared on it.
                rows += [("p02.pddl", "abstract"), ("p02.pddl", "concrete")]
                for problem, mode in rows:
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {"domain": "example", "problem": problem, "mode": mode, "status": "success"}
                    )

            modes, problems, dropped = _finished_problems(results)

        self.assertEqual(modes, ("abstract", "concrete", "lama"))
        self.assertEqual(len(problems), 1)
        self.assertEqual(dropped, 1)


if __name__ == "__main__":
    unittest.main()


class DomainLookupTests(unittest.TestCase):
    def _collection(self, names):
        directory = Path(tempfile.mkdtemp())
        for name in names:
            (directory / name).write_text("", encoding="utf-8")
        return directory

    def test_finds_a_domain_shared_by_every_problem(self):
        directory = self._collection(["domain.pddl", "p01.pddl"])

        self.assertEqual(_find_domain(directory / "p01.pddl").name, "domain.pddl")

    def test_finds_the_domain_numbered_with_the_problem(self):
        directory = self._collection(["dom01.pddl", "prob01.pddl", "dom02.pddl", "prob02.pddl"])

        self.assertEqual(_find_domain(directory / "prob02.pddl").name, "dom02.pddl")

    def test_finds_the_domain_of_a_named_problem_variant(self):
        directory = self._collection(["satdom02.pddl", "satprob02.pddl", "dom02.pddl", "prob02.pddl"])

        self.assertEqual(_find_domain(directory / "satprob02.pddl").name, "satdom02.pddl")

    def test_falls_back_to_the_domain_the_variant_shares_with_its_problem(self):
        directory = self._collection(["dom02.pddl", "prob02.pddl", "satprob02.pddl"])

        self.assertEqual(_find_domain(directory / "satprob02.pddl").name, "dom02.pddl")

    def test_reports_a_problem_with_no_domain(self):
        directory = self._collection(["p01.pddl"])

        with self.assertRaises(FileNotFoundError):
            _find_domain(directory / "p01.pddl")
