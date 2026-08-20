import tempfile
import unittest
from pathlib import Path

from core.integrations.unified_planning import PddlError, parse_problem, read_problem, write_problem

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BELUGA = PROJECT_ROOT / "data" / "beluga" / "concrete" / "standard"


class UnifiedPlanningCodecTests(unittest.TestCase):
    def test_reads_and_round_trips_a_beluga_task(self):
        source = read_problem(BELUGA / "domain.pddl", BELUGA / "problem_3_s45_j3_r2_oc44_f3.pddl")

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
