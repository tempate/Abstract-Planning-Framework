import os
import time
import json
import logging
import shutil
import uuid

from core.paths import TEMP_DIR

def setup_debug_logger(base_dir):
    debug_dir = os.path.join(base_dir, "debug")
    os.makedirs(debug_dir, exist_ok=True)

    log_file = os.path.join(debug_dir, "planner_debug.log")

    logger = logging.getLogger("planner_debug")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        logger.handlers.clear()

    fh = logging.FileHandler(log_file, mode="a")
    formatter = logging.Formatter(
        "%(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.debug_dir = debug_dir

    return logger, debug_dir

def save_iteration_file(debug_dir, iteration, name, content):
    path = os.path.join(_iteration_dir(debug_dir, iteration), name)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path

def copy_iteration_file(debug_dir, iteration, file_path):
    filename = os.path.basename(file_path)
    dst_path = os.path.join(_iteration_dir(debug_dir, iteration), filename)

    shutil.copyfile(file_path, dst_path)

    return dst_path

def save_json_iteration_file(debug_dir, iteration, name, obj):
    save_iteration_file(
        debug_dir,
        iteration,
        name,
        json.dumps(obj, indent=2)
    )

def log_phase(logger, name, start_time):
    elapsed = time.perf_counter() - start_time
    logger.info(f"{name}: {elapsed:.3f}s")
    return elapsed

def get_logger():
    return logging.getLogger("planner_debug")

def get_debug_dir():
    logger = get_logger()

    if not hasattr(logger, "debug_dir"):
        raise RuntimeError(
            "Debug directory not initialized. Call setup_debug_logger first."
        )

    return logger.debug_dir

def create_run_dir(dir_name="concrete"):
    dir_name = dir_name or "concrete"
    run_id = str(uuid.uuid4())
    base_dir = os.path.join(TEMP_DIR, dir_name, run_id)
    print(base_dir)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir, run_id


def _iteration_dir(debug_dir, iteration):
    folder = os.path.join(debug_dir, f"iter_{iteration:03d}")
    os.makedirs(folder, exist_ok=True)
    return folder
