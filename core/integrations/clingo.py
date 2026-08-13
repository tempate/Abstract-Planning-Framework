"""Clingo integration for finding the first plan."""

import os

import clingo

from core.execution import get_logger, timed_phase


THREADS = os.cpu_count() or 1


def run_clingo(asp_files, horizon):
    """Solve a collection of ASP files and return their shown atoms."""
    logger = get_logger()
    logger.info("[CLINGO] Starting solve")
    logger.info(f"[CLINGO] Horizon={horizon}")
    logger.info(f"[CLINGO] Threads={THREADS}")
    logger.info(f"[CLINGO] Files={asp_files}")

    with timed_phase(logger, "[CLINGO] Solve runtime"):
        plan = collect_plan(create_control(asp_files, horizon))
    logger.info(f"[CLINGO] Plan found={plan is not None}")
    return plan


def create_control(asp_files, horizon):
    """Load and ground ASP files in a configured Clingo control."""
    arguments = [
        "-c",
        f"horizon={horizon}",
        "-t",
        str(THREADS),
        "--warn=none",
    ]
    control = clingo.Control(arguments)
    control.configuration.solve.models = 1
    for asp_file in asp_files:
        control.load(asp_file)
    control.ground([("base", [])])
    return control


def collect_plan(control, assumptions=None):
    """Return the shown atoms from the first plan, if one exists."""
    with control.solve(yield_=True, assumptions=assumptions or []) as handle:
        for plan in handle:
            return [str(atom) for atom in plan.symbols(shown=True)]
    return None
