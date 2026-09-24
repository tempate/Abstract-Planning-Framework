import unittest

from core.abstraction.factory import _create_abstraction
from core.abstraction.relaxation import find_relaxable_deletes
from core.abstraction.statistics import describe_class, describe_relaxation
from core.integrations.unified_planning import parse_problem

DOMAIN = """
(define (domain depot)
  (:requirements :strips :typing)
  (:types crate place)
  (:predicates
    (at ?c - crate ?p - place)
    (clear ?c - crate)
    (linked ?a - place ?b - place))
  (:action move
    :parameters (?c - crate ?from - place ?to - place)
    :precondition (and (at ?c ?from) (clear ?c) (linked ?from ?to))
    :effect (and (at ?c ?to) (not (at ?c ?from))))
  (:action stack
    :parameters (?c - crate ?d - crate)
    :precondition (and (clear ?c) (clear ?d) (not (= ?c ?d)))
    :effect (not (clear ?d))))
"""

PROBLEM = """
(define (problem depot-task)
  (:domain depot)
  (:objects
    crate-a crate-b crate-c crate-d - crate
    depot-1 depot-2 siding-1 siding-2 - place)
  (:init
    (linked depot-1 depot-2)
    (linked depot-2 depot-1)
    (linked siding-1 siding-2)
    (linked siding-2 siding-1)
    (at crate-a depot-1)
    (at crate-b depot-1)
    (at crate-c depot-1)
    (at crate-d depot-2)
    (clear crate-a)
    (clear crate-b)
    (clear crate-c)
    (clear crate-d))
  (:goal (and (at crate-a depot-2) (at crate-b depot-2) (at crate-c depot-2) (at crate-d depot-2))))
"""


def _describe(object_names):
    problem = parse_problem(DOMAIN, PROBLEM)
    abstraction = _create_abstraction(problem, object_names, None)
    return problem, abstraction, describe_class(problem, abstraction)


class SharedStateTests(unittest.TestCase):
    def test_a_class_that_starts_alike_shares_its_whole_initial_state(self):
        _problem, _abstraction, statistics = _describe(["crate-a", "crate-b"])

        self.assertEqual(statistics["ratios"]["shared_initial_state"], 1.0)

    def test_the_odd_object_out_lowers_the_share(self):
        """Three crates start in depot-1 and the fourth in depot-2."""
        _problem, _abstraction, statistics = _describe(["crate-a", "crate-b", "crate-c", "crate-d"])

        self.assertEqual(statistics["ratios"]["shared_initial_state"], 0.75)

    def test_a_class_with_one_goal_between_them_shares_it(self):
        _problem, _abstraction, statistics = _describe(["crate-a", "crate-d"])

        self.assertEqual(statistics["ratios"]["shared_goal"], 1.0)

    def test_objects_are_alike_when_only_their_peers_tell_them_apart(self):
        """The sidings appear only in the two links that name each other."""
        _problem, _abstraction, statistics = _describe(["siding-1", "siding-2"])

        self.assertEqual(statistics["ratios"]["shared_initial_state"], 1.0)

    def test_a_peer_is_not_mistaken_for_any_other_object(self):
        """The depots carry the same links but different crates."""
        _problem, _abstraction, statistics = _describe(["depot-1", "depot-2"])

        self.assertEqual(statistics["ratios"]["shared_initial_state"], 0.5)


class ClassShapeTests(unittest.TestCase):
    def test_the_class_is_measured_against_the_whole_problem(self):
        _problem, _abstraction, statistics = _describe(["crate-a", "crate-b"])

        self.assertEqual(statistics["counters"]["problem_object_count"], 8)

    def test_only_the_actions_that_can_bind_the_class_are_counted(self):
        _problem, _abstraction, statistics = _describe(["depot-1", "depot-2"])

        self.assertEqual(statistics["counters"]["actions_binding_class"], 1)

    def test_an_inequality_counts_once_the_class_can_reach_it(self):
        _problem, _abstraction, crates = _describe(["crate-a", "crate-b"])
        _problem, _abstraction, places = _describe(["depot-1", "depot-2"])

        self.assertEqual(crates["counters"]["class_inequalities"], 1)
        self.assertEqual(places["counters"]["class_inequalities"], 0)


class RelaxationTests(unittest.TestCase):
    def test_a_delete_of_a_one_argument_predicate_counts_as_unary(self):
        problem, abstraction, _statistics = _describe(["crate-a", "crate-b"])
        relaxed = find_relaxable_deletes(problem, abstraction)

        statistics = describe_relaxation(problem, abstraction, relaxed)

        self.assertEqual(statistics["unary_relaxed_deletes"], 1)

    def test_every_delete_the_class_reaches_is_counted_beside_the_relaxed_ones(self):
        problem, abstraction, _statistics = _describe(["crate-a", "crate-b"])
        relaxed = find_relaxable_deletes(problem, abstraction)

        statistics = describe_relaxation(problem, abstraction, relaxed)

        self.assertGreaterEqual(statistics["class_deletes"], len(relaxed))


if __name__ == "__main__":
    unittest.main()
