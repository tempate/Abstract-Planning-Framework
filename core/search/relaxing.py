"""Solving that relaxes assumptions until the program becomes satisfiable."""

from dataclasses import dataclass

from core.search.incremental import IncrementalSolver, SolveResult


@dataclass(frozen=True)
class RelaxedResult(SolveResult):
    """A plan, and how many assumptions had to be given up to reach it."""

    dropped: int


class RelaxingSolver(IncrementalSolver):
    """An incremental solver that relaxes the assumptions it cannot satisfy."""

    def search(self, symbols=(), on_attempt=None):
        """Assume every symbol, give them up in the order given, then raise the horizon."""
        assumptions = {symbol: True for symbol in symbols}
        dropped = 0
        attempts = 0

        while True:
            attempts += 1
            if on_attempt is not None:
                on_attempt(self.horizon, dropped, attempts)

            plan = self.solve(list(assumptions.items()))
            if plan is not None:
                return RelaxedResult(plan, self.horizon, attempts, dropped)

            if dropped < len(symbols):
                assumptions[symbols[dropped]] = False
                dropped += 1
            else:
                # Nothing constrains the search any more, so the only way left to
                # satisfy the program is to give it another time step.
                self.extend()
