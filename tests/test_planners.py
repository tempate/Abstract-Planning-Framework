import tempfile
import unittest
from pathlib import Path

from core.planners.BelugaPlanner import BelugaPlanner
from core.planners.NoMysteryPlanner import NoMysteryPlanner
from core.planners.factory import get_planner


class PlannerFactoryTests(unittest.TestCase):
    def test_factory_returns_domain_specific_planners(self):
        self.assertIsInstance(get_planner("beluga"), BelugaPlanner)
        self.assertIsInstance(get_planner("no_mystery"), NoMysteryPlanner)

    def test_factory_rejects_unknown_profiles(self):
        with self.assertRaisesRegex(ValueError, "Unknown profile"):
            get_planner("unknown")

    def test_beluga_requires_mapping_arguments(self):
        planner = BelugaPlanner()

        for symbol, objects in ((None, None), ("hangarabs", []), (None, ["h1"])):
            with self.subTest(symbol=symbol, objects=objects):
                with self.assertRaisesRegex(ValueError, "--abstract-symbol"):
                    planner.validate_configuration(symbol, objects)

    def test_no_mystery_does_not_require_mapping_arguments(self):
        NoMysteryPlanner().validate_configuration(None, None)


class MappingTests(unittest.TestCase):
    def _build(self, planner, occurrences, symbol=None, objects=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        occurs_path = Path(directory.name, "occurrences.lp")
        mapping_path = Path(directory.name, "mapping.lp")
        occurs_path.write_text(occurrences, encoding="utf-8")
        switch_map = planner.build_mapping(
            occurs_path,
            mapping_path,
            symbol,
            objects,
        )
        return mapping_path.read_text(encoding="utf-8"), switch_map

    def test_beluga_maps_concrete_actions_directly_and_abstract_objects_by_choice(self):
        occurrences = """\
occurs_abstract(action(("move","hangarabs","dock")),2).
occurs_abstract(action(("inspect","jig1")),1).
"""

        mapping, switch_map = self._build(
            BelugaPlanner(),
            occurrences,
            "hangarabs",
            ["hangar1", "hangar2"],
        )

        self.assertIn("0 { switch(1) } 1.", mapping)
        self.assertIn("0 { switch(2) } 1.", mapping)
        self.assertIn(
            'occurs(action(("inspect","jig1")),1) :- '
            'occurs_abstract(action(("inspect","jig1")),1), switch(1).',
            mapping,
        )
        self.assertIn(
            'occurs(action(("move","hangar1","dock")), 2)',
            mapping,
        )
        self.assertIn(
            'occurs(action(("move","hangar2","dock")), 2)',
            mapping,
        )
        self.assertEqual(list(switch_map), [1, 2])
        self.assertFalse(switch_map[1]["is_abstract"])
        self.assertTrue(switch_map[2]["is_abstract"])

    def test_mapping_rejects_occurrences_that_are_not_concrete_actions(self):
        mapping, _ = self._build(
            BelugaPlanner(),
            'occurs_abstract(action(("inspect","jig1")),1).\n',
            "hangarabs",
            ["hangar1"],
        )

        self.assertIn(
            ":- occurs(Action, T), not action(Action).",
            mapping,
        )

    def test_no_mystery_expands_abstract_drive_fuel_arguments(self):
        occurrences = (
            'occurs_abstract(action(("drive","t0","l0","l1",'
            '"abslevel1","abslevel2","abslevel1")),4).\n'
        )

        mapping, switch_map = self._build(NoMysteryPlanner(), occurrences)

        self.assertIn(
            'occurs(action(("drive","t0","l0","l1",Post,Diff,Pre)),4)',
            mapping,
        )
        self.assertIn('fuelcost(Diff,"l0","l1")', mapping)
        self.assertIn("sum(Post,Diff,Pre)", mapping)
        self.assertTrue(switch_map[4]["is_abstract"])

    def test_no_mystery_maps_non_drive_actions_directly(self):
        occurrences = (
            'occurs_abstract(action(("load","p0","t0","l0")),1).\n'
        )

        mapping, switch_map = self._build(NoMysteryPlanner(), occurrences)

        self.assertIn(
            'occurs(action(("load","p0","t0","l0")),1) :-',
            mapping,
        )
        self.assertFalse(switch_map[1]["is_abstract"])

    def test_no_mystery_rejects_an_unparseable_drive_action(self):
        occurrences = 'occurs_abstract(action("drive"),1).\n'

        with self.assertRaisesRegex(ValueError, "Cannot parse action"):
            self._build(NoMysteryPlanner(), occurrences)


if __name__ == "__main__":
    unittest.main()
