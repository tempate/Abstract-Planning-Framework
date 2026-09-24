"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.integrations.clingo import parse_plan_actions
from core.integrations.fast_downward import has_plan, pddl_to_sas, sas_size
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.metrics import PlanningMetrics
from core.abstraction.factory import build_abstract_problem, report_abstraction, write_abstract_problem
from core.outcomes import UNKNOWN, UNSOLVABLE, UnsolvableTaskError
from core.planning.config import AbstractPlanningConfig
from core.planning.execution import temp_run_dir
from core.planning.validation import validated
from core.refinement.pipeline import RefinementContext, refine


def solve(config: AbstractPlanningConfig, find_abstract_plan, on_update=None):
    """Abstract one concrete task, plan it with ``find_abstract_plan``, and refine that plan with ASP."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            result = _abstract_and_refine(config, find_abstract_plan, base_dir, run_id, metrics)
    # Outside the measured phases, so that checking a plan cannot move a timing.
    result["plan_valid"] = validated(config, result.get("plan"), parse_plan_actions)
    result["metrics"] = metrics.as_dict()
    return result


def _abstract_and_refine(config, find_abstract_plan, base_dir, run_id, metrics):
    abstract_problem = build_abstract_problem(config, metrics)
    report_abstraction(abstract_problem, metrics)

    concrete_sas, abstract_sas = _to_sas(base_dir, abstract_problem.problem, config, metrics)
    concrete_asp = _to_asp(concrete_sas, metrics)
    abstract_plan, abstract_horizon = find_abstract_plan(base_dir, abstract_sas, metrics)

    context = RefinementContext(
        config=config,
        abstraction=abstract_problem.abstraction,
        run_id=run_id,
        metrics=metrics,
        concrete_asp=concrete_asp,
    )
    return refine(context, abstract_plan, abstract_horizon)


def _to_sas(base_dir, problem, config, metrics):
    """Translate the concrete and abstract tasks and return their SAS files."""
    with metrics.measure("concrete_fd"):
        concrete_dir = os.path.join(base_dir, "concrete")
        concrete_sas = pddl_to_sas(concrete_dir, config.domain_path, config.problem_path, "concrete")
    _report_sas_size("concrete", concrete_sas, metrics)

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
    sizes = dict(zip(("variables", "operators"), sas_size(sas_path)))
    metrics.set_counters({f"{label}_sas_{name}": value for name, value in sizes.items() if value is not None})


def _to_asp(concrete_sas, metrics):
    """Translate the concrete SAS file into the ASP program the refinement searches."""
    with metrics.measure("concrete_asp"):
        concrete_asp = sas_to_asp(concrete_sas)
        return add_switch_to_asp_rule(concrete_asp)


def check_solvability(config: AbstractPlanningConfig, on_update=None):
    """Search the abstraction, which can only settle the task one way.

    The abstraction drops deletes and relaxes inequalities, so it
    over-approximates: no abstract plan means no concrete plan, but an abstract
    plan may exist only because of the relaxation.
    """
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            try:
                abstract_problem = build_abstract_problem(config, metrics)
                report_abstraction(abstract_problem, metrics)

                with metrics.measure("abstract_pddl_writing"):
                    domain_path, problem_path = write_abstract_problem(abstract_problem.problem, base_dir)

                with metrics.measure("abstract_fd_search"):
                    found = has_plan(base_dir, domain_path, problem_path, "abstract")
            except UnsolvableTaskError:
                # Symmetry discovery reads the concrete task, so proving it
                # unsolvable there is the verdict, not a failure to reach one.
                found = False

    return {
        "configuration": config.as_dict(),
        "verdict": UNKNOWN if found else UNSOLVABLE,
        "run_id": run_id,
        "metrics": metrics.as_dict(),
    }
