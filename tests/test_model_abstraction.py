import unittest
from pathlib import Path

from core.integrations.unified_planning import parse_problem, read_problem, write_problem
from core.model_abstraction import AbstractionError, abstract_problem, rank_symmetry_classes

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BELUGA = PROJECT_ROOT / "data" / "beluga" / "concrete" / "standard"


class ModelAbstractionTests(unittest.TestCase):
    def test_collapses_beluga_hangars_without_mutating_source(self):
        source = read_problem(BELUGA / "domain.pddl", BELUGA / "problem_3_s45_j3_r2_oc44_f3.pddl")
        source_objects = tuple(item.name for item in source.all_objects)

        result = abstract_problem(source, ["hangar1", "hangar2", "hangar3"], "hangarabs")

        self.assertEqual(tuple(item.name for item in source.all_objects), source_objects)
        result_objects = {item.name for item in result.problem.all_objects}
        self.assertTrue({"hangar1", "hangar2", "hangar3"}.isdisjoint(result_objects))
        self.assertIn("hangarabs", result_objects)
        self.assertEqual(result.object_type, "hangar")
        self.assertEqual([item.action for item in result.removed_deletes], ["deliver-to-hangar"])
        serialized = write_problem(result.problem)
        for selected in ("hangar1", "hangar2", "hangar3"):
            self.assertNotIn(selected, serialized.domain)
            self.assertNotIn(selected, serialized.problem)
        parse_problem(serialized.domain, serialized.problem)
        expected = read_problem(
            PROJECT_ROOT / "data" / "beluga" / "abstract" / "hangar" / "domain.pddl",
            PROJECT_ROOT / "data" / "beluga" / "abstract" / "hangar" / "problem_3_s45_j3_r2_oc44_f3_abs.pddl",
        )
        self.assertEqual(result.problem, expected)

    def test_preserves_static_applicability_filter_for_trailers(self):
        source = read_problem(BELUGA / "domain.pddl", BELUGA / "problem_3_s45_j3_r2_oc44_f3.pddl")

        result = abstract_problem(source, ["beluga_trailer_1", "beluga_trailer_2"], "beluga_abs_trailer")

        self.assertEqual(
            [item.action for item in result.removed_deletes], ["unload-beluga", "pick-up-rack", "unstack-rack"]
        )

    def test_rejects_false_inequality_and_initial_value_collisions(self):
        domain = """
(define (domain d)
  (:requirements :typing :equality :fluents)
  (:types item)
  (:predicates (ready ?x - item))
  (:functions (value ?x - item)))
"""
        inequality = """
(define (problem p) (:domain d)
  (:objects a b - item) (:init) (:goal (not (= a b))))
"""
        conflicting = """
(define (problem p) (:domain d)
  (:objects a b - item)
  (:init (= (value a) 1) (= (value b) 2)) (:goal (and)))
"""

        with self.assertRaisesRegex(AbstractionError, "false"):
            abstract_problem(parse_problem(domain, inequality), ["a", "b"])
        with self.assertRaisesRegex(AbstractionError, "conflicting initial values"):
            abstract_problem(parse_problem(domain, conflicting), ["a", "b"])

    def test_deduplicates_equal_values_and_rejects_boolean_conflicts(self):
        domain = """
(define (domain d)
  (:requirements :typing :negative-preconditions :fluents)
  (:types item)
  (:predicates (ready ?x - item))
  (:functions (value ?x - item)))
"""
        equal_values = """
(define (problem p) (:domain d)
  (:objects a b - item)
  (:init (= (value a) 1) (= (value b) 1)) (:goal (and)))
"""
        contradictory = """
(define (problem p) (:domain d)
  (:objects a b - item)
  (:init (ready a) (not (ready b))) (:goal (and)))
"""

        result = abstract_problem(parse_problem(domain, equal_values), ["a", "b"])
        values = [
            (fluent, value)
            for fluent, value in result.problem.explicit_initial_values.items()
            if "value" in str(fluent)
        ]
        self.assertEqual(len(values), 1)
        contradictory_problem = parse_problem(domain, contradictory)
        contradictory_problem.set_initial_value(
            contradictory_problem.fluent("ready")(contradictory_problem.object("b")), False
        )
        with self.assertRaisesRegex(AbstractionError, "contradictory initial facts"):
            abstract_problem(contradictory_problem, ["a", "b"])

    def test_ranks_beluga_classes_like_the_legacy_transformer(self):
        source = read_problem(BELUGA / "domain.pddl", BELUGA / "problem_3_s45_j3_r2_oc44_f3.pddl")
        classes = [
            ["factory_trailer_1", "factory_trailer_2"],
            ["hangar1", "hangar2", "hangar3"],
            ["beluga_trailer_1", "beluga_trailer_2"],
            ["BSIDE", "FSIDE"],
        ]

        ranked = rank_symmetry_classes(source, classes)

        self.assertEqual(ranked[0].objects, ("hangar1", "hangar2", "hangar3"))
        self.assertEqual([item.unary_delete_score for item in ranked], [1, 3, 3])
        self.assertEqual(
            [item.action for item in ranked[1].removed_deletes], ["unload-beluga", "pick-up-rack", "unstack-rack"]
        )


if __name__ == "__main__":
    unittest.main()
