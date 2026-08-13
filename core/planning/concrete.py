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
    logger.info(f"Requested horizon: {horizon if horizon is not None else 'auto'}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)
    with timed_phase() as total_timing:
        # Translate the concrete problem into SAS.
        with timed_phase(logger, "Fast Downward time") as downward_timing:
            with (
                open(domain_path, "rb") as domain,
                open(problem_path, "rb") as problem,
            ):
                task, _ = run_fast_downward(
                    base_dir, domain.read(), problem.read(), "concrete", "plan"
                )

        effective_horizon = task["horizon"] if horizon is None else horizon
        logger.info(f"Effective horizon: {effective_horizon}")

        # Generate the ASP representation of the concrete problem.
        asp_path = os.path.join(base_dir, "output_c.lp")
        with timed_phase(logger, "ASP generation time") as asp_timing:
            plan_to_asp(task["sasFile"], asp_path, encoding, time_step)

        # Solve the concrete problem using Clingo.
        with timed_phase(logger, "Concrete solving time") as solve_timing:
            plan = run_clingo([asp_path], effective_horizon)

    downward_time = downward_timing.elapsed
    asp_time = asp_timing.elapsed
    solve_time = solve_timing.elapsed
    total_time = total_timing.elapsed

    logger.info(f"Plan found: {plan is not None}")
    logger.info(f"Total runtime: {total_time:.3f}s")
    logger.info("=" * 70)

    return {
        "horizon": effective_horizon,
        "plan": plan,
        "success": plan is not None,
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
