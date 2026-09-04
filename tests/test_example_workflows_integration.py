import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

import core.planning.abstract as abstract_module
import core.planning.concrete as concrete_module
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from core.planning.config import AbstractPlanningConfig, PlanningConfig

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUN_INTEGRATION = os.environ.get("RUN_PLANNER_INTEGRATION") == "1"
GRIPPER_DIR = PROJECT_ROOT / "benchmarks" / "downward-benchmarks" / "gripper"


@unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
class ExampleWorkflowTests(unittest.TestCase):
    def _run(self, example):
        environment = os.environ.copy()
        environment["PYTHON_BIN"] = sys.executable
        with tempfile.TemporaryDirectory(prefix="apf-example-") as directory:
            environment["APF_TEMP_DIR"] = directory
            return subprocess.run(
                [f"examples/{example}.sh"],
                cwd=PROJECT_ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

    def _assert_success(self, result, expected_plans=1):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("Plan found: yes"), expected_plans, result.stdout)

    def test_gripper_concrete_example_finds_a_plan(self):
        self._assert_success(self._run("concrete"))

    def test_gripper_abstract_example_runs_the_refinement_pipeline(self):
        result = self._run("abstract")

        self._assert_success(result)
        self.assertIn("Collapsed ['ball1', 'ball2', 'ball3', 'ball4'] into object_abs", result.stdout)
        self.assertRegex(result.stdout, r"(?m)^    Refinement decrements +\d+$")


@unittest.skipUnless(RUN_INTEGRATION, "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain")
class ConcreteBaselineTests(unittest.TestCase):
    def test_both_modes_translate_the_same_concrete_sas_file(self):
        domain = GRIPPER_DIR / "domain.pddl"
        problem = GRIPPER_DIR / "prob01.pddl"

        with tempfile.TemporaryDirectory(prefix="apf-sas-") as directory:
            root = Path(directory)
            with patch.object(concrete_module, "temp_run_dir", _kept_run_dir(root / "concrete-mode")):
                compute_concrete_plan(PlanningConfig(domain, problem))
            with patch.object(abstract_module, "temp_run_dir", _kept_run_dir(root / "abstract-mode")):
                compute_abstract_plan(AbstractPlanningConfig(domain, problem))

            from_concrete_mode = (root / "concrete-mode" / "output.sas").read_bytes()
            from_abstract_mode = (root / "abstract-mode" / "concrete" / "output.sas").read_bytes()

        self.assertEqual(from_concrete_mode, from_abstract_mode)


def _kept_run_dir(run_dir):
    """Replace the disposable planner workspace with a directory the test can read."""

    @contextmanager
    def factory(dir_name="concrete"):
        run_dir.mkdir(parents=True)
        yield str(run_dir), run_dir.name

    return factory


if __name__ == "__main__":
    unittest.main()
