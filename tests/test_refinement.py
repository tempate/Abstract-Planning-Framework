import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from core.planning.abstract import _select_abstract_horizon
from core.planning.config import AbstractPlanningConfig
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

    @patch("core.planning.refinement.base.build_mapping")
    def test_mapping_receives_resolved_abstraction_values(self, build_mapping):
        config = AbstractPlanningConfig("domain.pddl", "problem.pddl")
        abstraction = SimpleNamespace(abstract_name="hangarabs", objects_to_abstract=("hangar1", "hangar2"))
        context = SimpleNamespace(config=config, abstraction=abstraction, logger=Mock())
        build_mapping.return_value = "mapping."

        mapping, _ = ClingoRefinement(context).build_mapping("abstract plan.")

        self.assertEqual(mapping, "mapping.")
        build_mapping.assert_called_once_with("abstract plan.", "hangarabs", ("hangar1", "hangar2"))

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

            atoms = FastDownwardRefinement.plan_to_abstract_atoms(object(), source)

            self.assertEqual(
                atoms,
                [
                    'occurs_abstract(action(("load","p0","t0","l0")), 1).',
                    'occurs_abstract(action(("drive","t0","l0","l1","level0","level1","level1")), 2).',
                    'occurs_abstract(action("wait"), 3).',
                ],
            )


if __name__ == "__main__":
    unittest.main()
