import unittest
from unittest.mock import patch

from core.abstraction.factory import Abstraction
from core.metrics import PlanningMetrics
from core.plan import PlanAction
from core.planning.config import AbstractPlanningConfig
from core.refinement.pipeline import RefinementContext, refine
from core.search.incremental import SolveResult
from core.search.relaxing import RelaxedResult


class RefinementTests(unittest.TestCase):
    def _context(self, **changes):
        values = {
            "config": AbstractPlanningConfig("domain.pddl", "problem.pddl"),
            "abstraction": Abstraction("item_abs", ("a", "b"), "item"),
            "concrete_asp": "concrete asp",
            "abstract_asp": "abstract asp",
            "horizon": 3,
            "run_id": "run-123",
            "metrics": PlanningMetrics(),
        }
        values.update(changes)
        return RefinementContext(**values)

    @patch("core.refinement.pipeline.collect_switches", return_value=[])
    @patch("core.refinement.pipeline.RelaxingSolver")
    @patch("core.refinement.pipeline.IncrementalSolver")
    @patch("core.refinement.pipeline.build_mapping", return_value="mapping asp")
    @patch("core.refinement.pipeline.parse_plan_actions", return_value=(PlanAction("move", ("item_abs",), 1),))
    def test_the_abstract_plan_is_mapped_and_its_horizon_is_reported(
        self, parse_plan_actions, build_mapping, incremental_solver, relaxing_solver, collect_switches
    ):
        incremental_solver.return_value.search.return_value = SolveResult(["occurs(abstract,1)"], horizon=2, attempts=3)
        relaxing_solver.return_value.search.return_value = RelaxedResult(
            ["occurs(concrete,1)"], horizon=5, attempts=3, dropped=2
        )
        context = self._context()

        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,1)"])
        self.assertEqual(result["run_id"], "run-123")
        self.assertEqual(context.metrics.counters["abstract_plan_length"], 2)
        self.assertEqual(context.metrics.counters["abstract_solve_calls"], 3)
        self.assertEqual(context.metrics.counters["decrements"], 2)
        self.assertEqual(context.metrics.counters["increments"], 0)
        self.assertEqual(context.metrics.counters["concrete_solve_calls"], 3)
        self.assertIn("abstract_solving", context.metrics.durations)
        # The guided search runs the mapping alongside the concrete program, and
        # starts from the mapped horizon that surrounds the two abstract actions
        # with gaps rather than from zero.
        self.assertEqual(relaxing_solver.call_args.args, ("concrete asp\nmapping asp", 5))

    @patch("core.refinement.pipeline.collect_switches", return_value=[])
    @patch("core.refinement.pipeline.RelaxingSolver")
    @patch("core.refinement.pipeline.IncrementalSolver")
    @patch("core.refinement.pipeline.build_mapping", return_value="mapping asp")
    @patch("core.refinement.pipeline.parse_plan_actions", return_value=())
    def test_the_plan_length_counts_actions_instead_of_time_steps(
        self, parse_plan_actions, build_mapping, incremental_solver, relaxing_solver, collect_switches
    ):
        incremental_solver.return_value.search.return_value = SolveResult(["occurs(abstract,1)"], horizon=2, attempts=1)
        relaxing_solver.return_value.search.return_value = RelaxedResult(
            ['occurs(action(("move","a")),2)', 'occurs(action(("move","b")),4)'], horizon=5, attempts=1, dropped=0
        )
        context = self._context()

        refine(context)

        # The two actions sit on a horizon of five, whose gaps stayed empty.
        self.assertEqual(context.metrics.counters["plan_length"], 2)

    @patch("core.refinement.pipeline.collect_switches", return_value=[])
    @patch("core.refinement.pipeline.RelaxingSolver")
    @patch("core.refinement.pipeline.IncrementalSolver")
    @patch("core.refinement.pipeline.build_mapping", return_value="mapping asp")
    @patch("core.refinement.pipeline.parse_plan_actions", return_value=())
    def test_a_search_above_the_mapped_horizon_is_reported_as_increments(
        self, parse_plan_actions, build_mapping, incremental_solver, relaxing_solver, collect_switches
    ):
        incremental_solver.return_value.search.return_value = SolveResult(["abstract atom"], horizon=3, attempts=4)
        relaxing_solver.return_value.search.return_value = RelaxedResult(
            ["occurs(concrete,9)"], horizon=9, attempts=6, dropped=3
        )

        context = self._context()
        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,9)"])
        self.assertEqual(context.metrics.counters["decrements"], 3)
        # The mapped horizon of seven was raised to nine.
        self.assertEqual(context.metrics.counters["increments"], 2)
        self.assertEqual(context.metrics.counters["concrete_solve_calls"], 6)
        self.assertEqual(relaxing_solver.call_args.args, ("concrete asp\nmapping asp", 7))


if __name__ == "__main__":
    unittest.main()
