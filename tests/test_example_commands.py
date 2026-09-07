import os
import subprocess
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from scripts import planner
from scripts.planner import _argument_parser
from core.outcomes import UnsolvableTaskError

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _argument_after(command, option):
    """Return the value the echoed example command passed for one option."""
    tokens = command.split()
    return tokens[tokens.index(option) + 1]


class PlannerOutputTests(unittest.TestCase):
    def test_metrics_are_grouped_and_human_readable(self):
        result = {
            "horizon": 5,
            "plan": ["occurs(move,5)"],
            "plan_length": 1,
            "success": True,
            "metrics": {"durations": {"total": 1.25}, "counters": {"decrements": 2, "concrete_solve_calls": 3}},
        }
        output = StringIO()

        with redirect_stdout(output):
            planner.print_planning_result(result)

        text = output.getvalue()
        self.assertIn("Metrics:\n  Durations (seconds):", text)
        self.assertRegex(text, r"(?m)^    Total +1\.250000$")
        self.assertIn("  Solver activity:", text)
        self.assertRegex(text, r"(?m)^    Refinement decrements +2$")
        self.assertNotIn('{"durations"', text)


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

    def test_examples_run_both_modes_on_one_comparable_task(self):
        commands = {}
        for example in ("concrete", "abstract"):
            result = self._run(example, python_bin="/bin/echo")
            self.assertEqual(result.returncode, 0, result.stderr)
            commands[example] = result.stdout

        for example, command in commands.items():
            with self.subTest(example=example):
                self.assertIn(f"-m scripts.planner {example}", command)
                self.assertTrue(_argument_after(command, "--domain").endswith(".pddl"))

        # The README compares the two runs, so they have to solve the same task.
        self.assertEqual(
            _argument_after(commands["concrete"], "--problem"), _argument_after(commands["abstract"], "--problem")
        )
        # The abstract example demonstrates automatic symmetry selection.
        self.assertNotIn("--objects-to-abstract", commands["abstract"])


class PlannerArgumentTests(unittest.TestCase):
    def test_concrete_mode_takes_a_domain_and_a_problem(self):
        args = _argument_parser().parse_args(["concrete", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(args.mode, "concrete")
        self.assertEqual(args.domain, "domain.pddl")
        self.assertEqual(args.problem, "problem.pddl")

    def test_abstract_mode_selects_objects_automatically_by_default(self):
        args = _argument_parser().parse_args(["abstract", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(args.mode, "abstract")
        self.assertIsNone(args.objects_to_abstract)

    def test_abstract_mode_accepts_explicit_objects(self):
        args = _argument_parser().parse_args(
            ["abstract", "--domain", "domain.pddl", "--problem", "problem.pddl", "--objects-to-abstract", "a", "b"]
        )

        self.assertEqual(args.objects_to_abstract, ["a", "b"])


class PlannerExitStatusTests(unittest.TestCase):
    """The exit codes are the benchmark runner's status source, so they are a contract."""

    def _main(self, argv):
        with patch.object(sys, "argv", ["planner", *argv]):
            return planner.main()

    def test_a_detected_unsolvable_task_exits_without_a_traceback(self):
        output = StringIO()
        with patch.object(planner, "_compute", side_effect=UnsolvableTaskError("task is unsolvable")):
            with redirect_stdout(output):
                status = self._main(["concrete", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(status, 1)
        self.assertIn("No plan: task is unsolvable", output.getvalue())
        self.assertNotIn("Traceback", output.getvalue())

    def test_both_modes_report_failure_when_no_plan_is_found(self):
        for mode in ("concrete", "abstract"):
            with self.subTest(mode=mode):
                with (
                    patch.object(planner, "_compute", return_value={"success": False}),
                    patch.object(planner, "print_planning_result"),
                ):
                    status = self._main([mode, "--domain", "domain.pddl", "--problem", "problem.pddl"])

                self.assertEqual(status, 1)

    def test_an_abstraction_error_exits_through_the_parser(self):
        errors = StringIO()
        with patch.object(planner, "_compute", side_effect=planner.AbstractionError("no abstractable object classes")):
            with redirect_stderr(errors), self.assertRaises(SystemExit) as raised:
                self._main(["abstract", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("no abstractable object classes", errors.getvalue())

    def test_explicit_selection_reaches_the_planning_pipeline(self):
        with (
            patch.object(planner, "compute_abstract_plan", return_value={"success": True}) as compute,
            patch.object(planner, "print_planning_result"),
        ):
            status = self._main(
                [
                    "abstract",
                    "--domain",
                    "domain.pddl",
                    "--problem",
                    "problem.pddl",
                    "--objects-to-abstract",
                    "a",
                    "b",
                    "--abstract-name",
                    "combined",
                ]
            )

        config = compute.call_args.args[0]
        self.assertEqual(status, 0)
        self.assertEqual(config.domain_path, "domain.pddl")
        self.assertEqual(config.objects_to_abstract, ("a", "b"))
        self.assertEqual(config.abstract_name, "combined")


if __name__ == "__main__":
    unittest.main()
