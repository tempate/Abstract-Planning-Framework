import unittest

from core.search.incremental import IncrementalSolver


class IncrementalSolverTests(unittest.TestCase):
    def test_control_is_grounded_through_the_requested_horizon(self):
        program = """
#program base.
step(0).
#show step/1.
#program step(t).
step(t).
"""
        plan = IncrementalSolver(program, init_horizon=3).solve()

        self.assertEqual(set(plan), {"step(0)", "step(1)", "step(2)", "step(3)"})

    def test_incremental_search_checks_horizon_zero(self):
        program = """
#program base.
ready.
#show ready/0.
#program check(t).
#external query(t).
:- query(t), not ready.
"""

        result = IncrementalSolver(program).search()

        self.assertEqual(result.plan, ["ready"])
        self.assertEqual(result.horizon, 0)
        self.assertEqual(result.attempts, 1)

    def test_incremental_search_can_start_above_zero_and_report_attempts(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 3.
"""
        attempts = []

        result = IncrementalSolver(program, init_horizon=2).search(
            on_attempt=lambda horizon, calls: attempts.append((horizon, calls))
        )

        self.assertEqual(result.horizon, 3)
        self.assertEqual(result.attempts, 2)
        self.assertEqual(attempts, [(2, 1), (3, 2)])
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)", "reached(3)"})

    def test_extending_raises_the_horizon_on_the_same_control(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 2.
"""
        solver = IncrementalSolver(program, init_horizon=1)
        control = solver.control

        self.assertIsNone(solver.solve())

        solver.extend()

        self.assertIs(solver.control, control)
        self.assertEqual(solver.horizon, 2)
        self.assertEqual(set(solver.solve()), {"reached(0)", "reached(1)", "reached(2)"})

    def test_exponential_search_skips_to_the_next_power_of_two(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 3.
"""
        horizons = []

        result = IncrementalSolver(program, exp_horizon=True).search(
            on_attempt=lambda horizon, _calls: horizons.append(horizon)
        )

        self.assertEqual(horizons, [0, 1, 2, 4])
        self.assertEqual(result.horizon, 4)

    def test_exponential_search_doubles_the_distance_above_its_initial_horizon(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 6.
"""
        horizons = []

        result = IncrementalSolver(program, init_horizon=3, exp_horizon=True).search(
            on_attempt=lambda horizon, _calls: horizons.append(horizon)
        )

        self.assertEqual(horizons, [3, 4, 5, 7])
        self.assertEqual(result.horizon, 7)


if __name__ == "__main__":
    unittest.main()
