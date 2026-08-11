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


def _encoding_files(encoding_type, abstract_time_steps):
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


def generate_lp_with_plasp(
    sas_or_pddl_path: str,
    lp_output_path: str,
    encoding_type: str = "exact",
    is_pddl_instance: bool = False,
    domain_file: str | None = None,
    abstract_time_steps: bool = False,
):
    encoding_file, time_file = _encoding_files(encoding_type, abstract_time_steps)

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

    with open(lp_output_path, "w") as lp_file:
        for source_path in (encoding_file, time_file):
            with open(source_path, "r") as source_file:
                lp_file.write(source_file.read())

        result = subprocess.run(
            command,
            stdout=lp_file,
            stderr=subprocess.PIPE,
            text=True,
        )

    if result.returncode != 0:
        raise RuntimeError(f"plasp failed:\n{result.stderr}")

def append_pddl_facts_to_lp(pddl_path, lp_output_path):
    fuelcost_facts = []
    sum_facts = []

    with open(pddl_path, "r") as f:
        for line in f:
            line = line.strip()

            # fuelcost
            if line.startswith("(fuelcost"):
                parts = line.replace("(", "").replace(")", "").split()
                _, level, x, y = parts
                fuelcost_facts.append(f'fuelcost("{level}","{x}","{y}").')

            # sum
            elif line.startswith("(sum"):
                parts = line.replace("(", "").replace(")", "").split()
                _, a, b, c = parts
                sum_facts.append(f'sum("{a}","{b}","{c}").')

    with open(lp_output_path, "a") as f:
        f.write("\n% --- ADDED FROM PDDL ---\n")
        for fact in fuelcost_facts + sum_facts:
            f.write(fact + "\n")

def add_switch_to_lp_rule(lp_path, encoding_type="exact"):
    """Add a switch guard to the action-occurrence constraint."""
    bounds = {"exact": "1", "bounded": "0"}
    try:
        bound = bounds[encoding_type]
    except KeyError as error:
        raise ValueError(f"Unsupported encoding type: {encoding_type}") from error
    rule_to_modify = f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- time(T), T > 0."
    modified_rule = (
        f"{bound} {{occurs(Action, T) : action(Action)}} 1 :- "
        "time(T), not switch(T), T > 0."
    )

    with open(lp_path, "r") as source_file:
        lines = source_file.readlines()

    with open(lp_path, "w") as output_file:
        for line in lines:
            if line.strip() == rule_to_modify:
                output_file.write(modified_rule + "\n")
            else:
                output_file.write(line)
