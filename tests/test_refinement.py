import logging
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, call, patch

from core.abstraction.factory import Abstraction
from core.metrics import PlanningMetrics
from core.planning.abstract import _select_abstract_horizon
from core.planning.config import AbstractPlanningConfig
from core.planning.plan import PlanAction
from core.planning.refinement import RefinementContext, _extend_concrete_search, read_fast_downward_plan, refine


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
            "relaxed_deletes": (object(), object()),
            "concrete_asp": "concrete asp",
            "abstract_asp": "abstract asp",
            "abstract_task": {"planFile": "sas_plan"},
            "horizon": 3,
            "run_id": "run-123",
            "logger": Mock(spec=logging.Logger),
            "metrics": PlanningMetrics(),
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
        self.assertEqual(context.metrics.counters["decrements"], 0)
        self.assertEqual(context.metrics.counters["increments"], 0)
        self.assertEqual(
            result["abstraction"],
            {
                "abstract_symbol": "item_abs",
                "objects_to_abstract": ["a", "b"],
                "object_type": "item",
                "relaxed_unary_deletes": 2,
            },
        )
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
        self.assertEqual(context.metrics.counters["decrements"], 2)
        self.assertEqual(context.metrics.counters["increments"], 0)
        run_clingo.assert_called_once_with("abstract asp", 3)
        parse_plan_actions.assert_called_once_with(["occurs(abstract,1)"])
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)

    @patch("core.planning.refinement._extend_concrete_search")
    @patch("core.planning.refinement.solve_decrementally", return_value=(False, None, 3))
    @patch("core.planning.refinement.build_mapping", return_value="mapping asp")
    @patch("core.planning.refinement.parse_plan_actions", return_value=())
    @patch("core.planning.refinement.run_clingo", return_value=["abstract atom"])
    def test_clingo_extends_concrete_search_after_refinement_failure(
        self, run_clingo, parse_plan_actions, build_mapping, solve_decrementally, extend_search
    ):
        context = self._context()

        def extended(_context):
            _context.horizon = 5
            return ["occurs(extended,5)"], 2

        extend_search.side_effect = extended
        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(extended,5)"])
        self.assertEqual(result["horizon"], 5)
        self.assertEqual(context.metrics.counters["decrements"], 3)
        self.assertEqual(context.metrics.counters["increments"], 2)
        solve_decrementally.assert_called_once_with("concrete asp\nmapping asp", 3)
        extend_search.assert_called_once_with(context)

    @patch("core.planning.refinement._extend_concrete_search", return_value=(["occurs(extended,4)"], 1))
    @patch("core.planning.refinement.solve_decrementally", return_value=(False, None, 1))
    @patch("core.planning.refinement.build_mapping", return_value="fd mapping")
    @patch("core.planning.refinement.read_fast_downward_plan", return_value=(PlanAction("move", ("item_abs",), 1),))
    def test_fd_source_extends_search_after_refinement_failure(
        self, read_plan, build_mapping, solve_decrementally, extend_search
    ):
        context = self._context(
            config=AbstractPlanningConfig("domain.pddl", "problem.pddl", plan_source="fd"),
            abstract_task={"planFile": "abstract.plan"},
        )

        result = refine(context)

        self.assertTrue(result["success"])
        self.assertEqual(result["plan"], ["occurs(extended,4)"])
        self.assertEqual(context.metrics.counters["decrements"], 1)
        self.assertEqual(context.metrics.counters["increments"], 1)
        read_plan.assert_called_once_with("abstract.plan")
        build_mapping.assert_called_once_with((PlanAction("move", ("item_abs",), 1),), context.abstraction)
        solve_decrementally.assert_called_once_with("concrete asp\nfd mapping", 3)
        extend_search.assert_called_once_with(context)

    @patch("core.planning.refinement.run_clingo", side_effect=[None, None, ["occurs(concrete,6)"]])
    def test_extended_search_starts_above_abstract_horizon(self, run_clingo):
        context = self._context(horizon=3)

        plan, increments = _extend_concrete_search(context)

        self.assertEqual(plan, ["occurs(concrete,6)"])
        self.assertEqual(increments, 3)
        self.assertEqual(context.horizon, 6)
        self.assertEqual(
            run_clingo.call_args_list, [call("concrete asp", 4), call("concrete asp", 5), call("concrete asp", 6)]
        )

    def test_extended_search_finds_a_plan_at_a_larger_fixed_horizon(self):
        context = self._context(horizon=1, concrete_asp=":- horizon < 3.\nselected(horizon).\n#show selected/1.\n")

        plan, increments = _extend_concrete_search(context)

        self.assertEqual(plan, ["selected(3)"])
        self.assertEqual(increments, 2)
        self.assertEqual(context.horizon, 3)

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
