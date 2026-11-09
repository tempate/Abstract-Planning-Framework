import unittest

import clingo

from core.search.relaxing import RelaxingSolver
from core.encodings.program import AspProgram


def _keep(number):
    return clingo.Function("keep", [clingo.Number(number)])


class RelaxingSolverTests(unittest.TestCase):
    def _search(self, program, numbers, on_attempt=None, hold=True):
        solver = RelaxingSolver(AspProgram(program), init_horizon=0)
        return solver.search([_keep(number) for number in numbers], on_attempt, hold)

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
        self.assertEqual(result.dropped, 0)

    def test_gives_up_every_assumption_at_once(self):
        result = self._search(
            """
{ keep(1) }.
{ keep(2) }.
:- keep(2).
selected(partial) :- keep(1).
selected(none) :- not keep(1).
#show selected/1.
""",
            [2, 1],
        )

        self.assertEqual(result.plan, ["selected(none)"])
        self.assertEqual(result.dropped, 2)

    def test_can_start_with_every_assumption_given_up(self):
        result = self._search(
            """
{ keep(1) }.
selected(full) :- keep(1).
selected(none) :- not keep(1).
#show selected/1.
""",
            [1],
            hold=False,
        )

        self.assertEqual(result.plan, ["selected(none)"])
        self.assertEqual(result.dropped, 1)

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
            on_attempt=lambda horizon, dropped, calls: attempts.append((horizon, dropped, calls)),
        )

        self.assertEqual(result.horizon, 2)
        self.assertEqual(result.dropped, 1)
        self.assertEqual(set(result.plan), {"reached(0)", "reached(1)", "reached(2)"})
        # Two attempts at horizon zero, one dropping the assumption, then one per horizon.
        self.assertEqual(attempts, [(0, 0, 1), (0, 1, 2), (1, 1, 3), (2, 1, 4)])


if __name__ == "__main__":
    unittest.main()
