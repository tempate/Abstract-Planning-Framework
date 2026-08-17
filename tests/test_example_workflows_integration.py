import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUN_INTEGRATION = os.environ.get("RUN_PLANNER_INTEGRATION") == "1"


@unittest.skipUnless(
    RUN_INTEGRATION,
    "set RUN_PLANNER_INTEGRATION=1 to run the external planner toolchain",
)
class ExampleWorkflowTests(unittest.TestCase):
    def _run(self, example, workflow):
        environment = os.environ.copy()
        environment["PYTHON_BIN"] = sys.executable
        with tempfile.TemporaryDirectory(prefix="apf-example-") as directory:
            environment["APF_TEMP_DIR"] = directory
            return subprocess.run(
                [f"examples/{example}.sh", workflow],
                cwd=PROJECT_ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

    def _assert_success(self, result, expected_plans=1):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout.count("Plan found: yes"),
            expected_plans,
            result.stdout,
        )

    def _assert_refinement(self, result):
        self._assert_success(result, expected_plans=2)
        decrements = [
            int(value)
            for value in re.findall(
                r"^Decrements: (\d+)$",
                result.stdout,
                flags=re.MULTILINE,
            )
        ]
        self.assertTrue(decrements, result.stdout)
        self.assertGreater(decrements[-1], 0, result.stdout)

    def test_no_mystery_concrete_example_finds_a_plan(self):
        self._assert_success(self._run("no_mystery", "concrete"))

    def test_no_mystery_abstract_example_is_fully_realizable(self):
        result = self._run("no_mystery", "abstract")

        self._assert_success(result)
        self.assertIn("Decrements: 0", result.stdout)

    def test_no_mystery_refinement_relaxes_the_abstract_plan(self):
        self._assert_refinement(self._run("no_mystery", "refinement"))

    def test_beluga_concrete_example_finds_a_plan(self):
        self._assert_success(self._run("beluga", "concrete"))

    def test_beluga_hangar_abstraction_is_fully_realizable(self):
        result = self._run("beluga", "abstract")

        self._assert_success(result)
        self.assertIn("Decrements: 0", result.stdout)

    def test_beluga_trailer_refinement_relaxes_the_abstract_plan(self):
        self._assert_refinement(self._run("beluga", "refinement"))


if __name__ == "__main__":
    unittest.main()
