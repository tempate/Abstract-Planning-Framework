import logging
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from core.abstraction.model import Abstraction
from core.planning.abstract import _select_abstract_horizon
from core.planning.config import AbstractPlanningConfig
from core.planning.plan import PlanAction
from core.planning.refinement import RefinementContext, read_fast_downward_plan, refine


class AbstractPlanningHelperTests(unittest.TestCase):
    def test_auto_horizon_uses_the_abstract_plan_length(self):
        self.assertEqual(_select_abstract_horizon(None, 6, "clingo"), 6)
        self.assertEqual(_select_abstract_horizon(None, 6, "fd"), 6)

    def test_explicit_clingo_horizon_can_be_shorter_than_fd_plan(self):
        self.assertEqual(_select_abstract_horizon(2, 6, "clingo"), 2)

    def test_fd_source_rejects_a_plan_that_exceeds_the_horizon(self):
        with self.assertRaisesRegex(ValueError, "plan length 6"):
            _select_abstract_horizon(5, 6, "fd")


class RefinementTests(unittest.TestCase):
    def _context(self, **changes):
        values = {
            "config": AbstractPlanningConfig("domain.pddl", "problem.pddl"),
            "abstraction": Abstraction("item_abs", ("a", "b"), "item"),
            "concrete_asp": "concrete asp",
            "abstract_asp": "abstract asp",
            "abstract_task": {"planFile": "sas_plan"},
            "horizon": 3,
            "fd_timings": {"fd_concrete_time": 1.0, "fd_abstract_time": 2.0, "fd_total_time": 3.0},
            "concrete_asp_time": 4.0,
            "abstract_asp_time": 5.0,
            "asp_total_time": 9.0,
            "total_timing": SimpleNamespace(elapsed=12.0),
            "run_id": "run-123",
            "logger": Mock(spec=logging.Logger),
        }
        values.update(changes)
        return RefinementContext(**values)

    @patch("core.planning.refinement.build_mapping")
    @patch("core.planning.refinement.run_clingo", return_value=None)
    def test_clingo_stops_when_no_abstract_plan_exists(self, run_clingo, build_mapping):
        context = self._context()

        result = refine(context)

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 0)
        run_clingo.assert_called_once_with("abstract asp", 3)
        build_mapping.assert_not_called()

    @patch("core.planning.refinement.solve_decrementally", return_value=(True, ["occurs(concrete,1)"], 2))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=(PlanAction("move", ("item_abs",), 1),))
    @patch("core.planning.refinement.run_clingo", return_value=["occurs(abstract,1)"])
    def test_clingo_maps_the_abstract_plan_and_reports_decrements(
        self, run_clingo, parse_plan_actions, build_mapping, solve_decrementally
    ):
        context = self._context()

        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,1)"])
        self.assertEqual(result["timings"]["decrements"], 2)
        run_clingo.assert_called_once_with("abstract asp", 3)
        parse_plan_actions.assert_called_once_with(["occurs(abstract,1)"])
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)

    @patch("core.planning.refinement.solve_decrementally", return_value=(False, None, 3))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=())
    @patch("core.planning.refinement.run_clingo", return_value=["abstract atom"])
    def test_clingo_reports_concrete_refinement_failure(
        self, run_clingo, parse_plan_actions, build_mapping, solve_decrementally
    ):
        result = refine(self._context())

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 3)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)

    @patch("core.planning.refinement.solve_decrementally", return_value=(False, None, 1))
    @patch("core.planning.refinement.build_mapping", return_value="fd mapping")
    @patch("core.planning.refinement.read_fast_downward_plan", return_value=(PlanAction("move", ("item_abs",), 1),))
    def test_fd_source_maps_its_plan_and_reports_failure(self, read_plan, build_mapping, solve_decrementally):
        context = self._context(
            config=AbstractPlanningConfig("domain.pddl", "problem.pddl", plan_source="fd"),
            abstract_task={"planFile": "abstract.plan"},
        )

        result = refine(context)

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 1)
        read_plan.assert_called_once_with("abstract.plan")
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        solve_decrementally.assert_called_once_with("concrete asp\nfd mapping", 3)

    def test_fast_downward_plan_conversion_skips_comments_and_numbers_steps(self):
        plan = """
; cost = 3
(load p0 t0 l0)

(drive t0 l0 l1 level0 level1 level1)
(wait)
"""
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory, "sas_plan")
            source.write_text(plan, encoding="utf-8")

            abstract_plan = read_fast_downward_plan(source)

            self.assertEqual(
                abstract_plan,
                (
                    PlanAction("load", ("p0", "t0", "l0"), 1),
                    PlanAction("drive", ("t0", "l0", "l1", "level0", "level1", "level1"), 2),
                    PlanAction("wait", (), 3),
                ),
            )

    def test_unknown_plan_source_is_rejected(self):
        context = self._context(config=AbstractPlanningConfig("domain.pddl", "problem.pddl", plan_source="unknown"))

        with self.assertRaisesRegex(ValueError, "Unknown abstract plan source: unknown"):
            refine(context)


if __name__ == "__main__":
    unittest.main()
