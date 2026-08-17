import tempfile
import unittest
from pathlib import Path

from scripts.abstraction.collapse_fuel_levels import collapse_fuel_levels
from scripts.abstraction.collapse_hangars import collapse_hangars, count_hangars
from scripts.abstraction.collapse_trailers import collapse_trailers, count_trailers


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class BelugaAbstractionTests(unittest.TestCase):
    def test_hangar_abstraction_collapses_declarations_facts_and_references(self):
        problem = """
(:objects
    ; hangars:
    hangar1 - hangar
    hangar2 - hangar
    jig1 - jig
)
(:init
    ; hangars:
    (empty hangar1)
    (empty hangar2)
    (at jig1 hangar2)
)
"""

        abstract = collapse_hangars(problem)

        self.assertEqual(count_hangars(problem), 2)
        self.assertNotIn("hangar1", abstract)
        self.assertNotIn("hangar2", abstract)
        self.assertEqual(abstract.count("hangarabs - hangar"), 1)
        self.assertEqual(abstract.count("(empty hangarabs)"), 1)
        self.assertIn("(at jig1 hangarabs)", abstract)

    def test_hangar_abstraction_supports_a_custom_name(self):
        problem = "; hangars:\n  hangar9 - hangar\n(at x hangar9)\n"

        abstract = collapse_hangars(problem, "shared_hangar")

        self.assertIn("shared_hangar - hangar", abstract)
        self.assertIn("(at x shared_hangar)", abstract)

    def test_trailer_abstraction_leaves_factory_trailers_concrete(self):
        problem = """
(:objects
    ; trailers:
    beluga_trailer_1 - trailer
    beluga_trailer_2 - trailer
    factory_trailer_1 - trailer
)
(:init
    ; trailers (Beluga side):
    (empty beluga_trailer_1)
    (at-side beluga_trailer_1 bside)
    (empty beluga_trailer_2)
    (at-side beluga_trailer_2 bside)
    (empty factory_trailer_1)
)
"""

        abstract = collapse_trailers(problem)

        self.assertEqual(count_trailers(problem), 2)
        self.assertNotIn("beluga_trailer_1", abstract)
        self.assertNotIn("beluga_trailer_2", abstract)
        self.assertEqual(abstract.count("beluga_abs_trailer - trailer"), 1)
        self.assertEqual(abstract.count("(empty beluga_abs_trailer)"), 1)
        self.assertIn("factory_trailer_1 - trailer", abstract)
        self.assertIn("(empty factory_trailer_1)", abstract)


class NoMysteryAbstractionTests(unittest.TestCase):
    def test_fuel_abstraction_replaces_arithmetic_with_two_levels(self):
        problem = """(define (problem sample)
(:objects
    level0 level1 level2 - fuellevel
    t0 - truck
)
(:init
    (sum level0 level1 level1)
    (sum level1 level1 level2)
    (fuel t0 level2)
    (fuelcost level1 l0 l1)
)
)
"""

        abstract = collapse_fuel_levels(problem)

        self.assertIn("abslevel1 abslevel2 - fuellevel", abstract)
        self.assertEqual(
            abstract.count("(sum abslevel1 abslevel2 abslevel1)"),
            1,
        )
        self.assertIn("(fuel t0 abslevel1)", abstract)
        self.assertIn("(fuelcost abslevel2 l0 l1)", abstract)
        self.assertNotRegex(abstract, r"\blevel\d+\b")
        self.assertTrue(abstract.endswith("\n"))

    def test_checked_in_example_is_generated_by_the_abstraction(self):
        example = PROJECT_ROOT / "data" / "examples" / "no_mystery"
        concrete = (example / "concrete" / "problem.pddl").read_text(
            encoding="utf-8"
        )
        expected = (example / "abstract" / "problem.pddl").read_text(
            encoding="utf-8"
        )

        generated = collapse_fuel_levels(concrete)

        # Layout is intentionally irrelevant to PDDL; compare its token stream.
        self.assertEqual(generated.split(), expected.split())

    def test_abstraction_cli_function_can_write_to_a_temporary_destination(self):
        source = "(:objects level0 level1 - fuellevel)\n(:init)\n"

        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory, "abstract.pddl")
            destination.write_text(collapse_fuel_levels(source), encoding="utf-8")

            self.assertIn(
                "abslevel1 abslevel2 - fuellevel",
                destination.read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
