"""Clingo multi-shot integration for finding the first plan."""

from dataclasses import dataclass

import clingo

from core.execution import get_logger, timed_phase
from core.planning.plan import PlanAction

THREADS = 1


@dataclass(frozen=True)
class ClingoSolveResult:
    """Result of an incremental horizon search."""

    plan: list[str]
    horizon: int
    attempts: int


def solve(asp):
    """Incrementally solve an ASP program until a plan is found."""
    logger = get_logger()
    logger.info("[CLINGO] Starting incremental solve")
    logger.info(f"[CLINGO] Threads={THREADS}")

    with timed_phase(logger, "[CLINGO] Solve runtime"):
        control = _create_base_control(asp)
        previous_query = None
        horizon = 0
        attempts = 0

        while True:
            if previous_query is not None:
                control.release_external(previous_query)
            if horizon > 0:
                control.ground([("step", [clingo.Number(horizon)])])

            control.ground([("check", [clingo.Number(horizon)])])
            query = _query(horizon)
            control.assign_external(query, True)
            attempts += 1
            logger.info(f"[CLINGO] Solving horizon={horizon}")

            plan = collect_plan(control)
            if plan is not None:
                logger.info(f"[CLINGO] Plan found=True at horizon={horizon}")
                return ClingoSolveResult(plan, horizon, attempts)

            previous_query = query
            horizon += 1


def create_control(asp, horizon):
    """Return a control grounded for one fixed horizon."""
    if horizon < 0:
        raise ValueError("Horizon must be nonnegative")

    control = _create_base_control(asp)
    for time_step in range(1, horizon + 1):
        control.ground([("step", [clingo.Number(time_step)])])
    control.ground([("check", [clingo.Number(horizon)])])
    control.assign_external(_query(horizon), True)
    return control


def _create_base_control(asp):
    """Add an ASP program and ground its static program part."""
    arguments = ["-t", str(THREADS), "--warn=none"]
    control = clingo.Control(arguments)
    control.configuration.solve.models = 1
    control.add("base", [], asp)
    control.ground([("base", [])])
    return control


def _query(horizon):
    return clingo.Function("query", [clingo.Number(horizon)])


def collect_plan(control, assumptions=None):
    """Return the shown atoms from the first plan, if one exists."""
    with control.solve(yield_=True, assumptions=assumptions or []) as handle:
        for plan in handle:
            return [str(atom) for atom in plan.symbols(shown=True)]
    return None


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
