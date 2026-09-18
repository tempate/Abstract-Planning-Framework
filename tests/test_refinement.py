import unittest
from unittest.mock import Mock, patch

from core.abstraction.factory import Abstraction
from core.metrics import PlanningMetrics
from core.plan import PlanAction
from core.planning.config import AbstractPlanningConfig
from core.refinement.pipeline import RefinementContext, refine
from core.search.incremental import SolveResult


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

    def _solvers(self, incremental_solver, abstract_result):
        """Hand out one mock per construction: the abstract search, then the concrete one."""
        abstract_solver = Mock()
        abstract_solver.search.return_value = abstract_result
        concrete_solver = Mock()
        incremental_solver.side_effect = [abstract_solver, concrete_solver]
        return abstract_solver, concrete_solver

    @patch("core.refinement.pipeline.IncrementalSolver")
    @patch("core.refinement.pipeline.solve_decrementally", return_value=(True, ["occurs(concrete,1)"], 2))
    @patch("core.refinement.pipeline.build_mapping", return_value="mapping asp")
    @patch("core.refinement.pipeline.parse_plan_actions", return_value=(PlanAction("move", ("item_abs",), 1),))
    def test_the_abstract_plan_is_mapped_and_its_horizon_is_reported(
        self, parse_plan_actions, build_mapping, solve_decrementally, incremental_solver
    ):
        self._solvers(incremental_solver, SolveResult(["occurs(abstract,1)"], horizon=2, attempts=3))
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
        self.assertEqual(incremental_solver.call_args.args, ("concrete asp\nmapping asp", 5))

    @patch("core.refinement.pipeline.IncrementalSolver")
    @patch(
        "core.refinement.pipeline.solve_decrementally",
        return_value=(True, ['occurs(action(("move","a")),2)', 'occurs(action(("move","b")),4)'], 0),
    )
    @patch("core.refinement.pipeline.build_mapping", return_value="mapping asp")
    @patch("core.refinement.pipeline.parse_plan_actions", return_value=())
    def test_the_plan_length_counts_actions_instead_of_time_steps(
        self, parse_plan_actions, build_mapping, solve_decrementally, incremental_solver
    ):
        self._solvers(incremental_solver, SolveResult(["occurs(abstract,1)"], horizon=2, attempts=1))
        context = self._context()

        refine(context)

        # The two actions sit on a horizon of five, whose gaps stayed empty.
        self.assertEqual(context.metrics.counters["plan_length"], 2)

    @patch("core.refinement.pipeline.disabled_switches", return_value=[])
    @patch("core.refinement.pipeline.IncrementalSolver")
    @patch("core.refinement.pipeline.solve_decrementally", return_value=(False, None, 3))
    @patch("core.refinement.pipeline.build_mapping", return_value="mapping asp")
    @patch("core.refinement.pipeline.parse_plan_actions", return_value=())
    def test_unrefinable_plans_extend_the_search_above_the_abstract_horizon(
        self, parse_plan_actions, build_mapping, solve_decrementally, incremental_solver, disabled_switches
    ):
        _abstract, solver = self._solvers(incremental_solver, SolveResult(["abstract atom"], horizon=3, attempts=4))
        solver.search.return_value = SolveResult(["occurs(concrete,9)"], horizon=9, attempts=2)

        context = self._context()
        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(concrete,9)"])
        self.assertEqual(context.metrics.counters["decrements"], 3)
        self.assertEqual(context.metrics.counters["increments"], 2)
        self.assertEqual(context.metrics.counters["concrete_solve_calls"], 6)
        self.assertIn("extended_concrete_solving", context.metrics.durations)
        self.assertEqual(incremental_solver.call_args.args, ("concrete asp\nmapping asp", 7))

        # The extension continues on the solver the decremental search used.
        self.assertIs(solve_decrementally.call_args.args[0], solver)
        solver.extend.assert_called_once_with()
        self.assertEqual(solver.search.call_args.args[0], [])


if __name__ == "__main__":
    unittest.main()
