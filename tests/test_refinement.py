import logging
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from core.abstraction.factory import Abstraction
from core.integrations.clingo import ClingoSolveResult
from core.planning.config import AbstractPlanningConfig
from core.planning.plan import PlanAction
from core.planning.refinement import RefinementContext, refine


class RefinementTests(unittest.TestCase):
    def _context(self, **changes):
        values = {
            "config": AbstractPlanningConfig("domain.pddl", "problem.pddl"),
            "abstraction": Abstraction("item_abs", ("a", "b"), "item"),
            "relaxed_deletes": (object(), object()),
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

    @patch("core.planning.refinement.solve_decrementally", return_value=(True, ["occurs(concrete,1)"], 2))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=(PlanAction("move", ("item_abs",), 1),))
    @patch(
        "core.planning.refinement.solve", return_value=ClingoSolveResult(["occurs(abstract,1)"], horizon=2, attempts=3)
    )
    def test_clingo_maps_the_abstract_plan_and_reports_decrements(
        self, solve, parse_plan_actions, build_mapping, solve_decrementally
    ):
        context = self._context()

        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,1)"])
        self.assertEqual(result["timings"]["decrements"], 2)
        self.assertEqual(result["horizon"], 2)
        solve.assert_called_once_with("abstract asp")
        parse_plan_actions.assert_called_once_with(["occurs(abstract,1)"])
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 2)

    @patch("core.planning.refinement.solve_decrementally", return_value=(False, None, 3))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=())
    @patch("core.planning.refinement.solve", return_value=ClingoSolveResult(["abstract atom"], horizon=3, attempts=4))
    def test_clingo_reports_concrete_refinement_failure(
        self, solve, parse_plan_actions, build_mapping, solve_decrementally
    ):
        result = refine(self._context())

        self.assertFalse(result["success"])
        self.assertIsNone(result["plan"])
        self.assertEqual(result["timings"]["decrements"], 3)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)


if __name__ == "__main__":
    unittest.main()
