"""Manage planning workspaces, diagnostic output, logging, and timing."""

import logging
import os
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field

from core.paths import TEMP_DIR

LOGGER_NAME = "planner_debug"


def setup_debug_logger(base_dir):
    """Configure the file logger for a single planning run."""
    debug_dir = os.path.join(base_dir, "debug")
    os.makedirs(debug_dir, exist_ok=True)

    log_file = os.path.join(debug_dir, "planner_debug.log")

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)

    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    file_handler = logging.FileHandler(log_file, mode="a")
    formatter = logging.Formatter("%(asctime)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.debug_dir = debug_dir

    return logger, debug_dir


@dataclass
class PhaseTiming:
    """A monotonic phase timer whose elapsed value can be read while running."""

    _started_at: float = field(default_factory=time.perf_counter)
    _elapsed: float | None = None

    @property
    def elapsed(self):
        if self._elapsed is not None:
            return self._elapsed
        return time.perf_counter() - self._started_at

    def stop(self):
        if self._elapsed is None:
            self._elapsed = time.perf_counter() - self._started_at


@contextmanager
def timed_phase(logger=None, name=None):
    """Measure a phase and optionally log its duration on exit."""
    timing = PhaseTiming()
    try:
        yield timing
    finally:
        timing.stop()
        if logger is not None and name is not None:
            logger.info(f"{name}: {timing.elapsed:.3f}s")


def get_logger():
    """Return the logger shared by the planning pipeline."""
    return logging.getLogger(LOGGER_NAME)


def create_run_dir(dir_name="concrete"):
    """Create and return an isolated directory for a planner run."""
    run_id = str(uuid.uuid4())
    base_dir = os.path.join(TEMP_DIR, dir_name, run_id)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir, run_id
