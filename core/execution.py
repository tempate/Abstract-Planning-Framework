"""Manage planning workspaces, diagnostic output, logging, and timing."""

import json
import logging
import os
import shutil
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Iterator

from core.paths import TEMP_DIR


LOGGER_NAME = "planner_debug"


def setup_debug_logger(base_dir):
    """Configure the file logger for a single planning run."""
    debug_dir = os.path.join(base_dir, "debug")
    os.makedirs(debug_dir, exist_ok=True)

    log_file = os.path.join(debug_dir, "planner_debug.log")

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode="a")
    formatter = logging.Formatter(
        "%(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.debug_dir = debug_dir

    return logger, debug_dir


def save_iteration_file(debug_dir, iteration, name, content):
    """Save text content under an iteration-specific debug directory."""
    path = os.path.join(_iteration_dir(debug_dir, iteration), name)

    with open(path, "w", encoding="utf-8") as output_file:
        output_file.write(content)

    return path


def copy_iteration_file(debug_dir, iteration, file_path):
    """Copy an existing file into an iteration-specific debug directory."""
    filename = os.path.basename(file_path)
    destination_path = os.path.join(_iteration_dir(debug_dir, iteration), filename)

    shutil.copyfile(file_path, destination_path)

    return destination_path


def save_json_iteration_file(debug_dir, iteration, name, data):
    """Serialize an object as a formatted JSON iteration artifact."""
    save_iteration_file(
        debug_dir,
        iteration,
        name,
        json.dumps(data, indent=2),
    )


@dataclass
class PhaseTiming:
    """A monotonic phase timer whose elapsed value can be read while running."""

    _started_at: float = field(default_factory=time.perf_counter)
    _elapsed: float | None = None

    @property
    def elapsed(self) -> float:
        if self._elapsed is not None:
            return self._elapsed
        return time.perf_counter() - self._started_at

    def stop(self) -> None:
        if self._elapsed is None:
            self._elapsed = time.perf_counter() - self._started_at


@contextmanager
def timed_phase(
    logger: logging.Logger | None = None,
    name: str | None = None,
) -> Iterator[PhaseTiming]:
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


def _iteration_dir(debug_dir, iteration):
    """Create and return the debug subdirectory for one iteration."""
    folder = os.path.join(debug_dir, f"iter_{iteration:03d}")
    os.makedirs(folder, exist_ok=True)
    return folder
