import unittest
from pathlib import Path
from unittest.mock import patch

from unified_planning.shortcuts import (
    Always,
    BoolType,
    DurativeAction,
    Fluent,
    InstantaneousAction,
    IntType,
    MaximizeExpressionOnFinalState,
    MinimizeExpressionOnFinalState,
    MinimizeSequentialPlanLength,
    Problem,
    StartTiming,
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


NEGATED_PRECONDITION_DOMAIN = """
(define (domain guarded-inventory)
  (:requirements :strips :typing)
  (:types item)
  (:predicates
    (available ?x - item)
    (used ?x - item))
  (:action consume
    :parameters (?x - item)
    :precondition (and (available ?x) (not (used ?x)))
    :effect (and (not (available ?x)) (used ?x))))
"""

NEGATED_PRECONDITION_PROBLEM = """
(define (problem guarded-inventory-task)
  (:domain guarded-inventory)
  (:objects item-a item-b - item)
  (:init
    (available item-a)
    (available item-b))
  (:goal (and (used item-a) (used item-b))))
"""


def _two_object_problem(name, type_name):
    """Build a problem holding two objects `a` and `b` of one user type."""
    problem = Problem(name)
    item = UserType(type_name)
    return problem, item, problem.add_object("a", item), problem.add_object("b", item)


def _build_from_problem(problem, objects_to_abstract, abstract_name=None):
    config = AbstractPlanningConfig(
        "domain.pddl", "problem.pddl", objects_to_abstract=objects_to_abstract, abstract_name=abstract_name
    )
    with patch("core.abstraction.factory.read_problem", return_value=problem):
        return build_abstract_problem(config)


NO_NEGATION_DOMAIN = """
(define (domain arithmetic)
  (:requirements :strips :typing)
  (:types level item)
  (:predicates
    (sum ?a ?b ?c - level)
    (held ?x - item)
    (done))
  (:action pick
    :parameters (?x - item)
    :precondition (held ?x)
    :effect (done)))
"""

NO_NEGATION_PROBLEM = """
(define (problem arithmetic-task)
  (:domain arithmetic)
  (:objects a b - item l1 l2 l3 l4 l5 - level)
  (:init (held a) (held b) (sum l1 l1 l1))
  (:goal (done)))
"""

NEGATED_GOAL_PROBLEM = """
(define (problem arithmetic-task)
  (:domain arithmetic)
  (:objects a b - item l1 l2 l3 l4 l5 - level)
  (:init (held a) (held b) (sum l1 l1 l1))
  (:goal (and (done) (not (held a)))))
"""


ONLY_DELETE_DOMAIN = """
(define (domain switches)
  (:requirements :strips :typing)
  (:types item)
  (:predicates
    (ready ?x - item)
    (done))
  (:action clear
    :parameters (?x - item)
    :precondition (ready ?x)
    :effect (not (ready ?x)))
  (:action finish
    :parameters (?x - item)
    :precondition (ready ?x)
    :effect (done)))
"""

ONLY_DELETE_PROBLEM = """
(define (problem switches-task)
  (:domain switches)
  (:objects a b - item)
  (:init (ready a) (ready b))
  (:goal (done)))
"""


INEQUALITY_DOMAIN = """
(define (domain roads)
  (:requirements :strips :typing :equality)
  (:types place vehicle)
  (:predicates
    (at ?v - vehicle ?p - place)
    (linked ?a ?b - place))
  (:action drive
    :parameters (?v - vehicle ?from ?to - place)
    :precondition (and (at ?v ?from) (linked ?from ?to) (not (= ?from ?to)))
    :effect (and (at ?v ?to) (not (at ?v ?from)))))
"""

INEQUALITY_PROBLEM = """
(define (problem roads-task)
  (:domain roads)
  (:objects van truck - vehicle hall study attic - place)
  (:init
    (at van hall)
    (at truck hall)
    (linked hall study)
    (linked study attic))
  (:goal (at van attic)))
"""


class InequalityRelaxationTests(unittest.TestCase):
    def test_relaxes_an_inequality_the_collapse_would_make_false(self):
        source = parse_problem(INEQUALITY_DOMAIN, INEQUALITY_PROBLEM)

        result = _build_from_problem(source, ["hall", "study"])

        self.assertEqual([item.variables for item in result.relaxed_inequalities], [("?from", "?to")])

    def test_the_collapsed_action_survives_the_collapse(self):
        source = parse_problem(INEQUALITY_DOMAIN, INEQUALITY_PROBLEM)

        result = _build_from_problem(source, ["hall", "study"])

        drive = result.problem.action("drive")
        abstract_object = result.problem.object("place_abs")
        substitution = {drive.parameters[1]: abstract_object, drive.parameters[2]: abstract_object}
        for precondition in drive.preconditions:
            self.assertFalse(precondition.substitute(substitution).simplify().is_false())

    def test_keeps_an_inequality_over_a_type_that_is_not_collapsed(self):
        source = parse_problem(INEQUALITY_DOMAIN, INEQUALITY_PROBLEM)

        result = _build_from_problem(source, ["van", "truck"])

        self.assertEqual(result.relaxed_inequalities, ())


class PositiveNormalFormTests(unittest.TestCase):
    def test_abstracts_a_negated_precondition_in_positive_normal_form(self):
        source = parse_problem(NEGATED_PRECONDITION_DOMAIN, NEGATED_PRECONDITION_PROBLEM)

        result = _build_from_problem(source, ["item-a", "item-b"])

        self.assertFalse(result.problem.kind.has_negative_conditions())

    def test_leaves_an_already_positive_task_alone(self):
        source = parse_problem(ABSTRACTION_DOMAIN, ABSTRACTION_PROBLEM)

        result = _build_from_problem(source, ["item-a", "item-b"])

        self.assertEqual(
            sorted(fluent.name for fluent in result.problem.fluents), sorted(fluent.name for fluent in source.fluents)
        )


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

    def test_drops_an_action_whose_every_effect_was_relaxed(self):
        source = parse_problem(ONLY_DELETE_DOMAIN, ONLY_DELETE_PROBLEM)

        result = _build_from_problem(source, ["a", "b"], "pooled-item")

        self.assertEqual([action.name for action in result.problem.actions], ["finish"])
        # Fast Downward's parser rejects an action serialized without :effect.
        serialized = write_problem(result.problem)
        parse_problem(serialized.domain, serialized.problem)

    def test_rejects_a_multi_argument_initial_value_collision(self):
        problem, item, a, b = _two_object_problem("collision", "collision_item")
        value = Fluent("value", IntType(), left=item, right=item)
        problem.add_fluent(value)
        problem.set_initial_value(value(a, b), 1)
        problem.set_initial_value(value(b, a), 2)

        with self.assertRaisesRegex(AbstractionError, "conflicting initial values"):
            _build_from_problem(problem, ["a", "b"])

    def test_deduplicates_equal_initial_values(self):
        problem, item, a, b = _two_object_problem("equal-values", "equal_value_item")
        value = Fluent("value", IntType(), target=item)
        problem.add_fluent(value)
        problem.set_initial_value(value(a), 1)
        problem.set_initial_value(value(b), 1)

        result = _build_from_problem(problem, ["a", "b"])
        abstract_object = result.problem.object("equal_value_item_abs")
        abstract_value = value(abstract_object)

        self.assertEqual(result.problem.initial_value(abstract_value).constant_value(), 1)
        self.assertEqual(sum(fluent.fluent() == value for fluent in result.problem.explicit_initial_values), 1)

    def test_the_abstract_object_holds_a_fact_the_collapsed_objects_disagree_on(self):
        problem, item, a, b = _two_object_problem("boolean-collision", "boolean_collision_item")
        ready = Fluent("ready", BoolType(), target=item)
        problem.add_fluent(ready, default_initial_value=False)
        problem.set_initial_value(ready(a), True)
        problem.set_initial_value(ready(b), False)

        result = _build_from_problem(problem, ["a", "b"])

        abstract_object = result.problem.object("boolean_collision_item_abs")
        self.assertTrue(result.problem.initial_values[ready(abstract_object)].bool_constant_value())

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
        busy = Fluent("busy", BoolType(), target=temporal_item)
        temporal.add_fluent(busy, default_initial_value=False)
        wait = DurativeAction("wait")
        wait.set_fixed_duration(1)
        wait.add_effect(StartTiming(), busy(temporal.object("a")), False)
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

    def test_rewrites_conditions_goals_and_constraints(self):
        problem, item, a, b = _two_object_problem("expressions", "expression_item")
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

        result = _build_from_problem(problem, ["a", "b"])
        abstract_object = result.problem.object("expression_item_abs")
        copied_action = result.problem.action("act")
        copied_effect = copied_action.effects[0]

        self.assertEqual(copied_action.preconditions, [marked(abstract_object)])
        self.assertEqual(copied_effect.condition, marked(abstract_object))
        self.assertEqual(len(copied_effect.forall), 1)
        self.assertEqual(result.problem.goals, [marked(abstract_object)])
        self.assertEqual(result.problem.trajectory_constraints[0].arg(0), marked(abstract_object))

    def test_drops_a_cost_metric_the_writer_would_strip_anyway(self):
        problem, item, a, b = _two_object_problem("final-state-metric", "metric_item")
        cost = Fluent("cost", IntType(), target=item)
        problem.add_fluent(cost, default_initial_value=0)
        problem.add_quality_metric(MinimizeExpressionOnFinalState(cost(a) + cost(b)))

        result = _build_from_problem(problem, ["a", "b"])

        self.assertEqual(result.problem.quality_metrics, [])

    def test_preserves_numeric_effects_and_plan_length_metric(self):
        problem, item, a, b = _two_object_problem("numeric-effects", "numeric_item")
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

    def test_relaxes_a_delete_that_takes_more_than_the_collapsed_object(self):
        domain = """
(define (domain transit)
  (:requirements :strips :typing)
  (:types item place)
  (:predicates
    (at ?x - item ?p - place)
    (linked ?a - place ?b - place))
  (:action shift
    :parameters (?x - item ?from - place ?to - place)
    :precondition (and (at ?x ?from) (linked ?from ?to))
    :effect (and (at ?x ?to) (not (at ?x ?from)))))
"""
        problem_text = """
(define (problem transit-task)
  (:domain transit)
  (:objects item-a item-b - item dock stage - place)
  (:init (at item-a dock) (at item-b dock) (linked dock stage))
  (:goal (and (at item-a stage) (at item-b stage))))
"""
        source = parse_problem(domain, problem_text)

        result = _build_from_problem(source, ["item-a", "item-b"], "pooled-item")

        # Keeping the delete would drop `at` for the collapsed object while the
        # other objects it stands for are still there. Only the item argument
        # matches; `?from` is a place and must not be picked up.
        self.assertEqual([item.predicate for item in result.relaxed_deletes], ["at"])
        self.assertEqual([item.variables for item in result.relaxed_deletes], [("?x",)])
        shift = result.problem.action("shift")
        self.assertFalse(any(effect.value.is_false() for effect in shift.effects))

    def test_relaxes_a_delete_that_names_a_collapsed_object_directly(self):
        domain = """
(define (domain depot)
  (:requirements :strips :typing)
  (:types item place)
  (:constants stage - place)
  (:predicates
    (at ?x - item ?p - place)
    (ready ?x - item))
  (:action clear-stage
    :parameters (?x - item)
    :precondition (at ?x stage)
    :effect (and (ready ?x) (not (at ?x stage)))))
"""
        problem_text = """
(define (problem depot-task)
  (:domain depot)
  (:objects crate - item dock - place)
  (:init (at crate stage))
  (:goal (ready crate)))
"""
        source = parse_problem(domain, problem_text)

        result = _build_from_problem(source, ["stage", "dock"], "pooled-place")

        # `?x` is an item, so only the named place matches.
        self.assertEqual([item.predicate for item in result.relaxed_deletes], ["at"])
        self.assertEqual([item.variables for item in result.relaxed_deletes], [("stage",)])
        clear_stage = result.problem.action("clear-stage")
        self.assertFalse(any(effect.value.is_false() for effect in clear_stage.effects))

    def test_relaxes_a_named_collapsed_object_a_static_precondition_rules_out(self):
        domain = """
(define (domain wiring)
  (:requirements :strips :typing)
  (:types port)
  (:constants hub - port)
  (:predicates
    (linked ?a - port ?b - port)
    (movable ?a - port)
    (cut ?a - port))
  (:action unlink
    :parameters (?a - port)
    :precondition (and (movable ?a) (linked ?a hub))
    :effect (and (cut ?a) (not (linked ?a hub)))))
"""
        problem_text = """
(define (problem wiring-task)
  (:domain wiring)
  (:objects spur gate - port)
  (:init (movable gate) (linked gate hub) (linked spur hub))
  (:goal (cut gate)))
"""
        source = parse_problem(domain, problem_text)

        result = _build_from_problem(source, ["hub", "spur"], "pooled-port")

        # `movable` is static and holds for no collapsed object, so `?a` cannot
        # bind one. The named `hub` still makes the delete apply.
        self.assertEqual([item.predicate for item in result.relaxed_deletes], ["linked"])
        self.assertEqual([item.variables for item in result.relaxed_deletes], [("?a", "hub")])
        unlink = result.problem.action("unlink")
        self.assertFalse(any(effect.value.is_false() for effect in unlink.effects))


if __name__ == "__main__":
    unittest.main()


class PositiveNormalFormSkipTests(unittest.TestCase):
    def test_a_problem_with_no_negated_condition_does_not_gain_the_closed_world(self):
        """The translation writes out every atom it leaves false, which costs
        more than it buys when there is no negated condition to rewrite."""
        problem = parse_problem(NO_NEGATION_DOMAIN, NO_NEGATION_PROBLEM)
        before = len(problem.explicit_initial_values)

        result = _build_from_problem(problem, ["a", "b"])

        self.assertLessEqual(len(result.problem.explicit_initial_values), before)

    def test_a_negated_goal_still_reaches_positive_normal_form(self):
        """A relaxed delete can falsify a negated goal just as it can a negated
        precondition, so the skip has to see goals too."""
        problem = parse_problem(NO_NEGATION_DOMAIN, NEGATED_GOAL_PROBLEM)

        result = _build_from_problem(problem, ["a", "b"])

        self.assertFalse(result.problem.kind.has_negative_conditions())
