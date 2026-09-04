"""Prepare and dispatch abstraction-based planning workflows."""

import os
from pathlib import Path

from core.execution import temp_run_dir
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.unified_planning import write_problem
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.metrics import PlanningMetrics
from core.abstraction.factory import build_abstract_problem
from core.planning.config import AbstractPlanningConfig
from core.planning.refinement import RefinementContext, refine


def compute_abstract_plan(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task and dispatch its plan-refinement workflow."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            result = _compute_abstract_plan(config, base_dir, run_id, metrics)
    result["metrics"] = metrics.as_dict()
    return result


def _compute_abstract_plan(config, base_dir, run_id, metrics):
    abstract_problem = build_abstract_problem(config, metrics)

    # Report the abstraction before solving so runs that fail later still record it.
    abstraction = abstract_problem.abstraction
    print(f"Collapsed {sorted(abstraction.objects)} into {abstraction.name} (type={abstraction.object_type})")

    context = RefinementContext(
        config=config,
        abstraction=abstract_problem.abstraction,
        relaxed_deletes=abstract_problem.relaxed_deletes,
        run_id=run_id,
        metrics=metrics,
    )

    # Translate the problem to SAS
    _to_sas(base_dir, abstract_problem.problem, context)

    # Translate the SAS to ASP
    _to_asp(context)

    return refine(context)


def _to_sas(base_dir, problem, context):
    config = context.config

    # Translate the concrete problem into SAS.
    dir = os.path.join(base_dir, "concrete")
    with context.metrics.measure("concrete_fd"):
        concrete_task = pddl_to_sas(dir, config.domain_path, config.problem_path, "concrete")

    # Write the temporary problem files
    with context.metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path = _write_abstract_problem(problem, base_dir)

    dir = os.path.join(base_dir, "abstract")
    with context.metrics.measure("abstract_fd"):
        abstract_task = pddl_to_sas(dir, domain_path, problem_path, "abstract")

    context.concrete_task = concrete_task
    context.abstract_task = abstract_task


def _to_asp(context):
    config = context.config

    # Generate the ASP representation of the concrete problem.
    with context.metrics.measure("concrete_asp"):
        concrete_asp = sas_to_asp(context.concrete_task["sasFile"], abstract_time_steps=config.time_step)
        concrete_asp = add_switch_to_asp_rule(concrete_asp)

    # Generate the ASP representation of the abstract problem.
    with context.metrics.measure("abstract_asp"):
        abstract_asp = sas_to_asp(context.abstract_task["sasFile"], abstract_time_steps=config.time_step)

    context.concrete_asp = concrete_asp
    context.abstract_asp = abstract_asp


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
