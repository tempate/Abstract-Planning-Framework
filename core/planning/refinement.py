"""Realize an abstract plan as a concrete plan."""

import logging
from dataclasses import dataclass
from pprint import pformat

from core.abstraction.model import Abstraction
from core.execution import PhaseTiming, timed_phase
from core.integrations.clingo import parse_plan_actions, run_clingo
from core.planning.config import AbstractPlanningConfig
from core.planning.mapping import build_mapping
from core.planning.plan import PlanAction
from core.solvers.decremental import solve_decrementally


@dataclass(frozen=True)
class RefinementContext:
    """Configuration and run state for abstract-plan refinement."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    concrete_asp: str
    abstract_asp: str | None
    abstract_task: dict
    horizon: int
    fd_timings: dict
    concrete_asp_time: float
    abstract_asp_time: float
    asp_total_time: float
    total_timing: PhaseTiming
    run_id: str
    logger: logging.Logger


def refine(context: RefinementContext):
    """Obtain an abstract plan and use it to guide concrete search."""
    abstract_plan, abstract_solve_time = _get_abstract_plan(context)
    if abstract_plan is None:
        return _build_result(
            context,
            success=False,
            plan=None,
            solver_operations=0,
            abstract_solve_time=abstract_solve_time,
            concrete_solve_time=0.0,
        )

    mapping = build_mapping(abstract_plan, context.abstraction)
    success, plan, solver_operations, concrete_solve_time = _solve_concrete(context, mapping)

    if success:
        _log_success(context.logger, plan)
    else:
        context.logger.info("No concrete plan found at the selected horizon.")
        context.logger.info("FAILED")

    return _build_result(
        context,
        success=success,
        plan=plan,
        solver_operations=solver_operations,
        abstract_solve_time=abstract_solve_time,
        concrete_solve_time=concrete_solve_time,
    )


def _get_abstract_plan(context):
    if context.config.plan_source == "clingo":
        return _solve_abstract_plan(context)
    if context.config.plan_source == "fd":
        context.logger.info("Using Fast Downward plan")
        with timed_phase(context.logger, "Abstract plan generation time"):
            abstract_plan = read_fast_downward_plan(context.abstract_task["planFile"])
        return abstract_plan, 0.0
    raise ValueError(f"Unknown abstract plan source: {context.config.plan_source}")


def _solve_abstract_plan(context):
    context.logger.info("Abstract plan search")
    with timed_phase(context.logger, "Abstract solving time") as timing:
        abstract_atoms = run_clingo(context.abstract_asp, context.horizon)

    if abstract_atoms is None:
        context.logger.info("No abstract plan possible.")
        context.logger.info("FAILED")
        return None, timing.elapsed

    context.logger.info("Abstract plan:")
    for atom in abstract_atoms:
        context.logger.info(f"  {atom}")

    with timed_phase(context.logger, "Abstract plan generation time"):
        abstract_plan = parse_plan_actions(abstract_atoms)
    return abstract_plan, timing.elapsed


def read_fast_downward_plan(plan_file_path):
    """Read a Fast Downward plan into chronological plan actions."""
    abstract_plan = []
    with open(plan_file_path, "r") as plan_file:
        time_step = 1
        for line in plan_file:
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            action_name, *arguments = line.strip("()").split()
            abstract_plan.append(PlanAction(action_name, tuple(arguments), time_step))
            time_step += 1

    return tuple(abstract_plan)


def _solve_concrete(context, refinement_asp):
    with timed_phase(context.logger, "Concrete solving time") as timing:
        success, plan, solver_operations = solve_decrementally(
            "\n".join((context.concrete_asp, refinement_asp)), context.horizon
        )
    return success, plan, solver_operations, timing.elapsed


def _build_result(context, *, success, plan, solver_operations, abstract_solve_time, concrete_solve_time):
    total_time = context.total_timing.elapsed
    context.logger.info(f"TOTAL TIME: {total_time:.3f}s")
    return {
        "configuration": context.config.as_dict(),
        "horizon": context.horizon,
        "plan": plan if success else None,
        "success": success,
        "timings": {
            "iterations": 1,
            "decrements": solver_operations,
            "fd_concrete_time": context.fd_timings["fd_concrete_time"],
            "fd_abstract_time": context.fd_timings["fd_abstract_time"],
            "fd_total_time": context.fd_timings["fd_total_time"],
            "asp_concrete_time": context.concrete_asp_time,
            "asp_abstract_time": context.abstract_asp_time,
            "asp_total_time": context.asp_total_time,
            "abstract_solve_time": abstract_solve_time,
            "concrete_solve_time": concrete_solve_time,
            "total_time": total_time,
            "run_id": context.run_id,
        },
    }


def _log_success(logger, plan):
    logger.info("SUCCESS: Concrete plan found.")
    logger.info("Plan:")
    logger.info(pformat(plan))
