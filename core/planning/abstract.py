"""Prepare and dispatch abstraction-based planning workflows."""

import os
from pathlib import Path

from core.integrations.fast_downward import pddl_to_sas, sas_size
from core.integrations.unified_planning import without_action_costs, write_problem
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.metrics import PlanningMetrics
from core.abstraction.factory import build_abstract_problem
from core.planning.config import AbstractPlanningConfig
from core.planning.execution import temp_run_dir
from core.refinement.pipeline import RefinementContext, refine


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
    report_abstraction(abstract_problem, metrics)

    concrete_sas, abstract_sas = _to_sas(base_dir, abstract_problem.problem, config, metrics)
    concrete_asp, abstract_asp = _to_asp(concrete_sas, abstract_sas, config, metrics)

    context = RefinementContext(
        config=config,
        abstraction=abstract_problem.abstraction,
        run_id=run_id,
        metrics=metrics,
        concrete_asp=concrete_asp,
        abstract_asp=abstract_asp,
    )
    return refine(context)


def _to_sas(base_dir, problem, config, metrics):
    """Translate the concrete and abstract tasks and return their SAS files."""
    with metrics.measure("concrete_fd"):
        concrete_dir = os.path.join(base_dir, "concrete")
        concrete_sas = pddl_to_sas(concrete_dir, config.domain_path, config.problem_path, "concrete")
    _report_sas_size("concrete", concrete_sas, metrics)

    # Write the temporary problem files
    with metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path = write_abstract_problem(problem, base_dir)

    with metrics.measure("abstract_fd"):
        abstract_dir = os.path.join(base_dir, "abstract")
        abstract_sas = pddl_to_sas(abstract_dir, domain_path, problem_path, "abstract")
    _report_sas_size("abstract", abstract_sas, metrics)

    return concrete_sas, abstract_sas


def _report_sas_size(label, sas_path, metrics):
    """Record how big a task the translator produced, which is what the collapse shrinks.

    A file cut short declares neither count, and a size nobody read is better
    left out of the results than written down as a zero.
    """
    for name, value in zip(("variables", "operators"), sas_size(sas_path)):
        if value is not None:
            metrics.set_counter(f"{label}_sas_{name}", value)


def _to_asp(concrete_sas, abstract_sas, config, metrics):
    """Translate both SAS files into their ASP programs."""
    with metrics.measure("concrete_asp"):
        concrete_asp = sas_to_asp(concrete_sas)
        concrete_asp = add_switch_to_asp_rule(concrete_asp)

    with metrics.measure("abstract_asp"):
        abstract_asp = sas_to_asp(abstract_sas)

    return concrete_asp, abstract_asp


def report_abstraction(abstract_problem, metrics):
    """Record the collapsed class and what relaxing it cost.

    Reported before solving, so a run that fails later still carries it: the
    metrics snapshot reaches the result file on every update, which is what
    survives a run killed at the benchmark timeout.
    """
    abstraction = abstract_problem.abstraction
    metrics.set_abstraction(abstraction.objects, abstraction.object_type)
    metrics.set_counter("relaxed_deletes", len(abstract_problem.relaxed_deletes))
    metrics.set_counter("relaxed_inequalities", len(abstract_problem.relaxed_inequalities))
    for name, value in abstract_problem.statistics["counters"].items():
        metrics.set_counter(name, value)
    for name, value in abstract_problem.statistics["ratios"].items():
        metrics.set_ratio(name, value)
    print(f"Collapsed {sorted(abstraction.objects)} into {abstraction.name} (type={abstraction.object_type})")


def write_abstract_problem(problem, base_dir):
    """Write the abstract problem to a temporary directory."""

    # Create the temporary directory.
    input_directory = Path(base_dir, "generated-abstraction")
    input_directory.mkdir(parents=True, exist_ok=True)

    # Write the abstract domain and problem files.
    serialized = write_problem(without_action_costs(problem))

    domain_path = input_directory / "domain.pddl"
    domain_path.write_text(serialized.domain, encoding="utf-8")

    problem_path = input_directory / "problem.pddl"
    problem_path.write_text(serialized.problem, encoding="utf-8")

    return domain_path, problem_path
