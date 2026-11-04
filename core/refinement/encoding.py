"""The abstract plan that refinement adds to the concrete ASP program."""

import json

import clingo


def concretize_abstract_actions(abstract_plan, abstraction):
    """Map an abstract plan to compatible grounded concrete actions."""
    rules = [f"concrete_object({_quote(name)})." for name in abstraction.objects]

    for action in abstract_plan:
        time_step = action.time_step

        # A switch per step, so the search can give up the abstract plan one action at a time.
        switch = _switch(time_step)
        rules.append(f"0 {{ {switch} }} 1.")

        # While the switch is on, some grounding of the abstract action occurs at its step.
        action_str, conds_str = _action_pattern(action, abstraction)
        rules.append(f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}.")

    return "\n".join(rules)


def switches(abstract_plan):
    """The switches holding the abstract plan, latest first, so that what survives relaxation is a prefix of it."""
    switches = []
    for action in abstract_plan:
        switches.append(_switch(action.time_step))

    return sorted(switches, reverse=True)


def _switch(time_step):
    return clingo.Function("switch", [clingo.Number(time_step)])


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
