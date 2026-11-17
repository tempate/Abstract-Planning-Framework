import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from unittest.mock import patch

from core.pipeline import pipeline
from scripts import planner
from core.pipeline.abstraction.collapse import AbstractionError
from core.utilities.metrics import COUNTER_LABELS, DURATION_LABELS
from core.utilities.outcomes import STATUS_BY_EXIT_CODE, UnsolvableTaskError
from core.utilities.plan import PlanAction
from experiments.collect import _values


class PlannerOutputTests(unittest.TestCase):
    def test_every_metric_the_planner_prints_is_collected(self):
        """The collector reads the printed metrics, so the two must agree on the format."""
        metrics = {
            "durations": {name: 0.25 for name in DURATION_LABELS},
            "counters": {name: 3 for name in COUNTER_LABELS},
            "abstraction": {"objects": ["a", "b"], "object_type": "item"},
        }
        output = StringIO()
        with redirect_stdout(output):
            planner.print_planning_result({"plan": (PlanAction("move", (), 1),), "success": True, "metrics": metrics})

        values = _values({"status": "success", "wall_time_seconds": 1.0, "output": output.getvalue()})

        for name in DURATION_LABELS:
            self.assertEqual(values[f"{name}_seconds"], 0.25, name)
        for name in COUNTER_LABELS:
            self.assertEqual(values[name], 3, name)


class PlannerExitStatusTests(unittest.TestCase):
    """The exit codes are the benchmark runner's status source, so they are a contract."""

    def _main(self, argv):
        with patch.object(sys, "argv", ["planner", *argv]):
            return planner.main()

    def test_a_detected_unsolvable_task_exits_without_a_traceback(self):
        output = StringIO()
        with patch.object(planner, "_compute", side_effect=UnsolvableTaskError("task is unsolvable")):
            with redirect_stdout(output):
                status = self._main(["asp", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(status, 1)
        self.assertIn("No plan: task is unsolvable", output.getvalue())
        self.assertNotIn("Traceback", output.getvalue())

    def test_a_crash_is_an_error_rather_than_a_task_without_a_plan(self):
        output = StringIO()
        with patch.object(planner, "_compute", side_effect=KeyError("plan")):
            with redirect_stdout(output):
                status = self._main(["asp", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(STATUS_BY_EXIT_CODE[status], "error")
        self.assertIn("KeyError", output.getvalue())

    def test_both_modes_report_failure_when_no_plan_is_found(self):
        for mode in ("asp", "abs-asp"):
            with self.subTest(mode=mode):
                with (
                    patch.object(planner, "_compute", return_value={"success": False}),
                    patch.object(planner, "print_planning_result"),
                ):
                    status = self._main([mode, "--domain", "domain.pddl", "--problem", "problem.pddl"])

                self.assertEqual(status, 1)

    def test_an_abstraction_error_exits_through_the_parser(self):
        errors = StringIO()
        with patch.object(planner, "_compute", side_effect=AbstractionError("no abstractable object classes")):
            with redirect_stderr(errors), self.assertRaises(SystemExit) as raised:
                self._main(["abs-asp", "--domain", "domain.pddl", "--problem", "problem.pddl"])

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("no abstractable object classes", errors.getvalue())

    def test_explicit_selection_reaches_the_planning_pipeline(self):
        with (
            patch.object(pipeline, "solve", return_value={"success": True}) as compute,
            patch.object(planner, "print_planning_result"),
        ):
            status = self._main(
                [
                    "abs-asp",
                    "--domain",
                    "domain.pddl",
                    "--problem",
                    "problem.pddl",
                    "--objects-to-abstract",
                    "a",
                    "b",
                ]
            )

        config = compute.call_args.args[0]
        self.assertEqual(status, 0)
        self.assertEqual(config.domain_path, "domain.pddl")
        self.assertEqual(config.objects_to_abstract, ("a", "b"))

    def test_the_planner_passes_the_abstraction_source_on(self):
        argv = ["planner", "abs-lama", "--domain", "d.pddl", "--problem", "p.pddl", "--abstraction-source", "resources"]
        with (
            patch.object(pipeline, "solve", return_value={"success": True}) as compute,
            patch.object(planner, "print_planning_result"),
            patch.object(sys, "argv", argv),
        ):
            planner.main()

        self.assertEqual(compute.call_args.args[0].abstraction_source, "resources")


if __name__ == "__main__":
    unittest.main()
