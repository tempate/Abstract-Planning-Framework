import tempfile
import unittest
from pathlib import Path

from core.integrations.unified_planning import (
    PddlError,
    parse_problem,
    read_problem,
    to_positive_normal_form,
    write_problem,
)

ROUND_TRIP_DOMAIN = """
(define (domain travel)
  (:requirements :strips :typing :action-costs)
  (:types location)
  (:predicates (at ?x - location) (connected ?from ?to - location))
  (:functions (total-cost))
  (:action move
    :parameters (?from ?to - location)
    :precondition (and (at ?from) (connected ?from ?to))
    :effect (and
      (not (at ?from))
      (at ?to)
      (increase (total-cost) 1))))
"""

ROUND_TRIP_PROBLEM = """
(define (problem travel-task)
  (:domain travel)
  (:objects start destination - location)
  (:init
    (at start)
    (connected start destination)
    (= (total-cost) 0))
  (:goal (at destination))
  (:metric minimize (total-cost)))
"""

SHARED_NAME_DOMAIN = """
(define (domain shared-name)
  (:requirements :strips :typing)
  (:types cart)
  (:predicates (parked ?item - cart)))
"""

SHARED_NAME_PROBLEM = """
(define (problem shared-name-task)
  (:domain shared-name)
  (:objects cart - cart)
  (:init (parked cart))
  (:goal (parked cart)))
"""


class UnifiedPlanningCodecTests(unittest.TestCase):
    def test_allows_different_model_elements_to_share_a_name(self):
        with self.assertWarnsRegex(UserWarning, "Name cart already defined"):
            problem = parse_problem(SHARED_NAME_DOMAIN, SHARED_NAME_PROBLEM)

        self.assertEqual(problem.object("cart").type.name, "cart")

    def test_round_trips_a_task_with_action_costs(self):
        source = parse_problem(ROUND_TRIP_DOMAIN, ROUND_TRIP_PROBLEM)

        serialized = write_problem(source)
        reparsed = parse_problem(serialized.domain, serialized.problem)

        self.assertEqual([action.name for action in reparsed.actions], ["move"])
        move = reparsed.action("move")
        self.assertEqual([parameter.name for parameter in move.parameters], ["from", "to"])
        self.assertEqual(len(move.preconditions), 1)
        self.assertEqual(len(move.effects), 2)

        self.assertEqual({item.name for item in reparsed.all_objects}, {"start", "destination"})
        at = reparsed.fluent("at")
        self.assertTrue(reparsed.initial_value(at(reparsed.object("start"))).is_true())
        self.assertEqual(reparsed.goals, [at(reparsed.object("destination"))])

        self.assertEqual([type(metric).__name__ for metric in reparsed.quality_metrics], ["MinimizeActionCosts"])
        metric = reparsed.quality_metrics[0]
        self.assertEqual(metric.costs[move].constant_value(), 1)
        self.assertEqual(metric.default.constant_value(), 0)

    def test_wraps_reader_failures(self):
        domain = "(define (domain d) (:predicates (ready))"
        problem = "(define (problem p) (:domain d) (:init) (:goal (ready)))"

        with tempfile.TemporaryDirectory() as directory:
            domain_path = Path(directory, "domain.pddl")
            problem_path = Path(directory, "problem.pddl")
            domain_path.write_text(domain, encoding="utf-8")
            problem_path.write_text(problem, encoding="utf-8")
            with self.assertRaisesRegex(PddlError, "Could not parse"):
                read_problem(domain_path, problem_path)


if __name__ == "__main__":
    unittest.main()


NEGATION_DOMAIN = """
(define (domain doors)
  (:requirements :strips :typing :equality)
  (:types room)
  (:predicates (at ?r - room) (locked ?r - room) (linked ?a ?b - room))
  (:action move
    :parameters (?from ?to - room)
    :precondition (and (at ?from) (not (locked ?to)) (not (= ?from ?to)))
    :effect (and (not (at ?from)) (at ?to)))
  (:action lock
    :parameters (?r - room)
    :precondition (at ?r)
    :effect (locked ?r)))
"""

NEGATION_PROBLEM = """
(define (problem doors-task)
  (:domain doors)
  (:objects hall study - room)
  (:init (at hall) (linked hall study))
  (:goal (at study)))
"""


class PositiveNormalFormTests(unittest.TestCase):
    def test_translation_leaves_no_condition_negating_a_fluent(self):
        problem = parse_problem(NEGATION_DOMAIN, NEGATION_PROBLEM)

        translated = to_positive_normal_form(problem)

        self.assertFalse(translated.kind.has_negative_conditions())

    def test_translation_keeps_the_actions_the_refinement_maps_back(self):
        problem = parse_problem(NEGATION_DOMAIN, NEGATION_PROBLEM)

        translated = to_positive_normal_form(problem)

        self.assertEqual(
            [(action.name, len(action.parameters)) for action in translated.actions],
            [(action.name, len(action.parameters)) for action in problem.actions],
        )

    def test_the_complement_starts_opposite_to_the_fluent_it_mirrors(self):
        problem = parse_problem(NEGATION_DOMAIN, NEGATION_PROBLEM)

        translated = to_positive_normal_form(problem)

        complements = [fluent for fluent in translated.fluents if fluent.name.startswith("not_locked")]
        self.assertEqual(len(complements), 1)
        values = translated.initial_values
        for room in translated.objects(translated.user_type("room")):
            locked = translated.environment.expression_manager.FluentExp(translated.fluent("locked"), (room,))
            complement = translated.environment.expression_manager.FluentExp(complements[0], (room,))
            self.assertNotEqual(values[locked].bool_constant_value(), values[complement].bool_constant_value())
