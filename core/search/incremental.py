"""Incremental horizon search over an ASP planning program."""

from dataclasses import dataclass

import clingo

from core.search.solver import Solver


@dataclass(frozen=True)
class SolveResult:
    """Result of an incremental horizon search."""

    plan: list[str]
    horizon: int
    attempts: int


class IncrementalSolver(Solver):
    """One Clingo control whose horizon can be raised without regrounding."""

    def __init__(self, asp, init_horizon=0):
        if init_horizon < 0:
            raise ValueError("Horizon must be nonnegative")

        super().__init__(asp)

        for time_step in range(1, init_horizon + 1):
            self.control.ground([("step", [clingo.Number(time_step)])])

        self.horizon = init_horizon
        self._add_goal()

    def search(self, assumptions=(), on_attempt=None):
        """Raise the horizon until the program becomes satisfiable."""
        attempts = 0
        while True:
            attempts += 1

            # Allow callers to report progress while the search runs.
            if on_attempt is not None:
                on_attempt(self.horizon, attempts)

            plan = self.solve(assumptions)
            if plan is not None:
                return SolveResult(plan, self.horizon, attempts)

            self.extend()

    def extend(self):
        """Raise the horizon by one, keeping everything grounded so far."""
        self._delete_goal()
        self.horizon += 1
        self.control.ground([("step", [clingo.Number(self.horizon)])])
        self._add_goal()

    def _add_goal(self):
        """Ground the goal test for the current horizon and activate it."""
        self.control.ground([("check", [clingo.Number(self.horizon)])])
        self.control.assign_external(_query(self.horizon), True)

    def _delete_goal(self):
        """Deactivate the goal test for the current horizon."""
        self.control.release_external(_query(self.horizon))


def _query(horizon):
    return clingo.Function("query", [clingo.Number(horizon)])
