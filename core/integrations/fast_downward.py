"""Fast Downward integration for translating PDDL tasks to SAS."""

import os
import subprocess
import sys

from core.paths import FAST_DOWNWARD_SCRIPT
from core.planning.outcomes import IntegrationError

_SUCCESS = 0


def pddl_to_sas(base_dir, domain_path, problem_path, label):
    """Translate a concrete or abstract PDDL task to SAS."""
    os.makedirs(base_dir, exist_ok=True)

    # Define the paths for the input and output files
    paths = {
        "domain": os.fspath(domain_path),
        "problem": os.fspath(problem_path),
        "sas": os.path.join(base_dir, "output.sas"),
    }

    # Run the Fast Downward translator
    completed_process = subprocess.run(_get_command(paths), capture_output=True, text=True)

    if completed_process.returncode != _SUCCESS:
        diagnostics = "\n".join(
            output.strip() for output in (completed_process.stdout, completed_process.stderr) if output.strip()
        )
        raise IntegrationError(
            f"Fast Downward ({label}) failed with exit code {completed_process.returncode}:\n{diagnostics}"
        )

    return {"sasFile": paths["sas"]}


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
