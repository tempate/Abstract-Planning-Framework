"""The gaps and the abstract plan that refinement adds to the concrete ASP program."""

import json

import clingo


def mapped_horizon(abstract_horizon):
    """Return the concrete horizon holding every abstract action and its gaps."""
    return _concrete_time_step(abstract_horizon) + 1


def optional_steps(asp):
    """Let every step stay empty unless its switch holds an abstract action there."""
    # Gaps hold no switch, so they stay optional. A step whose switch is off
    # stays optional too, or a plan shorter than a satisficing abstract plan is
    # never found.
    every_step_filled = "1 {occurs(Action, t) : action(Action)} 1."
    at_most_one_action = "0 {occurs(Action, t) : action(Action)} 1."
    return asp.replace(every_step_filled, at_most_one_action)


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
