"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass

from core.abstraction.factory import Abstraction
from core.integrations.clingo import parse_plan_actions, plan_length
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.refinement.mapping import build_mapping, mapped_horizon
from core.refinement.switches import collect_switches
from core.search.relaxing import RelaxingSolver
from core.search.incremental import IncrementalSolver


@dataclass
class RefinementContext:
    """Configuration and run state for abstract-plan refinement."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    run_id: str
    metrics: PlanningMetrics
    concrete_asp: str
    abstract_asp: str
    horizon: int = 0


def refine(context: RefinementContext):
    """Obtain an abstract plan and use it to guide concrete search."""
    # Find an abstract plan
    abstract_plan = _solve_abstract_plan(context)

    # Build the ASP to map abstract to concrete actions
    mapping = build_mapping(abstract_plan, context.abstraction)

    # Solve the ASP
    asp = "\n".join((context.concrete_asp, mapping))
    plan = _solve_concrete_plan(context, asp)

    if plan is not None:
        context.metrics.set_counter("plan_length", plan_length(plan))

    return {
        "configuration": context.config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": context.run_id,
    }


def _solve_abstract_plan(context):
    """Search for the shortest abstract plan and read the horizon it maps to."""

    def record_attempt(horizon, solve_calls):
        context.metrics.set_counters({"abstract_plan_length": horizon, "abstract_solve_calls": solve_calls})

    with context.metrics.measure("abstract_solving"):
        solver = IncrementalSolver(context.abstract_asp)
        solve_result = solver.search(on_attempt=record_attempt)

    # The concrete search runs on the mapped time line, which surrounds every
    # abstract action with a gap for one optional concrete action.
    context.horizon = mapped_horizon(solve_result.horizon)
    context.metrics.set_counters(
        {"abstract_plan_length": solve_result.horizon, "abstract_solve_calls": solve_result.attempts}
    )

    return parse_plan_actions(solve_result.plan)


def _solve_concrete_plan(context, asp):
    """Refine the abstract plan, then search above its horizon if it does not refine."""
    mapped = context.horizon

    # Publish the counters before searching so an interrupted run still has them.
    _publish_counters(context, decrements=0, increments=0, solve_calls=0)

    def record_attempt(horizon, dropped, solve_calls):
        context.horizon = horizon
        _publish_counters(context, decrements=dropped, increments=horizon - mapped, solve_calls=solve_calls)

    with context.metrics.measure("guided_concrete_solving"):
        solver = RelaxingSolver(asp, mapped)
        # Give up the abstract plan from its end, so what survives is a prefix of it.
        result = solver.search(list(reversed(collect_switches(solver))), record_attempt)

    context.horizon = result.horizon
    _publish_counters(
        context, decrements=result.dropped, increments=result.horizon - mapped, solve_calls=result.attempts
    )
    return result.plan


def _publish_counters(context, *, decrements, increments, solve_calls):
    """Report the concrete search's progress so far."""
    context.metrics.set_counters(
        {"decrements": decrements, "increments": increments, "concrete_solve_calls": solve_calls}
    )
