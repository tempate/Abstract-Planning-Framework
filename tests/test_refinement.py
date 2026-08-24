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
from core.planning.refinement.base import RefinementContext
from core.planning.refinement.clingo import ClingoRefinement
from core.planning.refinement.fast_downward import FastDownwardRefinement
from core.planning.refinement.factory import get_refinement_strategy


class AbstractPlanningHelperTests(unittest.TestCase):
    def test_auto_horizon_uses_the_abstract_plan_length(self):
        self.assertEqual(_select_abstract_horizon(None, 6, "clingo"), 6)
        self.assertEqual(_select_abstract_horizon(None, 6, "fd"), 6)

    def test_explicit_clingo_horizon_can_be_shorter_than_fd_plan(self):
        self.assertEqual(_select_abstract_horizon(2, 6, "clingo"), 2)

    def test_fd_source_rejects_a_plan_that_exceeds_the_horizon(self):
        with self.assertRaisesRegex(ValueError, "plan length 6"):
            _select_abstract_horizon(5, 6, "fd")


class RefinementStrategyTests(unittest.TestCase):
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

    def test_factory_selects_the_requested_strategy(self):
        context = object()

        self.assertIsInstance(get_refinement_strategy("clingo", context), ClingoRefinement)
        self.assertIsInstance(get_refinement_strategy("fd", context), FastDownwardRefinement)

    @patch("core.planning.refinement.clingo.build_mapping")
    @patch("core.planning.refinement.clingo.run_clingo", return_value=None)
    def test_clingo_stops_when_no_abstract_plan_exists(self, run_clingo, build_mapping):
        context = self._context()

        result = ClingoRefinement(context).refine()

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 0)
        run_clingo.assert_called_once_with("abstract asp", 3)
        build_mapping.assert_not_called()

    @patch("core.planning.refinement.base.solve_decrementally", return_value=(True, ["occurs(concrete,1)"], 2))
    @patch("core.planning.refinement.clingo.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.clingo.parse_plan_actions", return_value=(PlanAction("move", ("item_abs",), 1),))
    @patch("core.planning.refinement.clingo.run_clingo", return_value=["occurs(abstract,1)"])
    def test_clingo_maps_the_abstract_plan_and_reports_decrements(
        self, run_clingo, parse_plan_actions, build_mapping, solve_decrementally
    ):
        context = self._context()

        result = ClingoRefinement(context).refine()

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,1)"])
        self.assertEqual(result["timings"]["decrements"], 2)
        run_clingo.assert_called_once_with("abstract asp", 3)
        parse_plan_actions.assert_called_once_with(["occurs(abstract,1)"])
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)

    @patch("core.planning.refinement.base.solve_decrementally", return_value=(False, None, 3))
    @patch("core.planning.refinement.clingo.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.clingo.parse_plan_actions", return_value=())
    @patch("core.planning.refinement.clingo.run_clingo", return_value=["abstract atom"])
    def test_clingo_reports_concrete_refinement_failure(
        self, run_clingo, parse_plan_actions, build_mapping, solve_decrementally
    ):
        result = ClingoRefinement(self._context()).refine()

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 3)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)

    @patch("core.planning.refinement.base.solve_decrementally", return_value=(False, None, 1))
    @patch("core.planning.refinement.fast_downward.build_mapping", return_value="fd mapping")
    @patch.object(FastDownwardRefinement, "read_abstract_plan", return_value=(PlanAction("move", ("item_abs",), 1),))
    def test_fd_source_maps_its_plan_and_reports_failure(self, read_abstract_plan, build_mapping, solve_decrementally):
        context = self._context(abstract_task={"planFile": "abstract.plan"})

        result = FastDownwardRefinement(context).refine()

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 1)
        read_abstract_plan.assert_called_once_with("abstract.plan")
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

            abstract_plan = FastDownwardRefinement.read_abstract_plan(object(), source)

            self.assertEqual(
                abstract_plan,
                (
                    PlanAction("load", ("p0", "t0", "l0"), 1),
                    PlanAction("drive", ("t0", "l0", "l1", "level0", "level1", "level1"), 2),
                    PlanAction("wait", (), 3),
                ),
            )


if __name__ == "__main__":
    unittest.main()
