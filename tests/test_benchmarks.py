import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.collect_benchmarks import collect
from scripts.run_benchmarks import (
    NO_SYMMETRIES_MESSAGE,
    _argument_parser,
    _benchmark_tasks,
    _human_status,
    _planner_command,
    _run_task,
)


class BenchmarkTests(unittest.TestCase):
    def test_default_timeout_is_one_minute(self):
        self.assertEqual(_argument_parser().parse_args([]).timeout, 60)

    def test_discovers_problem_and_its_domain(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            domain = benchmark / "domain.pddl"
            problem = benchmark / "p01.pddl"
            domain.touch()
            problem.touch()

            self.assertEqual(list(_benchmark_tasks(root, ["example"])), [("example", domain, problem)])

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

    def test_existing_result_is_not_returned_as_a_task(self):
        with tempfile.TemporaryDirectory() as benchmarks, tempfile.TemporaryDirectory() as results:
            benchmark = Path(benchmarks) / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            result = Path(results) / "example" / "p01.json"
            result.parent.mkdir()
            result.touch()

            self.assertEqual(list(_benchmark_tasks(benchmarks, ["example"], results)), [])

    def test_run_and_collect(self):
        abstract_output = "Horizon: 4\nPlan found: yes\nRefinement iterations: 1\nDecrements: 2\nTotal time: 1.250s\n"
        concrete_output = "Horizon: 6\nPlan found: yes\nTotal time: 2.500s\n"
        completed = [
            subprocess.CompletedProcess([], 0, stdout=abstract_output),
            subprocess.CompletedProcess([], 0, stdout=concrete_output),
        ]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmarks.subprocess.run", side_effect=completed) as run,
        ):
            _run_task("example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)
            stored = json.loads((Path(directory) / "example" / "p01.json").read_text())

        self.assertEqual(stored["return_code"], 0)
        self.assertNotIn("status", stored)
        self.assertEqual(rows[0]["status"], "success")
        self.assertEqual(rows[0]["horizon"], 4)
        self.assertEqual(rows[0]["decrements"], 2)
        self.assertEqual(rows[0]["planner_time_seconds"], 1.25)
        self.assertEqual(stored["concrete"]["return_code"], 0)
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

    def test_abstract_timeout_is_recorded_and_concrete_comparison_still_runs(self):
        timeout = subprocess.TimeoutExpired([], 30, output="Starting\n")
        completed = subprocess.CompletedProcess([], 0, stdout="Plan found: yes\n")
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmarks.subprocess.run", side_effect=[timeout, completed]) as run,
        ):
            result = _run_task("example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=30)

        self.assertTrue(result["timed_out"])
        self.assertIsNone(result["return_code"])
        self.assertEqual(result["concrete"]["return_code"], 0)
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args_list[0].kwargs["timeout"], 30)
        self.assertEqual(
            run.call_args_list[0].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "abstract")
        )
        self.assertEqual(
            run.call_args_list[1].args[0], _planner_command(Path("domain.pddl"), Path("p01.pddl"), "concrete")
        )

    def test_benchmark_status_is_human_readable(self):
        self.assertEqual(_human_status({"timed_out": False, "return_code": 0, "output": ""}), "success")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 1, "output": ""}), "no plan found")
        self.assertEqual(_human_status({"timed_out": False, "return_code": 2, "output": ""}), "error (exit code 2)")
        self.assertEqual(_human_status({"timed_out": True, "return_code": None, "output": ""}), "timed out")

    def test_no_symmetries_is_its_own_run_and_collection_category(self):
        completed = subprocess.CompletedProcess([], 2, stdout=f"planner.py: error: {NO_SYMMETRIES_MESSAGE}\n")
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmarks.subprocess.run", return_value=completed) as run,
        ):
            result = _run_task("example", Path("domain.pddl"), Path("p01.pddl"), directory)
            rows = collect(directory)

        self.assertEqual(_human_status(result), "no symmetries")
        self.assertEqual(rows[0]["status"], "no symmetries")
        self.assertEqual(rows[0]["concrete_status"], "")
        self.assertNotIn("concrete", result)
        run.assert_called_once()

    def test_no_plan_from_abstract_pipeline_still_runs_concrete_comparison(self):
        completed = [
            subprocess.CompletedProcess([], 1, stdout="Plan found: no\n"),
            subprocess.CompletedProcess([], 0, stdout="Plan found: yes\n"),
        ]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmarks.subprocess.run", side_effect=completed) as run,
        ):
            result = _run_task("example", Path("domain.pddl"), Path("p01.pddl"), directory)

        self.assertEqual(_human_status(result), "no plan found")
        self.assertEqual(_human_status(result["concrete"]), "success")
        self.assertEqual(run.call_count, 2)

    def test_abstract_error_still_runs_concrete_comparison(self):
        completed = subprocess.CompletedProcess([], 2, stdout="planner.py: error: invalid task\n")
        concrete = subprocess.CompletedProcess([], 0, stdout="Plan found: yes\n")
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmarks.subprocess.run", side_effect=[completed, concrete]) as run,
        ):
            result = _run_task("example", Path("domain.pddl"), Path("p01.pddl"), directory)

        self.assertEqual(result["concrete"]["return_code"], 0)
        self.assertEqual(run.call_count, 2)

    def test_each_pipeline_receives_the_full_timeout(self):
        completed = subprocess.CompletedProcess([], 0, stdout="Plan found: yes\n")
        concrete_timeout = subprocess.TimeoutExpired([], 30, output=b"Starting concrete\n")
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("scripts.run_benchmarks.subprocess.run", side_effect=[completed, concrete_timeout]) as run,
        ):
            result = _run_task("example", Path("domain.pddl"), Path("p01.pddl"), directory, timeout=30)

        self.assertTrue(result["concrete"]["timed_out"])
        self.assertEqual(result["concrete"]["output"], "Starting concrete\n")
        self.assertEqual([call.kwargs["timeout"] for call in run.call_args_list], [30, 30])


if __name__ == "__main__":
    unittest.main()
