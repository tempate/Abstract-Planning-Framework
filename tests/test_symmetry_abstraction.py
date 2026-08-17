import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.symmetry_abstraction import (
    AbstractionError,
    abstract_task,
    find_symmetric_object_sets,
    rank_symmetry_classes,
)
from scripts.abstract_object import _argument_parser


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BELUGA_CONCRETE = PROJECT_ROOT / "data" / "benchmarks" / "beluga" / "concrete" / "standard"


def pddl_tokens(text: str) -> list[str]:
    without_comments = re.sub(r";[^\n]*", "", text)
    return [
        token.casefold()
        for token in re.findall(r"[()]|[^\s();]+", without_comments)
    ]


class ObjectAbstractionTests(unittest.TestCase):
    def test_collapses_objects_and_relaxes_compatible_unary_deletes(self):
        domain = """
(define (domain transport)
  (:requirements :typing :conditional-effects)
  (:types vehicle - location location - object)
  (:predicates (free ?location - location) (at ?x - object ?l - location))
  (:action occupy
    :parameters (?vehicle - vehicle)
    :precondition (free ?vehicle)
    :effect (and (not (free ?vehicle)) (at ?vehicle ?vehicle)))
  (:action conditional-occupy
    :parameters (?location - location)
    :precondition (and)
    :effect (when (free ?location) (not (free ?location)))))
"""
        problem = """
(define (problem sample)
  (:domain transport)
  (:objects van1 van2 - vehicle depot - location)
  (:init (free van1) (free van2))
  (:goal (and (free van1) (free van2)))
  (:constraints (always (free van1))))
"""

        result = abstract_task(domain, problem, ["van1", "van2"])

        self.assertEqual(result.abstract_name, "vehicle_abs")
        self.assertEqual(result.unary_delete_score, 2)
        self.assertNotIn("van1", result.problem_text)
        self.assertNotIn("van2", result.problem_text)
        self.assertEqual(result.problem_text.count("(free vehicle_abs)"), 3)
        self.assertIn("(always", result.problem_text)
        self.assertNotIn("(not (free", result.domain_text)
        self.assertIn("conditional-occupy", result.domain_text)

    def test_rejects_unknown_mixed_type_and_colliding_selections(self):
        domain = "(define (domain d) (:types a b) (:predicates))"
        problem = """
(define (problem p) (:domain d)
  (:objects a1 a2 existing - a b1 - b)
  (:init) (:goal (and)))
"""

        with self.assertRaisesRegex(AbstractionError, "Unknown"):
            abstract_task(domain, problem, ["a1", "missing"])
        with self.assertRaisesRegex(AbstractionError, "same declared type"):
            abstract_task(domain, problem, ["a1", "b1"])
        with self.assertRaisesRegex(AbstractionError, "already exists"):
            abstract_task(domain, problem, ["a1", "a2"], "existing")
        with self.assertRaisesRegex(AbstractionError, "Invalid PDDL object name"):
            abstract_task(domain, problem, ["a1", "a2"], "bad name")

    def test_rejects_conflicting_numeric_values_created_by_collapse(self):
        domain = """
(define (domain d)
  (:requirements :typing :fluents)
  (:types item)
  (:predicates)
  (:functions (value ?x - item)))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects x1 x2 - item)
  (:init (= (value x1) 1) (= (value x2) 2))
  (:goal (and)))
"""

        with self.assertRaisesRegex(AbstractionError, "conflicting initial values"):
            abstract_task(domain, problem, ["x1", "x2"])

    def test_hangar_output_matches_checked_in_abstraction(self):
        domain = (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8")
        problem_name = "problem_3_s45_j3_r2_oc44_f3"
        problem = (BELUGA_CONCRETE / f"{problem_name}.pddl").read_text(encoding="utf-8")

        result = abstract_task(
            domain, problem, ["hangar1", "hangar2", "hangar3"], "hangarabs",
        )
        expected_dir = PROJECT_ROOT / "data" / "benchmarks" / "beluga" / "abstract" / "hangar"

        self.assertEqual(
            pddl_tokens(result.domain_text),
            pddl_tokens((expected_dir / "domain.pddl").read_text(encoding="utf-8")),
        )
        self.assertEqual(
            pddl_tokens(result.problem_text),
            pddl_tokens((expected_dir / f"{problem_name}_abs.pddl").read_text(encoding="utf-8")),
        )

    def test_type_wide_trailer_output_matches_legacy_domain(self):
        domain = (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8")
        problem_name = "problem_3_s45_j3_r2_oc44_f3"
        problem = (BELUGA_CONCRETE / f"{problem_name}.pddl").read_text(encoding="utf-8")

        result = abstract_task(
            domain,
            problem,
            ["beluga_trailer_1", "beluga_trailer_2"],
            "beluga_abs_trailer",
        )
        expected_dir = PROJECT_ROOT / "data" / "benchmarks" / "beluga" / "abstract" / "trailer"

        self.assertEqual(result.unary_delete_score, 4)
        self.assertEqual(
            pddl_tokens(result.domain_text),
            pddl_tokens((expected_dir / "domain_legacy.pddl").read_text(encoding="utf-8")),
        )
        self.assertEqual(
            pddl_tokens(result.problem_text),
            pddl_tokens((expected_dir / f"{problem_name}_abs.pddl").read_text(encoding="utf-8")),
        )


class SymmetrySelectionTests(unittest.TestCase):
    def setUp(self):
        self.domain = (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8")
        self.problem_path = BELUGA_CONCRETE / "problem_3_s45_j3_r2_oc44_f3.pddl"
        self.problem = self.problem_path.read_text(encoding="utf-8")

    def test_ranks_by_score_then_size_then_lexical_order(self):
        classes = [
            ["factory_trailer_1", "factory_trailer_2"],
            ["hangar1", "hangar2", "hangar3"],
            ["beluga_trailer_1", "beluga_trailer_2"],
        ]

        ranked = rank_symmetry_classes(self.domain, self.problem, classes)

        self.assertEqual(ranked[0].objects, ("hangar1", "hangar2", "hangar3"))
        self.assertEqual(ranked[0].unary_delete_score, 1)
        self.assertEqual(ranked[1].objects[0], "beluga_trailer_1")
        self.assertEqual(ranked[1].unary_delete_score, 4)

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

        ranked = rank_symmetry_classes(
            domain, problem, [["a1", "a2"], ["b1", "b2", "b3"]],
        )

        self.assertEqual(ranked[0].objects, ("b1", "b2", "b3"))

    @patch("core.symmetry_abstraction.subprocess.run")
    def test_extracts_object_sets_from_translator_output(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout=(
                "translator diagnostics\n"
                "Non-trivial symmetric object sets: [['b', 'a'], ['x', 'y']]\n"
            ),
            stderr="",
        )
        with tempfile.TemporaryDirectory() as directory:
            translator = Path(directory, "translate.py")
            translator.write_text("", encoding="utf-8")

            result = find_symmetric_object_sets(
                "domain.pddl", "problem.pddl", 17, translator,
            )

        self.assertEqual(result, [["b", "a"], ["x", "y"]])
        command = run.call_args.args[0]
        self.assertIn("--only-object-symmetries", command)
        self.assertEqual(command[command.index("--bliss-time-limit") + 1], "17")

    @patch("core.symmetry_abstraction.subprocess.run")
    def test_surfaces_translator_diagnostics(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=1, stdout="", stderr="bliss is not built",
        )
        with tempfile.TemporaryDirectory() as directory:
            translator = Path(directory, "translate.py")
            translator.write_text("", encoding="utf-8")

            with self.assertRaisesRegex(RuntimeError, "bliss is not built"):
                find_symmetric_object_sets("d.pddl", "p.pddl", 10, translator)


class AbstractionArgumentTests(unittest.TestCase):
    def test_explicit_selection_arguments(self):
        args = _argument_parser().parse_args([
            "--domain", "domain.pddl",
            "--problem", "problem.pddl",
            "--output-domain", "abstract-domain.pddl",
            "--output-problem", "abstract-problem.pddl",
            "--objects", "hangar1", "hangar2",
        ])

        self.assertEqual(args.domain, Path("domain.pddl"))
        self.assertEqual(args.objects, ["hangar1", "hangar2"])
        self.assertFalse(args.auto)

    def test_automatic_selection_arguments(self):
        args = _argument_parser().parse_args([
            "--domain", "domain.pddl",
            "--problem", "problem.pddl",
            "--output-domain", "abstract-domain.pddl",
            "--output-problem", "abstract-problem.pddl",
            "--auto",
        ])

        self.assertTrue(args.auto)
        self.assertIsNone(args.objects)


@unittest.skipUnless(
    os.environ.get("RUN_PLANNER_INTEGRATION") == "1",
    "set RUN_PLANNER_INTEGRATION=1 to run PDDL Symmetries",
)
class RealSymmetryIntegrationTests(unittest.TestCase):
    def test_beluga_symmetries_select_hangars(self):
        problem = BELUGA_CONCRETE / "problem_3_s45_j3_r2_oc44_f3.pddl"

        classes = find_symmetric_object_sets(BELUGA_CONCRETE / "domain.pddl", problem)
        ranked = rank_symmetry_classes(
            (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8"),
            problem.read_text(encoding="utf-8"),
            classes,
        )

        self.assertEqual(
            {tuple(group) for group in classes},
            {
                ("beluga_trailer_1", "beluga_trailer_2"),
                ("factory_trailer_1", "factory_trailer_2"),
                ("hangar1", "hangar2", "hangar3"),
            },
        )
        self.assertEqual(ranked[0].objects, ("hangar1", "hangar2", "hangar3"))


if __name__ == "__main__":
    unittest.main()
