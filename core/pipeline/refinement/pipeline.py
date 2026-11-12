"""Realize an abstract plan as a concrete plan."""

import os
from dataclasses import dataclass, replace

from core.pipeline.abstraction.factory import Abstraction
from core.pipeline.abstraction.relaxation import SPLIT_SEPARATOR
from core.integrations.clingo import parse_plan_actions
from core.integrations.fast_downward import partial_pddl_to_sas, pddl_to_sas
from core.integrations.paths import PARTIAL_GROUNDING_TRANSLATOR
from core.integrations.plasp import sas_to_asp
from core.utilities.metrics import PlanningMetrics
from core.utilities.outcomes import IntegrationError, UnsolvableTaskError
from core.utilities.config import AbstractPlanningConfig
from core.pipeline.refinement.encoding import (
    add_concrete_objects,
    add_switches,
    concrete_groundings,
    drop_action_choice,
    map_abstract_actions,
    switches,
)
from core.asp.solver import Solver


@dataclass
class RefinementContext:
    """What refining an abstract plan needs."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    metrics: PlanningMetrics
    base_dir: str
    # Written name to original, for what the writer renamed in the abstract task.
    renamings: dict[str, str]


def refine(context: RefinementContext, abstract_plan, abstract_horizon):
    """Ground the concrete task, then use an abstract plan to guide its search."""
    abstract_plan = _with_original_names(abstract_plan, context.renamings)
    atoms = _solve_concrete_plan(context, abstract_plan, abstract_horizon)
    if atoms is None:
        return None
    plan = parse_plan_actions(atoms)
    context.metrics.set_counter("plan_length", len(plan))
    return plan


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


def _solve_concrete_plan(context, abstract_plan, abstract_horizon):
    """Refine the abstract plan as it is, then give it up step by step and search above its horizon."""
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

    record_attempt(0, 0, 0)
    if os.path.exists(PARTIAL_GROUNDING_TRANSLATOR):
        plan = _partial_one_shot(context, abstract_plan, abstract_horizon)
        if plan is not None:
            return plan
        asp = _concrete_asp(context)
    else:
        asp = _concrete_asp(context)
        with context.metrics.measure("guided_concrete_solving"):
            plan = _one_shot(context, asp, abstract_plan, abstract_horizon)
        if plan is not None:
            return plan

    with context.metrics.measure("guided_concrete_solving"):
        solver = _fallback_solver(context, asp, abstract_plan, abstract_horizon)
        # Clingo holds its own copy of the program, so the text would only take memory from the search.
        del asp
        return _fallback(context, solver, abstract_plan, record_attempt)


def _partial_one_shot(context, abstract_plan, abstract_horizon):
    """The one-shot on a task grounded with only the actions the abstract plan may refine into."""
    partial_dir = os.path.join(context.base_dir, "partial")
    os.makedirs(partial_dir, exist_ok=True)
    actions_path = os.path.join(partial_dir, "actions.txt")
    with open(actions_path, "w", encoding="utf-8") as actions_file:
        actions_file.write("\n".join(concrete_groundings(abstract_plan, context.abstraction)) + "\n")

    config = context.config
    try:
        with context.metrics.measure("partial_fd"):
            partial_sas = partial_pddl_to_sas(partial_dir, config.domain_path, config.problem_path, actions_path)
    except UnsolvableTaskError:
        # The listed actions cannot reach the goal even with deletes relaxed.
        return None
    except IntegrationError as error:
        # The partial grounder cannot read a line without arguments, which an empty abstract
        # plan or an action without parameters writes. The full grounding needs no list.
        reason = str(error).splitlines()[0]
        print(f"Grounding the whole task, since the partial grounding failed: {reason}", flush=True)
        return None

    with context.metrics.measure("partial_asp"):
        partial_asp = sas_to_asp(partial_sas)

    with context.metrics.measure("partial_one_shot"):
        return _one_shot(context, partial_asp, abstract_plan, abstract_horizon)


def _one_shot(context, asp, abstract_plan, abstract_horizon):
    """Refine the abstract plan as it is, in one solve at its horizon."""
    choices = map_abstract_actions(abstract_plan, context.abstraction, gaps=False)
    rules = [drop_action_choice(asp.rules), *add_concrete_objects(context.abstraction), *choices.values()]
    solver = Solver(
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
    return Solver(asp=replace(asp, rules="\n".join(rules)), init_horizon=init_horizon, optimize=context.config.optimize)


def _fallback(context, solver, abstract_plan, record_attempt):
    """Give the abstract plan up step by step, from its end, and search above its horizon."""
    gaps = not context.config.optimize

    def record_search(horizon, dropped, search_calls):
        record_attempt(horizon - solver.init_horizon, dropped, search_calls)

    # Without gaps, holding every switch is the one-shot that already failed, so the first switch starts released.
    result = solver.search(switches(abstract_plan, gaps), record_search, dropped=int(not gaps))

    record_search(result.horizon, result.dropped, result.attempts)
    return result.plan
