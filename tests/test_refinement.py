import unittest
from unittest.mock import patch

from core.abstraction.factory import Abstraction
from core.integrations.clingo import ClingoSolveResult
from core.metrics import PlanningMetrics
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
            "abstract_task": {"sasFile": "abstract.sas"},
            "horizon": 3,
            "run_id": "run-123",
            "metrics": PlanningMetrics(),
        }
        values.update(changes)
        return RefinementContext(**values)

    @patch("core.planning.refinement.solve_decrementally", return_value=(True, ["occurs(concrete,1)"], 2))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=(PlanAction("move", ("item_abs",), 1),))
    @patch(
        "core.planning.refinement.solve", return_value=ClingoSolveResult(["occurs(abstract,1)"], horizon=2, attempts=3)
    )
    def test_the_abstract_plan_is_mapped_and_its_horizon_is_reported(
        self, solve, parse_plan_actions, build_mapping, solve_decrementally
    ):
        context = self._context()

        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,1)"])
        self.assertEqual(result["horizon"], 2)
        self.assertEqual(result["run_id"], "run-123")
        self.assertEqual(context.metrics.counters["abstract_horizon"], 2)
        self.assertEqual(context.metrics.counters["abstract_solve_calls"], 3)
        self.assertEqual(context.metrics.counters["decrements"], 2)
        self.assertEqual(context.metrics.counters["increments"], 0)
        self.assertEqual(context.metrics.counters["final_horizon"], 2)
        self.assertEqual(context.metrics.counters["concrete_solve_calls"], 3)
        self.assertEqual(set(context.metrics.durations), {"abstract_solving", "guided_concrete_solving"})
        self.assertEqual(solve.call_args.args, ("abstract asp",))
        parse_plan_actions.assert_called_once_with(["occurs(abstract,1)"])
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        self.assertEqual(solve_decrementally.call_args.args[:2], ("concrete asp\nmapping asp", 2))

    @patch("core.planning.refinement.solve_decrementally", return_value=(False, None, 3))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=())
    @patch("core.planning.refinement.solve")
    def test_unrefinable_plans_extend_the_search_above_the_abstract_horizon(
        self, solve, parse_plan_actions, build_mapping, solve_decrementally
    ):
        solve.side_effect = [
            ClingoSolveResult(["abstract atom"], horizon=3, attempts=4),
            ClingoSolveResult(["occurs(concrete,5)"], horizon=5, attempts=2),
        ]

        context = self._context()
        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,5)"])
        self.assertEqual(result["horizon"], 5)
        self.assertEqual(context.metrics.counters["decrements"], 3)
        self.assertEqual(context.metrics.counters["increments"], 2)
        self.assertEqual(context.metrics.counters["final_horizon"], 5)
        self.assertEqual(context.metrics.counters["concrete_solve_calls"], 6)
        self.assertIn("extended_concrete_solving", context.metrics.durations)
        self.assertEqual(solve.call_args_list[1].args[:2], ("concrete asp", 4))
        self.assertEqual(solve_decrementally.call_args.args[:2], ("concrete asp\nmapping asp", 3))


if __name__ == "__main__":
    unittest.main()
