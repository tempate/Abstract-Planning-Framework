"""Create per-run artifacts and provide the shared planner logger."""

import json
import logging
import os
import shutil
import time
import uuid

from core.paths import TEMP_DIR

def setup_debug_logger(base_dir):
    """Configure the file logger for a single planning run."""
    debug_dir = os.path.join(base_dir, "debug")
    os.makedirs(debug_dir, exist_ok=True)

    log_file = os.path.join(debug_dir, "planner_debug.log")

    logger = logging.getLogger("planner_debug")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode="a")
    formatter = logging.Formatter(
        "%(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
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

def save_json_iteration_file(debug_dir, iteration, name, obj):
    """Serialize an object as a formatted JSON iteration artifact."""
    save_iteration_file(
        debug_dir,
        iteration,
        name,
        json.dumps(obj, indent=2)
    )

def log_phase(logger, name, start_time):
    """Log and return the elapsed time since ``start_time``."""
    elapsed = time.perf_counter() - start_time
    logger.info(f"{name}: {elapsed:.3f}s")
    return elapsed

def get_logger():
    """Return the logger shared by the planning pipeline."""
    return logging.getLogger("planner_debug")

def get_debug_dir():
    """Return the current run's debug directory after logger setup."""
    logger = get_logger()

    if not hasattr(logger, "debug_dir"):
        raise RuntimeError(
            "Debug directory not initialized. Call setup_debug_logger first."
        )

    return logger.debug_dir

def create_run_dir(dir_name="concrete"):
    """Create and return an isolated directory for a planner run."""
    directory_name = dir_name or "concrete"
    run_id = str(uuid.uuid4())
    base_dir = os.path.join(TEMP_DIR, directory_name, run_id)
    print(base_dir)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir, run_id


def _iteration_dir(debug_dir, iteration):
    """Create and return the debug subdirectory for one iteration."""
    folder = os.path.join(debug_dir, f"iter_{iteration:03d}")
    os.makedirs(folder, exist_ok=True)
    return folder
