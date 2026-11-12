"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.integrations.fast_downward import pddl_to_sas
from core.integrations.ms_unsat import has_plan
from core.utilities.metrics import PlanningMetrics
from core.pipeline.abstraction.factory import build_abstract_problem, report_abstraction, write_abstract_problem
from core.utilities.outcomes import UNKNOWN, UNSOLVABLE, UnsolvableTaskError
from core.baselines.backends import BACKENDS
from core.utilities.config import AbstractPlanningConfig
from core.utilities.execution import temp_run_dir
from core.pipeline.refinement.pipeline import RefinementContext, refine


def solve(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task, plan it with the config's planner, and refine that plan with ASP."""
    metrics = PlanningMetrics(on_update=on_update)

    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            problem, abstract_sas, renamings = _abstract(config, base_dir, metrics)
            backend = BACKENDS[config.planner]
            abstract_plan, horizon = backend.find_abstract_plan(config, base_dir, abstract_sas, metrics)
            context = RefinementContext(
                config=config,
                abstraction=problem.abstraction,
                metrics=metrics,
                base_dir=base_dir,
                renamings=renamings,
            )
            plan = refine(context, abstract_plan, horizon)

    return {
        "configuration": config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": run_id,
        "metrics": metrics.as_dict(),
    }


def _abstract(config, base_dir, metrics):
    abstract_problem = build_abstract_problem(config, metrics)
    report_abstraction(abstract_problem, metrics)

    with metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path, renamings = write_abstract_problem(abstract_problem.problem, base_dir)

    with metrics.measure("abstract_fd"):
        abstract_dir = os.path.join(base_dir, "abstract")
        abstract_sas = pddl_to_sas(abstract_dir, domain_path, problem_path, "abstract")

    return abstract_problem, abstract_sas, renamings


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
                    domain_path, problem_path, _ = write_abstract_problem(abstract_problem.problem, base_dir)

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
