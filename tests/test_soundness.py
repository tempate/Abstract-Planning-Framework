import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from unified_planning.engines.plan_validator import SequentialPlanValidator
from unified_planning.engines.results import ValidationResultStatus
from unified_planning.plans import ActionInstance, SequentialPlan
from unified_planning.shortcuts import SequentialSimulator

from core.pipeline.abstraction.abstract_task import build_abstract_task
from core.pipeline.abstraction.relaxation import SPLIT_SEPARATOR
from core.integrations.unified_planning import parse_problem
from core.utilities.plan import PlanAction
from core.pipeline.solve import solve
from core.integrations.fast_downward import LAMA, LMCUT, find_pddl_plan
from core.integrations.paths import PARTIAL_GROUNDING_TRANSLATOR
from core.pipeline.refinement.refine import _with_original_names
from core.planners.asp import Asp
from core.planners.fd import FastDownward
from scripts.utils.arguments import find_domain
from core.utilities.config import AbstractPlanningConfig, PlanningConfig

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


def _abstract_plan_on(problem, steps, rename):
    """The plan on the abstraction, each step taking the copy of its action that applies."""
    actions = []
    with SequentialSimulator(problem=problem) as simulator:
        state = simulator.get_initial_state()
        for name, *args in steps:
            objects = [problem.object(rename.get(arg, arg)) for arg in args]
            copies = [action for action in problem.actions if action.name.split(SPLIT_SEPARATOR)[0] == name]
            applicable = [
                ActionInstance(action, objects)
                for action in copies
                if simulator.is_applicable(state, ActionInstance(action, objects))
            ]
            # A step no copy can take is a lost plan, which the validation reports.
            instance = applicable[0] if applicable else ActionInstance(copies[0], objects)
            actions.append(instance)
            if applicable:
                state = simulator.apply(state, instance)
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

    def _config(self, objects, planner="asp"):
        return AbstractPlanningConfig(self.domain, self.problem, planner=planner, objects_to_abstract=objects)

    def test_every_concrete_plan_is_a_plan_of_the_abstraction(self):
        """What lets an abstraction without a plan prove the task unsolvable."""
        self.assertTrue(_is_valid(self.concrete, _plan_on(self.concrete, PLAN)))
        for objects in CLASSES:
            with self.subTest(objects=objects):
                with redirect_stdout(StringIO()):
                    abstract = build_abstract_task(self._config(objects))
                rename = dict.fromkeys(objects, abstract.collapsed_set.name)

                self.assertTrue(_is_valid(abstract.problem, _abstract_plan_on(abstract.problem, PLAN, rename)))

    @unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
    def test_the_refined_plan_solves_the_concrete_task(self):
        for objects in CLASSES:
            for planner in ("asp", "lama"):
                with self.subTest(objects=objects, planner=planner):
                    with redirect_stdout(StringIO()):
                        result = solve(self._config(objects, planner))
                    steps = [(action.name, *action.args) for action in result["plan"]]

                    self.assertTrue(_is_valid(self.concrete, _plan_on(self.concrete, steps)), steps)


BENCHMARKS = Path(__file__).resolve().parents[1] / "experiments" / "benchmarks" / "downward-benchmarks"
# Each collapses part of a type, so actions split, and quantum-layout also needs PNF.
REAL_TASKS = (
    ("gripper", "prob01.pddl", ("ball1", "ball2")),
    ("driverlog", "p01.pddl", ("s0", "s1")),
    ("quantum-layout-sat23-strips", "p14.pddl", ("p4", "p9")),
)


@unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
class RealDomainSoundnessTests(unittest.TestCase):
    def test_a_baseline_plan_renamed_is_a_plan_of_the_abstraction(self):
        for domain_name, problem_name, objects in REAL_TASKS:
            with self.subTest(domain=domain_name, objects=objects):
                problem_path = BENCHMARKS / domain_name / problem_name
                domain_path = find_domain(problem_path)
                with tempfile.TemporaryDirectory() as directory:
                    lines = find_pddl_plan(directory, domain_path, problem_path, "baseline", LAMA)
                steps = [line.strip("()").split() for line in lines]
                config = AbstractPlanningConfig(domain_path, problem_path, objects_to_abstract=objects)

                with redirect_stdout(StringIO()):
                    abstract = build_abstract_task(config)
                rename = dict.fromkeys(objects, abstract.collapsed_set.name)

                self.assertTrue(any(SPLIT_SEPARATOR in action.name for action in abstract.problem.actions))
                self.assertTrue(_is_valid(abstract.problem, _abstract_plan_on(abstract.problem, steps, rename)))


@unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
class OptimalRefinementTests(unittest.TestCase):
    def test_an_optimal_abstract_plan_refines_into_an_optimal_plan(self):
        problem_path = BENCHMARKS / "gripper" / "prob01.pddl"
        domain_path = find_domain(problem_path)
        with redirect_stdout(StringIO()):
            optimum = len(FastDownward(LMCUT, PlanningConfig(domain_path, problem_path)).solve()["plan"])

            for planner in ("asp", "lmcut"):
                with self.subTest(planner=planner):
                    config = AbstractPlanningConfig(
                        domain_path,
                        problem_path,
                        planner=planner,
                        optimize=True,
                        objects_to_abstract=("ball1", "ball2"),
                    )
                    self.assertEqual(len(solve(config)["plan"]), optimum)


# Two lights to switch on, and a tick that undoes no light, so a step can stay
# busy. The goal needs the tick, or the translator would drop it.
LIGHTS_DOMAIN = """
(define (domain lights)
  (:requirements :strips :typing)
  (:types light)
  (:predicates (on ?l - light) (off ?l - light) (ticked))
  (:action switch-on
    :parameters (?l - light)
    :precondition (off ?l)
    :effect (and (on ?l) (not (off ?l))))
  (:action tick
    :parameters ()
    :precondition (and)
    :effect (ticked)))
"""
LIGHTS_PROBLEM = """
(define (problem both-on)
  (:domain lights)
  (:objects l1 l2 - light)
  (:init (off l1) (off l2))
  (:goal (and (on l1) (on l2) (ticked))))
"""


@unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
class RefinementTests(unittest.TestCase):
    """Refinement given an abstract plan, standing in for the abstract planner's."""

    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.domain = Path(directory.name, "domain.pddl")
        self.problem = Path(directory.name, "problem.pddl")
        self.domain.write_text(LIGHTS_DOMAIN, encoding="utf-8")
        self.problem.write_text(LIGHTS_PROBLEM, encoding="utf-8")
        self.concrete = parse_problem(LIGHTS_DOMAIN, LIGHTS_PROBLEM)

    def _refine(self, abstract_steps, optimize, partial_grounder=PARTIAL_GROUNDING_TRANSLATOR):
        config = AbstractPlanningConfig(
            self.domain, self.problem, planner="asp", optimize=optimize, objects_to_abstract=("l1", "l2")
        )
        with redirect_stdout(StringIO()):
            light = build_abstract_task(config).collapsed_set.name
        plan = tuple(
            PlanAction(name, (light,) if name == "switch-on" else (), step)
            for step, name in enumerate(abstract_steps, 1)
        )
        with (
            patch.object(Asp, "plan_sas", return_value=plan),
            patch("core.pipeline.refinement.refine.PARTIAL_GROUNDING_TRANSLATOR", partial_grounder),
            redirect_stdout(StringIO()),
        ):
            result = solve(config)

        steps = [(action.name, *action.args) for action in result["plan"]]
        self.assertTrue(_is_valid(self.concrete, _plan_on(self.concrete, steps)), steps)
        return [name for name, *_ in steps], result["metrics"]

    def test_a_plan_that_refines_as_it_is_keeps_every_step(self):
        names, _ = self._refine(["switch-on", "tick", "switch-on"], optimize=True)

        self.assertEqual(names, ["switch-on", "tick", "switch-on"])

    def test_refinement_gives_up_the_last_steps_first(self):
        # No light is left for the third switch-on, so its step is the one given up.
        names, metrics = self._refine(["switch-on", "switch-on", "switch-on"], optimize=True)

        self.assertEqual(names, ["switch-on", "switch-on", "tick"])
        self.assertEqual(metrics["counters"]["switches_off"], 1)

    def test_the_horizon_rises_only_once_every_step_is_given_up(self):
        names, metrics = self._refine(["switch-on", "switch-on"], optimize=True)

        self.assertEqual(sorted(names), ["switch-on", "switch-on", "tick"])
        self.assertEqual(metrics["counters"]["switches_off"], 2)
        self.assertEqual(metrics["counters"]["increments"], 1)

    def test_a_gap_holds_an_action_the_abstract_plan_lacks(self):
        names, metrics = self._refine(["switch-on"], optimize=False)

        self.assertEqual(sorted(names), ["switch-on", "switch-on", "tick"])
        self.assertEqual(metrics["counters"]["increments"], 0)

    def test_the_whole_task_is_grounded_when_the_partial_grounder_is_missing(self):
        runs = {"missing": self._refine(["switch-on", "switch-on"], optimize=False, partial_grounder="/nonexistent")}
        if Path(PARTIAL_GROUNDING_TRANSLATOR).exists():
            runs["present"] = self._refine(["switch-on", "switch-on"], optimize=False)

        for grounder, (names, metrics) in runs.items():
            with self.subTest(grounder=grounder):
                self.assertEqual(sorted(names), ["switch-on", "switch-on", "tick"])
                self.assertEqual("partial_fd" in metrics["durations"], grounder == "present")


class AbstractNameTests(unittest.TestCase):
    def test_refinement_reads_the_abstract_plan_in_the_concrete_task_s_names(self):
        abstract_plan = (PlanAction(f"carry{SPLIT_SEPARATOR}3", ("k",), 1), PlanAction("up_0", ("k",), 2))

        renamed = _with_original_names(abstract_plan, {"up_0": "up"})

        self.assertEqual([action.name for action in renamed], ["carry", "up"])


if __name__ == "__main__":
    unittest.main()
