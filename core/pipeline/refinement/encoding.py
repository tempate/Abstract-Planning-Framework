"""The gaps and the abstract plan that refinement adds to the concrete ASP program."""

import itertools
import json

import clingo

from core.asp.program import AT_MOST_ONE_ACTION, EXACTLY_ONE_ACTION


def drop_action_choice(asp):
    """Remove the choice of any action at every step, leaving each step to the abstract plan."""
    # EXACTLY_ONE_ACTION ends in AT_MOST_ONE_ACTION, so it goes first.
    return asp.replace(f"{EXACTLY_ONE_ACTION}.", "").replace(f"{AT_MOST_ONE_ACTION}.", "")


def add_concrete_objects(abstraction):
    """The constants an abstract action's groundings may use in place of the abstract one."""
    rules = []
    for name in abstraction.objects:
        rules.append(f"concrete_object({_quote(name)}).")
    return rules


def map_abstract_actions(abstract_plan, abstraction, gaps=True):
    """Each abstract action's step, and the rule choosing exactly one of its groundings there."""
    choices = {}

    for action in abstract_plan:
        time_step = _concrete_time_step(action.time_step, gaps)

        # Map each abstract action to one of its groundings.
        action_str, conds_str = _action_pattern(action, abstraction)
        choices[time_step] = f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1."

    return choices


def concrete_groundings(abstract_plan, abstraction):
    """Every concrete action the abstract plan's actions may refine into, as plan-file lines."""
    groundings = set()
    for action in abstract_plan:
        options = []
        for arg in action.args:
            if arg.casefold() == abstraction.name.casefold():
                options.append(abstraction.objects)
            else:
                options.append((arg,))
        for args in itertools.product(*options):
            groundings.add(f"({' '.join((action.name, *args))})".lower())

    return sorted(groundings)


def add_switches(choices):
    """Rules that refine an abstract action only while the switch at its step is on."""
    rules = []

    for time_step, choice in choices.items():
        # A switch per step, so the search can give up the abstract plan one action at a time.
        switch = _switch(time_step)
        rules.append(f"0 {{ {switch} }} 1.")
        # Only the final period ends the rule; a constant in it may hold periods of its own.
        rules.append(f"{choice.removesuffix('.')} :- {switch}.")

    return rules


def switches(abstract_plan, gaps=True):
    """The switches holding the abstract plan, latest first, so that what survives relaxation is a prefix of it."""
    switches = []
    for action in abstract_plan:
        time_step = _concrete_time_step(action.time_step, gaps)
        switches.append(_switch(time_step))

    return sorted(switches, reverse=True)


def _switch(time_step):
    return clingo.Function("switch", [clingo.Number(time_step)])


def _concrete_time_step(abstract_time_step, gaps=True):
    """Place an abstract action after the gap that precedes it, if there are gaps."""
    if gaps:
        return 2 * abstract_time_step
    else:
        return abstract_time_step


def _action_pattern(action, abstraction):
    """Extract the action pattern and independent variables from an abstract action."""
    vars = []
    args = []
    for arg in action.args:
        if arg.casefold() == abstraction.name.casefold():
            var = f"ConcreteObject{len(vars) + 1}"
            vars.append(var)
            args.append(var)
        else:
            args.append(_quote(arg))

    action_name = _quote(action.name)
    action_str = f"action(({','.join((action_name, *args))}))"

    conds = [f"concrete_object({var})" for var in vars]
    conds.append(f"action({action_str})")
    conds_str = ", ".join(conds)

    return action_str, conds_str


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
