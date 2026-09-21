"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.integrations.clingo import parse_plan_actions
from core.integrations.fast_downward import has_plan, pddl_to_sas
from core.integrations.plasp import add_switch_to_asp_rule, sas_to_asp
from core.metrics import PlanningMetrics
from core.abstraction.factory import build_abstract_problem, report_abstraction, write_abstract_problem
from core.outcomes import UNKNOWN, UNSOLVABLE, UnsolvableTaskError
from core.planning.config import AbstractPlanningConfig
from core.planning.execution import temp_run_dir
from core.planning.validation import validated
from core.refinement.pipeline import RefinementContext, refine


def solve_via_abstraction(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task and dispatch its plan-refinement workflow."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            result = _abstract_and_refine(config, base_dir, run_id, metrics)
    # Outside the measured phases, so that checking a plan cannot move a timing.
    result["plan_valid"] = validated(config, result.get("plan"), parse_plan_actions)
    result["metrics"] = metrics.as_dict()
    return result


def _abstract_and_refine(config, base_dir, run_id, metrics):
    abstract_problem = build_abstract_problem(config, metrics)
    report_abstraction(abstract_problem, metrics)

    concrete_sas, abstract_sas = _to_sas(base_dir, abstract_problem.problem, config, metrics)
    concrete_asp, abstract_asp = _to_asp(concrete_sas, abstract_sas, metrics)

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

    with metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path = write_abstract_problem(problem, base_dir)

    with metrics.measure("abstract_fd"):
        abstract_dir = os.path.join(base_dir, "abstract")
        abstract_sas = pddl_to_sas(abstract_dir, domain_path, problem_path, "abstract")

    return concrete_sas, abstract_sas


def _to_asp(concrete_sas, abstract_sas, metrics):
    """Translate both SAS files into their ASP programs."""
    with metrics.measure("concrete_asp"):
        concrete_asp = sas_to_asp(concrete_sas)
        concrete_asp = add_switch_to_asp_rule(concrete_asp)

    with metrics.measure("abstract_asp"):
        abstract_asp = sas_to_asp(abstract_sas)

    return concrete_asp, abstract_asp


def check_solvability_via_abstraction(config: AbstractPlanningConfig, on_update=None):
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

                with metrics.measure("abstract_fd"):
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
