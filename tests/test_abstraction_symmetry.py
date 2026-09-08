import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import parse_problem, read_problem
from core.abstraction.factory import AbstractionError, NoSymmetriesError, _select_abstraction, build_abstract_problem
from core.outcomes import IntegrationError, SymmetryTimeoutError, UnsolvableTaskError
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
  (:objects item1 item2 - item gadget1 gadget2 gadget3 - gadget)
  (:init (ready item1) (ready item2) (armed item1) (armed item2) (set gadget1) (set gadget2) (set gadget3))
  (:goal (and (done gadget1) (done gadget2) (done gadget3))))
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

    def test_selection_takes_the_largest_class(self):
        # The gadgets win on size alone: they also fill every goal conjunct and
        # relax fewer deletes than the items, and neither counts.
        source = parse_problem(ORDERING_DOMAIN, ORDERING_PROBLEM)

        selected, _ = _select_abstraction(source, [["item1", "item2"], ["gadget1", "gadget2", "gadget3"]])

        self.assertEqual(set(selected.objects), {"gadget1", "gadget2", "gadget3"})

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
                AbstractPlanningConfig("domain.pddl", "problem.pddl", symmetry_time_limit=17)
            )

        find_classes.assert_called_once_with("domain.pddl", "problem.pddl", 17)
        self.assertEqual(set(result.abstraction.objects), {"vehicle-a", "vehicle-b", "vehicle-c", "vehicle-d"})
        self.assertEqual(result.abstraction.name, "vehicle_abs")

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
            with self.assertRaisesRegex(IntegrationError, "bliss is not built"):
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
            with self.assertRaisesRegex(IntegrationError, "malformed"):
                find_symmetric_object_sets(domain, problem, 10, translator)

    def test_rejects_nonpositive_symmetry_time_limit(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            find_symmetric_object_sets("d.pddl", "p.pddl", 0)

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_reports_process_timeouts(self, run):
        run.side_effect = subprocess.TimeoutExpired("translate.py", 10)
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)
            with self.assertRaisesRegex(SymmetryTimeoutError, "exceeded"):
                find_symmetric_object_sets(domain, problem, 10, translator)


@unittest.skipUnless(
    os.environ.get("RUN_PLANNER_INTEGRATION") == "1", "set RUN_PLANNER_INTEGRATION=1 to run PDDL Symmetries"
)
class RealSymmetryIntegrationTests(unittest.TestCase):
    def test_gripper_symmetries_select_the_balls(self):
        problem_path = GRIPPER / "prob01.pddl"
        classes = find_symmetric_object_sets(GRIPPER / "domain.pddl", problem_path)
        selected, _ = _select_abstraction(read_problem(GRIPPER / "domain.pddl", problem_path), classes)

        self.assertEqual({tuple(group) for group in classes}, {("ball1", "ball2", "ball3", "ball4"), ("left", "right")})
        # The goal names every ball, and the four of them still win over the two
        # grippers: collapsing them is what drops the abstract horizon.
        self.assertEqual(set(selected.objects), {"ball1", "ball2", "ball3", "ball4"})


if __name__ == "__main__":
    unittest.main()
