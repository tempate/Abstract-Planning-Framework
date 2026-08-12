"""Orchestrate concrete planning from PDDL translation through ASP solving."""

import os

from core.execution import create_run_dir, setup_debug_logger, timed_phase
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import plan_to_asp


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
    with timed_phase() as total_timing:
        with timed_phase(logger, "Fast Downward time") as downward_timing:
            with (
                open(domain_path, "rb") as domain_file,
                open(problem_path, "rb") as problem_file,
            ):
                concrete_task, _ = run_fast_downward(
                    base_dir, domain_file, problem_file, "concrete", "plan"
                )

        if horizon is None:
            horizon = concrete_task["horizon"]

        concrete_asp_path = os.path.join(base_dir, "output_c.lp")
        with timed_phase(logger, "ASP generation time") as asp_timing:
            plan_to_asp(
                concrete_task["sasFile"], concrete_asp_path, encoding, time_step
            )

        with timed_phase(logger, "Concrete solving time") as solve_timing:
            plans = run_clingo([concrete_asp_path], horizon)

    downward_time = downward_timing.elapsed
    asp_time = asp_timing.elapsed
    solve_time = solve_timing.elapsed
    total_time = total_timing.elapsed

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
            "asp_concrete_time": asp_time,
            "asp_abstract_time": None,
            "asp_total_time": asp_time,
            "abstract_solve_time": None,
            "concrete_solve_time": solve_time,
            "total_time": total_time,
            "run_id": base_dir,
        },
    }
