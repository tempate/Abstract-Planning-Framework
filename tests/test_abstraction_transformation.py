import unittest
from unittest.mock import patch

from unified_planning.shortcuts import (
    Always,
    BoolType,
    DurativeAction,
    Fluent,
    InstantaneousAction,
    IntType,
    MaximizeExpressionOnFinalState,
    MinimizeActionCosts,
    MinimizeSequentialPlanLength,
    Problem,
    UserType,
    Variable,
)

from core.integrations.unified_planning import parse_problem, write_problem
from core.abstraction.factory import AbstractionError, build_abstract_problem
from core.planning.config import AbstractPlanningConfig

ABSTRACTION_DOMAIN = """
(define (domain inventory)
  (:requirements :strips :typing)
  (:types item)
  (:predicates
    (available ?x - item)
    (eligible ?x - item)
    (reserved ?x - item)
    (used ?x - item))
  (:action consume
    :parameters (?x - item)
    :precondition (and (available ?x) (eligible ?x))
    :effect (and (not (available ?x)) (used ?x)))
  (:action release
    :parameters (?x - item)
    :precondition (and (available ?x) (reserved ?x))
    :effect (not (available ?x))))
"""

ABSTRACTION_PROBLEM = """
(define (problem inventory-task)
  (:domain inventory)
  (:objects item-a item-b item-c - item)
  (:init
    (available item-a)
    (available item-b)
    (available item-c)
    (eligible item-a)
    (eligible item-b)
    (reserved item-c))
  (:goal (and (used item-a) (used item-b))))
"""


def _build_from_problem(problem, objects_to_abstract, abstract_name=None):
    config = AbstractPlanningConfig(
        "domain.pddl", "problem.pddl", objects_to_abstract=objects_to_abstract, abstract_name=abstract_name
    )
    with patch("core.abstraction.factory.read_problem", return_value=problem):
        return build_abstract_problem(config)


class AbstractionTransformationTests(unittest.TestCase):
    def test_collapses_objects_without_mutating_source(self):
        source = parse_problem(ABSTRACTION_DOMAIN, ABSTRACTION_PROBLEM)
        source_objects = tuple(item.name for item in source.all_objects)

        result = _build_from_problem(source, ["item-a", "item-b"], "pooled-item")

        self.assertEqual(tuple(item.name for item in source.all_objects), source_objects)
        result_objects = {item.name for item in result.problem.all_objects}
        self.assertTrue({"item-a", "item-b"}.isdisjoint(result_objects))
        self.assertEqual(result_objects, {"item-c", "pooled-item"})
        self.assertEqual(result.abstraction.object_type, "item")
        self.assertEqual([item.action for item in result.relaxed_deletes], ["consume"])
        serialized = write_problem(result.problem)
        for selected in ("item-a", "item-b"):
            self.assertNotIn(selected, serialized.problem)
        parse_problem(serialized.domain, serialized.problem)

    def test_preserves_deletes_when_static_facts_make_an_action_inapplicable(self):
        source = parse_problem(ABSTRACTION_DOMAIN, ABSTRACTION_PROBLEM)

        result = _build_from_problem(source, ["item-a", "item-b"], "pooled-item")

        self.assertEqual([item.action for item in result.relaxed_deletes], ["consume"])
        release = result.problem.action("release")
        self.assertTrue(
            any(
                effect.fluent.is_fluent_exp() and effect.fluent.fluent().name == "available" and effect.value.is_false()
                for effect in release.effects
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
        result = _build_from_problem(source, ["a", "b"])

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
            _build_from_problem(problem, ["a", "b"])

    def test_deduplicates_equal_initial_values(self):
        problem = Problem("equal-values")
        item = UserType("equal_value_item")
        value = Fluent("value", IntType(), target=item)
        problem.add_fluent(value)
        a = problem.add_object("a", item)
        b = problem.add_object("b", item)
        problem.set_initial_value(value(a), 1)
        problem.set_initial_value(value(b), 1)

        result = _build_from_problem(problem, ["a", "b"])
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
            _build_from_problem(problem, ["a", "b"])

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
                _build_from_problem(problem, objects)

    def test_rejects_abstract_names_that_collide_with_model_symbols(self):
        problem = Problem("name-collision")
        item = UserType("collision_item")
        ready = Fluent("ready", BoolType())
        use = InstantaneousAction("use")
        problem.add_fluent(ready)
        problem.add_action(use)
        problem.add_object("a", item)
        problem.add_object("b", item)
        problem.add_object("taken", item)

        for name in ("taken", "ready", "use", "collision_item"):
            with self.subTest(name=name), self.assertRaisesRegex(AbstractionError, "already used"):
                _build_from_problem(problem, ["a", "b"], name)

        result = _build_from_problem(problem, ["a", "b"], "a")
        self.assertEqual({item.name for item in result.problem.all_objects}, {"a", "taken"})

    def test_rejects_model_features_the_copier_does_not_support(self):
        temporal = Problem("temporal")
        temporal_item = UserType("temporal_item")
        temporal.add_object("a", temporal_item)
        temporal.add_object("b", temporal_item)
        wait = DurativeAction("wait")
        wait.set_fixed_duration(1)
        temporal.add_action(wait)

        with self.assertRaisesRegex(AbstractionError, "temporal planning"):
            _build_from_problem(temporal, ["a", "b"])

        optimized = Problem("unsupported-metric")
        optimized_item = UserType("optimized_item")
        optimized.add_object("a", optimized_item)
        optimized.add_object("b", optimized_item)
        score = Fluent("score", IntType())
        optimized.add_fluent(score, default_initial_value=0)
        optimized.add_quality_metric(MaximizeExpressionOnFinalState(score))

        with self.assertRaisesRegex(AbstractionError, "quality metric"):
            _build_from_problem(optimized, ["a", "b"])

    def test_rewrites_conditions_goals_constraints_and_action_costs(self):
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

        result = _build_from_problem(problem, ["a", "b"])
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

    def test_preserves_numeric_effects_and_plan_length_metric(self):
        problem = Problem("numeric-effects")
        item = UserType("numeric_item")
        a = problem.add_object("a", item)
        b = problem.add_object("b", item)
        level = Fluent("level", IntType(), target=item)
        problem.add_fluent(level, default_initial_value=0)

        increase = InstantaneousAction("increase")
        increase.add_increase_effect(level(a), 1)
        problem.add_action(increase)
        decrease = InstantaneousAction("decrease")
        decrease.add_decrease_effect(level(b), 1)
        problem.add_action(decrease)
        problem.add_quality_metric(MinimizeSequentialPlanLength())

        result = _build_from_problem(problem, ["a", "b"])
        abstract_object = result.problem.object("numeric_item_abs")
        increased = result.problem.action("increase").effects[0]
        decreased = result.problem.action("decrease").effects[0]

        self.assertTrue(increased.is_increase())
        self.assertEqual(increased.fluent, level(abstract_object))
        self.assertTrue(decreased.is_decrease())
        self.assertEqual(decreased.fluent, level(abstract_object))
        self.assertIsInstance(result.problem.quality_metrics[0], MinimizeSequentialPlanLength)


if __name__ == "__main__":
    unittest.main()
