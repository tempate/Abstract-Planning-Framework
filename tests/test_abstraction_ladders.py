import unittest
from unittest.mock import patch

from core.abstraction.factory import _select_abstraction, build_abstract_problem
from core.abstraction.ladders import find_ladders
from core.integrations.unified_planning import parse_problem
from core.planning.config import AbstractPlanningConfig

LADDER_DOMAIN = """
(define (domain ladder)
  (:requirements :strips :typing)
  (:types truck level cargo)
  (:predicates
    (fuel ?t - truck ?l - level)
    (next ?before ?after - level)
    (loaded ?c - cargo))
  (:action burn
    :parameters (?t - truck ?before ?after - level)
    :precondition (and (fuel ?t ?before) (next ?after ?before))
    :effect (and (not (fuel ?t ?before)) (fuel ?t ?after)))
  (:action load
    :parameters (?c - cargo)
    :precondition (not (loaded ?c))
    :effect (loaded ?c)))
"""

LADDER_PROBLEM = """
(define (problem ladder-task)
  (:domain ladder)
  (:objects
    t0 - truck
    l0 l1 l2 l3 l4 - level
    c0 c1 c2 c3 c4 c5 - cargo)
  (:init
    (fuel t0 l4)
    (next l0 l1)
    (next l1 l2)
    (next l2 l3)
    (next l3 l4))
  (:goal (and (loaded c0) (loaded c1))))
"""


class LadderDetectionTests(unittest.TestCase):
    def setUp(self):
        self.problem = parse_problem(LADDER_DOMAIN, LADDER_PROBLEM)

    def test_a_static_successor_relation_reports_its_rungs(self):
        ladders = find_ladders(self.problem)

        self.assertEqual(len(ladders), 1)
        self.assertEqual(ladders[0].relation, "next")
        self.assertEqual(set(ladders[0].objects), {"l0", "l1", "l2", "l3", "l4"})

    def test_a_ladder_carries_a_task_pddl_symmetries_reports_nothing_for(self):
        with (
            patch("core.abstraction.factory.read_problem", return_value=self.problem),
            patch("core.abstraction.factory.find_symmetric_object_sets", return_value=[]),
        ):
            result = build_abstract_problem(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        self.assertEqual(set(result.abstraction.objects), {"l0", "l1", "l2", "l3", "l4"})

    def test_the_ladder_wins_over_a_smaller_symmetry_class(self):
        candidates = [["c0", "c1"]]
        for ladder in find_ladders(self.problem):
            candidates.append(list(ladder.objects))

        selected, _ = _select_abstraction(self.problem, candidates)

        self.assertEqual(set(selected.objects), {"l0", "l1", "l2", "l3", "l4"})

    def test_a_larger_symmetry_class_still_wins_over_the_ladder(self):
        candidates = [["c0", "c1", "c2", "c3", "c4", "c5"]]
        for ladder in find_ladders(self.problem):
            candidates.append(list(ladder.objects))

        selected, _ = _select_abstraction(self.problem, candidates)

        self.assertEqual(set(selected.objects), {"c0", "c1", "c2", "c3", "c4", "c5"})


if __name__ == "__main__":
    unittest.main()
