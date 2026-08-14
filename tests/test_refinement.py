import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

from core.planning.abstract import (
    _get_planning_paths,
    _select_abstract_horizon,
)
from core.planning.config import AbstractPlanningConfig
from core.planning.refinement.ClingoRefinement import ClingoRefinement
from core.planning.refinement.FastDownwardRefinement import FastDownwardRefinement
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

    def test_planning_paths_are_isolated_below_the_run_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = _get_planning_paths(directory)

            self.assertEqual(paths.concrete_asp, str(Path(directory, "output_c.lp")))
            self.assertEqual(
                paths.abstract_asp,
                str(Path(directory, "abstract", "output_a.lp")),
            )
            self.assertTrue(Path(directory, "clingo").is_dir())
            self.assertEqual(paths.occurrences, str(Path(directory, "clingo", "occurs_abs.lp")))
            self.assertEqual(paths.mapping, str(Path(directory, "clingo", "map.lp")))


class RefinementStrategyTests(unittest.TestCase):
    def test_factory_selects_the_requested_strategy(self):
        context = object()

        self.assertIsInstance(
            get_refinement_strategy("clingo", context),
            ClingoRefinement,
        )
        self.assertIsInstance(
            get_refinement_strategy("fd", context),
            FastDownwardRefinement,
        )

    def test_mapping_receives_configuration_values(self):
        planner = Mock()
        config = AbstractPlanningConfig(
            "abstract-domain.pddl",
            "abstract-problem.pddl",
            "concrete-domain.pddl",
            "concrete-problem.pddl",
            abstract_symbol="hangarabs",
            concrete_objects=["hangar1", "hangar2"],
        )
        context = SimpleNamespace(
            config=config,
            planner=planner,
            paths=SimpleNamespace(
                occurrences="occurrences.lp",
                mapping="mapping.lp",
            ),
            logger=Mock(),
        )

        ClingoRefinement(context).build_mapping()

        planner.build_mapping.assert_called_once_with(
            "occurrences.lp",
            "mapping.lp",
            "hangarabs",
            ("hangar1", "hangar2"),
        )

    def test_fast_downward_plan_conversion_skips_comments_and_numbers_steps(self):
        plan = """
; cost = 3
(load p0 t0 l0)

(drive t0 l0 l1 level0 level1 level1)
(wait)
"""
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory, "sas_plan")
            destination = Path(directory, "occurrences.lp")
            source.write_text(plan, encoding="utf-8")

            atoms = FastDownwardRefinement.plan_to_abstract_atoms(
                object(), source, destination
            )

            self.assertEqual(
                atoms,
                [
                    'occurs_abstract(action(("load","p0","t0","l0")), 1).',
                    'occurs_abstract(action(("drive","t0","l0","l1","level0","level1","level1")), 2).',
                    'occurs_abstract(action("wait"), 3).',
                ],
            )
            self.assertEqual(
                destination.read_text(encoding="utf-8"),
                "\n".join(atoms),
            )


if __name__ == "__main__":
    unittest.main()
