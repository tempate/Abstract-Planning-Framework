"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.integrations.fast_downward import pddl_to_sas
from core.integrations.ms_unsat import has_plan
from core.pipeline.abstraction.factory import build_abstract_problem, report_abstraction, write_abstract_problem
from core.utilities.outcomes import UNKNOWN, UNSOLVABLE, UnsolvableTaskError
from core.planners.registry import PLANNERS
from core.utilities.config import AbstractPlanningConfig
from core.utilities.execution import planning_run
from core.pipeline.refinement.pipeline import RefinementContext, refine


def solve(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task, plan it with the config's planner, and refine that plan with ASP."""
    with planning_run("abstract", on_update) as run:
        problem, abstract_sas, renamings = _abstract(config, run.base_dir, run.metrics)
        planner = PLANNERS[config.planner]
        abstract_plan, horizon = planner.find_abstract_plan(config, run.base_dir, abstract_sas, run.metrics)
        context = RefinementContext(
            config=config,
            abstraction=problem.abstraction,
            metrics=run.metrics,
            base_dir=run.base_dir,
            renamings=renamings,
        )
        plan = refine(context, abstract_plan, horizon)

    return run.plan_result(config, plan)


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
    with planning_run("abstract", on_update) as run:
        try:
            abstract_problem = build_abstract_problem(config, run.metrics)
            report_abstraction(abstract_problem, run.metrics)

            with run.metrics.measure("abstract_pddl_writing"):
                domain_path, problem_path, _ = write_abstract_problem(abstract_problem.problem, run.base_dir)

            with run.metrics.measure("abstract_fd_search"):
                found = has_plan(run.base_dir, domain_path, problem_path, "abstract")
        except UnsolvableTaskError:
            # Symmetry discovery reads the concrete task, so proving it
            # unsolvable there is the verdict, not a failure to reach one.
            found = False

    return run.verdict_result(config, UNKNOWN if found else UNSOLVABLE)
