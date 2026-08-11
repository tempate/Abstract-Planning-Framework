import os
import subprocess
from core.repo import (
    ABSTRACT_TIME_STEPS_ENCODING,
    ACTION_PER_TIME_STEP_ENCODING,
    BOUNDED_HORIZON_ENCODING,
    EXACT_HORIZON_ENCODING,
    PLASP_BIN,
)


def generate_lp_with_plasp(
    sas_or_pddl_path: str,
    lp_output_path: str,
    encoding_type: str = "exact",
    is_pddl_instance: bool = False,
    domain_file: str | None = None,
    abstract_time_steps: bool = False,
):
    plasp_binary = PLASP_BIN
    encoding_file = (
        EXACT_HORIZON_ENCODING
        if encoding_type == "exact"
        else BOUNDED_HORIZON_ENCODING
    )
    time_file = (
        ABSTRACT_TIME_STEPS_ENCODING
        if abstract_time_steps
        else ACTION_PER_TIME_STEP_ENCODING
    )

    if not os.path.exists(plasp_binary):
        raise FileNotFoundError(f"plasp binary not found: {plasp_binary}")

    command = [plasp_binary, "translate"]

    if is_pddl_instance:
        if not domain_file:
            raise ValueError("Domain file is required for PDDL input.")
        command.extend([domain_file, sas_or_pddl_path])
    else:
        command.append(sas_or_pddl_path)

    os.makedirs(os.path.dirname(lp_output_path), exist_ok=True)

    with open(lp_output_path, "w") as lp_file:
        with open(encoding_file, "r") as ef:
            lp_file.write(ef.read())
        with open(time_file, "r") as tf:
            lp_file.write(tf.read())

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

def add_switch_to_lp_rule(lp_path, encoding_type: str = "exact",):
    """
    Modifies the LP file at lp_path by adding 'not switch(T)' to the
    action occurrence constraint rule.
    """
    if encoding_type == "exact":
        rule_to_modify = "1 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0."
        modified_rule = "1 {occurs(Action, T) : action(Action)} 1 :- time(T), not switch(T), T > 0."
    elif encoding_type == "bounded":
        rule_to_modify = "0 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0."
        modified_rule = "0 {occurs(Action, T) : action(Action)} 1 :- time(T), not switch(T), T > 0."

    # Read the LP file
    with open(lp_path, "r") as f:
        lines = f.readlines()

    # Modify the rule if it exists
    with open(lp_path, "w") as f:
        for line in lines:
            if line.strip() == rule_to_modify:
                f.write(modified_rule + "\n")
            else:
                f.write(line)
