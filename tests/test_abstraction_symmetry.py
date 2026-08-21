import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.integrations.pddl_symmetries import PddlSymmetriesError, find_symmetric_object_sets
from core.integrations.unified_planning import parse_problem, read_problem
from core.abstraction.model import rank_symmetry_classes
from core.abstraction.symmetry import prepare_abstraction

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BELUGA_CONCRETE = PROJECT_ROOT / "data" / "beluga" / "concrete" / "standard"


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
        self.problem_path = BELUGA_CONCRETE / "problem_3_s45_j3_r2_oc44_f3.pddl"
        self.problem = read_problem(BELUGA_CONCRETE / "domain.pddl", self.problem_path)

    def test_ranks_by_score_then_size_then_lexical_order(self):
        classes = [
            ["factory_trailer_1", "factory_trailer_2"],
            ["hangar1", "hangar2", "hangar3"],
            ["beluga_trailer_1", "beluga_trailer_2"],
        ]
        ranked = rank_symmetry_classes(self.problem, classes)

        self.assertEqual(ranked[0].abstraction.objects, ("hangar1", "hangar2", "hangar3"))
        self.assertEqual(ranked[0].unary_delete_score, 1)
        self.assertEqual(ranked[1].abstraction.objects[0], "beluga_trailer_1")
        self.assertEqual(ranked[1].unary_delete_score, 3)
        self.assertEqual(
            [removed.action for removed in ranked[1].removed_deletes], ["unload-beluga", "pick-up-rack", "unstack-rack"]
        )
        self.assertEqual(
            [removed.action for removed in ranked[2].removed_deletes],
            ["get-from-hangar", "pick-up-rack", "unstack-rack"],
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

        source = parse_problem(domain, problem)
        ranked = rank_symmetry_classes(source, [["a1", "a2"], ["b1", "b2", "b3"]])

        self.assertEqual(ranked[0].abstraction.objects, ("b1", "b2", "b3"))

    @patch("core.abstraction.symmetry.find_symmetric_object_sets")
    def test_planner_abstraction_uses_the_top_pddl_symmetries_class(self, find_classes):
        find_classes.return_value = [
            ["factory_trailer_1", "factory_trailer_2"],
            ["hangar1", "hangar2", "hangar3"],
            ["beluga_trailer_1", "beluga_trailer_2"],
        ]

        abstract_problem = prepare_abstraction(BELUGA_CONCRETE / "domain.pddl", self.problem_path, bliss_time_limit=17)

        find_classes.assert_called_once_with(BELUGA_CONCRETE / "domain.pddl", self.problem_path, 17)
        self.assertEqual(abstract_problem.abstraction.objects, ("hangar1", "hangar2", "hangar3"))
        self.assertEqual(abstract_problem.abstraction.name, "hangar_abs")

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


@unittest.skipUnless(
    os.environ.get("RUN_PLANNER_INTEGRATION") == "1", "set RUN_PLANNER_INTEGRATION=1 to run PDDL Symmetries"
)
class RealSymmetryIntegrationTests(unittest.TestCase):
    def test_beluga_symmetries_select_hangars(self):
        problem_path = BELUGA_CONCRETE / "problem_3_s45_j3_r2_oc44_f3.pddl"
        classes = find_symmetric_object_sets(BELUGA_CONCRETE / "domain.pddl", problem_path)
        ranked = rank_symmetry_classes(read_problem(BELUGA_CONCRETE / "domain.pddl", problem_path), classes)

        self.assertEqual(
            {tuple(group) for group in classes},
            {
                ("beluga_trailer_1", "beluga_trailer_2"),
                ("factory_trailer_1", "factory_trailer_2"),
                ("hangar1", "hangar2", "hangar3"),
            },
        )
        self.assertEqual(ranked[0].abstraction.objects, ("hangar1", "hangar2", "hangar3"))


if __name__ == "__main__":
    unittest.main()
