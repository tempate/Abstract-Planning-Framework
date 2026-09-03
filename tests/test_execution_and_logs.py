import unittest
from pathlib import Path

from core.execution import temp_run_dir


class ExecutionTests(unittest.TestCase):
    def test_temp_run_directory_is_removed_after_use(self):
        with temp_run_dir("planning") as (run_directory, run_id):
            path = Path(run_directory)
            self.assertTrue(path.is_dir())
            self.assertEqual(run_id, path.name)

        self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
