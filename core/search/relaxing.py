"""Solving that relaxes assumptions until the program becomes satisfiable."""

from dataclasses import dataclass

from core.search.incremental import IncrementalSolver, SolveResult


class RelaxingSolver(IncrementalSolver):
    """An incremental solver that relaxes the assumptions it cannot satisfy."""

    def search(self, symbols=(), on_attempt=None, hold=True):
        """Assume every symbol if told to hold them, give them all up at once, then raise the horizon."""
        assumptions = {symbol: hold for symbol in symbols}
        dropped = 0 if hold else len(symbols)
        attempts = 0

        while True:
            attempts += 1

            # Allow callers to report progress while the search runs.
            if on_attempt is not None:
                on_attempt(self.horizon, dropped, attempts)

            plan = self.solve(list(assumptions.items()))
            if plan is not None:
                return SolveResult(plan, self.horizon, attempts, dropped)

            if dropped < len(symbols):
                assumptions = {symbol: False for symbol in symbols}
                dropped = len(symbols)
            else:
                # Nothing constrains the search any more, so the only way left to
                # satisfy the program is to give it another time step.
                self.extend()
