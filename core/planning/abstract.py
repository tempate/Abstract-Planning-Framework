"""Prepare and dispatch abstraction-based planning workflows."""

import os
from pathlib import Path

from core.execution import get_logger, temp_run_dir
from core.integrations.fast_downward import run_fast_downward
from core.integrations.unified_planning import write_problem
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.metrics import PlanningMetrics
from core.abstraction.factory import build_abstract_problem
from core.planning.config import AbstractPlanningConfig
from core.planning.refinement import RefinementContext, refine


def compute_abstract_plan(config: AbstractPlanningConfig):
    """Abstract one concrete task and dispatch its plan-refinement workflow."""
    metrics = PlanningMetrics()
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            result = _compute_abstract_plan(config, base_dir, run_id, metrics)
    result["metrics"] = metrics.as_dict()
    return result


def _compute_abstract_plan(config, base_dir, run_id, metrics):
    abstract_problem = build_abstract_problem(config, metrics)

    logger = get_logger()
    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Configuration: {config.as_dict()}")
    logger.info(f"Requested horizon: {config.horizon if config.horizon is not None else 'auto'}")
    logger.info(f"Encoding: {config.encoding}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    context = RefinementContext(
        config=config,
        abstraction=abstract_problem.abstraction,
        relaxed_deletes=abstract_problem.relaxed_deletes,
        run_id=run_id,
        logger=logger,
        metrics=metrics,
    )

    # Translate the problem to SAS
    _to_sas(base_dir, abstract_problem.problem, context)

    fd_horizon = context.abstract_task.get("horizon", 0)
    context.horizon = _select_abstract_horizon(config.horizon, fd_horizon, config.plan_source)
    metrics.set_counter("abstract_horizon", context.horizon)
    logger.info(f"Effective horizon: {context.horizon}")

    # Translate the SAS to ASP
    _to_asp(context)

    return refine(context)


def _to_sas(base_dir, problem, context):
    config = context.config

    # Translate the concrete problem into SAS.
    dir = os.path.join(base_dir, "concrete")
    with context.metrics.measure("concrete_fd"):
        concrete_task = run_fast_downward(dir, config.domain_path, config.problem_path, "concrete", "translate")

    # A Fast Downward plan is needed only when it is the selected plan
    # source or when its length is being used as an automatic horizon.
    fd_task = "plan" if config.plan_source == "fd" or config.horizon is None else "translate"

    # Write the temporary problem files
    with context.metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path = _write_abstract_problem(problem, base_dir)

    dir = os.path.join(base_dir, "abstract")
    with context.metrics.measure("abstract_fd"):
        abstract_task = run_fast_downward(dir, domain_path, problem_path, "abstract", fd_task)

    context.concrete_task = concrete_task
    context.abstract_task = abstract_task


def _to_asp(context):
    config = context.config

    # Generate the ASP representation of the concrete problem.
    with context.metrics.measure("concrete_asp"):
        concrete_asp = sas_to_asp(context.concrete_task["sasFile"], config.encoding, config.time_step)
        concrete_asp = add_switch_to_asp_rule(concrete_asp, config.encoding)

    # Generate the ASP representation of the abstract problem.
    abstract_asp = None
    if config.plan_source == "clingo":
        with context.metrics.measure("abstract_asp"):
            abstract_asp = sas_to_asp(context.abstract_task["sasFile"], config.encoding, config.time_step)

    context.concrete_asp = concrete_asp
    context.abstract_asp = abstract_asp


def _select_abstract_horizon(requested_horizon, plan_horizon, plan_source):
    """Select a horizon that can contain a Fast Downward-sourced plan."""
    if requested_horizon is None:
        return plan_horizon
    if plan_source == "fd" and requested_horizon < plan_horizon:
        raise ValueError(f"Fast Downward plan length {plan_horizon} exceeds the explicit horizon {requested_horizon}")
    return requested_horizon


def _write_abstract_problem(problem, base_dir):
    """Write the abstract problem to a temporary directory."""

    # Create the temporary directory.
    input_directory = Path(base_dir, "generated-abstraction")
    input_directory.mkdir(parents=True, exist_ok=True)

    # Write the abstract domain and problem files.
    serialized = write_problem(problem)

    domain_path = input_directory / "domain.pddl"
    domain_path.write_text(serialized.domain, encoding="utf-8")

    problem_path = input_directory / "problem.pddl"
    problem_path.write_text(serialized.problem, encoding="utf-8")

    return domain_path, problem_path
