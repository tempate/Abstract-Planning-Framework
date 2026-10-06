"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass

from core.abstraction.factory import Abstraction
from core.integrations.clingo import plan_length
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.refinement.mapping import build_mapping, mapped_horizon
from core.search.incremental import IncrementalSolver


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

    def record_attempt(horizon, solve_calls):
        _publish_counters(context, decrements=len(switches), increments=horizon - mapped, solve_calls=solve_calls + 1)

    with context.metrics.measure("guided_concrete_solving"):
        # The switches are free choices, so one call covers every way of following
        # part of the abstract plan. The heuristic decides them true first, so the
        # solver gives an abstract action up only where a conflict makes it.
        solver = IncrementalSolver(asp, mapped, domain_heuristic=True)
        switches = _switches(solver)
        plan = solver.solve()
        if plan is not None:
            kept = sum(1 for atom in plan if atom.startswith("switch("))
            _publish_counters(context, decrements=len(switches) - kept, increments=0, solve_calls=1)
            return plan

        # No part of the abstract plan refines at this horizon, so give all of it up.
        solver.extend()
        result = solver.search([(switch, False) for switch in switches], record_attempt)

    _publish_counters(
        context, decrements=len(switches), increments=result.horizon - mapped, solve_calls=result.attempts + 1
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
