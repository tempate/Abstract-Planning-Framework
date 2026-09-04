"""Clingo multi-shot integration for finding the first plan."""

from dataclasses import dataclass

import clingo

from core.planning.plan import PlanAction

THREADS = 1


@dataclass(frozen=True)
class ClingoSolveResult:
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

    def extend(self):
        """Raise the horizon by one, keeping everything grounded so far."""
        self.control.release_external(_query(self.horizon))
        self.horizon += 1
        self.control.ground([("step", [clingo.Number(self.horizon)])])
        self._check_goal()

    def solve(self, assumptions=None):
        """Return the shown atoms from the first plan at the current horizon."""
        with self.control.solve(yield_=True, assumptions=assumptions or []) as handle:
            for plan in handle:
                return [str(atom) for atom in plan.symbols(shown=True)]
        return None

    def search(self, assumptions=None, on_attempt=None):
        """Raise the horizon until the program becomes satisfiable."""
        attempts = 0
        while True:
            attempts += 1
            if on_attempt is not None:
                on_attempt(self.horizon, attempts)

            plan = self.solve(assumptions)
            if plan is not None:
                return ClingoSolveResult(plan, self.horizon, attempts)

            self.extend()

    def _check_goal(self):
        """Ground the goal test for the current horizon and activate it."""
        self.control.ground([("check", [clingo.Number(self.horizon)])])
        self.control.assign_external(_query(self.horizon), True)


def solve(asp, start_horizon=0, on_attempt=None):
    """Incrementally solve an ASP program until a plan is found.

    The search starts at ``start_horizon`` and reuses one solver instance.
    ``on_attempt`` receives the horizon being tried and the number of solver
    calls made so far, so callers can report progress while the search runs.
    """
    return IncrementalSolver(asp, start_horizon).search(on_attempt=on_attempt)


def _query(horizon):
    return clingo.Function("query", [clingo.Number(horizon)])


def parse_plan_actions(atoms):
    """Convert shown ``occurs/2`` atoms into chronological plan actions."""
    actions = []
    for atom in atoms:
        symbol = clingo.parse_term(atom.rstrip("."))
        if symbol.type != clingo.SymbolType.Function or symbol.name != "occurs" or len(symbol.arguments) != 2:
            continue

        action, time_step = symbol.arguments
        if action.type != clingo.SymbolType.Function or action.name != "action" or len(action.arguments) != 1:
            continue
        payload = action.arguments[0]
        if payload.type == clingo.SymbolType.String:
            fields = (payload.string,)
        elif payload.type == clingo.SymbolType.Function and payload.name == "":
            if not payload.arguments or any(item.type != clingo.SymbolType.String for item in payload.arguments):
                continue
            fields = tuple(item.string for item in payload.arguments)
        else:
            continue
        if time_step.type != clingo.SymbolType.Number:
            continue
        actions.append(PlanAction(fields[0], fields[1:], time_step.number))

    return tuple(sorted(actions, key=lambda action: action.time_step))
