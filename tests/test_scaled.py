import tempfile
import unittest
from pathlib import Path

from unified_planning.io import PDDLReader

from experiments.unsat.scaled.generate import scale, scale_domain

DOMAIN = """
(define (domain dive)
  (:requirements :strips :typing)
  (:types diver place)
  (:constants d0 d1 - diver)
  (:predicates (available ?d - diver) (at ?d - diver ?p - place))
  (:action hire-diver-d0
    :parameters (?p - place)
    :precondition (available d0)
    :effect (and (at d0 ?p) (not (available d0))))
  (:action hire-diver-d1
    :parameters (?p - place)
    :precondition (available d1)
    :effect (and (at d1 ?p) (not (available d1)))))
"""

PROBLEM = """
(define (problem dive-task)
  (:domain dive)
  (:objects surface - place)
  (:init (available d0) (available d1))
  (:goal (and (at d0 surface))))
"""


class ScaledTests(unittest.TestCase):
    def test_a_copied_domain_constant_gets_its_own_actions_and_atoms(self):
        with tempfile.TemporaryDirectory() as directory:
            domain = Path(directory) / "domain.pddl"
            problem = Path(directory) / "problem.pddl"
            domain.write_text(scale_domain(DOMAIN, "d0", 2))
            problem.write_text(scale(PROBLEM, "d0", 2))
            task = PDDLReader().parse_problem(str(domain), str(problem))

        self.assertTrue({"d0-copy1", "d0-copy2"} <= {item.name for item in task.all_objects})
        self.assertTrue({"hire-diver-d0-copy1", "hire-diver-d0-copy2"} <= {action.name for action in task.actions})
        initial = {str(fluent) for fluent, value in task.explicit_initial_values.items() if value.is_true()}
        self.assertIn("available(d0-copy2)", initial)
