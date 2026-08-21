import tempfile
import unittest
from pathlib import Path

from core.planning.abstract import _select_abstract_horizon
from core.planning.plan import PlanAction
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
    def test_factory_selects_the_requested_strategy(self):
        context = object()

        self.assertIsInstance(get_refinement_strategy("clingo", context), ClingoRefinement)
        self.assertIsInstance(get_refinement_strategy("fd", context), FastDownwardRefinement)

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
