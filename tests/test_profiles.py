import unittest

from core.profiles.beluga import BelugaProfile
from core.profiles.factory import get_profile
from core.profiles.no_mystery import NoMysteryProfile


class ProfileFactoryTests(unittest.TestCase):
    def test_factory_returns_domain_specific_profiles(self):
        self.assertIsInstance(get_profile("beluga"), BelugaProfile)
        self.assertIsInstance(get_profile("no_mystery"), NoMysteryProfile)

    def test_factory_rejects_unknown_profiles(self):
        with self.assertRaisesRegex(ValueError, "Unknown profile"):
            get_profile("unknown")

    def test_beluga_requires_mapping_arguments(self):
        profile = BelugaProfile()

        for symbol, objects in ((None, None), ("hangarabs", []), (None, ["h1"])):
            with self.subTest(symbol=symbol, objects=objects):
                with self.assertRaisesRegex(ValueError, "abstract object mapping"):
                    profile.validate_configuration(symbol, objects)

    def test_no_mystery_does_not_require_mapping_arguments(self):
        NoMysteryProfile().validate_configuration(None, None)


class MappingTests(unittest.TestCase):
    def _build(self, profile, occurrences, symbol=None, objects=None):
        return profile.build_mapping(occurrences, symbol, objects)

    def test_beluga_maps_concrete_actions_directly_and_abstract_objects_by_choice(self):
        occurrences = """\
occurs_abstract(action(("move","hangarabs","dock")),2).
occurs_abstract(action(("inspect","jig1")),1).
"""

        mapping, switch_map = self._build(BelugaProfile(), occurrences, "hangarabs", ["hangar1", "hangar2"])

        self.assertIn("0 { switch(1) } 1.", mapping)
        self.assertIn("0 { switch(2) } 1.", mapping)
        self.assertIn(
            'occurs(action(("inspect","jig1")),1) :- ' 'occurs_abstract(action(("inspect","jig1")),1), switch(1).',
            mapping,
        )
        self.assertIn('occurs(action(("move","hangar1","dock")), 2)', mapping)
        self.assertIn('occurs(action(("move","hangar2","dock")), 2)', mapping)
        self.assertEqual(list(switch_map), [1, 2])
        self.assertFalse(switch_map[1]["is_abstract"])
        self.assertTrue(switch_map[2]["is_abstract"])

    def test_mapping_rejects_occurrences_that_are_not_concrete_actions(self):
        mapping, _ = self._build(
            BelugaProfile(), 'occurs_abstract(action(("inspect","jig1")),1).\n', "hangarabs", ["hangar1"]
        )

        self.assertIn(":- occurs(Action, T), not action(Action).", mapping)

    def test_no_mystery_expands_abstract_drive_fuel_arguments(self):
        occurrences = 'occurs_abstract(action(("drive","t0","l0","l1",' '"abslevel1","abslevel2","abslevel1")),4).\n'

        mapping, switch_map = self._build(NoMysteryProfile(), occurrences)

        self.assertIn('occurs(action(("drive","t0","l0","l1",Post,Diff,Pre)),4)', mapping)
        self.assertIn('fuelcost(Diff,"l0","l1")', mapping)
        self.assertIn("sum(Post,Diff,Pre)", mapping)
        self.assertTrue(switch_map[4]["is_abstract"])

    def test_no_mystery_maps_non_drive_actions_directly(self):
        occurrences = 'occurs_abstract(action(("load","p0","t0","l0")),1).\n'

        mapping, switch_map = self._build(NoMysteryProfile(), occurrences)

        self.assertIn('occurs(action(("load","p0","t0","l0")),1) :-', mapping)
        self.assertFalse(switch_map[1]["is_abstract"])

    def test_no_mystery_rejects_an_unparseable_drive_action(self):
        occurrences = 'occurs_abstract(action("drive"),1).\n'

        with self.assertRaisesRegex(ValueError, "Cannot parse action"):
            self._build(NoMysteryProfile(), occurrences)


if __name__ == "__main__":
    unittest.main()
