import unittest

import clingo

from core.asp.program import AspProgram
from core.asp.solver import Solver


class SolverTests(unittest.TestCase):
    def test_rules_ground_over_the_facts_given_apart(self):
        facts = '% variables\ncontains(variable(0), value("at(a)", true)).\n\n'
        rules = "found(V) :- contains(variable(V), value(_, true)). #show found/1."

        self.assertEqual(Solver(AspProgram(rules, facts), optimize=True).solve(), ["found(0)"])

    def test_unsatisfiable_program_has_no_plan(self):
        self.assertIsNone(Solver(AspProgram(":-.\n"), optimize=True).solve())


class IncrementalSolverTests(unittest.TestCase):
    def test_control_is_grounded_through_the_requested_horizon(self):
        program = """
#program base.
step(0).
#show step/1.
#program step(t).
step(t).
"""
        plan = Solver(AspProgram(program), init_horizon=3, optimize=True).solve()

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

        result = Solver(AspProgram(program), optimize=True).search()

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

        result = Solver(AspProgram(program), init_horizon=2, optimize=True).search(
            on_attempt=lambda horizon, _dropped, calls: attempts.append((horizon, calls))
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
        solver = Solver(AspProgram(program), init_horizon=1, optimize=True)

        self.assertIsNone(solver.solve())

        solver.extend()

        self.assertEqual(solver.horizon, 2)
        self.assertEqual(set(solver.solve()), {"reached(0)", "reached(1)", "reached(2)"})

    def test_a_satisficing_search_doubles_the_distance_above_its_initial_horizon(self):
        program = """
#program base.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < goal.
"""
        for init_horizon, goal, expected in ((0, 3, [0, 1, 2, 4]), (3, 6, [3, 4, 5, 7])):
            with self.subTest(init_horizon=init_horizon):
                horizons = []
                solver = Solver(AspProgram(program.replace("goal", str(goal))), init_horizon, optimize=False)

                solver.search(on_attempt=lambda horizon, _dropped, _calls: horizons.append(horizon))

                self.assertEqual(horizons, expected)


def _keep(number):
    return clingo.Function("keep", [clingo.Number(number)])


class RelaxingSolverTests(unittest.TestCase):
    def _search(self, program, numbers, on_attempt=None, switches_off=0):
        solver = Solver(AspProgram(program), init_horizon=0, optimize=True)
        return solver.search([_keep(number) for number in numbers], on_attempt, switches_off)

    def test_keeps_every_assumption_when_they_hold_together(self):
        result = self._search(
            """
{ keep(1) }.
selected(full).
#show selected/1.
""",
            [1],
        )

        self.assertEqual(result.plan, ["selected(full)"])
        self.assertEqual(result.switches_off, 0)

    def test_gives_up_assumptions_in_the_order_they_are_given(self):
        result = self._search(
            """
{ keep(1) }.
{ keep(2) }.
:- keep(2).
selected(fallback) :- not keep(2).
#show selected/1.
""",
            [2, 1],
        )

        self.assertEqual(result.plan, ["selected(fallback)"])
        self.assertEqual(result.switches_off, 1)

    def test_starts_with_the_first_assumptions_already_given_up(self):
        result = self._search(
            """
{ keep(1) }.
{ keep(2) }.
selected(full) :- keep(1), keep(2).
selected(fallback) :- keep(1), not keep(2).
#show selected/1.
""",
            [2, 1],
            switches_off=1,
        )

        self.assertEqual(result.plan, ["selected(fallback)"])
        self.assertEqual(result.switches_off, 1)

    def test_raises_the_horizon_once_there_is_nothing_left_to_give_up(self):
        attempts = []

        result = self._search(
            """
#program base.
{ keep(1) }.
reached(0).
#show reached/1.
#program step(t).
reached(t).
#program check(t).
#external query(t).
:- query(t), t < 2.
""",
            [1],
            on_attempt=lambda horizon, switches_off, calls: attempts.append((horizon, switches_off, calls)),
        )

        self.assertEqual(result.horizon, 2)
        self.assertEqual(result.switches_off, 1)
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)"})
        # Two attempts at horizon zero, one dropping the assumption, then one per horizon.
        self.assertEqual(attempts, [(0, 0, 1), (0, 1, 2), (1, 1, 3), (2, 1, 4)])


if __name__ == "__main__":
    unittest.main()
