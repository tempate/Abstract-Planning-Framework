"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass

from core.abstraction.factory import Abstraction
from core.integrations.clingo import plan_length
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.refinement.encoding import add_gaps, concretize_abstract_actions, mapped_horizon, switches
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
    horizon = mapped_horizon(abstract_horizon)

    asp = add_gaps(context.concrete_asp, horizon, context.config.minimize_gaps)
    asp += "\n" + concretize_abstract_actions(abstract_plan, context.abstraction)

    plan = _solve_concrete_plan(context, asp, horizon, switches(abstract_plan))
    if plan is not None:
        context.metrics.set_counter("plan_length", plan_length(plan))

    return {
        "configuration": context.config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": context.run_id,
    }


def _solve_concrete_plan(context, asp, init_horizon, switches):
    """Refine the abstract plan, then search above its horizon if it does not refine."""
    # Publish the counters before searching so an interrupted run still has them.
    counters = {
        "increments": 0,
        "decrements": 0,
        "concrete_solve_calls": 0,
    }
    context.metrics.set_counters(counters)

    def record_attempt(horizon, dropped, solve_calls):
        counters["increments"] = horizon - init_horizon
        counters["decrements"] = dropped
        counters["concrete_solve_calls"] = solve_calls
        context.metrics.set_counters(counters)

    with context.metrics.measure("guided_concrete_solving"):
        solver = RelaxingSolver(asp, init_horizon)
        result = solver.search(switches, record_attempt)

    record_attempt(result.horizon, result.dropped, result.attempts)
    return result.plan
