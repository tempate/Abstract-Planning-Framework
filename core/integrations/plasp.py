"""PlanPilot integration for translating planning instances to ASP."""

import os
import subprocess

from core.asp import join_asp
from core.paths import (
    ABSTRACT_TIME_STEPS_ENCODING,
    ACTION_PER_TIME_STEP_ENCODING,
    BOUNDED_HORIZON_ENCODING,
    EXACT_HORIZON_ENCODING,
    PLASP_BIN,
)

_HORIZON_ENCODINGS = {"exact": EXACT_HORIZON_ENCODING, "bounded": BOUNDED_HORIZON_ENCODING}

_SWITCH_RULE_BOUNDS = {"exact": "1", "bounded": "0"}


def sas_to_asp(sas_path, encoding_type="exact", abstract_time_steps=False):
    """Translate a SAS instance and return an in-memory ASP program."""
    # Encoding files for translation
    encoding_file = _HORIZON_ENCODINGS[encoding_type]

    if abstract_time_steps:
        time_file = ABSTRACT_TIME_STEPS_ENCODING
    else:
        time_file = ACTION_PER_TIME_STEP_ENCODING

    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}")

    with open(encoding_file, "r", encoding="utf-8") as encoding_source:
        encoding = encoding_source.read()
    with open(time_file, "r", encoding="utf-8") as time_source:
        time_encoding = time_source.read()

    command = [PLASP_BIN, "translate", sas_path]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if completed_process.returncode != 0:
        raise RuntimeError(f"plasp failed:\n{completed_process.stderr}")
    return join_asp(encoding, time_encoding, completed_process.stdout)


def append_pddl_facts_to_asp(pddl_path, asp):
    """Return an ASP program with No-Mystery fuel and arithmetic facts."""

    # Extract supported facts from the PDDL
    facts = []
    with open(pddl_path, "r", encoding="utf-8") as pddl_file:
        for line in pddl_file:
            line = line.strip()
            # Convert a supported one-line PDDL fact to its ASP representation.
            if line.startswith("(fuelcost"):
                _, level, origin, destination = line.replace("(", "").replace(")", "").split()
                fact = f'fuelcost("{level}","{origin}","{destination}").'
                facts.append(fact)

            if line.startswith("(sum"):
                _, left, right, total = line.replace("(", "").replace(")", "").split()
                fact = f'sum("{left}","{right}","{total}").'
                facts.append(fact)

    additions = "\n".join(["% --- ADDED FROM PDDL ---", *facts])
    return join_asp(asp, additions)


def add_switch_to_asp_rule(asp, encoding_type="exact"):
    """Return an ASP program with a switch-guarded occurrence constraint."""

    # Define the original rule and the modified rule based on the encoding type
    bound = _SWITCH_RULE_BOUNDS[encoding_type]
    rule_to_modify = f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- time(T), T > 0."
    modified_rule = f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- time(T), not switch(T), T > 0."

    lines = [modified_rule if line.strip() == rule_to_modify else line for line in asp.splitlines()]
    return "\n".join(lines) + ("\n" if asp.endswith("\n") else "")
