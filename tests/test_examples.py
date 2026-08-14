import os
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from examples import beluga, no_mystery
from examples._runner import print_comparison


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class RunnableExampleTests(unittest.TestCase):
    def _run_help(self, example):
        environment = os.environ.copy()
        environment["PYTHONPATH"] = os.pathsep.join(
            filter(
                None,
                (str(PROJECT_ROOT), environment.get("PYTHONPATH")),
            )
        )
        return subprocess.run(
            [sys.executable, f"examples/{example}.py", "--help"],
            cwd=PROJECT_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_no_mystery_example_supports_direct_file_execution(self):
        result = self._run_help("no_mystery")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "{concrete,abstract,refinement,performance,quick,all}",
            result.stdout,
        )

    def test_beluga_example_supports_direct_file_execution(self):
        result = self._run_help("beluga")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "{concrete,abstract,refinement,performance,quick,all}",
            result.stdout,
        )


class ComparisonExampleTests(unittest.TestCase):
    def test_comparison_output_places_end_to_end_results_side_by_side(self):
        concrete = self._result(total_time=8.0, decrements=None)
        abstract = self._result(total_time=2.0, decrements=3)
        output = StringIO()

        with redirect_stdout(output):
            print_comparison("example", concrete, abstract)

        text = output.getvalue()
        self.assertIn("Concrete", text)
        self.assertIn("Abstraction", text)
        self.assertIn("Refinement decrements", text)
        self.assertIn("8.000s", text)
        self.assertIn("2.000s", text)
        self.assertIn("Abstraction was 4.00x faster", text)

    def test_no_mystery_performance_pair_uses_the_same_p04_problem(self):
        with (
            patch.object(no_mystery, "compute_concrete_plan") as concrete,
            patch.object(no_mystery, "compute_abstract_plan") as abstract,
        ):
            no_mystery.run_performance_concrete()
            no_mystery.run_performance_abstract()

        concrete_arguments = concrete.call_args.kwargs
        abstract_arguments = abstract.call_args.kwargs
        self.assertEqual(
            concrete_arguments["problem_path"],
            abstract_arguments["concrete_problem_path"],
        )
        self.assertEqual(concrete_arguments["horizon"], 19)
        self.assertEqual(abstract_arguments["horizon"], 19)
        self.assertEqual(concrete_arguments["problem_path"].name, "p04.pddl")

    def test_beluga_performance_pair_uses_standard_problem_38(self):
        with (
            patch.object(beluga, "compute_concrete_plan") as concrete,
            patch.object(beluga, "compute_abstract_plan") as abstract,
        ):
            beluga.run_performance_concrete()
            beluga.run_performance_abstract()

        concrete_arguments = concrete.call_args.kwargs
        abstract_arguments = abstract.call_args.kwargs
        self.assertEqual(
            concrete_arguments["problem_path"],
            abstract_arguments["concrete_problem_path"],
        )
        self.assertIn("standard", concrete_arguments["problem_path"].parts)
        self.assertEqual(
            concrete_arguments["problem_path"].name,
            "problem_38_s81_j5_r2_oc31_f4.pddl",
        )
        self.assertEqual(concrete_arguments["horizon"], 26)
        self.assertEqual(abstract_arguments["horizon"], 26)
        self.assertEqual(
            abstract_arguments["concrete_objects"],
            ["hangar1", "hangar2", "hangar3"],
        )

    @staticmethod
    def _result(total_time, decrements):
        return {
            "success": True,
            "horizon": 12,
            "timings": {
                "total_time": total_time,
                "decrements": decrements,
            },
        }


if __name__ == "__main__":
    unittest.main()
