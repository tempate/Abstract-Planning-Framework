"""Incremental horizon search over an ASP planning program."""

from dataclasses import dataclass

import clingo

THREADS = 1


@dataclass(frozen=True)
class SolveResult:
    """Result of an incremental horizon search."""

    plan: list[str]
    horizon: int
    attempts: int


class IncrementalSolver:
    """One Clingo control whose horizon can be raised without regrounding."""

    def __init__(self, asp, horizon=0):
        if horizon < 0:
            raise ValueError("Horizon must be nonnegative")

        arguments = ["-t", str(THREADS), "--warn=none"]
        self.control = clingo.Control(arguments)
        self.control.configuration.solve.models = 1
        self.control.add("base", [], asp)
        self.control.ground([("base", [])])

        for time_step in range(1, horizon + 1):
            self.control.ground([("step", [clingo.Number(time_step)])])

        self.horizon = horizon
        self._check_goal()

    def solve(self, assumptions=None):
        """Return the shown atoms from the first plan at the current horizon."""
        with self.control.solve(yield_=True, assumptions=assumptions or []) as handle:
            for plan in handle:
                return [str(atom) for atom in plan.symbols(shown=True)]
        return None

    def search(self, assumptions=None, on_attempt=None):
        """Raise the horizon until the program becomes satisfiable.

        ``on_attempt`` receives the horizon being tried and the number of solver
        calls made so far, so callers can report progress while the search runs.
        """
        attempts = 0
        while True:
            attempts += 1
            if on_attempt is not None:
                on_attempt(self.horizon, attempts)

            plan = self.solve(assumptions)
            if plan is not None:
                return SolveResult(plan, self.horizon, attempts)

            self.extend()

    def extend(self):
        """Raise the horizon by one, keeping everything grounded so far."""
        self.control.release_external(_query(self.horizon))
        self.horizon += 1
        self.control.ground([("step", [clingo.Number(self.horizon)])])
        self._check_goal()

    def _check_goal(self):
        """Ground the goal test for the current horizon and activate it."""
        self.control.ground([("check", [clingo.Number(self.horizon)])])
        self.control.assign_external(_query(self.horizon), True)


def _query(horizon):
    return clingo.Function("query", [clingo.Number(horizon)])
