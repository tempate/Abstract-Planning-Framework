"""Fast Downward integration for translating PDDL tasks to SAS."""

import os
import subprocess
import sys

from core.execution import get_logger, timed_phase
from core.paths import FAST_DOWNWARD_SCRIPT
from core.planning.outcomes import IntegrationError

_SUCCESS = 0


def pddl_to_sas(base_dir, domain_path, problem_path, label):
    """Translate a concrete or abstract PDDL task to SAS."""
    logger = get_logger()
    logger.info("=" * 65)
    logger.info("[FD] Fast Downward started")

    task_result, elapsed_time = _pddl_to_sas(label, base_dir, domain_path, problem_path, logger)

    logger.info(f"[FD] SUMMARY | {elapsed_time:.3f}s")
    logger.info("[FD] Fast Downward finished")

    return task_result, elapsed_time


def _pddl_to_sas(label, task_directory, domain_path, problem_path, logger):
    # Create the directory for the task
    os.makedirs(task_directory, exist_ok=True)

    # Define the paths for the input and output files
    paths = {
        "domain": os.fspath(domain_path),
        "problem": os.fspath(problem_path),
        "sas": os.path.join(task_directory, "output.sas"),
    }

    # Run Fast Downward for the task
    logger.info(f"[FD] Running {label} translator")
    with timed_phase(logger, f"[FD] {label.title()} translator runtime") as runtime:
        completed_process = subprocess.run(_get_command(paths), capture_output=True, text=True)

    if completed_process.returncode != _SUCCESS:
        diagnostics = "\n".join(
            output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
        )
        logger.error(f"[FD] {label.title()} translator FAILED")
        logger.error(diagnostics)
        raise IntegrationError(
            f"Fast Downward ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
        )

    logger.info(f"[FD] {label.title()} translator success")

    return {"sasFile": paths["sas"]}, runtime.elapsed


def _get_command(paths):
    """Get the Fast Downward translation command."""
    return [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--sas-file",
        paths["sas"],
        "--keep-sas-file",
        "--translate",
        paths["domain"],
        paths["problem"],
    ]
