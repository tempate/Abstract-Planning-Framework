import unittest
from unittest.mock import Mock

from core.metrics import PlanningMetrics


class PlanningMetricsTests(unittest.TestCase):
    def test_repeated_measurements_are_accumulated(self):
        clock = Mock(side_effect=[10.0, 12.5, 20.0, 21.0])
        metrics = PlanningMetrics(_clock=clock)

        with metrics.measure("concrete_fd"):
            pass
        with metrics.measure("concrete_fd"):
            pass

        self.assertEqual(metrics.durations["concrete_fd"], 3.5)

    def test_snapshot_separates_durations_and_counters(self):
        metrics = PlanningMetrics(durations={"total": 1.25}, counters={"final_horizon": 4})

        self.assertEqual(metrics.as_dict(), {"durations": {"total": 1.25}, "counters": {"final_horizon": 4}})

    def test_unknown_metrics_are_rejected(self):
        metrics = PlanningMetrics()

        with self.assertRaisesRegex(ValueError, "Unknown duration metric"):
            with metrics.measure("typo"):
                pass
        with self.assertRaisesRegex(ValueError, "Unknown counter metric"):
            metrics.set_counter("typo", 1)

    def test_reports_only_completed_phases(self):
        events = []
        metrics = PlanningMetrics(on_phase_complete=lambda *event: events.append(event))

        with metrics.measure("concrete_fd"):
            pass
        with self.assertRaisesRegex(RuntimeError, "stopped"):
            with metrics.measure("concrete_asp"):
                raise RuntimeError("stopped")

        self.assertEqual([phase for phase, _snapshot in events], ["concrete_fd"])
        self.assertIn("concrete_fd", events[0][1]["durations"])


if __name__ == "__main__":
    unittest.main()
