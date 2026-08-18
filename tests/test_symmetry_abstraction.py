import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.integrations.pddl_symmetries import PddlSymmetriesError, find_symmetric_object_sets
from core.symmetry_abstraction import AbstractionError, abstract_task, rank_symmetry_classes
from scripts.abstract_object import _argument_parser

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BELUGA_CONCRETE = PROJECT_ROOT / "data" / "beluga" / "concrete" / "standard"


def pddl_tokens(text):
    without_comments = re.sub(r";[^\n]*", "", text)
    return [token.casefold() for token in re.findall(r"[()]|[^\s();]+", without_comments)]


def _stub_symmetry_inputs(directory):
    root = Path(directory)
    translator = root / "translate.py"
    domain = root / "domain.pddl"
    problem = root / "problem.pddl"
    for path in (translator, domain, problem):
        path.write_text("", encoding="utf-8")
    return translator, domain, problem


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

    def test_handles_inline_comments_and_parameterless_actions(self):
        domain = """
(define (domain d)
  (:requirements :typing)
  (:types item; the comment starts without preceding whitespace
  )
  (:predicates (free ?x - item) (ticked))
  (:action use
    :parameters (?x - item)
    :effect (not (free ?x)))
  (:action tick
    :effect (ticked)))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects a b - item; another adjacent comment
  )
  (:init (free a) (free b))
  (:goal (ticked)))
"""

        result = abstract_task(domain, problem, ["a", "b"])

        self.assertEqual(result.unary_delete_score, 1)
        self.assertIn("tick", pddl_tokens(result.domain_text))
        self.assertNotIn("comment", result.domain_text)

    def test_preserves_untyped_object_syntax(self):
        domain = """
(define (domain d)
  (:predicates (free ?x))
  (:action use :parameters (?x) :effect (not (free ?x))))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects a b) (:init (free a) (free b)) (:goal (and)))
"""

        result = abstract_task(domain, problem, ["a", "b"])

        self.assertIn("(:objects object_abs)", result.problem_text)
        self.assertNotIn("- object", result.problem_text)
        self.assertEqual(result.unary_delete_score, 1)

    def test_does_not_rewrite_quantifier_types_or_preference_names(self):
        domain = """
(define (domain d)
  (:requirements :typing :preferences)
  (:types item)
  (:predicates (linked ?left ?right - item)))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects item other - item)
  (:init)
  (:goal (forall (?x - item)
    (preference item (linked item ?x))))
  (:metric minimize (is-violated item)))
"""

        result = abstract_task(domain, problem, ["item", "other"], "shared")

        expected = """
(define (problem p) (:domain d)
  (:objects shared - item)
  (:init)
  (:goal (forall (?x - item)
    (preference item (linked shared ?x))))
  (:metric minimize (is-violated item)))
"""
        self.assertEqual(pddl_tokens(result.problem_text), pddl_tokens(expected))

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

    def test_rejects_domain_mismatches_constant_collisions_and_false_inequality(self):
        domain = """
(define (domain d)
  (:requirements :typing :equality)
  (:types item)
  (:constants item_abs - item)
  (:predicates))
"""
        mismatch = """
(define (problem p) (:domain other)
  (:objects a b - item) (:init) (:goal (and)))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects a b - item) (:init) (:goal (not (= a b))))
"""
        masked_inequality = """
(define (problem p) (:domain d)
  (:objects a b - item) (:init)
  (:goal (and (not (= a a)) (not (= a b)))))
"""

        with self.assertRaisesRegex(AbstractionError, "Problem references domain"):
            abstract_task(domain, mismatch, ["a", "b"])
        with self.assertRaisesRegex(AbstractionError, "domain constant"):
            abstract_task(domain, problem, ["a", "b"])
        with self.assertRaisesRegex(AbstractionError, "false.*constraint"):
            abstract_task(domain, problem, ["a", "b"], "abstract_item")
        with self.assertRaisesRegex(AbstractionError, "false.*constraint"):
            abstract_task(domain, masked_inequality, ["a", "b"], "a")

    def test_hangar_output_matches_checked_in_abstraction(self):
        domain = (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8")
        problem_name = "problem_3_s45_j3_r2_oc44_f3"
        problem = (BELUGA_CONCRETE / f"{problem_name}.pddl").read_text(encoding="utf-8")

        result = abstract_task(domain, problem, ["hangar1", "hangar2", "hangar3"], "hangarabs")
        expected_dir = PROJECT_ROOT / "data" / "beluga" / "abstract" / "hangar"

        self.assertEqual(
            pddl_tokens(result.domain_text), pddl_tokens((expected_dir / "domain.pddl").read_text(encoding="utf-8"))
        )
        self.assertEqual(
            pddl_tokens(result.problem_text),
            pddl_tokens((expected_dir / f"{problem_name}_abs.pddl").read_text(encoding="utf-8")),
        )

    def test_type_wide_trailer_output_matches_legacy_domain(self):
        domain = (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8")
        problem_name = "problem_3_s45_j3_r2_oc44_f3"
        problem = (BELUGA_CONCRETE / f"{problem_name}.pddl").read_text(encoding="utf-8")

        result = abstract_task(domain, problem, ["beluga_trailer_1", "beluga_trailer_2"], "beluga_abs_trailer")
        expected_dir = PROJECT_ROOT / "data" / "beluga" / "abstract" / "trailer"

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
        self.assertEqual(
            [removed.action for removed in ranked[1].removed_deletes],
            ["unload-beluga", "get-from-hangar", "pick-up-rack", "unstack-rack"],
        )

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

        ranked = rank_symmetry_classes(domain, problem, [["a1", "a2"], ["b1", "b2", "b3"]])

        self.assertEqual(ranked[0].objects, ("b1", "b2", "b3"))

    def test_skips_domain_constant_classes_and_duplicate_classes(self):
        domain = """
(define (domain d) (:types item) (:constants c1 c2 - item)
  (:predicates (free ?x - item)))
"""
        problem = """
(define (problem p) (:domain d)
  (:objects a1 a2 - item) (:init) (:goal (and)))
"""

        ranked = rank_symmetry_classes(domain, problem, [["c1", "c2"], ["a2", "a1"], ["a1", "a2"]])

        self.assertEqual([item.objects for item in ranked], [("a1", "a2")])

    def test_rejects_unknown_objects_from_symmetry_output(self):
        with self.assertRaisesRegex(AbstractionError, "unknown object"):
            rank_symmetry_classes(self.domain, self.problem, [["hangar1", "not-an-object"]])

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_extracts_object_sets_from_translator_output(self, run):
        run.return_value = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout=("translator diagnostics\n" "Non-trivial symmetric object sets: [['b', 'a'], ['x', 'y']]\n"),
            stderr="",
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

    def test_rejects_nonpositive_symmetry_time_limit(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            find_symmetric_object_sets("d.pddl", "p.pddl", 0)

    @patch("core.integrations.pddl_symmetries.subprocess.run")
    def test_reports_process_timeouts(self, run):
        run.side_effect = subprocess.TimeoutExpired("translate.py", 10)
        with tempfile.TemporaryDirectory() as directory:
            translator, domain, problem = _stub_symmetry_inputs(directory)

            with self.assertRaisesRegex(PddlSymmetriesError, "exceeded"):
                find_symmetric_object_sets(domain, problem, 10, translator)


class AbstractionArgumentTests(unittest.TestCase):
    def test_explicit_selection_arguments(self):
        args = _argument_parser().parse_args(
            [
                "--domain",
                "domain.pddl",
                "--problem",
                "problem.pddl",
                "--output-domain",
                "abstract-domain.pddl",
                "--output-problem",
                "abstract-problem.pddl",
                "--objects",
                "hangar1",
                "hangar2",
            ]
        )

        self.assertEqual(args.domain, Path("domain.pddl"))
        self.assertEqual(args.objects, ["hangar1", "hangar2"])
        self.assertFalse(args.auto)

    def test_automatic_selection_arguments(self):
        args = _argument_parser().parse_args(
            [
                "--domain",
                "domain.pddl",
                "--problem",
                "problem.pddl",
                "--output-domain",
                "abstract-domain.pddl",
                "--output-problem",
                "abstract-problem.pddl",
                "--auto",
            ]
        )

        self.assertTrue(args.auto)
        self.assertIsNone(args.objects)

    def test_explicit_cli_writes_domain_and_problem(self):
        domain = "(define (domain d) (:types item) (:predicates))"
        problem = """
(define (problem p) (:domain d)
  (:objects a b - item) (:init) (:goal (and)))
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            domain_path = root / "domain.pddl"
            problem_path = root / "problem.pddl"
            output_domain = root / "abstract" / "domain.pddl"
            output_problem = root / "abstract" / "problem.pddl"
            domain_path.write_text(domain, encoding="utf-8")
            problem_path.write_text(problem, encoding="utf-8")

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "scripts.abstract_object",
                    "--domain",
                    str(domain_path),
                    "--problem",
                    str(problem_path),
                    "--output-domain",
                    str(output_domain),
                    "--output-problem",
                    str(output_problem),
                    "--objects",
                    "a",
                    "b",
                ],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(output_domain.is_file())
            self.assertIn("item_abs", output_problem.read_text(encoding="utf-8"))
            self.assertIn("Collapsed ['a', 'b']", completed.stdout)


@unittest.skipUnless(
    os.environ.get("RUN_PLANNER_INTEGRATION") == "1", "set RUN_PLANNER_INTEGRATION=1 to run PDDL Symmetries"
)
class RealSymmetryIntegrationTests(unittest.TestCase):
    def test_beluga_symmetries_select_hangars(self):
        problem = BELUGA_CONCRETE / "problem_3_s45_j3_r2_oc44_f3.pddl"

        classes = find_symmetric_object_sets(BELUGA_CONCRETE / "domain.pddl", problem)
        ranked = rank_symmetry_classes(
            (BELUGA_CONCRETE / "domain.pddl").read_text(encoding="utf-8"), problem.read_text(encoding="utf-8"), classes
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
