import os
import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class RunnableExampleTests(unittest.TestCase):
    def test_no_mystery_example_supports_direct_file_execution(self):
        environment = os.environ.copy()
        environment["PYTHONPATH"] = os.pathsep.join(
            filter(
                None,
                (str(PROJECT_ROOT), environment.get("PYTHONPATH")),
            )
        )
        result = subprocess.run(
            [sys.executable, "examples/no_mystery.py", "--help"],
            cwd=PROJECT_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("{concrete,abstract,all}", result.stdout)


if __name__ == "__main__":
    unittest.main()
