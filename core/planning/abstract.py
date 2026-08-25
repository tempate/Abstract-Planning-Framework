"""Prepare and dispatch abstraction-based planning workflows."""

import os
from pathlib import Path

from core.execution import get_logger, temp_run_dir, timed_phase
from core.integrations.fast_downward import run_fast_downward
from core.integrations.unified_planning import write_problem
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.abstraction.symmetry import prepare_abstraction
from core.planning.concrete import compute_concrete_plan
from core.planning.config import AbstractPlanningConfig
from core.planning.refinement import RefinementContext, refine


def compute_abstract_plan(config: AbstractPlanningConfig):
    """Abstract one concrete task and dispatch its plan-refinement workflow."""
    with temp_run_dir("abstract") as (base_dir, run_id):
        abstract_problem = prepare_abstraction(
            config.domain_path,
            config.problem_path,
            objects_to_abstract=config.objects_to_abstract,
            abstract_name=config.abstract_name,
            symmetry_time_limit=config.symmetry_time_limit,
        )
        if abstract_problem is not None:
            domain_path, problem_path = _write_abstract_problem(abstract_problem.problem, base_dir)
            abstraction = abstract_problem.abstraction
            result = _compute_abstract_plan(config, abstraction, base_dir, run_id, domain_path, problem_path)
            result["abstraction"] = {
                "abstract_symbol": abstraction.name,
                "objects_to_abstract": list(abstraction.objects),
                "object_type": abstraction.object_type,
                "relaxed_unary_deletes": abstract_problem.unary_delete_score,
            }
        else:
            result = compute_concrete_plan(config)
            result["fallback"] = {"mode": "concrete", "reason": "PDDL Symmetries found no abstractable object classes"}
        return result


def _write_abstract_problem(problem, base_dir):
    """Write the abstract problem to a temporary directory."""
    serialized = write_problem(problem)
    input_directory = Path(base_dir, "generated-abstraction")
    input_directory.mkdir(parents=True, exist_ok=True)
    domain_path = input_directory / "domain.pddl"
    problem_path = input_directory / "problem.pddl"
    domain_path.write_text(serialized.domain, encoding="utf-8")
    problem_path.write_text(serialized.problem, encoding="utf-8")
    return domain_path, problem_path


def _compute_abstract_plan(config, abstraction, base_dir, run_id, abstract_domain_path, abstract_problem_path):
    logger = get_logger()

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Configuration: {config.as_dict()}")
    logger.info(f"Requested horizon: {config.horizon if config.horizon is not None else 'auto'}")
    logger.info(f"Encoding: {config.encoding}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    with timed_phase() as run_timing:
        with timed_phase(logger, "Fast Downward time") as fd_total:
            # Translate the concrete problem into SAS.
            concrete_task, concrete_time = run_fast_downward(
                os.path.join(base_dir, "concrete"), config.domain_path, config.problem_path, "concrete", "translate"
            )

            # A Fast Downward plan is needed only when it is the selected plan
            # source or when its length is being used as an automatic horizon.
            fd_task = "plan" if config.plan_source == "fd" or config.horizon is None else "translate"

            abstract_task, abstract_time = run_fast_downward(
                os.path.join(base_dir, "abstract"), abstract_domain_path, abstract_problem_path, "abstract", fd_task
            )

        fd_timings = {
            "fd_concrete_time": concrete_time,
            "fd_abstract_time": abstract_time,
            "fd_total_time": fd_total.elapsed,
        }

        horizon = _select_abstract_horizon(config.horizon, abstract_task.get("horizon", 0), config.plan_source)
        logger.info(f"Effective horizon: {horizon}")

        with timed_phase(logger, "Total ASP generation") as asp_total_timing:

            # Generate the ASP representation of the concrete problem.
            with timed_phase(logger, "Concrete ASP generation") as concrete_timing:
                concrete_asp = sas_to_asp(concrete_task["sasFile"], config.encoding, config.time_step)

                concrete_asp = add_switch_to_asp_rule(concrete_asp, config.encoding)
            # Generate the ASP representation of the abstract problem.
            abstract_time = 0.0
            abstract_asp = None
            if config.plan_source == "clingo":
                with timed_phase(logger, "Abstract ASP generation") as abstract_timing:
                    abstract_asp = sas_to_asp(abstract_task["sasFile"], config.encoding, config.time_step)
                abstract_time = abstract_timing.elapsed

        context = RefinementContext(
            config=config,
            abstraction=abstraction,
            concrete_asp=concrete_asp,
            abstract_asp=abstract_asp,
            abstract_task=abstract_task,
            horizon=horizon,
            fd_timings=fd_timings,
            concrete_asp_time=concrete_timing.elapsed,
            abstract_asp_time=abstract_time,
            asp_total_time=asp_total_timing.elapsed,
            total_timing=run_timing,
            run_id=run_id,
            logger=logger,
        )
        return refine(context)


def _select_abstract_horizon(requested_horizon, plan_horizon, plan_source):
    """Select a horizon that can contain a Fast Downward-sourced plan."""
    if requested_horizon is None:
        return plan_horizon
    if plan_source == "fd" and requested_horizon < plan_horizon:
        raise ValueError(f"Fast Downward plan length {plan_horizon} exceeds the explicit horizon {requested_horizon}")
    return requested_horizon
