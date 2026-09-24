import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from unified_planning.engines.plan_validator import SequentialPlanValidator
from unified_planning.engines.results import ValidationResultStatus
from unified_planning.plans import ActionInstance, SequentialPlan

from core.abstraction.factory import build_abstract_problem
from core.integrations.clingo import parse_plan_actions
from core.integrations.unified_planning import parse_problem
from core.planning import abstraction, asp, fd
from core.planning.config import AbstractPlanningConfig

RUN_INTEGRATION = os.environ.get("RUN_PLANNER_INTEGRATION") == "1"

# Collapsing each class below loses a plan unless the collapse relaxes what it
# should: the trucks share a negated condition and their deletes, the locations
# an inequality.
DOMAIN = """
(define (domain logistics)
  (:requirements :strips :typing :negative-preconditions :equality)
  (:types package truck location)
  (:predicates (at ?p - package ?l - location) (in ?p - package ?t - truck)
               (truck-at ?t - truck ?l - location) (road ?a ?b - location) (loaded ?t - truck))
  (:action load
    :parameters (?p - package ?t - truck ?l - location)
    :precondition (and (at ?p ?l) (truck-at ?t ?l) (not (loaded ?t)))
    :effect (and (not (at ?p ?l)) (in ?p ?t) (loaded ?t)))
  (:action unload
    :parameters (?p - package ?t - truck ?l - location)
    :precondition (and (in ?p ?t) (truck-at ?t ?l))
    :effect (and (not (in ?p ?t)) (at ?p ?l) (not (loaded ?t))))
  (:action drive
    :parameters (?t - truck ?a ?b - location)
    :precondition (and (truck-at ?t ?a) (road ?a ?b) (not (= ?a ?b)))
    :effect (and (not (truck-at ?t ?a)) (truck-at ?t ?b))))
"""
PROBLEM = """
(define (problem swap)
  (:domain logistics)
  (:objects p1 p2 - package t1 t2 - truck l1 l2 l3 - location)
  (:init (at p1 l1) (at p2 l3) (truck-at t1 l1) (truck-at t2 l3)
         (road l1 l2) (road l2 l1) (road l2 l3) (road l3 l2))
  (:goal (and (at p1 l3) (at p2 l1))))
"""
# The two trucks work at once, so a collapsed truck is loaded while it loads again.
PLAN = (
    ("load", "p1", "t1", "l1"),
    ("load", "p2", "t2", "l3"),
    ("drive", "t1", "l1", "l2"),
    ("drive", "t2", "l3", "l2"),
    ("drive", "t1", "l2", "l3"),
    ("drive", "t2", "l2", "l1"),
    ("unload", "p1", "t1", "l3"),
    ("unload", "p2", "t2", "l1"),
)
CLASSES = (("p1", "p2"), ("t1", "t2"), ("l1", "l2", "l3"))


def _plan_on(problem, steps, rename=None):
    rename = rename or {}
    actions = []
    for name, *args in steps:
        objects = [problem.object(rename.get(arg, arg)) for arg in args]
        actions.append(ActionInstance(problem.action(name), objects))
    return SequentialPlan(actions)


def _is_valid(problem, plan):
    return SequentialPlanValidator().validate(problem, plan).status == ValidationResultStatus.VALID


class SoundnessTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.domain = Path(directory.name, "domain.pddl")
        self.problem = Path(directory.name, "problem.pddl")
        self.domain.write_text(DOMAIN, encoding="utf-8")
        self.problem.write_text(PROBLEM, encoding="utf-8")
        self.concrete = parse_problem(DOMAIN, PROBLEM)

    def _config(self, objects):
        return AbstractPlanningConfig(self.domain, self.problem, objects_to_abstract=objects)

    def test_every_concrete_plan_is_a_plan_of_the_abstraction(self):
        """What lets an abstraction without a plan prove the task unsolvable."""
        self.assertTrue(_is_valid(self.concrete, _plan_on(self.concrete, PLAN)))
        for objects in CLASSES:
            with self.subTest(objects=objects):
                with redirect_stdout(StringIO()):
                    abstract = build_abstract_problem(self._config(objects))
                rename = dict.fromkeys(objects, abstract.abstraction.name)

                self.assertTrue(_is_valid(abstract.problem, _plan_on(abstract.problem, PLAN, rename)))

    @unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
    def test_the_refined_plan_solves_the_concrete_task(self):
        for objects in CLASSES:
            for search in (asp.find_abstract_plan, fd.find_abstract_plan):
                with self.subTest(objects=objects, search=search.__module__):
                    with redirect_stdout(StringIO()):
                        result = abstraction.solve(self._config(objects), search)
                    steps = [(action.name, *action.args) for action in parse_plan_actions(result["plan"])]

                    self.assertTrue(_is_valid(self.concrete, _plan_on(self.concrete, steps)), steps)


if __name__ == "__main__":
    unittest.main()
