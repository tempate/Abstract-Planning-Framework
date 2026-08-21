import os
import subprocess
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import abstract_planner, concrete_planner
from scripts.abstract_planner import _argument_parser as abstract_argument_parser
from scripts.concrete_planner import _argument_parser as concrete_argument_parser

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ShellExampleTests(unittest.TestCase):
    def _run(self, example, workflow=None, python_bin=None):
        environment = os.environ.copy()
        if python_bin is not None:
            environment["PYTHON_BIN"] = python_bin
        command = [f"examples/{example}.sh"]
        if workflow is not None:
            command.append(workflow)
        return subprocess.run(command, cwd=PROJECT_ROOT, env=environment, capture_output=True, text=True, check=False)

    def test_planning_examples_support_domain_selection(self):
        for example in ("concrete", "abstract", "refinement"):
            with self.subTest(example=example):
                result = self._run(example, "--help")

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("[no_mystery|beluga|all]", result.stdout)

    def test_performance_example_supports_domain_selection(self):
        result = self._run("performance", "--help")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[no_mystery|beluga|all]", result.stdout)

    def test_planning_workflows_default_to_beluga(self):
        for example in ("concrete", "abstract", "refinement", "performance"):
            with self.subTest(example=example):
                result = self._run(example, python_bin="/bin/echo")

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("beluga", result.stdout)
                self.assertNotIn("no_mystery", result.stdout)

    def test_abstract_object_example_supports_explicit_and_auto_modes(self):
        result = self._run("abstract_object", "--help")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[explicit|auto|all]", result.stdout)

    def test_abstract_object_auto_command_uses_symmetry_selection(self):
        result = self._run("abstract_object", "auto", "/bin/echo")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("-m scripts.abstract_object", result.stdout)
        self.assertIn("--auto", result.stdout)
        self.assertIn("--bliss-time-limit 300", result.stdout)
        self.assertNotIn("--objects", result.stdout)

    def test_abstract_object_explicit_command_selects_three_hangars(self):
        result = self._run("abstract_object", "explicit", "/bin/echo")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("-m scripts.abstract_object", result.stdout)
        self.assertIn("--objects hangar1 hangar2 hangar3", result.stdout)
        self.assertNotIn("--auto", result.stdout)

    def test_abstract_object_explicit_example_writes_both_pddl_files(self):
        with tempfile.TemporaryDirectory(prefix="apf-abstract-object-") as directory:
            environment = os.environ.copy()
            environment["PYTHON_BIN"] = sys.executable
            environment["APF_TEMP_DIR"] = directory
            result = subprocess.run(
                ["examples/abstract_object.sh", "explicit"],
                cwd=PROJECT_ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

            output = Path(directory, "abstract_object", "explicit")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(Path(output, "domain.pddl").is_file())
            self.assertTrue(Path(output, "problem.pddl").is_file())
            problem_text = Path(output, "problem.pddl").read_text()
            self.assertIn("hangarabs", problem_text)

    def test_no_mystery_performance_uses_the_same_p04_problem(self):
        result = self._run("performance", "no_mystery", "/bin/echo")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("concrete/p04.pddl"), 2)
        self.assertIn("abstract/p04.pddl", result.stdout)
        self.assertEqual(result.stdout.count("--horizon 19"), 2)

    def test_beluga_performance_uses_standard_problem_38(self):
        result = self._run("performance", "beluga", "/bin/echo")

        self.assertEqual(result.returncode, 0, result.stderr)
        problem = "standard/problem_38_s81_j5_r2_oc31_f4.pddl"
        self.assertEqual(result.stdout.count(problem), 2)
        self.assertEqual(result.stdout.count("--horizon 26"), 2)
        self.assertIn("--concrete-objects hangar1 hangar2 hangar3", result.stdout)


class PlannerHelpTests(unittest.TestCase):
    def test_concrete_help_displays_shared_defaults(self):
        help_text = concrete_argument_parser().format_help()

        self.assertIn("ASP encoding type (default: exact)", help_text)
        self.assertIn("time-step based encoding (default: False)", help_text)

    def test_abstract_help_displays_abstract_defaults(self):
        help_text = abstract_argument_parser().format_help()

        self.assertIn("(default: beluga)", help_text)
        self.assertIn("(default: clingo)", help_text)


class PlannerExitStatusTests(unittest.TestCase):
    def test_concrete_cli_returns_failure_when_no_plan_is_found(self):
        parser = Mock()
        parser.parse_args.return_value = Namespace(
            domain="domain.pddl", problem="problem.pddl", horizon=1, encoding="exact", time_step=False
        )
        with (
            patch.object(concrete_planner, "_argument_parser", return_value=parser),
            patch.object(concrete_planner, "compute_concrete_plan", return_value={"success": False}),
            patch.object(concrete_planner, "print_planning_result"),
            patch.object(concrete_planner, "get_logger"),
        ):
            status = concrete_planner.main()

        self.assertEqual(status, 1)

    def test_abstract_cli_returns_failure_when_no_plan_is_found(self):
        parser = Mock()
        parser.parse_args.return_value = Namespace(
            profile="no_mystery",
            abstract_domain="abstract-domain.pddl",
            abstract_problem="abstract-problem.pddl",
            concrete_domain="concrete-domain.pddl",
            concrete_problem="concrete-problem.pddl",
            horizon=1,
            encoding="exact",
            time_step=False,
            abstract_symbol=None,
            concrete_objects=None,
            plan_source="clingo",
        )
        planner = Mock(run_directory="noMystery")
        with (
            patch.object(abstract_planner, "_argument_parser", return_value=parser),
            patch.object(abstract_planner, "get_planner", return_value=planner),
            patch.object(abstract_planner, "compute_abstract_plan", return_value={"success": False}),
            patch.object(abstract_planner, "print_planning_result"),
            patch.object(abstract_planner, "get_logger"),
        ):
            status = abstract_planner.main()

        self.assertEqual(status, 1)


if __name__ == "__main__":
    unittest.main()
