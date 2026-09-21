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
        plan = IncrementalSolver(program, horizon=3).solve()

        self.assertEqual(set(plan), {"step(0)", "step(1)", "step(2)", "step(3)"})

    def test_incremental_search_returns_the_first_satisfiable_horizon(self):
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

        result = IncrementalSolver(program).search()

        self.assertEqual(result.horizon, 2)
        self.assertEqual(result.attempts, 3)
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)"})

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

        result = IncrementalSolver(program, horizon=2).search(
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
        solver = IncrementalSolver(program, horizon=1)
        control = solver.control

        self.assertIsNone(solver.solve())

        solver.extend()

        self.assertIs(solver.control, control)
        self.assertEqual(solver.horizon, 2)
        self.assertEqual(set(solver.solve()), {"reached(0)", "reached(1)", "reached(2)"})


if __name__ == "__main__":
    unittest.main()
