"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass, field

from core.abstraction.factory import Abstraction
from core.integrations.clingo import IncrementalSolver, parse_plan_actions, solve
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.planning.mapping import build_mapping
from core.solvers.decremental import disabled_switches, solve_decrementally


@dataclass
class RefinementContext:
    """Configuration and run state for abstract-plan refinement."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    relaxed_deletes: tuple
    run_id: str
    metrics: PlanningMetrics
    concrete_task: dict = field(default_factory=dict)
    abstract_task: dict = field(default_factory=dict)
    concrete_asp: str = ""
    abstract_asp: str = ""
    horizon: int = 0


def refine(context: RefinementContext):
    """Obtain an abstract plan and use it to guide concrete search."""
    abstract_plan = _solve_abstract_plan(context)
    mapping = build_mapping(abstract_plan, context.abstraction)

    asp = "\n".join((context.concrete_asp, mapping))
    context.metrics.set_counter("decrements", 0)
    context.metrics.set_counter("increments", 0)
    context.metrics.set_counter("final_horizon", context.horizon)
    context.metrics.set_counter("concrete_solve_calls", 0)

    def record_attempt(decrements, solve_calls):
        context.metrics.set_counter("decrements", decrements)
        context.metrics.set_counter("concrete_solve_calls", solve_calls)

    with context.metrics.measure("guided_concrete_solving"):
        solver = IncrementalSolver(asp, context.horizon)
        success, plan, decrements = solve_decrementally(solver, record_attempt)

    guided_solve_calls = decrements + 1
    context.metrics.set_counter("decrements", decrements)
    context.metrics.set_counter("concrete_solve_calls", guided_solve_calls)

    increments = 0
    if not success:
        with context.metrics.measure("extended_concrete_solving"):
            plan, increments = _extend_concrete_search(context, solver, guided_solve_calls)
        success = True

    context.metrics.set_counter("increments", increments)
    context.metrics.set_counter("final_horizon", context.horizon)

    return _build_result(context, success=success, plan=plan)


def _solve_abstract_plan(context):
    """Search for the shortest abstract plan and read its horizon."""

    def record_attempt(horizon, solve_calls):
        context.metrics.set_counter("abstract_horizon", horizon)
        context.metrics.set_counter("abstract_solve_calls", solve_calls)

    with context.metrics.measure("abstract_solving"):
        solve_result = solve(context.abstract_asp, on_attempt=record_attempt)

    context.horizon = solve_result.horizon
    context.metrics.set_counter("abstract_horizon", solve_result.horizon)
    context.metrics.set_counter("abstract_solve_calls", solve_result.attempts)

    return parse_plan_actions(solve_result.plan)


def _extend_concrete_search(context, solver, guided_solve_calls):
    """Search above the abstract horizon without abstract-plan constraints."""
    initial_horizon = context.horizon

    def record_attempt(horizon, solve_calls):
        context.metrics.set_counter("increments", horizon - initial_horizon)
        context.metrics.set_counter("final_horizon", horizon)
        context.metrics.set_counter("concrete_solve_calls", guided_solve_calls + solve_calls)

    # Every switch is off, so the guided solver now behaves like the plain
    # concrete program while keeping the grounding the decremental search built.
    solver.extend()
    solve_result = solver.search(disabled_switches(solver), record_attempt)

    context.horizon = solve_result.horizon
    context.metrics.set_counter("concrete_solve_calls", guided_solve_calls + solve_result.attempts)
    return solve_result.plan, context.horizon - initial_horizon


def _build_result(context, *, success, plan):
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
        "run_id": context.run_id,
    }
