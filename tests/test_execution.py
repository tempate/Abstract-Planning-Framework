import contextlib
import shutil
import unittest
from pathlib import Path
from unittest.mock import patch

from core.utilities.execution import KEEP_FAILED_RUNS, temp_run_dir


class ExecutionTests(unittest.TestCase):
    def test_a_run_directory_is_removed_whether_the_run_succeeds_or_fails(self):
        for fails in (False, True):
            with self.subTest(fails=fails), patch.dict("os.environ", {KEEP_FAILED_RUNS: ""}):
                with contextlib.suppress(ValueError):
                    with temp_run_dir("planning") as (run_directory, run_id):
                        path = Path(run_directory)
                        self.assertTrue(path.is_dir())
                        self.assertEqual(run_id, path.name)
                        if fails:
                            raise ValueError("planning failed")

                self.assertFalse(path.exists())

    def test_a_failed_run_keeps_its_files_when_asked(self):
        with patch.dict("os.environ", {KEEP_FAILED_RUNS: "1"}):
            with self.assertRaises(ValueError):
                with temp_run_dir("planning") as (run_directory, _):
                    path = Path(run_directory)
                    Path(run_directory, "output.sas").write_text("sas", encoding="utf-8")
                    raise ValueError("planning failed")

        self.addCleanup(shutil.rmtree, path, ignore_errors=True)
        self.assertEqual(Path(path, "output.sas").read_text(encoding="utf-8"), "sas")


if __name__ == "__main__":
    unittest.main()
