import os
import subprocess
import unittest
from argparse import Namespace
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import planner
from scripts.planner import _argument_parser

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ShellExampleTests(unittest.TestCase):
    def _run(self, example, argument=None, python_bin=None):
        environment = os.environ.copy()
        if python_bin is not None:
            environment["PYTHON_BIN"] = python_bin
        command = [f"examples/{example}.sh"]
        if argument is not None:
            command.append(argument)
        return subprocess.run(command, cwd=PROJECT_ROOT, env=environment, capture_output=True, text=True, check=False)

    def test_examples_support_help(self):
        for example in ("concrete", "abstract"):
            with self.subTest(example=example):
                result = self._run(example, "--help")

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), f"Usage: examples/{example}.sh")

    def test_examples_reject_positional_arguments(self):
        for example in ("concrete", "abstract"):
            with self.subTest(example=example):
                result = self._run(example, "unexpected", "/bin/echo")

                self.assertEqual(result.returncode, 2)
                self.assertIn("Usage:", result.stderr)

    def test_quick_examples_use_gripper_prob01(self):
        for example in ("concrete", "abstract"):
            with self.subTest(example=example):
                result = self._run(example, python_bin="/bin/echo")

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.count("lib/downward-benchmarks/gripper/domain.pddl"), 1)
                self.assertEqual(result.stdout.count("gripper/prob01.pddl"), 1)
                self.assertEqual(result.stdout.count("--horizon 11"), 1)

    def test_abstract_examples_use_automatic_symmetry_selection(self):
        result = self._run("abstract", python_bin="/bin/echo")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("-m scripts.planner abstract", result.stdout)
        self.assertIn("--abstract-name ball_abs", result.stdout)
        self.assertNotIn("--symmetry-time-limit", result.stdout)
        self.assertNotIn("--objects-to-abstract", result.stdout)


class PlannerHelpTests(unittest.TestCase):
    def _help(self, mode):
        output = StringIO()
        with self.assertRaises(SystemExit), redirect_stdout(output):
            _argument_parser().parse_args([mode, "--help"])
        return output.getvalue()

    def test_top_level_help_lists_both_planning_modes(self):
        help_text = _argument_parser().format_help()

        self.assertIn("concrete", help_text)
        self.assertIn("abstract", help_text)

    def test_concrete_help_displays_shared_defaults(self):
        help_text = self._help("concrete")

        self.assertIn("ASP encoding type (default: bounded)", help_text)
        self.assertIn("time-step based encoding (default: False)", help_text)

    def test_abstract_help_displays_abstract_defaults(self):
        help_text = self._help("abstract")

        self.assertIn("(default: clingo)", help_text)

    def test_abstract_mode_accepts_one_concrete_task_for_automatic_abstraction(self):
        args = _argument_parser().parse_args(["abstract", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(args.domain, "domain.pddl")
        self.assertEqual(args.problem, "problem.pddl")
        self.assertIsNone(args.objects_to_abstract)

    def test_abstract_mode_accepts_explicit_objects(self):
        args = _argument_parser().parse_args(
            ["abstract", "--domain", "domain.pddl", "--problem", "problem.pddl", "--objects-to-abstract", "a", "b"]
        )

        self.assertEqual(args.objects_to_abstract, ["a", "b"])


class PlannerExitStatusTests(unittest.TestCase):
    def test_concrete_cli_returns_failure_when_no_plan_is_found(self):
        parser = Mock()
        parser.parse_args.return_value = Namespace(
            mode="concrete",
            domain="domain.pddl",
            problem="problem.pddl",
            horizon=1,
            encoding="bounded",
            time_step=False,
        )
        with (
            patch.object(planner, "_argument_parser", return_value=parser),
            patch.object(planner, "compute_concrete_plan", return_value={"success": False}),
            patch.object(planner, "print_planning_result"),
            patch.object(planner, "get_logger"),
        ):
            status = planner.main()

        self.assertEqual(status, 1)

    def test_abstract_cli_returns_failure_when_no_plan_is_found(self):
        parser = Mock()
        parser.parse_args.return_value = Namespace(
            mode="abstract",
            domain="domain.pddl",
            problem="problem.pddl",
            horizon=1,
            encoding="bounded",
            time_step=False,
            abstract_name=None,
            objects_to_abstract=None,
            symmetry_time_limit=300,
            plan_source="clingo",
        )
        with (
            patch.object(planner, "_argument_parser", return_value=parser),
            patch.object(planner, "compute_abstract_plan", return_value={"success": False}),
            patch.object(planner, "print_planning_result"),
            patch.object(planner, "get_logger"),
        ):
            status = planner.main()

        self.assertEqual(status, 1)

    def test_abstract_cli_reports_concrete_fallback(self):
        parser = Mock()
        parser.parse_args.return_value = Namespace(
            mode="abstract",
            domain="domain.pddl",
            problem="problem.pddl",
            horizon=1,
            encoding="bounded",
            time_step=False,
            abstract_name=None,
            objects_to_abstract=None,
            symmetry_time_limit=300,
            plan_source="clingo",
        )
        result = {
            "success": True,
            "fallback": {"mode": "concrete", "reason": "PDDL Symmetries found no abstractable object classes"},
        }
        output = StringIO()
        with (
            patch.object(planner, "_argument_parser", return_value=parser),
            patch.object(planner, "compute_abstract_plan", return_value=result),
            patch.object(planner, "print_planning_result"),
            patch.object(planner, "get_logger"),
            redirect_stdout(output),
        ):
            status = planner.main()

        self.assertEqual(status, 0)
        self.assertIn("No symmetry class found; used the concrete pipeline", output.getvalue())

    def test_abstract_cli_passes_explicit_selection_to_the_planning_pipeline(self):
        parser = Mock()
        parser.parse_args.return_value = Namespace(
            mode="abstract",
            domain="domain.pddl",
            problem="problem.pddl",
            horizon=4,
            encoding="bounded",
            time_step=False,
            abstract_name="combined",
            objects_to_abstract=["a", "b"],
            symmetry_time_limit=17,
            plan_source="clingo",
        )
        output = StringIO()
        with (
            patch.object(planner, "_argument_parser", return_value=parser),
            patch.object(
                planner,
                "compute_abstract_plan",
                return_value={
                    "success": True,
                    "abstraction": {
                        "objects_to_abstract": ["b", "a"],
                        "abstract_symbol": "combined",
                        "object_type": "item",
                    },
                },
            ) as compute,
            patch.object(planner, "print_planning_result"),
            patch.object(planner, "get_logger"),
            redirect_stdout(output),
        ):
            status = planner.main()

        self.assertEqual(status, 0)
        config = compute.call_args.args[0]
        self.assertEqual(config.domain_path, "domain.pddl")
        self.assertEqual(config.problem_path, "problem.pddl")
        self.assertEqual(config.objects_to_abstract, ("a", "b"))
        self.assertEqual(config.abstract_name, "combined")
        self.assertEqual(config.symmetry_time_limit, 17)
        self.assertIn("Collapsed ['a', 'b'] into combined", output.getvalue())


if __name__ == "__main__":
    unittest.main()
