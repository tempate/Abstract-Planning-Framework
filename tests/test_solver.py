import unittest

from core.integrations.clingo import IncrementalSolver
from core.refinement.minimized import solve_fewest_switches_off


def program(switch_steps, rules):
    """Build the switch and minimize rules that a mapping emits, plus a test's own rules."""
    lines = []
    for step in switch_steps:
        lines.append(f"0 {{ switch({step}) }} 1.")
    switches = "; ".join(f"1,{step} : not switch({step})" for step in switch_steps)
    lines.append(f"#minimize{{ {switches} }}.")
    lines.append(rules)
    return "\n".join(lines)


class MinimizedSolverTests(unittest.TestCase):
    def _solve(self, switch_steps, rules, on_attempt=None):
        solver = IncrementalSolver(program(switch_steps, rules), horizon=1)
        return solve_fewest_switches_off(solver, on_attempt)

    def test_keeps_the_whole_abstract_plan_when_it_is_satisfiable(self):
        attempts = []
        success, _plan, switched_off = self._solve(
            [2, 4], "selected(full).\n#show selected/1.", on_attempt=lambda off, calls: attempts.append((off, calls))
        )

        self.assertTrue(success)
        # Nothing forces a switch off, so the minimum keeps every abstract action.
        self.assertEqual(switched_off, 0)
        self.assertEqual(attempts, [(0, 1)])

    def test_gives_up_only_the_switches_that_block_a_plan(self):
        # Switch 2 cannot stay on, but switch 4 is free to, so the optimum is one.
        success, _plan, switched_off = self._solve([2, 4], ":- switch(2).")

        self.assertTrue(success)
        self.assertEqual(switched_off, 1)

    def test_reports_failure_when_no_plan_exists_below_the_horizon(self):
        success, plan, switched_off = self._solve([2], ":-.\n#show switch/1.")

        self.assertFalse(success)
        self.assertIsNone(plan)
        self.assertEqual(switched_off, 1)


if __name__ == "__main__":
    unittest.main()
