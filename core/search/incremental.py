"""Incremental horizon search over an ASP planning program."""

import clingo

from core.search.solver import Solver, SolveResult


class IncrementalSolver(Solver):
    """One Clingo control whose horizon can be raised without regrounding."""

    def __init__(self, asp, init_horizon=0, optimize=False, exp_horizon=False):
        if init_horizon < 0:
            raise ValueError("Horizon must be nonnegative")

        super().__init__(asp, optimize)
        self.init_horizon = init_horizon
        self.exp_horizon = exp_horizon

        self.horizon = init_horizon
        self.increment = 1

        self._ground_steps(0, init_horizon)
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

            self.extend()

    def extend(self):
        """Raise the horizon keeping everything grounded so far."""
        next_horizon = self.horizon + self.increment

        if self.exp_horizon and self.horizon != self.init_horizon:
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
