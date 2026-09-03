"""Orchestrate concrete planning from PDDL translation through ASP solving."""

from core.execution import get_logger, temp_run_dir
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import sas_to_asp
from core.planning.config import PlanningConfig


def compute_concrete_plan(config: PlanningConfig):
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

    # Translate the concrete problem into SAS. With no requested horizon,
    # Fast Downward also finds a plan whose length supplies the horizon.
    fd_task = "plan" if config.horizon is None else "translate"
    task = run_fast_downward(base_dir, config.domain_path, config.problem_path, "concrete", fd_task)

    effective_horizon = task["horizon"] if config.horizon is None else config.horizon
    logger.info(f"Effective horizon: {effective_horizon}")

    # Generate the ASP representation of the concrete problem.
    asp = sas_to_asp(task["sasFile"], config.encoding, config.time_step)

    # Solve the concrete problem using Clingo.
    plan = run_clingo(asp, effective_horizon)

    logger.info(f"Plan found: {plan is not None}")
    logger.info("=" * 70)

    return {
        "configuration": config.as_dict(),
        "horizon": effective_horizon,
        "plan": plan,
        "success": plan is not None,
        "run_id": run_id,
        "iterations": None,
        "decrements": None,
        "increments": None,
    }
