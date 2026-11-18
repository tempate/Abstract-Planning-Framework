import unittest
from unittest.mock import Mock

from core.utilities.metrics import PlanningMetrics


class PlanningMetricsTests(unittest.TestCase):
    def test_repeated_measurements_are_accumulated(self):
        clock = Mock(side_effect=[10.0, 12.5, 20.0, 21.0])
        metrics = PlanningMetrics(_clock=clock)

        with metrics.measure("concrete_fd"):
            pass
        with metrics.measure("concrete_fd"):
            pass

        self.assertEqual(metrics.durations["concrete_fd"], 3.5)

    def test_the_collapsed_class_reaches_the_snapshot_as_it_is_selected(self):
        updates = []
        metrics = PlanningMetrics(on_update=lambda *update: updates.append(update))

        metrics.set_abstraction(("ball2", "ball1"), "ball")

        self.assertEqual(updates[0][1]["abstraction"], {"objects": ["ball1", "ball2"], "object_type": "ball"})

    def test_unknown_metrics_are_rejected(self):
        metrics = PlanningMetrics()

        with self.assertRaisesRegex(ValueError, "Unknown duration metric"):
            with metrics.measure("typo"):
                pass
        with self.assertRaisesRegex(ValueError, "Unknown counter metric"):
            metrics.set_counter("typo", 1)

    def test_reports_completed_phases_and_counter_updates(self):
        updates = []
        metrics = PlanningMetrics(on_update=lambda *update: updates.append(update))

        with metrics.measure("concrete_fd"):
            pass
        with self.assertRaisesRegex(RuntimeError, "stopped"):
            with metrics.measure("concrete_asp"):
                raise RuntimeError("stopped")
        metrics.set_counter("switches_off", 1)
        metrics.set_counter("concrete_solve_calls", 2)

        # A phase that raised never completed, so only the first one is reported as done.
        completed = [event["phase"] for event, _snapshot in updates if event["kind"] == "phase_completed"]
        self.assertEqual(completed, ["concrete_fd"])
        self.assertEqual(updates[-1][1]["counters"]["switches_off"], 1)


if __name__ == "__main__":
    unittest.main()
