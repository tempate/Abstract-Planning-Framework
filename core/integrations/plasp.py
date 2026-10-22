"""plasp integration for translating planning instances to ASP."""

import os
import subprocess

from core.encodings.rules import AT_MOST_ONE_ACTION, EXACTLY_ONE_ACTION
from core.integrations.paths import PLASP_BIN, SEQUENTIAL_ENCODING
from core.outcomes import IntegrationError


def sas_to_asp(sas_path, exp_horizon=False):
    """Translate a SAS instance using the sequential incremental encoding."""
    with open(SEQUENTIAL_ENCODING, "r", encoding="utf-8") as encoding_source:
        encoding = encoding_source.read()

    if exp_horizon:
        encoding = encoding.replace(EXACTLY_ONE_ACTION, AT_MOST_ONE_ACTION)

    return encoding + "\n" + _translate(sas_path) + "\n"


def _translate(sas_path):
    """Run plasp on the SAS file and return the task as ASP facts."""
    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}; run `python -m scripts.setup`")

    command = [PLASP_BIN, "translate", sas_path]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if completed_process.returncode != 0:
        raise IntegrationError(f"plasp failed:\n{completed_process.stderr}")

    return completed_process.stdout
