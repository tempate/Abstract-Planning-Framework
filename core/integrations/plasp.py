"""plasp integration for translating planning instances to ASP."""

import os
import subprocess

from core.integrations.paths import PLASP_BIN, SEQUENTIAL_ENCODING
from core.utilities.outcomes import IntegrationError
from core.asp.program import AspProgram, make_steps_optional


def sas_to_asp(sas_path, optimize=True):
    """Translate a SAS instance using the sequential incremental encoding."""
    with open(SEQUENTIAL_ENCODING, "r", encoding="utf-8") as encoding_source:
        encoding = encoding_source.read()

    # A doubling horizon finds the plans shorter than it only if a step can stay empty.
    if not optimize:
        encoding = make_steps_optional(encoding)

    return AspProgram(encoding, _translate(sas_path))


def _translate(sas_path):
    """Run plasp on the SAS file and return the task as ASP facts."""
    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}; run `python -m scripts.setup`")

    command = [PLASP_BIN, "translate", sas_path]
    completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if completed.returncode != 0:
        raise IntegrationError(f"plasp failed:\n{completed.stderr}")

    return completed.stdout
