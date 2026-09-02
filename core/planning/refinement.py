"""Realize an abstract plan as a concrete plan."""

import logging
from dataclasses import dataclass, field
from pprint import pformat

from core.abstraction.factory import Abstraction
from core.execution import PhaseTiming, timed_phase
from core.integrations.clingo import parse_plan_actions, run_clingo
from core.planning.config import AbstractPlanningConfig
from core.planning.mapping import build_mapping
from core.solvers.decremental import solve_decrementally


@dataclass
class RefinementContext:
    """Configuration and run state for abstract-plan refinement."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    relaxed_deletes: tuple
    total_timing: PhaseTiming
    run_id: str
    logger: logging.Logger
    concrete_task: dict = field(default_factory=dict)
    abstract_task: dict = field(default_factory=dict)
    concrete_asp: str = ""
    abstract_asp: str = ""
    horizon: int = 0
    fd_timings: dict = field(default_factory=dict)
    concrete_asp_time: float = 0.0
    abstract_asp_time: float = 0.0
    asp_total_time: float = 0.0


def refine(context: RefinementContext):
    """Obtain an abstract plan and use it to guide concrete search."""
    abstract_plan, abstract_solve_time = _solve_abstract_plan(context)
    mapping = build_mapping(abstract_plan, context.abstraction)

    with timed_phase(context.logger, "Concrete solving time") as concrete_timing:
        asp = "\n".join((context.concrete_asp, mapping))
        success, plan, solver_operations = solve_decrementally(asp, context.horizon)

    if success:
        context.logger.info("SUCCESS: Concrete plan found.")
        context.logger.info("Plan:")
        context.logger.info(pformat(plan))
    else:
        context.logger.info("No concrete plan found at the selected horizon.")
        context.logger.info("FAILED")

    total_time = context.total_timing.elapsed
    context.logger.info(f"TOTAL TIME: {total_time:.3f}s")

    return {
        "abstraction": {
            "abstract_symbol": context.abstraction.name,
            "objects_to_abstract": list(context.abstraction.objects),
            "object_type": context.abstraction.object_type,
            "relaxed_unary_deletes": len(context.relaxed_deletes),
        },
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
            "concrete_solve_time": concrete_timing.elapsed,
            "total_time": total_time,
            "run_id": context.run_id,
        },
    }


def _solve_abstract_plan(context):
    context.logger.info("Abstract plan search")
    with timed_phase(context.logger, "Abstract solving time") as timing:
        solve_result = run_clingo(context.abstract_asp)

    context.horizon = solve_result.horizon
    context.logger.info(f"Effective horizon: {context.horizon}")
    abstract_atoms = solve_result.plan

    context.logger.info("Abstract plan:")
    for atom in abstract_atoms:
        context.logger.info(f"  {atom}")

    with timed_phase(context.logger, "Abstract plan generation time"):
        abstract_plan = parse_plan_actions(abstract_atoms)
    return abstract_plan, timing.elapsed
