import unittest

import clingo

from core.search.relaxing import RelaxingSolver


def _keep(number):
    return clingo.Function("keep", [clingo.Number(number)])


class RelaxingSolverTests(unittest.TestCase):
    def _search(self, program, numbers, on_attempt=None):
        solver = RelaxingSolver(program, horizon=0)
        return solver.search([_keep(number) for number in numbers], on_attempt)

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
