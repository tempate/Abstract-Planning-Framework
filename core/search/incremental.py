"""Incremental horizon search over an ASP planning program."""

import clingo

from core.search.solver import Solver, SolveResult


class IncrementalSolver(Solver):
    """One Clingo control whose horizon can be raised without regrounding, and whose assumptions can be given up."""

    def __init__(self, asp, init_horizon=0, optimize=True):
        if init_horizon < 0:
            raise ValueError("Horizon must be nonnegative")

        super().__init__(asp)
        self.init_horizon = init_horizon
        self.optimize = optimize

        self.horizon = init_horizon
        self.increment = 1

        self._ground_steps(0, init_horizon)
        self._add_goal()

    def search(self, symbols=(), on_attempt=None, dropped=0):
        """Assume every symbol but the first `dropped`, give the rest up in the order given, then raise the horizon."""
        assumptions = {symbol: index >= dropped for index, symbol in enumerate(symbols)}
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
                assumptions[symbols[dropped]] = False
                dropped += 1
            else:
                # Nothing constrains the search any more, so the only way left to
                # satisfy the program is to give it another time step.
                self.extend()

    def extend(self):
        """Raise the horizon keeping everything grounded so far."""
        next_horizon = self.horizon + self.increment

        if not self.optimize and self.horizon != self.init_horizon:
            self.increment *= 2

        self._delete_goal()
        self._ground_steps(self.horizon, next_horizon)
        self.horizon = next_horizon
        self._add_goal()

    def _ground_steps(self, from_horizon, to_horizon):
        """Ground the steps after one horizon up to another."""
        for time_step in range(from_horizon + 1, to_horizon + 1):
            self.control.ground([("step", [clingo.Number(time_step)])])

    def _add_goal(self):
        """Ground the goal test for the current horizon and activate it."""
        self.control.ground([("check", [clingo.Number(self.horizon)])])
        self.control.assign_external(_query(self.horizon), True)

    def _delete_goal(self):
        """Deactivate the goal test for the current horizon."""
        self.control.release_external(_query(self.horizon))


def _query(horizon):
    return clingo.Function("query", [clingo.Number(horizon)])
