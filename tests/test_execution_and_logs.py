import unittest
from pathlib import Path
from unittest.mock import patch

from core.execution import PhaseTiming, temp_run_dir


class ExecutionTests(unittest.TestCase):
    def test_temp_run_directory_is_removed_after_use(self):
        with temp_run_dir("planning") as (run_directory, run_id):
            path = Path(run_directory)
            self.assertTrue(path.is_dir())
            self.assertEqual(run_id, path.name)

        self.assertFalse(path.exists())

    @patch("core.execution.time.perf_counter", return_value=12.5)
    def test_phase_timing_stops_once(self, perf_counter):
        timing = PhaseTiming(_started_at=10.0)

        timing.stop()
        timing.stop()

        self.assertEqual(timing.elapsed, 2.5)
        self.assertEqual(perf_counter.call_count, 1)


if __name__ == "__main__":
    unittest.main()
