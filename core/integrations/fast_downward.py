"""Fast Downward integration and plan conversion helpers."""

import os
from statistics import mode
import subprocess

from core.execution import get_logger, timed_phase
from core.paths import FAST_DOWNWARD_SCRIPT


# Fast Downward exit codes
_PLAN_FOUND = {0, 1, 2, 3}
_UNSOLVABLE = {10, 11}


def run_fast_downward(base_dir, domain, problem, label, task):
    """Run concrete planning and, when provided, abstract planning."""
    logger = get_logger()
    logger.info("=" * 65)
    logger.info("[FD] Fast Downward started")

    result, time = _run_task(
        label, base_dir, domain, problem, task, logger
    )

    logger.info(f"[FD] SUMMARY | {time:.3f}s")
    logger.info("[FD] Fast Downward finished")

    return result, time


def _run_task(label, dir, domain, problem, task, logger):
    # Create the directory for the task
    os.makedirs(dir, exist_ok=True)

    # Define the paths for the input and output files
    paths = {
        "domain": os.path.join(dir, "domain.pddl"),
        "problem": os.path.join(dir, "problem.pddl"),
        "sas": os.path.join(dir, "output.sas"),
        "plan": os.path.join(dir, "sas_plan"),
    }

    # Write input files to the temporary directory
    with open(paths["domain"], "wb") as file:
        file.write(domain)
    with open(paths["problem"], "wb") as file:
        file.write(problem)

    # Run Fast Downward for the task
    logger.info(f"[FD] Running {label} planner")
    with timed_phase(
        logger, f"[FD] {label.title()} planner runtime"
    ) as runtime:
        result = subprocess.run(
            _get_command(paths, task),
            capture_output=True,
            text=True,
        )

    if result.returncode in _UNSOLVABLE:
        raise RuntimeError(f"Fast Downward ({label}): problem is unsolvable")

    if result.returncode not in _PLAN_FOUND:
        diagnostics = "\n".join(
            output.strip() for output in (result.stdout, result.stderr) if output.strip()
        )
        logger.error(f"[FD] {label.title()} planner FAILED")
        logger.error(diagnostics)
        raise RuntimeError(
            f"Fast Downward ({label}) failed with exit code "
            f"{result.returncode}:\n{diagnostics}"
        )

    logger.info(f"[FD] {label.title()} planner success")

    # Only calculate the horizon for planning tasks
    horizon = 0
    if task == "plan":
        horizon = calc_horizon(paths["plan"])
        logger.info(f"[FD] {label.title()} horizon={horizon}")

    return {
        "horizon": horizon,
        "sasFile": paths["sas"],
        "planFile": paths["plan"],
    }, runtime.elapsed


def _get_command(paths, task):
    """Get the Fast Downward command for a task."""
    commands = {
        "plan": [
            "python3",
            FAST_DOWNWARD_SCRIPT,
            "--plan-file", paths["plan"],
            "--sas-file", paths["sas"],
            "--keep-sas-file",
            paths["domain"],
            paths["problem"],
            "--search",
            "astar(lmcut())",
        ],
        "translate": [
            "python3",
            FAST_DOWNWARD_SCRIPT,
            "--sas-file", paths["sas"],
            "--keep-sas-file",
            "--translate",
            paths["domain"],
            paths["problem"],
        ]
    }
    return commands[task]


def calc_horizon(plan_file_path):
    with open(plan_file_path, encoding="utf-8") as plan_file:
        # Only count non-empty lines that aren't comments
        return sum(
            1
            for line in plan_file
            if line.strip() and not line.lstrip().startswith(";")
        )
