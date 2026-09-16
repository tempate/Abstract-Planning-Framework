"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass

from core.abstraction.factory import Abstraction
from core.integrations.clingo import IncrementalSolver, parse_plan_actions, plan_length, solve
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.refinement.budgeted import disabled_switches, solve_within_budget
from core.refinement.mapping import build_mapping, mapped_horizon


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

    return _build_result(context, plan)


def _solve_abstract_plan(context):
    """Search for the shortest abstract plan and read the horizon it maps to."""

    def record_attempt(horizon, solve_calls):
        context.metrics.set_counter("abstract_plan_length", horizon)
        context.metrics.set_counter("abstract_solve_calls", solve_calls)

    with context.metrics.measure("abstract_solving"):
        solve_result = solve(context.abstract_asp, on_attempt=record_attempt)

    # The concrete search runs on the mapped time line, which surrounds every
    # abstract action with a gap for one optional concrete action.
    context.horizon = mapped_horizon(solve_result.horizon)
    context.metrics.set_counter("abstract_plan_length", solve_result.horizon)
    context.metrics.set_counter("abstract_solve_calls", solve_result.attempts)

    return parse_plan_actions(solve_result.plan)


def _solve_concrete_plan(context, asp):
    """Refine the abstract plan, then search above its horizon if it does not refine."""
    # Publish the counters before searching so an interrupted run still has them.
    _publish_counters(context, decrements=0, increments=0, solve_calls=0)

    def record_attempt(decrements, solve_calls):
        _publish_counters(context, decrements=decrements, increments=0, solve_calls=solve_calls)

    with context.metrics.measure("guided_concrete_solving"):
        solver = IncrementalSolver(asp, context.horizon)
        refined, plan, decrements = solve_within_budget(solver, record_attempt)

    _publish_counters(context, decrements=decrements, increments=0, solve_calls=decrements + 1)
    if refined:
        return plan

    with context.metrics.measure("extended_concrete_solving"):
        return _extend_concrete_search(context, solver, decrements)


def _extend_concrete_search(context, solver, decrements):
    """Search above the mapped horizon without abstract-plan constraints."""
    mapped = context.horizon
    guided_solve_calls = decrements + 1

    def record_attempt(horizon, solve_calls):
        context.horizon = horizon
        _publish_counters(
            context, decrements=decrements, increments=horizon - mapped, solve_calls=guided_solve_calls + solve_calls
        )

    # Every switch is off, so no abstract action constrains the search any more.
    # The mapped gaps stay optional, which only admits shorter plans than the
    # plain concrete program, and the budgeted search's grounding is kept.
    solver.extend()
    solve_result = solver.search(disabled_switches(solver), record_attempt)

    context.horizon = solve_result.horizon
    _publish_counters(
        context,
        decrements=decrements,
        increments=context.horizon - mapped,
        solve_calls=guided_solve_calls + solve_result.attempts,
    )
    return solve_result.plan


def _publish_counters(context, *, decrements, increments, solve_calls):
    """Report the concrete search's progress so far."""
    context.metrics.set_counter("decrements", decrements)
    context.metrics.set_counter("increments", increments)
    context.metrics.set_counter("concrete_solve_calls", solve_calls)


def _build_result(context, plan):
    if plan is not None:
        context.metrics.set_counter("plan_length", plan_length(plan))

    return {
        "configuration": context.config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": context.run_id,
    }
