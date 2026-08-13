import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from examples.beluga import run_abstract as run_beluga_abstract
from examples.beluga import run_concrete as run_beluga_concrete
from examples.beluga import run_refinement as run_beluga_refinement
from examples.no_mystery import run_refinement as run_no_mystery_refinement
from examples.no_mystery import (
    run_refinement_concrete as run_no_mystery_refinement_concrete,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUN_INTEGRATION = os.environ.get("RUN_PLANNER_INTEGRATION") == "1"


@unittest.skipUnless(
    RUN_INTEGRATION,
    "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain",
)
class NoMysteryWorkflowTests(unittest.TestCase):
    def setUp(self):
        example = PROJECT_ROOT / "data" / "examples" / "no_mystery"
        self.concrete_domain = example / "concrete" / "domain.pddl"
        self.concrete_problem = example / "concrete" / "problem.pddl"
        self.abstract_domain = example / "abstract" / "domain.pddl"
        self.abstract_problem = example / "abstract" / "problem.pddl"

    def test_concrete_example_finds_a_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = compute_concrete_plan(
                    self.concrete_domain,
                    self.concrete_problem,
                )

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertGreater(result["horizon"], 0)
        self.assertTrue(any(atom.startswith("occurs(") for atom in result["plan"]))

    def test_abstract_baseline_is_fully_realizable(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = compute_abstract_plan(
                    abstract_domain_path=self.abstract_domain,
                    abstract_problem_path=self.abstract_problem,
                    concrete_domain_path=self.concrete_domain,
                    concrete_problem_path=self.concrete_problem,
                    plan_source="clingo",
                    profile_name="no_mystery",
                )

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertEqual(result["timings"]["iterations"], 1)
        self.assertEqual(result["timings"]["decrements"], 0)

    def test_refinement_example_relaxes_the_abstract_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = run_no_mystery_refinement()

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertGreater(result["timings"]["decrements"], 0)

    def test_refinement_example_has_a_matching_concrete_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = run_no_mystery_refinement_concrete()

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertEqual(result["horizon"], 11)


@unittest.skipUnless(
    RUN_INTEGRATION,
    "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain",
)
class BelugaWorkflowTests(unittest.TestCase):
    def test_concrete_example_finds_a_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = run_beluga_concrete()

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertGreater(result["horizon"], 0)

    def test_hangar_abstraction_baseline_is_fully_realizable(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = run_beluga_abstract()

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertEqual(result["timings"]["iterations"], 1)
        self.assertEqual(result["timings"]["decrements"], 0)

    def test_trailer_refinement_relaxes_the_abstract_plan(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("core.execution.TEMP_DIR", directory):
                result = run_beluga_refinement()

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["plan"])
        self.assertGreater(result["timings"]["decrements"], 0)


if __name__ == "__main__":
    unittest.main()
