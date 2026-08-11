"""Clingo integration for creating controls and collecting answer-set models."""

import os
import time

import clingo

from core.runtime.run_artifacts import get_logger, log_phase


THREADS = os.cpu_count()


def run_clingo(lp_files, horizon):
    """Solve a collection of LP files and return their shown atoms."""
    logger = get_logger()
    start = time.perf_counter()
    logger.info("[CLINGO] Starting solve")
    logger.info(f"[CLINGO] Horizon={horizon}")
    logger.info(f"[CLINGO] Threads={THREADS}")
    logger.info(f"[CLINGO] Files={lp_files}")

    models = collect_models(create_control(lp_files, horizon))
    log_phase(logger, "[CLINGO] Solve runtime", start)
    logger.info(f"[CLINGO] Models found={len(models)}")
    return models


def create_control(lp_files, horizon):
    """Load and ground LP files in a configured Clingo control."""
    arguments = ["-c", f"horizon={horizon}", "-t", str(THREADS), "--warn=none"]
    control = clingo.Control(arguments)
    for lp_file in lp_files:
        control.load(lp_file)
    control.ground([("base", [])])
    return control


def collect_models(control, assumptions=None):
    """Return all shown atoms from models produced by a control."""
    models = []
    with control.solve(yield_=True, assumptions=assumptions or []) as handle:
        for model in handle:
            models.append([str(atom) for atom in model.symbols(shown=True)])
    return models
