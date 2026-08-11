import subprocess
import os, re
from scripts.utils.log_utils import *
from core.repo import CLINGO_BIN

THREADS = os.cpu_count()

def run_clingo(lp_files, horizon):
    logger = get_logger()
    start = time.perf_counter()

    logger.info("[CLINGO] Starting solve")
    logger.info(f"[CLINGO] Horizon={horizon}")
    logger.info(f"[CLINGO] Threads={THREADS}")
    logger.info(f"[CLINGO] Files={lp_files}")

    cmd = [CLINGO_BIN] + lp_files + ["-c", f"horizon={horizon}", "-t", str(THREADS), "--warn=none"]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    output = result.stdout

    models = []
    current_model = []

    collecting = False
    for line in output.splitlines():
        line = line.strip()

        if line.startswith("Answer:"):
            collecting = True
            current_model = []
            continue

        if collecting:
            if line == "" or line.startswith("SATISFIABLE") or line.startswith("UNSATISFIABLE"):
                if current_model:
                    models.append(current_model)
                collecting = False
                continue
            # Add each atom
            current_model.extend(line.split())

    log_phase(logger, "[CLINGO] Solve runtime", start)
    logger.info(f"[CLINGO] Models found={len(models)}")

    return models

def write_occurs_abs_lp(atoms, output_path):
    logger = get_logger()
    start = time.perf_counter()

    lines = []

    for atom in atoms:
        atom = atom.strip()

        if atom.startswith("occurs("):
            # occurs(action(...),T) → occurs_abstract(action(...),T)
            lines.append("occurs_abstract" + atom[len("occurs"): ] + ".")

        elif atom.startswith("occurs_abstract("):
            # already abstract (defensive)
            lines.append(atom + ".")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    logger.info(f"[FILES] wrote {output_path}")
    log_phase(logger, "[FILES] occurs_abs generation", start)


def create_map_lp(occurs_abs_path, output_path, abstract_symbol, concrete_objects):
    # concrete_hangars = ["hangar1", "hangar2"]

    logger = get_logger()
    start = time.perf_counter()

    with open(occurs_abs_path, "r") as f:
        lines_in = [line.strip() for line in f if line.strip()]

    lines_out = []
    for line in lines_in:
        if not line.startswith("occurs_abstract("):
            continue

        # Extract the inner part: occurs_abstract(inner)
        inner = line[len("occurs_abstract("):].rstrip(").")
        # Split into action_term and time by the last comma
        if ',' not in inner:
            continue
        action_str, time_str = inner.rsplit(",", 1)
        action_str = action_str.strip()
        time_str = time_str.strip()

        # Case 1: this action uses the abstract symbol -> choice rule
        if abstract_symbol in action_str:
            choices = []
            for obj in concrete_objects:
                new_action = action_str.replace(abstract_symbol, obj)
                choices.append(f"occurs({new_action}, {time_str})")

            lines_out.append(f"1 {{ {'; '.join(choices)} }} 1 :- occurs_abstract({action_str},{time_str}).")
        else:
            # case 2: no abstraction -> direct mapping
            lines_out.append(f"occurs({action_str},{time_str}) :- occurs_abstract({action_str},{time_str}).")

    # Write the map.lp
    with open(output_path, "w") as f:
        f.write("\n".join(lines_out))

    logger.info(f"[FILES] wrote {output_path}")
    log_phase(logger, "[MAP] create_map_lp", start)


def solve_concrete_incremental(lp_files, switch_map_lp, horizon):
    logger = get_logger()
    start = time.perf_counter()

    logger.info("[INC] Starting incremental solve")

    with open(switch_map_lp, "r") as f:
        raw_lines = [line.strip() for line in f if line.strip()]

    def extract_time(rule):
        """
        Finds last number before closing ')'
        Example:
            occurs(move(a),13)
        returns 13
        """
        nums = re.findall(r",\s*(\d+)\)", rule)
        if nums:
            return int(nums[-1])
        return 999999

    map_lines = sorted(raw_lines, key=extract_time)

    logger.info(f"[INC] Rules found={len(map_lines)}")

    base_dir = os.path.dirname(switch_map_lp)

    temp_active_lp = os.path.join(base_dir, "tmp_active_map.lp")

    if os.path.exists(temp_active_lp):
        os.remove(temp_active_lp)

    active_lines = []
    activated_abstract_actions = []

    def is_abstract_rule(rule: str):
        return "{" in rule and "}" in rule

    # Incrementally activate lines and test satisfiability
    for i, line in enumerate(map_lines):
        active_lines.append(line)

        current_is_abstract = is_abstract_rule(line)
        if current_is_abstract:
            activated_abstract_actions.append(line)

        # Look ahead: test if next action is abstract
        next_is_abstract = False
        if i + 1 < len(map_lines):
            next_is_abstract = is_abstract_rule(map_lines[i + 1])

        if next_is_abstract:
            with open(temp_active_lp, "w") as f:
                f.write("\n".join(active_lines))

            with open(temp_active_lp, "r") as f:
                content = f.read()

            logger.info("[MAP] tmp_active_map.lp content:")
            logger.info("\n" + content)

            cmd = (
                [CLINGO_BIN]
                + lp_files
                + [temp_active_lp]
                + ["-c", f"horizon={horizon}", "--seed=1", "--rand-freq=0", "--warn=none"]
            )

            print(cmd)

            logger.info(f"[INC] Testing prefix 1..{i+1}")
            logger.info(f"[INC] Testing before next abstract action (line {i+2})")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )

            logger.info("[CLINGO] STDOUT:")
            logger.info("\n" + result.stdout)

            logger.info("[CLINGO] STDERR:")
            logger.info("\n" + result.stderr)

            output = result.stdout

            if "UNSATISFIABLE" in output:
                logger.info("[INC] UNSAT detected")
                logger.info(f"[INC] Failing abstract actions={activated_abstract_actions}")
                log_phase(logger, "[INC] Runtime", start)
                return False, [], activated_abstract_actions

    # If all switches are consistent, compute concrete plans
    logger.info("[INC] All prefixes SAT. Solving full model.")

    with open(temp_active_lp, "w") as f:
        f.write("\n".join(active_lines))

    cmd = (
        [CLINGO_BIN]
        + lp_files
        + [temp_active_lp]
        + ["-c", f"horizon={horizon}", "-t", str(THREADS), "--warn=none"]
    )

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    output = result.stdout

    plans = []
    current_model = []
    collecting = False

    for line in output.splitlines():
        line = line.strip()

        if line.startswith("Answer:"):
            collecting = True
            current_model = []
            continue

        if collecting:
            if (
                line == ""
                or line.startswith("SATISFIABLE")
                or line.startswith("UNSATISFIABLE")
            ):
                if current_model:
                    plans.append(current_model)
                collecting = False
                continue

            current_model.extend(line.split())

    logger.info(f"[INC] Plans found={len(plans)}")
    log_phase(logger, "[INC] Runtime", start)

    return True, plans, activated_abstract_actions

def write_forbid_abstract_lp(abstract_atoms_to_forbid, output_path):
    logger = get_logger()
    start = time.perf_counter()

    logger.info("[REFINE] Writing forbid rules (abstract occurs atoms)")

    lines = []
    seen = set()

    for rule in abstract_atoms_to_forbid:
        rule = rule.strip().rstrip(".")

        abstract_atom = None

        # normal mapping rule with body
        if ":-" in rule:
            _, body = rule.split(":-", 1)
            body = body.strip()

            if body.startswith("occurs_abstract("):
                abstract_atom = "occurs" + body[len("occurs_abstract"):]

        # fallback if directly given occurs_abstract(...)
        elif rule.startswith("occurs_abstract("):
            abstract_atom = "occurs" + rule[len("occurs_abstract"):]

        if abstract_atom and abstract_atom not in seen:
            seen.add(abstract_atom)
            logger.info(f"[REFINE] forbid {abstract_atom}")
            lines.append(f":- {abstract_atom}.")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    logger.info(f"[FILES] wrote {output_path}")
    log_phase(logger, "[REFINE] forbid file generation", start)
