import unittest

import clingo

from core.search.relaxing import RelaxingSolver


def _keep(number):
    return clingo.Function("keep", [clingo.Number(number)])


class RelaxingSolverTests(unittest.TestCase):
    def _relax(self, program, numbers, on_attempt=None):
        solver = RelaxingSolver(program, horizon=1)
        return solver.relax([_keep(number) for number in numbers], on_attempt)

    def test_keeps_every_assumption_when_they_hold_together(self):
        plan, dropped = self._relax(
            """
{ keep(1) }.
selected(full).
#show selected/1.
""",
            [1],
        )

        self.assertEqual(plan, ["selected(full)"])
        self.assertEqual(dropped, 0)

    def test_drops_assumptions_starting_from_the_last(self):
        plan, dropped = self._relax(
            """
{ keep(1) }.
{ keep(2) }.
:- keep(2).
selected(fallback) :- not keep(2).
#show selected/1.
""",
            [1, 2],
        )

        self.assertEqual(plan, ["selected(fallback)"])
        self.assertEqual(dropped, 1)

    def test_reports_no_plan_once_every_assumption_is_dropped(self):
        plan, dropped = self._relax(
            """
{ keep(1) }.
:-.
#show keep/1.
""",
            [1],
        )

        self.assertIsNone(plan)
        self.assertEqual(dropped, 1)

    def test_reports_every_attempt_and_how_many_were_dropped(self):
        attempts = []

        plan, dropped = self._relax(
            """
{ keep(1) }.
{ keep(2) }.
:- keep(1).
:- keep(2).
selected(done) :- not keep(1), not keep(2).
#show selected/1.
""",
            [1, 2],
            on_attempt=lambda dropped, calls: attempts.append((dropped, calls)),
        )

        self.assertEqual(plan, ["selected(done)"])
        self.assertEqual(dropped, 2)
        self.assertEqual(attempts, [(0, 1), (1, 2), (2, 3)])


if __name__ == "__main__":
    unittest.main()
