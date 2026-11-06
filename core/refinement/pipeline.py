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
from core.refinement.encoding import (
    add_concrete_objects,
    add_switches,
    drop_action_choice,
    map_abstract_actions,
    make_steps_optional,
    switches,
)
from core.search.incremental import IncrementalSolver
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
    plan = _solve_concrete_plan(context, abstract_plan, abstract_horizon)
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
        concrete_asp = sas_to_asp(concrete_sas)

    if not context.config.optimize:
        concrete_asp = replace(concrete_asp, rules=make_steps_optional(concrete_asp.rules))

    return concrete_asp


def _solve_concrete_plan(context, abstract_plan, abstract_horizon):
    """Refine the abstract plan as it is, then give it up step by step and search above its horizon."""
    asp = _concrete_asp(context)

    # Publish the counters before searching so an interrupted run still has them.
    counters = {
        "increments": 0,
        "decrements": 0,
        "concrete_solve_calls": 0,
    }
    context.metrics.set_counters(counters)

    def record_attempt(increments, dropped, search_calls):
        counters["increments"] = increments
        counters["decrements"] = dropped
        # The solve with every switch held comes before the search's own calls.
        counters["concrete_solve_calls"] = search_calls + 1
        context.metrics.set_counters(counters)

    with context.metrics.measure("guided_concrete_solving"):
        record_attempt(0, 0, 0)
        plan = _one_shot(context, asp, abstract_plan, abstract_horizon)
        if plan is not None:
            return plan
        solver = _fallback_solver(context, asp, abstract_plan, abstract_horizon)
        # Clingo holds its own copy of the program, so the text would only take memory from the search.
        del asp
        return _fallback(context, solver, abstract_plan, record_attempt)


def _one_shot(context, asp, abstract_plan, abstract_horizon):
    """Refine the abstract plan as it is, in one solve at its horizon."""
    choices = map_abstract_actions(abstract_plan, context.abstraction, gaps=False)
    rules = [drop_action_choice(asp.rules), *add_concrete_objects(context.abstraction), *choices.values()]
    solver = IncrementalSolver(
        asp=replace(asp, rules="\n".join(rules)), init_horizon=abstract_horizon, optimize=context.config.optimize
    )
    return solver.solve()


def _fallback_solver(context, asp, abstract_plan, abstract_horizon):
    """Load the program whose switches can give the abstract plan up step by step."""
    gaps = not context.config.optimize
    if gaps:
        init_horizon = 2 * abstract_horizon + 1
    else:
        init_horizon = abstract_horizon

    choices = map_abstract_actions(abstract_plan, context.abstraction, gaps)
    rules = [asp.rules, *add_concrete_objects(context.abstraction), *add_switches(choices)]
    return RelaxingSolver(
        asp=replace(asp, rules="\n".join(rules)), init_horizon=init_horizon, optimize=context.config.optimize
    )


def _fallback(context, solver, abstract_plan, record_attempt):
    """Give the abstract plan up step by step, from its end, and search above its horizon."""
    gaps = not context.config.optimize

    def record_search(horizon, dropped, search_calls):
        record_attempt(horizon - solver.init_horizon, dropped, search_calls)

    result = solver.search(switches(abstract_plan, gaps), record_search)

    record_search(result.horizon, result.dropped, result.attempts)
    return result.plan
