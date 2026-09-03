"""plasp integration for translating planning instances to ASP."""

import os
import subprocess

from core.planning.outcomes import IntegrationError

from core.paths import ABSTRACT_TIME_STEPS_ENCODING, ACTION_PER_TIME_STEP_ENCODING, EXACT_HORIZON_ENCODING, PLASP_BIN


def sas_to_asp(sas_path, abstract_time_steps=False):
    """Translate a SAS instance using the exact incremental encoding."""
    if abstract_time_steps:
        time_file = ABSTRACT_TIME_STEPS_ENCODING
    else:
        time_file = ACTION_PER_TIME_STEP_ENCODING

    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}; run `python scripts/install_plasp.py`")

    with open(EXACT_HORIZON_ENCODING, "r", encoding="utf-8") as encoding_source:
        encoding = encoding_source.read()
    with open(time_file, "r", encoding="utf-8") as time_source:
        time_encoding = time_source.read()

    command = [PLASP_BIN, "translate", sas_path]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if completed_process.returncode != 0:
        raise IntegrationError(f"plasp failed:\n{completed_process.stderr}")
    fragments = (encoding, time_encoding, completed_process.stdout)
    return "\n".join(fragment.rstrip("\n") for fragment in fragments) + "\n"


def add_switch_to_asp_rule(asp):
    """Guard the exact encoding's occurrence constraint with a switch."""
    rule_to_modify = "1 {occurs(Action, t) : action(Action)} 1."
    modified_rule = "1 {occurs(Action, t) : action(Action)} 1 :- not switch(t)."

    lines = []
    guarded = 0
    for line in asp.splitlines():
        if line.strip() == rule_to_modify:
            lines.append(modified_rule)
            guarded += 1
        else:
            lines.append(line)

    # Without the guard the switches never suppress the rule, so the abstract
    # plan would silently stop constraining the concrete search.
    if guarded == 0:
        raise IntegrationError(f"No occurrence rule to guard with switches in the {encoding_type} encoding")

    return "\n".join(lines) + ("\n" if asp.endswith("\n") else "")
