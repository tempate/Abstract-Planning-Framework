"""Clingo integration for finding the first plan."""

from dataclasses import dataclass

import clingo

from core.execution import get_logger, timed_phase
from core.planning.plan import PlanAction

THREADS = 1


@dataclass(frozen=True)
class ClingoSolveResult:
    """Result of an incremental horizon search."""

    plan: list[str] | None
    horizon: int
    attempts: int


def run_clingo(asp, max_horizon=None):
    """Search increasing horizons up to an optional maximum."""
    if max_horizon is not None and max_horizon < 0:
        raise ValueError("Maximum horizon must be nonnegative")

    logger = get_logger()
    logger.info("[CLINGO] Starting horizon search")
    logger.info(f"[CLINGO] Maximum horizon={max_horizon if max_horizon is not None else 'unbounded'}")
    logger.info(f"[CLINGO] Threads={THREADS}")

    with timed_phase(logger, "[CLINGO] Solve runtime"):
        horizon = 0
        attempts = 0

        while max_horizon is None or horizon <= max_horizon:
            attempts += 1
            logger.info(f"[CLINGO] Solving horizon={horizon}")

            plan = collect_plan(create_control(asp, horizon))
            if plan is not None:
                logger.info(f"[CLINGO] Plan found=True at horizon={horizon}")
                return ClingoSolveResult(plan, horizon, attempts)

            horizon += 1

    logger.info("[CLINGO] Plan found=False")
    return ClingoSolveResult(None, max_horizon, attempts)


def create_control(asp, horizon):
    """Add an ASP program and return a grounded Clingo control."""
    if horizon < 0:
        raise ValueError("Horizon must be nonnegative")

    arguments = ["-c", f"horizon={horizon}", "-t", str(THREADS), "--warn=none"]
    control = clingo.Control(arguments)
    control.configuration.solve.models = 1
    control.add("base", [], asp)
    control.ground([("base", [])])
    return control


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
