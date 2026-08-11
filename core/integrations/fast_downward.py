"""Fast Downward integration and plan conversion helpers."""

import os
import subprocess
import time

from core.paths import FAST_DOWNWARD_SCRIPT

from core.runtime.run_artifacts import get_logger, log_phase


def run_fast_downward(
    base_dir,
    domain_file,
    problem_file,
    abstract_domain_file=None,
    abstract_problem_file=None,
    fd_task="plan",
):
    """Run Fast Downward for a concrete problem and, optionally, its abstraction."""
    logger = get_logger()
    total_start = time.perf_counter()
    logger.info("=" * 65)
    logger.info("[FD] Fast Downward started")

    concrete_result, concrete_time = _run_task(
        "concrete",
        base_dir,
        domain_file.read(),
        problem_file.read(),
        fd_task,
        logger,
    )

    abstract_result = None
    abstract_time = None
    if abstract_domain_file and abstract_problem_file:
        abstract_result, abstract_time = _run_task(
            "abstract",
            os.path.join(base_dir, "abstract"),
            abstract_domain_file.read(),
            abstract_problem_file.read(),
            "plan",
            logger,
        )

    total_time = time.perf_counter() - total_start
    logger.info(
        f"[FD] SUMMARY | concrete={concrete_time:.3f}s | "
        f"abstract={(abstract_time or 0):.3f}s | total={total_time:.3f}s"
    )
    logger.info("[FD] Fast Downward finished")

    return {
        "concrete": concrete_result,
        "abstract": abstract_result,
        "timings": {
            "fd_concrete_time": concrete_time,
            "fd_abstract_time": abstract_time,
            "fd_total_time": total_time,
        },
    }


def _run_task(label, directory, domain_bytes, problem_bytes, mode, logger):
    os.makedirs(directory, exist_ok=True)
    paths = _task_paths(directory)
    _write_input_files(paths, domain_bytes, problem_bytes)

    logger.info(f"[FD] Running {label} planner")
    start = time.perf_counter()
    result = subprocess.run(
        _command(paths, mode),
        capture_output=True,
        text=True,
    )
    elapsed = log_phase(logger, f"[FD] {label.title()} planner runtime", start)

    if result.returncode != 0:
        logger.error(f"[FD] {label.title()} planner FAILED")
        logger.error(result.stderr)
        raise RuntimeError(f"Fast Downward ({label}) failed:\n{result.stderr}")

    horizon = calculate_horizon(paths["plan"]) if mode == "plan" else 0
    logger.info(f"[FD] {label.title()} planner success")
    if mode == "plan":
        logger.info(f"[FD] {label.title()} horizon={horizon}")
    return {
        "horizon": horizon,
        "sasFile": paths["sas"],
        "planFile": paths["plan"],
    }, elapsed


def _task_paths(directory):
    return {
        "domain": os.path.join(directory, "domain.pddl"),
        "problem": os.path.join(directory, "problem.pddl"),
        "sas": os.path.join(directory, "output.sas"),
        "plan": os.path.join(directory, "sas_plan"),
    }


def _write_input_files(paths, domain_bytes, problem_bytes):
    with open(paths["domain"], "wb") as file:
        file.write(domain_bytes)
    with open(paths["problem"], "wb") as file:
        file.write(problem_bytes)


def _command(paths, mode):
    if mode == "plan":
        return [
            "python3",
            FAST_DOWNWARD_SCRIPT,
            "--plan-file", paths["plan"],
            "--sas-file", paths["sas"],
            "--keep-sas-file",
            paths["domain"],
            paths["problem"],
            "--search",
            "astar(lmcut())",
        ]
    if mode == "translate":
        return [
            "python3",
            FAST_DOWNWARD_SCRIPT,
            "--sas-file", paths["sas"],
            "--keep-sas-file",
            "--translate",
            paths["domain"],
            paths["problem"],
        ]
    raise ValueError(f"Unsupported Fast Downward task: {mode}")


def calculate_horizon(plan_file_path):
    with open(plan_file_path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]
    return len(lines) - 1 if lines and lines[-1].startswith(";") else len(lines)


def fast_downward_plan_to_abstract_atoms(plan_file_path, output_path):
    """Convert a Fast Downward plan into ``occurs_abstract`` facts."""
    abstract_atoms = []
    with open(plan_file_path, "r") as plan_file:
        time_step = 1
        for line in plan_file:
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            action_name, *arguments = line.strip("()").split()
            quoted_arguments = ",".join(f'"{argument}"' for argument in arguments)
            abstract_atoms.append(
                f'occurs_abstract(action(("{action_name}",{quoted_arguments})), {time_step}).'
            )
            time_step += 1

    with open(output_path, "w") as output_file:
        output_file.write("\n".join(abstract_atoms))
    return abstract_atoms
