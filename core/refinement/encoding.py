"""The gaps and the abstract plan that refinement adds to the concrete ASP program."""

import json

import clingo

from core.encodings.rules import AT_MOST_ONE_ACTION, EXACTLY_ONE_ACTION


def make_steps_optional(asp):
    """Let every step stay empty unless its switch holds an abstract action there."""
    return asp.replace(f"{EXACTLY_ONE_ACTION}.", f"{AT_MOST_ONE_ACTION}.")


def choose_freely_while_switched_off(asp):
    """Let a step choose among every action only while no switch holds it to an abstract action."""
    # A held step already chooses among the groundings of its abstract action, so the free choice
    # there only adds candidates the switch rules out anyway.
    # EXACTLY_ONE_ACTION ends in AT_MOST_ONE_ACTION, so these two replacements cover both choices.
    asp = asp.replace(f"{AT_MOST_ONE_ACTION} :- ", f"{AT_MOST_ONE_ACTION} :- not switch(t), ")
    return asp.replace(f"{AT_MOST_ONE_ACTION}.", f"{AT_MOST_ONE_ACTION} :- not switch(t).")


def concretize_abstract_actions(abstract_plan, abstraction, gaps=True, held=False):
    """Map an abstract plan to compatible grounded concrete actions, every switch a fact if held."""
    rules = [f"concrete_object({_quote(name)})." for name in abstraction.objects]

    for action in abstract_plan:
        time_step = _concrete_time_step(action.time_step, gaps)

        # A switch per step, so the search can give up the abstract plan one action at a time.
        switch = _switch(time_step)
        rules.append(f"{switch}." if held else f"0 {{ {switch} }} 1.")

        # While the switch is on, some grounding of the abstract action occurs at its step.
        action_str, conds_str = _action_pattern(action, abstraction)
        rules.append(f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}.")

    return "\n".join(rules)


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
