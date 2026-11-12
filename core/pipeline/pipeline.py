"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.integrations.fast_downward import pddl_to_sas
from core.integrations.ms_unsat import has_plan
from core.pipeline.abstraction.factory import build_abstract_problem, report_abstraction, write_abstract_problem
from core.utilities.outcomes import UNKNOWN, UNSOLVABLE, UnsolvableTaskError
from core.planners.registry import PLANNERS
from core.utilities.config import AbstractPlanningConfig
from core.utilities.execution import planning_run
from core.utilities.plan import one_action_per_step
from core.pipeline.refinement.pipeline import RefinementContext, refine


def solve(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task, plan it with the config's planner, and refine that plan with ASP."""
    with planning_run("abstract", on_update) as run:
        problem, abstract_sas, renamings = _abstract(config, run.base_dir, run.metrics)
        actions = PLANNERS[config.planner].plan_sas(config, run.base_dir, abstract_sas, run.metrics)
        # The abstraction over-approximates, so an abstract task without a plan
        # proves the concrete one has none either.
        if actions is None:
            raise UnsolvableTaskError("The abstract task has no plan")
        # A doubling horizon leaves empty steps, while the refinement maps one
        # abstract action onto each step from 1.
        abstract_plan = one_action_per_step(actions)
        run.metrics.set_counter("abstract_plan_length", len(abstract_plan))
        context = RefinementContext(
            config=config,
            abstraction=problem.abstraction,
            metrics=run.metrics,
            base_dir=run.base_dir,
            renamings=renamings,
        )
        plan = refine(context, abstract_plan, len(abstract_plan))

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
