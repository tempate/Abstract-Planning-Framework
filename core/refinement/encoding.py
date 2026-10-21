"""The gaps and the abstract plan that refinement adds to the concrete ASP program."""

import json

import clingo

from core.encodings.rules import AT_MOST_ONE_ACTION, EXACTLY_ONE_ACTION


def mapped_horizon(abstract_horizon):
    """Return the concrete horizon holding every abstract action and its gaps."""
    return _concrete_time_step(abstract_horizon) + 1


def add_gaps(asp, horizon):
    """Let the odd time steps up to the horizon stay empty."""
    # Remove the rule forcing actions into every time step,
    # since gaps may not run an action.
    asp = asp.replace(f"{EXACTLY_ONE_ACTION}.", "")

    rules = [
        "#program step(t).",
        f"{AT_MOST_ONE_ACTION} :- gap(t).",
    ]

    # The horizon doubles above the abstract plan, which only finds the shorter plans when those steps can stay empty.
    rules.append(f"{EXACTLY_ONE_ACTION} :- not gap(t), t <= {horizon}.")
    rules.append(f"{AT_MOST_ONE_ACTION} :- t > {horizon}.")

    rules.append("#program base.")
    for t in range(1, horizon + 1, 2):
        rules.append(f"gap({t}).")

    return asp + "\n" + "\n".join(rules) + "\n"


def concretize_abstract_actions(abstract_plan, abstraction, gaps=True):
    """Map an abstract plan to compatible grounded concrete actions."""
    rules = [f"concrete_object({_quote(name)})." for name in abstraction.objects]

    for action in abstract_plan:
        time_step = _concrete_time_step(action.time_step, gaps)

        # A switch per step, so the search can give up the abstract plan one action at a time.
        switch = _switch(time_step)
        rules.append(f"0 {{ {switch} }} 1.")

        # While the switch is on, some grounding of the abstract action occurs at its step.
        action_str, conds_str = _action_pattern(action, abstraction)
        rules.append(f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}.")

    return "\n".join(rules)


def switches(abstract_plan, gaps=True):
    """The switches holding the abstract plan, one per abstract action."""
    switches = []
    for action in abstract_plan:
        time_step = _concrete_time_step(action.time_step, gaps)
        switches.append(_switch(time_step))

    return switches


def _switch(time_step):
    return clingo.Function("switch", [clingo.Number(time_step)])


def _concrete_time_step(abstract_time_step, gaps=True):
    """Place an abstract action after the gap that precedes it, if there are gaps."""
    return 2 * abstract_time_step if gaps else abstract_time_step


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
