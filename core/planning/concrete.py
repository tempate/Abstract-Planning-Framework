"""Orchestrate concrete planning from PDDL translation through ASP solving."""

from core.execution import get_logger, temp_run_dir, timed_phase
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import sas_to_asp
from core.planning.config import ConcretePlanningConfig


def compute_concrete_plan(config: ConcretePlanningConfig):
    """Translate and solve one concrete PDDL planning problem."""
    with temp_run_dir() as (base_dir, run_id):
        return _compute_concrete_plan(config, base_dir, run_id)


def _compute_concrete_plan(config, base_dir, run_id):
    logger = get_logger()

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Configuration: {config.as_dict()}")
    logger.info(f"Requested horizon: {config.horizon if config.horizon is not None else 'auto'}")
    logger.info(f"Encoding: {config.encoding}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    with timed_phase() as total_timing:
        # Translate the concrete problem into SAS. With no requested horizon,
        # Fast Downward also finds a plan whose length supplies the horizon.
        fd_task = "plan" if config.horizon is None else "translate"

        with timed_phase(logger, "Fast Downward time") as downward_timing:
            task, _ = run_fast_downward(base_dir, config.domain_path, config.problem_path, "concrete", fd_task)

        effective_horizon = task["horizon"] if config.horizon is None else config.horizon
        logger.info(f"Effective horizon: {effective_horizon}")

        # Generate the ASP representation of the concrete problem.
        with timed_phase(logger, "ASP generation time") as asp_timing:
            asp = sas_to_asp(task["sasFile"], config.encoding, config.time_step)

        # Solve the concrete problem using Clingo.
        with timed_phase(logger, "Concrete solving time") as solve_timing:
            plan = run_clingo(asp, effective_horizon)

    downward_time = downward_timing.elapsed
    asp_time = asp_timing.elapsed
    solve_time = solve_timing.elapsed
    total_time = total_timing.elapsed

    logger.info(f"Plan found: {plan is not None}")
    logger.info(f"Total runtime: {total_time:.3f}s")
    logger.info("=" * 70)

    return {
        "configuration": config.as_dict(),
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
            "run_id": run_id,
        },
    }
