import unittest
from contextlib import contextmanager
from types import SimpleNamespace
from unittest.mock import Mock, patch

from core.planning.refinement.ClingoRefinement import ClingoRefinement


def _context():
    return SimpleNamespace(
        paths=SimpleNamespace(
            abstract_asp="abstract.lp",
            forbidden_actions="forbidden.lp",
        ),
        horizon=3,
        debug_dir="debug",
        logger=Mock(),
        total_timing=SimpleNamespace(elapsed=5.0),
        solving_mode="dec",
        fd_timings={
            "fd_concrete_time": 0.1,
            "fd_abstract_time": 0.2,
            "fd_total_time": 0.3,
        },
        concrete_asp_time=0.4,
        abstract_asp_time=0.5,
        asp_total_time=0.9,
        base_dir="run",
    )


class RefinementTimingTests(unittest.TestCase):
    def test_terminal_abstract_solve_is_counted_as_an_iteration(self):
        refinement = ClingoRefinement(_context())
        refinement._solve_abstract = Mock(return_value=(None, 1.25))

        result = refinement.refine()

        self.assertEqual(1, result["timings"]["iterations"])
        self.assertEqual(1.25, refinement.iteration_times[0]["abs"])
        self.assertEqual(0.0, refinement.iteration_times[0]["occ"])
        self.assertEqual(0.0, refinement.iteration_times[0]["map"])
        self.assertEqual(0.0, refinement.iteration_times[0]["conc"])
        self.assertEqual(0.0, refinement.iteration_times[0]["ref"])

    def test_forbidden_file_io_is_outside_abstract_solve_timing(self):
        refinement = ClingoRefinement(_context())
        refinement.forbidden_actions = ["occurs_abstract(action(\"a\"),1)"]
        events = []

        @contextmanager
        def fake_timed_phase(*args):
            events.append("timer-enter")
            yield SimpleNamespace(elapsed=2.0)
            events.append("timer-exit")

        with (
            patch(
                "core.planning.refinement.ClingoRefinement.write_forbidden_actions",
                side_effect=lambda *args: events.append("write"),
            ),
            patch(
                "core.planning.refinement.ClingoRefinement.save_iteration_file",
                side_effect=lambda *args: events.append("save"),
            ),
            patch(
                "core.planning.refinement.ClingoRefinement.timed_phase",
                side_effect=fake_timed_phase,
            ),
            patch(
                "core.planning.refinement.ClingoRefinement.run_clingo",
                side_effect=lambda *args: events.append("solve") or [],
            ),
        ):
            model, elapsed = refinement._solve_abstract(iteration=2)

        self.assertIsNone(model)
        self.assertEqual(2.0, elapsed)
        self.assertEqual(2.0, refinement.abstract_solve_time)
        self.assertEqual(
            ["write", "save", "timer-enter", "solve", "timer-exit"],
            events,
        )


if __name__ == "__main__":
    unittest.main()
