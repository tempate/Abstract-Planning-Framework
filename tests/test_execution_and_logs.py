import unittest
from unittest.mock import patch

from core.execution import PhaseTiming


class ExecutionTests(unittest.TestCase):
    @patch("core.execution.time.perf_counter", return_value=12.5)
    def test_phase_timing_stops_once(self, perf_counter):
        timing = PhaseTiming(_started_at=10.0)

        timing.stop()
        timing.stop()

        self.assertEqual(timing.elapsed, 2.5)
        self.assertEqual(perf_counter.call_count, 1)


if __name__ == "__main__":
    unittest.main()
