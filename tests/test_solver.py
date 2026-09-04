import unittest

from core.integrations.clingo import IncrementalSolver
from core.solvers.decremental import solve_decrementally


class DecrementalSolverTests(unittest.TestCase):
    def _solve(self, program):
        return solve_decrementally(IncrementalSolver(program, horizon=1))

    def test_returns_the_full_plan_without_relaxation_when_it_is_satisfiable(self):
        success, plan, decrements = self._solve("""
{ switch(1) }.
selected(full).
#show selected/1.
""")

        self.assertTrue(success)
        self.assertEqual(plan, ["selected(full)"])
        self.assertEqual(decrements, 0)

    def test_disables_switches_in_reverse_chronological_order(self):
        success, plan, decrements = self._solve("""
{ switch(1) }.
{ switch(2) }.
:- switch(2).
selected(fallback) :- not switch(2).
#show selected/1.
""")

        self.assertTrue(success)
        self.assertEqual(plan, ["selected(fallback)"])
        self.assertEqual(decrements, 1)

    def test_reports_failure_after_all_switches_are_disabled(self):
        success, plan, decrements = self._solve("""
{ switch(1) }.
:-.
#show switch/1.
""")

        self.assertFalse(success)
        self.assertIsNone(plan)
        self.assertEqual(decrements, 1)

    def test_numeric_switch_order_is_used_instead_of_lexical_order(self):
        success, plan, decrements = self._solve("""
{ switch(2) }.
{ switch(10) }.
:- switch(10).
selected(ten_disabled) :- not switch(10).
#show selected/1.
""")

        self.assertTrue(success)
        self.assertEqual(plan, ["selected(ten_disabled)"])
        self.assertEqual(decrements, 1)

    def test_reports_every_solver_attempt_and_decrement(self):
        attempts = []
        solver = IncrementalSolver(
            """
{ switch(1) }.
{ switch(2) }.
:- switch(1).
:- switch(2).
selected(done) :- not switch(1), not switch(2).
#show selected/1.
""",
            horizon=1,
        )
        success, _plan, _decrements = solve_decrementally(
            solver, on_attempt=lambda decrements, calls: attempts.append((decrements, calls))
        )

        self.assertTrue(success)
        self.assertEqual(attempts, [(0, 1), (1, 2), (2, 3)])


if __name__ == "__main__":
    unittest.main()
