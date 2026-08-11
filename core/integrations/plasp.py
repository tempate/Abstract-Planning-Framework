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


def generate_lp_with_plasp(
    sas_or_pddl_path: str,
    lp_output_path: str,
    encoding_type: str = "exact",
    is_pddl_instance: bool = False,
    domain_file: str | None = None,
    abstract_time_steps: bool = False,
):
    """Translate a SAS or PDDL instance and prepend its encodings."""
    encoding_file, time_file = _encoding_files(
        encoding_type, abstract_time_steps
    )

    if not os.path.exists(PLASP_BIN):
        raise FileNotFoundError(f"plasp binary not found: {PLASP_BIN}")

    command = [PLASP_BIN, "translate"]
    if is_pddl_instance:
        if not domain_file:
            raise ValueError("Domain file is required for PDDL input.")
        command.extend([domain_file, sas_or_pddl_path])
    else:
        command.append(sas_or_pddl_path)

    os.makedirs(os.path.dirname(lp_output_path), exist_ok=True)
    with open(lp_output_path, "w", encoding="utf-8") as lp_file:
        _write_encoding_files(lp_file, encoding_file, time_file)
        result = subprocess.run(
            command,
            stdout=lp_file,
            stderr=subprocess.PIPE,
            text=True,
        )

    if result.returncode != 0:
        raise RuntimeError(f"plasp failed:\n{result.stderr}")


def _encoding_files(encoding_type, abstract_time_steps):
    """Return the encoding files for a translation."""
    try:
        horizon_file = _HORIZON_ENCODINGS[encoding_type]
    except KeyError as error:
        raise ValueError(f"Unsupported encoding type: {encoding_type}") from error
    time_file = (
        ABSTRACT_TIME_STEPS_ENCODING
        if abstract_time_steps
        else ACTION_PER_TIME_STEP_ENCODING
    )
    return horizon_file, time_file


def append_pddl_facts_to_lp(pddl_path, lp_output_path):
    """Append No-Mystery fuel and arithmetic facts from a PDDL problem."""
    facts = _extract_supported_pddl_facts(pddl_path)

    with open(lp_output_path, "a", encoding="utf-8") as lp_file:
        lp_file.write("\n% --- ADDED FROM PDDL ---\n")
        lp_file.writelines(f"{fact}\n" for fact in facts)


def add_switch_to_lp_rule(lp_path, encoding_type="exact"):
    """Add a switch guard to the action-occurrence constraint."""
    try:
        bound = _SWITCH_RULE_BOUNDS[encoding_type]
    except KeyError as error:
        raise ValueError(f"Unsupported encoding type: {encoding_type}") from error
    rule_to_modify = f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- time(T), T > 0."
    modified_rule = (
        f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- "
        "time(T), not switch(T), T > 0."
    )

    with open(lp_path, "r", encoding="utf-8") as source_file:
        lines = source_file.readlines()

    with open(lp_path, "w", encoding="utf-8") as output_file:
        for line in lines:
            if line.strip() == rule_to_modify:
                output_file.write(modified_rule + "\n")
            else:
                output_file.write(line)


def _write_encoding_files(destination, *source_paths):
    for source_path in source_paths:
        with open(source_path, "r", encoding="utf-8") as source_file:
            destination.write(source_file.read())


def _extract_supported_pddl_facts(pddl_path):
    facts = []
    with open(pddl_path, "r", encoding="utf-8") as pddl_file:
        for line in pddl_file:
            fact = _pddl_line_to_lp_fact(line.strip())
            if fact:
                facts.append(fact)
    return facts


def _pddl_line_to_lp_fact(line):
    """Convert a supported one-line PDDL fact to its ASP representation."""
    if line.startswith("(fuelcost"):
        _, level, origin, destination = line.replace("(", "").replace(")", "").split()
        return f'fuelcost("{level}","{origin}","{destination}").'
    if line.startswith("(sum"):
        _, left, right, total = line.replace("(", "").replace(")", "").split()
        return f'sum("{left}","{right}","{total}").'
    return None
