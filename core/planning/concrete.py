"""Orchestrate concrete planning from PDDL translation through ASP solving."""

import os
import time

from core.execution import create_run_dir, setup_debug_logger
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import generate_lp_with_plasp


def compute_concrete_plan(
    domain_path,
    problem_path,
    horizon=None,
    encoding="exact",
    time_step=False,
):
    """Translate and solve one concrete PDDL planning problem."""
    base_dir, run_id = create_run_dir()
    logger, _ = setup_debug_logger(base_dir)

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)
    total_start = time.perf_counter()

    downward_start = time.perf_counter()
    with (
        open(domain_path, "rb") as domain_file,
        open(problem_path, "rb") as problem_file,
    ):
        downward_result = run_fast_downward(
            base_dir=base_dir,
            domain_file=domain_file,
            problem_file=problem_file,
        )

    concrete_task = downward_result["concrete"]
    downward_time = time.perf_counter() - downward_start
    if horizon is None:
        horizon = concrete_task["horizon"]
    logger.info(f"Fast Downward time: {downward_time:.3f}s")

    concrete_lp_path = os.path.join(base_dir, "output_c.lp")
    lp_start = time.perf_counter()
    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_task["sasFile"],
        lp_output_path=concrete_lp_path,
        encoding_type=encoding,
        abstract_time_steps=time_step,
    )
    lp_time = time.perf_counter() - lp_start
    logger.info(f"LP generation time: {lp_time:.3f}s")

    solve_start = time.perf_counter()
    plans = run_clingo([concrete_lp_path], horizon)
    solve_time = time.perf_counter() - solve_start
    total_time = time.perf_counter() - total_start

    logger.info(f"Plans found: {len(plans)}")
    logger.info(f"Total runtime: {total_time:.3f}s")
    logger.info("=" * 70)

    return {
        "horizon": horizon,
        "numPlans": len(plans),
        "plans": plans,
        "success": bool(plans),
        "timings": {
            "iterations": None,
            "fd_conc": downward_time,
            "fd_abs": None,
            "fd_total": downward_time,
            "lp_concrete_time": lp_time,
            "lp_abstract_time": None,
            "lp_total_time": lp_time,
            "abstract_solve_time": None,
            "concrete_solve_time": solve_time,
            "total_time": total_time,
            "run_id": base_dir,
        },
    }
