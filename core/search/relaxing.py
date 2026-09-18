"""Solving that relaxes assumptions until the program becomes satisfiable."""

from core.search.incremental import IncrementalSolver


class RelaxingSolver(IncrementalSolver):
    """An incremental solver that relaxes the assumptions it cannot satisfy."""

    def relax(self, symbols, on_attempt=None):
        """Assume every symbol, then drop them from the last until a plan appears.

        Returns the plan and how many symbols were given up, or no plan and all of
        them when even the empty assumption set is unsatisfiable.  ``on_attempt``
        receives the number dropped so far and the number of solver calls made.
        """
        assumptions = {symbol: True for symbol in symbols}

        if on_attempt is not None:
            on_attempt(0, 1)
        plan = self.solve(list(assumptions.items()))
        if plan is not None:
            return plan, 0

        for dropped, symbol in enumerate(reversed(symbols), start=1):
            assumptions[symbol] = False

            if on_attempt is not None:
                on_attempt(dropped, dropped + 1)
            plan = self.solve(list(assumptions.items()))
            if plan is not None:
                return plan, dropped

        return None, len(symbols)
