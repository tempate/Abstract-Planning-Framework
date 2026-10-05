"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass

from core.abstraction.factory import Abstraction
from core.integrations.clingo import plan_length
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.refinement.mapping import build_mapping, mapped_horizon
from core.search.relaxing import RelaxingSolver


@dataclass
class RefinementContext:
    """What refining an abstract plan needs."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    run_id: str
    metrics: PlanningMetrics
    concrete_asp: str


def refine(context: RefinementContext, abstract_plan, abstract_horizon):
    """Use an abstract plan to guide concrete search."""
    mapping = build_mapping(abstract_plan, context.abstraction)
    asp = "\n".join((context.concrete_asp, mapping))
    # The concrete search runs on the mapped time line, which surrounds every
    # abstract action with a gap for one optional concrete action.
    plan = _solve_concrete_plan(context, asp, mapped_horizon(abstract_horizon))

    if plan is not None:
        context.metrics.set_counter("plan_length", plan_length(plan))

    return {
        "configuration": context.config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": context.run_id,
    }


def _solve_concrete_plan(context, asp, mapped):
    """Refine the abstract plan, then search above its horizon if it does not refine."""
    # Publish the counters before searching so an interrupted run still has them.
    _publish_counters(context, decrements=0, increments=0, solve_calls=0)

    def record_attempt(horizon, dropped, solve_calls):
        _publish_counters(context, decrements=dropped, increments=horizon - mapped, solve_calls=solve_calls)

    with context.metrics.measure("guided_concrete_solving"):
        solver = RelaxingSolver(asp, mapped)
        # Give up the abstract plan from its end, so what survives is a prefix of it.
        result = solver.search(list(reversed(_switches(solver))), record_attempt)

    _publish_counters(
        context, decrements=result.dropped, increments=result.horizon - mapped, solve_calls=result.attempts
    )
    return result.plan


def _switches(solver):
    """The switches holding the abstract plan, ordered by time step rather than lexically."""
    switches = [atom.symbol for atom in solver.control.symbolic_atoms if atom.symbol.name == "switch"]
    return sorted(switches, key=lambda switch: switch.arguments[0].number)


def _publish_counters(context, *, decrements, increments, solve_calls):
    """Report the concrete search's progress so far."""
    context.metrics.set_counters(
        {
            "decrements": decrements,
            "increments": increments,
            "concrete_solve_calls": solve_calls,
        }
    )
