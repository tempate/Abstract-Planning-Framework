"""Fast Downward integration for translating PDDL tasks to SAS and searching them."""

import os
import subprocess
import sys

from core.integrations.paths import FAST_DOWNWARD_SCRIPT
from core.outcomes import IntegrationError, UnsolvableTaskError

# Fast Downward's exit codes, documented at
# https://www.fast-downward.org/latest/documentation/exit-codes/.
_SUCCESS = 0
_TRANSLATE_UNSOLVABLE = 10
_SEARCH_UNSOLVABLE = 11

SEARCH = "astar(blind())"


def pddl_to_sas(base_dir, domain_path, problem_path, label):
    """Translate a concrete or abstract PDDL task and return its SAS file."""
    os.makedirs(base_dir, exist_ok=True)
    sas_path = os.path.join(base_dir, "output.sas")
    command = [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--sas-file",
        sas_path,
        "--keep-sas-file",
        "--translate",
        os.fspath(domain_path),
        os.fspath(problem_path),
    ]
    completed_process = subprocess.run(command, capture_output=True, text=True)

    if completed_process.returncode == _TRANSLATE_UNSOLVABLE:
        raise UnsolvableTaskError(f"Fast Downward ({label}) proved the task unsolvable while translating")

    if completed_process.returncode != _SUCCESS:
        diagnostics = "\n".join(
            output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
        )
        raise IntegrationError(
            f"Fast Downward ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
        )

    return sas_path


def has_plan(base_dir, domain_path, problem_path, label):
    """Translate and search one PDDL task, reporting only whether it has a plan."""
    os.makedirs(base_dir, exist_ok=True)
    plan_path = os.path.join(base_dir, f"{label}.plan")
    # Both paths have to be named. Left to itself the driver writes and reads
    # output.sas in the working directory, which every task of a cluster run
    # shares, so concurrent tasks truncate and delete each other's file.
    sas_path = os.path.join(base_dir, f"{label}.sas")
    command = [
        sys.executable,
        FAST_DOWNWARD_SCRIPT,
        "--sas-file",
        sas_path,
        "--plan-file",
        plan_path,
        os.fspath(domain_path),
        os.fspath(problem_path),
        "--search",
        SEARCH,
    ]
    completed_process = subprocess.run(command, capture_output=True, text=True)

    if completed_process.returncode == _SUCCESS:
        return True
    if completed_process.returncode in (_TRANSLATE_UNSOLVABLE, _SEARCH_UNSOLVABLE):
        return False

    diagnostics = "\n".join(
        output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
    )
    raise IntegrationError(
        f"Fast Downward ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
    )
