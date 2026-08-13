import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class RunnableExampleTests(unittest.TestCase):
    def test_decremental_solver_example_runs_without_external_planners(self):
        result = subprocess.run(
            [sys.executable, "-m", "examples.decremental_solver"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Plan found: yes", result.stdout)
        self.assertIn("Relaxed switches: 1", result.stdout)
        self.assertIn("occurs(action(\"fallback\"),1)", result.stdout)


if __name__ == "__main__":
    unittest.main()
