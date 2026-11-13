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
    drop_action_choice,
    expand_abstract_actions,
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


def refine(context: RefinementContext, abstract_plan):
    """Refine an abstract plan as it is, then give it up step by step and search above its horizon.

    The plan holds one action per step, from 1.
    """
    abstract_plan = _with_original_names(abstract_plan, context.renamings)

    # Publish the counters before searching so an interrupted run still has them.
    _record_search(context.metrics, increments=0, decrements=0, solve_calls=1)

    partial = os.path.exists(PARTIAL_GROUNDING_TRANSLATOR)
    atoms = None
    if partial:
        atoms = _partial_one_shot(context, abstract_plan)

    if atoms is None:
        # A one-shot that fails on the partial grounding fails on the full one too.
        atoms = _refine_on_full_grounding(context, abstract_plan, one_shot=not partial)

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


def _record_search(metrics, increments, decrements, solve_calls):
    metrics.set_counters(
        {
            "increments": increments,
            "decrements": decrements,
            "concrete_solve_calls": solve_calls,
        }
    )


def _partial_one_shot(context, abstract_plan):
    """The one-shot on a task grounded with only the actions the abstract plan may refine into."""
    partial_dir = os.path.join(context.base_dir, "partial")
    os.makedirs(partial_dir, exist_ok=True)

    actions_path = os.path.join(partial_dir, "actions.txt")
    with open(actions_path, "w", encoding="utf-8") as actions_file:
        expanded_actions = expand_abstract_actions(abstract_plan, context.abstraction)
        actions_file.write("\n".join(expanded_actions) + "\n")

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
        return _one_shot(context, partial_asp, abstract_plan)


def _one_shot(context, asp, abstract_plan):
    """Refine the abstract plan as it is, in one solve at its horizon."""
    choices = map_abstract_actions(abstract_plan, context.abstraction, gaps=False)
    rules = [drop_action_choice(asp.rules), *add_concrete_objects(context.abstraction), *choices.values()]

    solver = Solver(
        asp=replace(asp, rules="\n".join(rules)), init_horizon=len(abstract_plan), optimize=context.config.optimize
    )
    return solver.solve()


def _refine_on_full_grounding(context, abstract_plan, one_shot):
    """Refine the abstract plan as it is if asked, then give it up from its end and search above its horizon."""
    config = context.config

    with context.metrics.measure("concrete_fd"):
        concrete_dir = os.path.join(context.base_dir, "concrete")
        concrete_sas = pddl_to_sas(concrete_dir, config.domain_path, config.problem_path, "concrete")

    # The program text stays local, so that nothing outside holds it once clingo has loaded it.
    with context.metrics.measure("concrete_asp"):
        asp = sas_to_asp(concrete_sas, config.optimize)

    with context.metrics.measure("guided_concrete_solving"):
        if one_shot:
            atoms = _one_shot(context, asp, abstract_plan)
            if atoms is not None:
                return atoms

        gaps = not config.optimize
        if gaps:
            # A gap before every abstract action and one after the last.
            init_horizon = 2 * len(abstract_plan) + 1
        else:
            init_horizon = len(abstract_plan)

        # Switches let the search give the abstract plan up one action at a time.
        choices = map_abstract_actions(abstract_plan, context.abstraction, gaps)
        rules = [asp.rules, *add_concrete_objects(context.abstraction), *add_switches(choices)]
        solver = Solver(asp=replace(asp, rules="\n".join(rules)), init_horizon=init_horizon, optimize=config.optimize)

        # Clingo holds its own copy of the program, so the text would only take memory from the search.
        del asp, rules

        def record_attempt(horizon, dropped, attempts):
            # The one-shot solve came before the search's own attempts.
            _record_search(context.metrics, horizon - init_horizon, dropped, attempts + 1)

        # Without gaps, holding every switch is the one-shot that already failed, so the first switch starts released.
        result = solver.search(switches(abstract_plan, gaps), record_attempt, dropped=int(not gaps))

        record_attempt(result.horizon, result.dropped, result.attempts)
        return result.plan
