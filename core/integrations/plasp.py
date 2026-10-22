"""plasp integration for translating planning instances to ASP."""

import os
import subprocess

from core.integrations.paths import PLASP_BIN, SEQUENTIAL_ENCODING
from core.outcomes import IntegrationError


def sas_to_asp(sas_path):
    """Translate a SAS instance using the sequential incremental encoding."""
    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}; run `python -m scripts.setup`")

    with open(SEQUENTIAL_ENCODING, "r", encoding="utf-8") as encoding_source:
        encoding = encoding_source.read()

    command = [PLASP_BIN, "translate", sas_path]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if completed_process.returncode != 0:
        raise IntegrationError(f"plasp failed:\n{completed_process.stderr}")
    fragments = (encoding, completed_process.stdout)
    return "\n".join(fragment.rstrip("\n") for fragment in fragments) + "\n"
