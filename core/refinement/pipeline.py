"""Realize an abstract plan as a concrete plan."""

import os
from dataclasses import dataclass, replace

from core.abstraction.factory import Abstraction
from core.abstraction.relaxation import SPLIT_SEPARATOR
from core.integrations.clingo import plan_length
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.refinement.encoding import concretize_abstract_actions, switches
from core.search.relaxing import RelaxingSolver


@dataclass
class RefinementContext:
    """What refining an abstract plan needs."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    run_id: str
    metrics: PlanningMetrics
    base_dir: str
    # Written name to original, for what the writer renamed in the abstract task.
    renamings: dict[str, str]


def refine(context: RefinementContext, abstract_plan, abstract_horizon):
    """Ground the concrete task, then use an abstract plan to guide its search."""
    abstract_plan = _with_original_names(abstract_plan, context.renamings)
    asp = _concrete_asp(context) + "\n" + concretize_abstract_actions(abstract_plan, context.abstraction)

    plan = _solve_concrete_plan(context, asp, abstract_horizon, switches(abstract_plan))
    if plan is not None:
        context.metrics.set_counter("plan_length", plan_length(plan))

    return {
        "configuration": context.config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": context.run_id,
    }


def _with_original_names(abstract_plan, renamings):
    """The abstract plan in the names of the concrete task, which refinement matches it against."""
    renamed = []
    for action in abstract_plan:
        # A split action carries its original name before the separator.
        name = renamings.get(action.name, action.name).split(SPLIT_SEPARATOR)[0]
        args = tuple(renamings.get(arg, arg) for arg in action.args)
        renamed.append(replace(action, name=name, args=args))

    return tuple(renamed)


def _concrete_asp(context):
    """Ground the concrete task and translate it into the ASP program the refinement searches."""
    config = context.config
    with context.metrics.measure("concrete_fd"):
        concrete_dir = os.path.join(context.base_dir, "concrete")
        concrete_sas = pddl_to_sas(concrete_dir, config.domain_path, config.problem_path, "concrete")

    with context.metrics.measure("concrete_asp"):
        return sas_to_asp(concrete_sas, config.optimize)


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
        solver = RelaxingSolver(asp, init_horizon, optimize=context.config.optimize)
        result = solver.search(switches, record_attempt)

    record_attempt(result.horizon, result.dropped, result.attempts)
    return result.plan
