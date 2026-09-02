"""Prepare and dispatch abstraction-based planning workflows."""

import os
from pathlib import Path

from core.execution import get_logger, temp_run_dir, timed_phase
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.unified_planning import write_problem
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.abstraction.factory import build_abstract_problem
from core.planning.config import AbstractPlanningConfig
from core.planning.refinement import RefinementContext, refine


def compute_abstract_plan(config: AbstractPlanningConfig):
    """Abstract one concrete task and dispatch its plan-refinement workflow."""
    with temp_run_dir("abstract") as (base_dir, run_id):
        abstract_problem = build_abstract_problem(config)

        logger = get_logger()
        logger.info("=" * 70)
        logger.info("NEW PLANNING RUN STARTED")
        logger.info(f"Configuration: {config.as_dict()}")
        logger.info(f"Run ID: {run_id}")
        logger.info(f"Base dir: {base_dir}")

        with timed_phase() as run_timing:
            context = RefinementContext(
                config=config,
                abstraction=abstract_problem.abstraction,
                relaxed_deletes=abstract_problem.relaxed_deletes,
                total_timing=run_timing,
                run_id=run_id,
                logger=logger,
            )

            # Translate the problem to SAS
            _to_sas(base_dir, abstract_problem.problem, context)

            # Translate the SAS to ASP
            _to_asp(context)

            return refine(context)


def _to_sas(base_dir, problem, context):
    config = context.config
    logger = context.logger

    with timed_phase(logger, "Fast Downward time") as fd_total:
        # Translate the concrete problem into SAS.
        dir = os.path.join(base_dir, "concrete")
        concrete_task, concrete_time = pddl_to_sas(dir, config.domain_path, config.problem_path, "concrete")

        # Write the temporary problem files
        domain_path, problem_path = _write_abstract_problem(problem, base_dir)

        dir = os.path.join(base_dir, "abstract")
        abstract_task, abstract_time = pddl_to_sas(dir, domain_path, problem_path, "abstract")

    context.concrete_task = concrete_task
    context.abstract_task = abstract_task
    context.fd_timings = {
        "fd_concrete_time": concrete_time,
        "fd_abstract_time": abstract_time,
        "fd_total_time": fd_total.elapsed,
    }


def _to_asp(context):
    config = context.config
    logger = context.logger

    with timed_phase(logger, "Total ASP generation") as asp_total_timing:
        # Generate the ASP representation of the concrete problem.
        with timed_phase(logger, "Concrete ASP generation") as concrete_timing:
            concrete_asp = sas_to_asp(context.concrete_task["sasFile"], abstract_time_steps=config.time_step)

            concrete_asp = add_switch_to_asp_rule(concrete_asp)

        # Generate the ASP representation of the abstract problem.
        with timed_phase(logger, "Abstract ASP generation") as abstract_timing:
            abstract_asp = sas_to_asp(context.abstract_task["sasFile"], abstract_time_steps=config.time_step)

    context.concrete_asp = concrete_asp
    context.abstract_asp = abstract_asp
    context.concrete_asp_time = concrete_timing.elapsed
    context.abstract_asp_time = abstract_timing.elapsed
    context.asp_total_time = asp_total_timing.elapsed


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
