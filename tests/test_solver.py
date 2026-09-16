import unittest

from core.integrations.clingo import IncrementalSolver
from core.refinement.budgeted import solve_within_budget


def program(switch_steps, rules):
    """Build the switch and budget rules that a mapping emits, plus a test's own rules."""
    lines = []
    off = []
    for step in switch_steps:
        lines.append(f"0 {{ switch({step}) }} 1.")
        off.append(f"{step} : not switch({step})")
    lines.append(f"{{ budget(0..{len(switch_steps)}) }}.")
    lines.append(f":- budget(B), #count{{ {'; '.join(off)} }} != B.")
    lines.append(rules)
    return "\n".join(lines)


class BudgetedSolverTests(unittest.TestCase):
    def _solve(self, switch_steps, rules):
        return solve_within_budget(IncrementalSolver(program(switch_steps, rules), horizon=1))

    def test_returns_the_full_plan_without_relaxation_when_it_is_satisfiable(self):
        success, plan, budget = self._solve(
            [2],
            """
selected(full).
#show selected/1.
""",
        )

        self.assertTrue(success)
        self.assertEqual(plan, ["selected(full)"])
        self.assertEqual(budget, 0)

    def test_the_solver_chooses_which_switch_to_turn_off(self):
        # Only the first switch may be off, which a search that relaxed the plan
        # from the last switch backwards would reach a budget later.
        success, plan, budget = self._solve(
            [2, 4],
            """
:- switch(2).
selected(first_off) :- not switch(2), switch(4).
#show selected/1.
""",
        )

        self.assertTrue(success)
        self.assertEqual(plan, ["selected(first_off)"])
        self.assertEqual(budget, 1)

    def test_reports_failure_after_the_largest_budget(self):
        success, plan, budget = self._solve([2], ":-.\n#show switch/1.")

        self.assertFalse(success)
        self.assertIsNone(plan)
        self.assertEqual(budget, 1)

    def test_reports_every_solver_attempt_and_budget(self):
        attempts = []
        solver = IncrementalSolver(
            program(
                [2, 4],
                """
:- switch(2).
:- switch(4).
selected(done) :- not switch(2), not switch(4).
#show selected/1.
""",
            ),
            horizon=1,
        )
        success, _plan, _budget = solve_within_budget(
            solver, on_attempt=lambda budget, calls: attempts.append((budget, calls))
        )

        self.assertTrue(success)
        self.assertEqual(attempts, [(0, 1), (1, 2), (2, 3)])


if __name__ == "__main__":
    unittest.main()
