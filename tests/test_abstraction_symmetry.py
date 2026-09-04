import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.integrations.pddl_symmetries import PddlSymmetriesError, PddlSymmetriesTimeout, find_symmetric_object_sets
from core.planning.outcomes import UnsolvableTaskError
from core.integrations.unified_planning import parse_problem, read_problem
from core.abstraction.factory import AbstractionError, NoSymmetriesError, _select_abstraction, build_abstract_problem
from core.planning.config import AbstractPlanningConfig

PROJECT_ROOT = Path(__file__).resolve().parents[1]
GRIPPER = PROJECT_ROOT / "benchmarks" / "downward-benchmarks" / "gripper"

SYMMETRY_DOMAIN = """
(define (domain selection)
  (:requirements :strips :typing)
  (:types cargo tool vehicle)
  (:predicates
    (cargo-ready ?x - cargo)
    (tool-ready ?x - tool)
    (tool-free ?x - tool)
    (parked ?x - vehicle))
  (:action pack
    :parameters (?x - cargo)
    :precondition (cargo-ready ?x)
    :effect (not (cargo-ready ?x)))
  (:action equip
    :parameters (?x - tool)
    :precondition (and (tool-ready ?x) (tool-free ?x))
    :effect (and (not (tool-ready ?x)) (not (tool-free ?x)))))
"""

SYMMETRY_PROBLEM = """
(define (problem selection-task)
  (:domain selection)
  (:objects
    cargo-a cargo-b cargo-c - cargo
    tool-a tool-b - tool
    vehicle-a vehicle-b vehicle-c vehicle-d - vehicle)
  (:init
    (cargo-ready cargo-a)
    (cargo-ready cargo-b)
    (cargo-ready cargo-c)
    (tool-ready tool-a)
    (tool-ready tool-b)
    (tool-free tool-a)
    (tool-free tool-b)
    (parked vehicle-a)
    (parked vehicle-b)
    (parked vehicle-c)
    (parked vehicle-d))
  (:goal (and)))
"""


GOAL_DOMAIN = """
(define (domain goals)
  (:requirements :strips :typing)
  (:types item)
  (:predicates (ready ?x - item) (done ?x - item))
  (:action finish
    :parameters (?x - item)
    :precondition (ready ?x)
    :effect (and (done ?x) (not (ready ?x)))))
"""

GOAL_PROBLEM = """
(define (problem goals-task)
  (:domain goals)
  (:objects a1 a2 b1 b2 b3 - item)
  (:init (ready a1) (ready a2) (ready b1) (ready b2) (ready b3))
  (:goal (and (done b1) (done b2) (done b3))))
"""

ORDERING_DOMAIN = """
(define (domain ordering)
  (:requirements :strips :typing)
  (:types item gadget)
  (:predicates (ready ?x - item) (armed ?x - item) (set ?x - gadget) (done ?x - gadget))
  (:action use-item
    :parameters (?x - item)
    :precondition (ready ?x)
    :effect (and (not (ready ?x)) (not (armed ?x))))
  (:action use-gadget
    :parameters (?x - gadget)
    :precondition (set ?x)
    :effect (and (done ?x) (not (set ?x)))))
"""

ORDERING_PROBLEM = """
(define (problem ordering-task)
  (:domain ordering)
  (:objects item1 item2 - item gadget1 gadget2 - gadget)
  (:init (ready item1) (ready item2) (armed item1) (armed item2) (set gadget1) (set gadget2))
  (:goal (and (done gadget1) (done gadget2))))
"""


def _stub_symmetry_inputs(directory):
    root = Path(directory)
    translator = root / "translate.py"
    domain = root / "domain.pddl"
    problem = root / "problem.pddl"
    for path in (translator, domain, problem):
        path.write_text("", encoding="utf-8")
    return translator, domain, problem


class SymmetrySelectionTests(unittest.TestCase):
    def setUp(self):
        self.problem = parse_problem(SYMMETRY_DOMAIN, SYMMETRY_PROBLEM)

    def test_selects_the_lowest_delete_score(self):
        classes = [
            ["cargo-c", "cargo-a", "cargo-b"],
            ["tool-b", "tool-a"],
            ["vehicle-d", "vehicle-b", "vehicle-c", "vehicle-a"],
        ]
        selected, _ = _select_abstraction(self.problem, classes)

        self.assertEqual(set(selected.objects), {"vehicle-a", "vehicle-b", "vehicle-c", "vehicle-d"})

    def test_equal_scores_prefer_the_largest_class(self):
        domain = """
(define (domain d) (:types item) (:predicates (free ?x - item))
  (:action use :parameters (?x - item) :precondition (free ?x)
    :effect (not (free ?x))))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects a1 a2 b1 b2 b3 - item)
  (:init) (:goal (and)))
"""

        source = parse_problem(domain, problem)
        selected, _ = _select_abstraction(source, [["a1", "a2"], ["b1", "b2", "b3"]])

        self.assertEqual(set(selected.objects), {"b1", "b2", "b3"})

    def test_prefers_a_class_the_goal_does_not_mention(self):
        source = parse_problem(GOAL_DOMAIN, GOAL_PROBLEM)

        selected, _ = _select_abstraction(source, [["b1", "b2", "b3"], ["a1", "a2"]])

        self.assertEqual(set(selected.objects), {"a1", "a2"})

    def test_prefers_the_class_the_goal_mentions_least(self):
        problem = """
(define (problem p) (:domain goals)
  (:objects a1 a2 b1 b2 - item)
  (:init (ready a1) (ready a2) (ready b1) (ready b2))
  (:goal (and (done a1) (done b1) (done b2))))
"""
        source = parse_problem(GOAL_DOMAIN, problem)

        selected, _ = _select_abstraction(source, [["b1", "b2"], ["a1", "a2"]])

        self.assertEqual(set(selected.objects), {"a1", "a2"})

    def test_goal_conjuncts_outrank_the_relaxed_delete_count(self):
        source = parse_problem(ORDERING_DOMAIN, ORDERING_PROBLEM)

        selected, relaxable_deletes = _select_abstraction(source, [["gadget1", "gadget2"], ["item1", "item2"]])

        # The items relax two deletes against the gadgets' one, and still win.
        self.assertEqual(set(selected.objects), {"item1", "item2"})
        self.assertEqual(len(relaxable_deletes), 2)

    def test_planner_abstraction_uses_the_top_pddl_symmetries_class(self):
        classes = [
            ["cargo-a", "cargo-b", "cargo-c"],
            ["tool-a", "tool-b"],
            ["vehicle-a", "vehicle-b", "vehicle-c", "vehicle-d"],
        ]
        with (
            patch("core.abstraction.factory.read_problem", return_value=self.problem),
            patch("core.abstraction.factory.find_symmetric_object_sets", return_value=classes) as find_classes,
        ):
            result = build_abstract_problem(
                AbstractPlanningConfig(
                    "domain.pddl", "problem.pddl", abstract_name="pooled-vehicles", symmetry_time_limit=17
                )
            )

        find_classes.assert_called_once_with("domain.pddl", "problem.pddl", 17)
        self.assertEqual(set(result.abstraction.objects), {"vehicle-a", "vehicle-b", "vehicle-c", "vehicle-d"})
        self.assertEqual(result.abstraction.name, "pooled-vehicles")

    def test_rejects_tasks_without_a_pddl_symmetries_object_class(self):
        with (
            patch("core.abstraction.factory.read_problem", return_value=self.problem),
            patch("core.abstraction.factory.find_symmetric_object_sets", return_value=[]),
            patch("core.abstraction.factory._select_abstraction") as select,
        ):
            with self.assertRaisesRegex(NoSymmetriesError, "found no abstractable object classes"):
                build_abstract_problem(AbstractPlanningConfig("domain.pddl", "problem.pddl"))

        select.assert_not_called()

    def test_accepts_domain_constants_reported_by_pddl_symmetries(self):
        domain = """
(define (domain constants)
  (:requirements :strips :typing)
  (:types depot)
  (:constants depot-a depot-b - depot)
  (:predicates (open ?x - depot)))
"""
        problem = """
(define (problem constants-task)
  (:domain constants)
  (:init (open depot-a) (open depot-b))
  (:goal (open depot-a)))
"""
        selected, _ = _select_abstraction(parse_problem(domain, problem), [["depot-b", "depot-a"]])

        self.assertEqual(set(selected.objects), {"depot-a", "depot-b"})

    def test_rejects_a_symmetry_class_that_cannot_be_collapsed(self):
        with self.assertRaisesRegex(AbstractionError, "same declared type"):
            _select_abstraction(self.problem, [["cargo-a", "tool-a"]])

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_extracts_object_sets_from_translator_output(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=0, stdout="Non-trivial symmetric object sets: [['b', 'a'], ['x', 'y']]\n", stderr=""
        )
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)
            result = find_symmetric_object_sets(domain, problem, 17, translator)

        self.assertEqual(result, [["b", "a"], ["x", "y"]])
        command = run.call_args.args[0]
        self.assertIn("--only-object-symmetries", command)
        self.assertEqual(command[command.index("--bliss-time-limit") + 1], "17")
        self.assertTrue(Path(command[1]).is_absolute())
        working_directory = Path(run.call_args.kwargs["cwd"])
        self.assertNotEqual(working_directory, translator.resolve().parent)
        self.assertFalse(working_directory.exists())

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_surfaces_translator_diagnostics(self, run):
        run.return_value = subprocess.CompletedProcess(args=[], returncode=1, stdout="", stderr="bliss is not built")
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)
            with self.assertRaisesRegex(PddlSymmetriesError, "bliss is not built"):
                find_symmetric_object_sets(domain, problem, 10, translator)

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_reports_an_unsolvable_translation(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=0, stdout="Translator phase\nNo relaxed solution!\n", stderr=""
        )
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)
            with self.assertRaisesRegex(UnsolvableTaskError, "no relaxed solution"):
                find_symmetric_object_sets(domain, problem, 10, translator)

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_rejects_malformed_object_sets(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=0, stdout="Non-trivial symmetric object sets: [not valid\n", stderr=""
        )
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)
            with self.assertRaisesRegex(PddlSymmetriesError, "malformed"):
                find_symmetric_object_sets(domain, problem, 10, translator)

    def test_rejects_nonpositive_symmetry_time_limit(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            find_symmetric_object_sets("d.pddl", "p.pddl", 0)

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_reports_process_timeouts(self, run):
        run.side_effect = subprocess.TimeoutExpired("translate.py", 10)
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)
            with self.assertRaisesRegex(PddlSymmetriesTimeout, "exceeded"):
                find_symmetric_object_sets(domain, problem, 10, translator)


@unittest.skipUnless(
    os.environ.get("RUN_PLANNER_INTEGRATION") == "1", "set RUN_PLANNER_INTEGRATION=1 to run PDDL Symmetries"
)
class RealSymmetryIntegrationTests(unittest.TestCase):
    def test_gripper_symmetries_select_the_grippers(self):
        problem_path = GRIPPER / "prob01.pddl"
        classes = find_symmetric_object_sets(GRIPPER / "domain.pddl", problem_path)
        selected, _ = _select_abstraction(read_problem(GRIPPER / "domain.pddl", problem_path), classes)

        self.assertEqual({tuple(group) for group in classes}, {("ball1", "ball2", "ball3", "ball4"), ("left", "right")})
        # Both classes relax two deletes, but the goal names every ball.
        self.assertEqual(set(selected.objects), {"left", "right"})


if __name__ == "__main__":
    unittest.main()
