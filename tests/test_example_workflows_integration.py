import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUN_INTEGRATION = os.environ.get("RUN_PLANNER_INTEGRATION") == "1"


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


if __name__ == "__main__":
    unittest.main()
