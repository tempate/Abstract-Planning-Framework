"""Prepare and dispatch abstraction-based planning workflows."""

import os
from dataclasses import replace

from core.integrations.fast_downward import pddl_to_sas
from core.integrations.ms_unsat import has_plan
from core.metrics import PlanningMetrics
from core.abstraction.factory import build_abstract_problem, report_abstraction, write_abstract_problem
from core.outcomes import SOLVABLE, UNSOLVABLE, UnsolvableTaskError
from core.planning.backends import BACKENDS
from core.planning.config import AbstractPlanningConfig
from core.planning.execution import temp_run_dir
from core.refinement.pipeline import RefinementContext, refine


def solve(config: AbstractPlanningConfig, on_update=None):
    """Abstract one concrete task, plan it with the config's planner, and refine that plan with ASP."""
    metrics = PlanningMetrics(on_update=on_update)

    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            # Create the abstraction
            problem, abstract_sas, renamings = _abstract(config, base_dir, metrics)

            # Find a plan for the abstraction
            plan, horizon = BACKENDS[config.planner].find_abstract_plan(config, base_dir, abstract_sas, metrics)

            # Refine the plan
            context = RefinementContext(
                config=config,
                abstraction=problem.abstraction,
                run_id=run_id,
                metrics=metrics,
                base_dir=base_dir,
                renamings=renamings,
            )
            result = refine(context, plan, horizon)

    result["metrics"] = metrics.as_dict()
    return result


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
    """Search ever finer abstractions, then the task itself, until one settles it.

    The abstraction drops deletes and relaxes inequalities, so it
    over-approximates: no abstract plan means no concrete plan, but an abstract
    plan may exist only because of the relaxation.
    """
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            try:
                abstract_problem = build_abstract_problem(config, metrics)
                found = _has_abstract_plan(abstract_problem, base_dir, metrics)

                # An abstract plan may exist only because of the collapse, so
                # collapse one object fewer and search again, down to a pair.
                # The objects are symmetric, so which one stays out does not matter.
                objects = abstract_problem.abstraction.objects
                while found and len(objects) > 2:
                    objects = objects[:-1]
                    abstract_problem = build_abstract_problem(replace(config, objects_to_abstract=objects), metrics)
                    found = _has_abstract_plan(abstract_problem, base_dir, metrics)

                # Below a pair nothing is collapsed, so the last step searches
                # the task itself, which settles it either way.
                if found:
                    with metrics.measure("fd_search"):
                        found = has_plan(base_dir, config.domain_path, config.problem_path, "concrete")
            except UnsolvableTaskError:
                # Symmetry discovery reads the concrete task, so proving it
                # unsolvable there is the verdict, not a failure to reach one.
                found = False

    return {
        "configuration": config.as_dict(),
        "verdict": SOLVABLE if found else UNSOLVABLE,
        "run_id": run_id,
        "metrics": metrics.as_dict(),
    }


def _has_abstract_plan(abstract_problem, base_dir, metrics):
    report_abstraction(abstract_problem, metrics)

    with metrics.measure("abstract_pddl_writing"):
        domain_path, problem_path, _ = write_abstract_problem(abstract_problem.problem, base_dir)

    with metrics.measure("abstract_fd_search"):
        return has_plan(base_dir, domain_path, problem_path, "abstract")
