import os
import subprocess
import uuid
import time

from log_utils import *

def run_fastdownward_service(
    base_dir,
    domain_file,
    problem_file,
    abstract_domain_file=None,
    abstract_problem_file=None,
    fd_task="plan",
):
    total_start = time.perf_counter()

    # Read file contents
    domain_bytes = domain_file.read()
    problem_bytes = problem_file.read()

    logger = get_logger()

    logger.info("=" * 65)
    logger.info("[FD] Fast Downward service started")

    current_directory = os.path.dirname(os.path.abspath(__file__))

    # File paths
    domain_file_path = os.path.join(base_dir, "domain.pddl")
    problem_file_path = os.path.join(base_dir, "problem.pddl")
    sas_file_path = os.path.join(base_dir, "output.sas")
    plan_file_path = os.path.join(base_dir, "sas_plan")

    # Write domain and problem files
    with open(domain_file_path, "wb") as f:
        f.write(domain_bytes)

    with open(problem_file_path, "wb") as f:
        f.write(problem_bytes)

    # Fast Downward script path
    fast_downward_script = os.path.join(
        current_directory, "lib", "downward", "fast-downward.py"
    )

    # Run Fast Downward (concrete)
    if fd_task == "plan":
        command = [
            "python3",
            fast_downward_script,
            "--plan-file",
            plan_file_path,
            "--sas-file",
            sas_file_path,
            "--keep-sas-file",
            domain_file_path,
            problem_file_path,
            "--search",
            "astar(lmcut())",
        ]
    else:
        command = [
            "python3",
            fast_downward_script,
            "--sas-file",
            sas_file_path,
            "--keep-sas-file",
            "--translate",
            domain_file_path,
            problem_file_path,
        ]

    logger.info("[FD] Running concrete planner")

    concrete_start = time.perf_counter()

    result = subprocess.run(command, capture_output=True, text=True)
    
    concrete_time = log_phase(
            logger,
            "[FD] Concrete planner runtime",
            concrete_start
        )

    if result.returncode != 0:
        logger.error("[FD] Concrete planner FAILED")
        logger.error(result.stderr)
        raise RuntimeError(f"Fast Downward failed:\n{result.stderr}")

    logger.info("[FD] Concrete planner success")

    horizon = 0

    if fd_task == "plan":
        horizon = calculate_horizon(plan_file_path)

        logger.info(f"[FD] Concrete horizon={horizon}")

    concrete_result = {
        "horizon": horizon,
        "sasFile": sas_file_path,
        "planFile": plan_file_path,
    }

    abstract_time = 0

    # Optional abstract run
    abstract_result = None
    if abstract_domain_file and abstract_problem_file:
        logger.info("[FD] Running abstract planner")

        abstract_dir = os.path.join(base_dir, "abstract")
        os.makedirs(abstract_dir, exist_ok=True)

        abstract_domain_path = os.path.join(abstract_dir, "domain.pddl")
        abstract_problem_path = os.path.join(abstract_dir, "problem.pddl")
        abstract_sas_file = os.path.join(abstract_dir, "output.sas")
        abstract_plan_file = os.path.join(abstract_dir, "sas_plan")

        with open(abstract_domain_path, "wb") as f:
            f.write(abstract_domain_file.read())

        with open(abstract_problem_path, "wb") as f:
            f.write(abstract_problem_file.read())

        cmd = [
            "python3",
            fast_downward_script,
            "--plan-file",
            abstract_plan_file,
            "--sas-file",
            abstract_sas_file,
            "--keep-sas-file",
            abstract_domain_path,
            abstract_problem_path,
            "--search",
            "astar(lmcut())",
        ]

        abstract_start = time.perf_counter()
        result = subprocess.run(cmd, capture_output=True, text=True)

        abstract_time = log_phase(
            logger,
            "[FD] Abstract planner runtime",
            abstract_start
        )

        if result.returncode != 0:
            logger.error("[FD] Abstract planner FAILED")
            logger.error(result.stderr)
            raise RuntimeError(f"Fast Downward (abstract) failed:\n{result.stderr}")

        logger.info("[FD] Abstract planner success")

        abstract_horizon = calculate_horizon(abstract_plan_file)

        logger.info(
            f"[FD] Abstract horizon={abstract_horizon}"
        )

        abstract_result = {
            "horizon": abstract_horizon,
            "sasFile": abstract_sas_file,
            "planFile": abstract_plan_file,
        }
    
    total_time = time.perf_counter() - total_start

    logger.info(
        f"[FD] SUMMARY | "
        f"concrete={concrete_time:.3f}s | "
        f"abstract={abstract_time:.3f}s | "
        f"total={total_time:.3f}s"
    )

    logger.info("[FD] Fast Downward service finished")

    return {
        "concrete": concrete_result,
        "abstract": abstract_result,
        "timings": {
            "fd_concrete_time": concrete_time,
            "fd_abstract_time": abstract_time if abstract_result else None,
            "fd_total_time": total_time
        }
    }


def calculate_horizon(plan_file_path):
    with open(plan_file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Ignore trailing cost comment
    if lines and lines[-1].startswith(";"):
        return len(lines) - 1
    return len(lines)

def fd_plan_to_occurs_abstract(plan_file_path, output_path):
    occurs_atoms = []

    with open(plan_file_path, "r") as f:
        t = 1  # your format starts at 1

        for line in f:
            line = line.strip()

            # skip empty lines and cost line
            if not line or line.startswith(";"):
                continue

            # remove parentheses
            line = line.strip("()")

            parts = line.split()
            action_name = parts[0]
            args = parts[1:]

            # build ("a","b","c") tuple
            arg_string = ",".join(f'"{a}"' for a in args)

            atom = (
                f'occurs_abstract(action(("'
                f'{action_name}",{arg_string}'
                f')), {t}).'
            )

            occurs_atoms.append(atom)
            t += 1

    # write to file
    with open(output_path, "w") as f:
        f.write("\n".join(occurs_atoms))

    return occurs_atoms