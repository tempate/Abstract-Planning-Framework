"""Incremental horizon search over an ASP planning program."""

import clingo

from core.search.solver import Solver, SolveResult


class IncrementalSolver(Solver):
    """One Clingo control whose horizon can be raised without regrounding."""

    def __init__(self, asp, init_horizon=0, optimize=False, exp_horizon=False):
        if init_horizon < 0:
            raise ValueError("Horizon must be nonnegative")

        super().__init__(asp, optimize)
        # Skipping horizons only finds the shorter plans when the program lets a step stay empty.
        self.exp_horizon = exp_horizon

        for time_step in range(1, init_horizon + 1):
            self.control.ground([("step", [clingo.Number(time_step)])])

        self.horizon = init_horizon
        self._add_goal()

    def search(self, assumptions=(), on_attempt=None):
        """Raise the horizon, by one or by doubling it, until the program becomes satisfiable."""
        attempts = 0
        while True:
            attempts += 1

            # Allow callers to report progress while the search runs.
            if on_attempt is not None:
                on_attempt(self.horizon, attempts)

            plan = self.solve(assumptions)
            if plan is not None:
                return SolveResult(plan, self.horizon, attempts)

            self.extend(max(1, 2 * self.horizon) if self.exp_horizon else None)

    def extend(self, horizon=None):
        """Raise the horizon, by one unless given another, keeping everything grounded so far."""
        self._delete_goal()
        horizon = self.horizon + 1 if horizon is None else horizon
        for time_step in range(self.horizon + 1, horizon + 1):
            self.control.ground([("step", [clingo.Number(time_step)])])
        self.horizon = horizon
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
