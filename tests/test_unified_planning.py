import tempfile
import unittest
from pathlib import Path

from core.integrations.unified_planning import PddlError, parse_problem, read_problem, write_problem

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


class UnifiedPlanningCodecTests(unittest.TestCase):
    def test_round_trips_a_task_with_action_costs(self):
        source = parse_problem(ROUND_TRIP_DOMAIN, ROUND_TRIP_PROBLEM)

        serialized = write_problem(source)
        reparsed = parse_problem(serialized.domain, serialized.problem)

        self.assertEqual(len(reparsed.actions), len(source.actions))
        self.assertEqual(len(list(reparsed.all_objects)), len(list(source.all_objects)))
        self.assertEqual([type(metric).__name__ for metric in reparsed.quality_metrics], ["MinimizeActionCosts"])

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
