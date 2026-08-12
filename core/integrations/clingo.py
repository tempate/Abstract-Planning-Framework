"""Clingo integration for creating controls and collecting answer-set models."""

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
        models = collect_models(create_control(asp_files, horizon))
    logger.info(f"[CLINGO] Models found={len(models)}")
    return models


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
    for asp_file in asp_files:
        control.load(asp_file)
    control.ground([("base", [])])
    return control


def collect_models(control, assumptions=None):
    """Return all shown atoms from models produced by a control."""
    models = []
    with control.solve(yield_=True, assumptions=assumptions or []) as handle:
        for model in handle:
            models.append([str(atom) for atom in model.symbols(shown=True)])
    return models
