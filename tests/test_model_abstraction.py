import unittest
from pathlib import Path

from unified_planning.shortcuts import (
    Always,
    BoolType,
    DurativeAction,
    Fluent,
    InstantaneousAction,
    IntType,
    MaximizeExpressionOnFinalState,
    MinimizeActionCosts,
    Problem,
    UserType,
    Variable,
)

from core.integrations.unified_planning import parse_problem, read_problem, write_problem
from core.model_abstraction import AbstractionError, abstract_problem

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
        get_from_hangar = result.problem.action("get-from-hangar")
        self.assertTrue(
            any(
                effect.fluent.is_fluent_exp()
                and effect.fluent.fluent().name == "empty"
                and effect.fluent.arg(0).is_parameter_exp()
                and effect.fluent.arg(0).parameter().name == "t"
                and effect.value.is_false()
                for effect in get_from_hangar.effects
            )
        )

    def test_simplifies_an_inequality_made_false_by_the_collapse(self):
        domain = """
(define (domain d)
  (:requirements :typing :equality)
  (:types item)
  (:predicates (ready ?x - item)))
"""
        inequality = """
(define (problem p) (:domain d)
  (:objects a b - item) (:init) (:goal (not (= a b))))
"""

        source = parse_problem(domain, inequality)
        result = abstract_problem(source, ["a", "b"])

        self.assertTrue(result.problem.goals[0].is_false())

    def test_rejects_a_multi_argument_initial_value_collision(self):
        problem = Problem("collision")
        item = UserType("collision_item")
        value = Fluent("value", IntType(), left=item, right=item)
        problem.add_fluent(value)
        a = problem.add_object("a", item)
        b = problem.add_object("b", item)
        problem.set_initial_value(value(a, b), 1)
        problem.set_initial_value(value(b, a), 2)

        with self.assertRaisesRegex(AbstractionError, "conflicting initial values"):
            abstract_problem(problem, ["a", "b"])

    def test_deduplicates_equal_initial_values(self):
        problem = Problem("equal-values")
        item = UserType("equal_value_item")
        value = Fluent("value", IntType(), target=item)
        problem.add_fluent(value)
        a = problem.add_object("a", item)
        b = problem.add_object("b", item)
        problem.set_initial_value(value(a), 1)
        problem.set_initial_value(value(b), 1)

        result = abstract_problem(problem, ["a", "b"])
        abstract_object = result.problem.object("equal_value_item_abs")
        abstract_value = value(abstract_object)

        self.assertEqual(result.problem.initial_value(abstract_value).constant_value(), 1)
        self.assertEqual(sum(fluent.fluent() == value for fluent in result.problem.explicit_initial_values), 1)

    def test_rejects_boolean_initial_value_collisions(self):
        problem = Problem("boolean-collision")
        item = UserType("boolean_collision_item")
        ready = Fluent("ready", BoolType(), target=item)
        problem.add_fluent(ready, default_initial_value=False)
        a = problem.add_object("a", item)
        b = problem.add_object("b", item)
        problem.set_initial_value(ready(a), True)
        problem.set_initial_value(ready(b), False)

        with self.assertRaisesRegex(AbstractionError, "contradictory initial facts"):
            abstract_problem(problem, ["a", "b"])

    def test_rejects_invalid_manual_selections(self):
        problem = Problem("selection")
        item = UserType("selection_item")
        place = UserType("selection_place")
        problem.add_object("a", item)
        problem.add_object("b", item)
        problem.add_object("p", place)

        cases = (
            (("a",), "At least two"),
            (("a", "missing"), "Unknown problem objects"),
            (("a", "p"), "same declared type"),
        )
        for objects, message in cases:
            with self.subTest(objects=objects), self.assertRaisesRegex(AbstractionError, message):
                abstract_problem(problem, objects)

    def test_rejects_model_features_the_copier_does_not_support(self):
        temporal = Problem("temporal")
        temporal_item = UserType("temporal_item")
        temporal.add_object("a", temporal_item)
        temporal.add_object("b", temporal_item)
        wait = DurativeAction("wait")
        wait.set_fixed_duration(1)
        temporal.add_action(wait)

        with self.assertRaisesRegex(AbstractionError, "temporal planning"):
            abstract_problem(temporal, ["a", "b"])

        optimized = Problem("unsupported-metric")
        optimized_item = UserType("optimized_item")
        optimized.add_object("a", optimized_item)
        optimized.add_object("b", optimized_item)
        score = Fluent("score", IntType())
        optimized.add_fluent(score, default_initial_value=0)
        optimized.add_quality_metric(MaximizeExpressionOnFinalState(score))

        with self.assertRaisesRegex(AbstractionError, "quality metric"):
            abstract_problem(optimized, ["a", "b"])

    def test_rewrites_every_supported_expression_location(self):
        problem = Problem("expressions")
        item = UserType("expression_item")
        a = problem.add_object("a", item)
        b = problem.add_object("b", item)
        marked = Fluent("marked", BoolType(), target=item)
        cost = Fluent("cost", IntType(), target=item)
        problem.add_fluent(marked, default_initial_value=False)
        problem.add_fluent(cost, default_initial_value=0)

        variable = Variable("candidate", item)
        action = InstantaneousAction("act")
        action.add_precondition(marked(a))
        action.add_effect(marked(variable), True, marked(b), forall=(variable,))
        problem.add_action(action)
        problem.add_goal(marked(b))
        problem.add_trajectory_constraint(Always(marked(a)))
        problem.add_quality_metric(MinimizeActionCosts({action: cost(a)}))

        result = abstract_problem(problem, ["a", "b"])
        abstract_object = result.problem.object("expression_item_abs")
        copied_action = result.problem.action("act")
        copied_effect = copied_action.effects[0]
        metric = result.problem.quality_metrics[0]

        self.assertEqual(copied_action.preconditions, [marked(abstract_object)])
        self.assertEqual(copied_effect.condition, marked(abstract_object))
        self.assertEqual(len(copied_effect.forall), 1)
        self.assertEqual(result.problem.goals, [marked(abstract_object)])
        self.assertEqual(result.problem.trajectory_constraints[0].arg(0), marked(abstract_object))
        self.assertEqual(metric.costs[copied_action], cost(abstract_object))


if __name__ == "__main__":
    unittest.main()
