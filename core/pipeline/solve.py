"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.integrations.fast_downward import pddl_to_sas
from core.pipeline.abstraction.abstract_task import build_abstract_task, report_abstraction, write_abstract_problem
from core.integrations.ms_unsat import has_plan
from core.utilities.outcomes import UNKNOWN, UNSOLVABLE, UnsolvableTaskError
from core.planners.powerlifted import Powerlifted
from core.planners.registry import PLANNERS
from core.utilities.config import AbstractPlanningConfig
from core.utilities.execution import planning_run
from core.utilities.plan import one_action_per_step
from core.pipeline.refinement.refine import RefinementContext, refine


def solve(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task, plan it with the config's planner, and refine that plan with ASP."""
    with planning_run("abstract", on_update) as run:
        abstract_task, domain_path, problem_path, renamings = _abstract(config, run.base_dir, run.metrics)

        planner = PLANNERS[config.planner](config)
        abstract_dir = os.path.join(run.base_dir, "abstract")
        actions = _plan_abstract(planner, abstract_dir, domain_path, problem_path, run.metrics)

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
            collapsed_set=abstract_task.collapsed_set,
            metrics=run.metrics,
            base_dir=run.base_dir,
            renamings=renamings,
        )
        plan = refine(context, abstract_plan)

    return run.plan_result(config, plan)


def _abstract(config, base_dir, metrics):
    abstract_task = build_abstract_task(config, metrics)
    report_abstraction(abstract_task, metrics)

    with metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path, renamings = write_abstract_problem(abstract_task.problem, base_dir)

    return abstract_task, domain_path, problem_path, renamings


def _plan_abstract(planner, abstract_dir, domain_path, problem_path, metrics):
    abstract_metrics = metrics.prefixed("abstract_")

    # Powerlifted searches the lifted task, so only the other planners need it grounded.
    if isinstance(planner, Powerlifted):
        return planner.plan_pddl(abstract_dir, domain_path, problem_path, abstract_metrics)

    with metrics.measure("abstract_fd"):
        abstract_sas = pddl_to_sas(abstract_dir, domain_path, problem_path, "abstract")

    return planner.plan_sas(abstract_sas, abstract_metrics)


def check_solvability(config: AbstractPlanningConfig, on_update=None):
    """Search the abstraction with MS-unsat, which can only prove the concrete task unsolvable.

    The abstraction over-approximates: no abstract plan means no concrete plan,
    but an abstract plan may exist only because of the relaxation.
    """
    with planning_run("abstract", on_update) as run:
        try:
            _, domain_path, problem_path, _ = _abstract(config, run.base_dir, run.metrics)

            with run.metrics.measure("abstract_fd_search"):
                found = has_plan(run.base_dir, domain_path, problem_path, "abstract")
        except UnsolvableTaskError:
            # Symmetry discovery reads the concrete task, so proving it
            # unsolvable there is the verdict, not a failure to reach one.
            found = False

    return run.verdict_result(config, UNKNOWN if found else UNSOLVABLE)
