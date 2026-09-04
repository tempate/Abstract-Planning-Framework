"""Fast Downward integration and plan conversion helpers."""

import os
import subprocess
import sys

from core.paths import FAST_DOWNWARD_SCRIPT
from core.planning.outcomes import IntegrationError, UnsolvableTaskError

# Fast Downward exit codes
_PLAN_FOUND = {0, 1, 2, 3}
_UNSOLVABLE = {10, 11}


def run_fast_downward(base_dir, domain_path, problem_path, label, task):
    """Run one Fast Downward translation or planning task."""
    os.makedirs(base_dir, exist_ok=True)

    # Define the paths for the input and output files
    paths = {
        "domain": os.fspath(domain_path),
        "problem": os.fspath(problem_path),
        "sas": os.path.join(base_dir, "output.sas"),
        "plan": os.path.join(base_dir, "sas_plan"),
    }

    # Run Fast Downward for the task
    completed_process = subprocess.run(_get_command(paths, task), capture_output=True, text=True)

    if completed_process.returncode in _UNSOLVABLE:
        raise UnsolvableTaskError(f"Fast Downward ({label}) reports that the problem is unsolvable")

    if completed_process.returncode not in _PLAN_FOUND:
        diagnostics = "\n".join(
            output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
        )
        raise IntegrationError(
            f"Fast Downward ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
        )

    # Only calculate the horizon for planning tasks
    horizon = 0
    if task == "plan":
        horizon = calc_horizon(paths["plan"])

    return {"horizon": horizon, "sasFile": paths["sas"], "planFile": paths["plan"]}


def _get_command(paths, task):
    """Get the Fast Downward command for a task."""
    commands = {
        "plan": [
            sys.executable,
            FAST_DOWNWARD_SCRIPT,
            "--plan-file",
            paths["plan"],
            "--sas-file",
            paths["sas"],
            "--keep-sas-file",
            paths["domain"],
            paths["problem"],
            "--search",
            "astar(lmcut())",
        ],
        "translate": [
            sys.executable,
            FAST_DOWNWARD_SCRIPT,
            "--sas-file",
            paths["sas"],
            "--keep-sas-file",
            "--translate",
            paths["domain"],
            paths["problem"],
        ],
    }
    return commands[task]


def calc_horizon(plan_file_path):
    with open(plan_file_path, encoding="utf-8") as plan_file:
        # Only count non-empty lines that aren't comments
        return sum(1 for line in plan_file if line.strip() and not line.lstrip().startswith(";"))
