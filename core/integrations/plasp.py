"""PlanPilot integration for translating planning instances to ASP."""

import os
import subprocess

from core.paths import (
    ABSTRACT_TIME_STEPS_ENCODING,
    ACTION_PER_TIME_STEP_ENCODING,
    BOUNDED_HORIZON_ENCODING,
    EXACT_HORIZON_ENCODING,
    PLASP_BIN,
)

_HORIZON_ENCODINGS = {
    "exact": EXACT_HORIZON_ENCODING,
    "bounded": BOUNDED_HORIZON_ENCODING,
}

_SWITCH_RULE_BOUNDS = {"exact": "1", "bounded": "0"}


def plan_to_asp(
    sas_path,
    asp_path,
    encoding_type = "exact",
    abstract_time_steps = False,
):
    """Translate a SAS instance to ASP and prepend its encodings."""
    # Encoding files for translation
    encoding_file = _HORIZON_ENCODINGS[encoding_type]

    if abstract_time_steps:
        time_file = ABSTRACT_TIME_STEPS_ENCODING
    else:
        time_file = ACTION_PER_TIME_STEP_ENCODING

    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}")

    # Create the output directory if it doesn't exist
    dir = os.path.dirname(asp_path)
    os.makedirs(dir, exist_ok=True)

    with open(asp_path, "w", encoding="utf-8") as asp_file:
        # Write encodings
        with open(encoding_file, "r", encoding="utf-8") as file:
            asp_file.write(file.read())
        with open(time_file, "r", encoding="utf-8") as file:
            asp_file.write(file.read())

        # Run plasp translation
        asp_file.flush()
        command = [PLASP_BIN, "translate", sas_path]
        result = subprocess.run(
            command,
            stdout=asp_file,
            stderr=subprocess.PIPE,
            text=True,
        )

    if result.returncode != 0:
        raise RuntimeError(f"plasp failed:\n{result.stderr}")


def append_pddl_facts_to_asp(pddl_path, asp_path):
    """Append No-Mystery fuel and arithmetic facts from a PDDL problem."""

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

    with open(asp_path, "a", encoding="utf-8") as asp_file:
        asp_file.write("\n% --- ADDED FROM PDDL ---\n")
        asp_file.writelines(f"{fact}\n" for fact in facts)


def add_switch_to_asp_rule(asp_path, encoding_type="exact"):
    """Add a switch guard to the action-occurrence constraint."""

    # Define the original rule and the modified rule based on the encoding type
    bound = _SWITCH_RULE_BOUNDS[encoding_type]
    rule_to_modify = f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- time(T), T > 0."
    modified_rule = (
        f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- "
        "time(T), not switch(T), T > 0."
    )

    # Read the ASP file, modify the rule, and write it back
    with open(asp_path, "r", encoding="utf-8") as source_file:
        lines = source_file.readlines()

    with open(asp_path, "w", encoding="utf-8") as output_file:
        for line in lines:
            if line.strip() == rule_to_modify:
                output_file.write(modified_rule + "\n")
            else:
                output_file.write(line)
