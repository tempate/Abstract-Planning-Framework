"""Generic mapping from an abstract plan to concrete actions."""

import json


def concrete_time_step(abstract_time_step):
    """Place an abstract action after the gap that precedes it."""
    return 2 * abstract_time_step


def mapped_horizon(abstract_horizon):
    """Return the concrete horizon holding every abstract action and its gaps."""
    return concrete_time_step(abstract_horizon) + 1


def build_mapping(abstract_plan, abstraction):
    """Map an abstract plan to compatible grounded concrete actions."""
    rules = []

    abstract_plan = sorted(abstract_plan, key=lambda action: action.time_step)
    abstract_horizon = abstract_plan[-1].time_step if len(abstract_plan) > 0 else 0
    concrete_horizon = mapped_horizon(abstract_horizon)

    for object_name in abstraction.objects:
        rules.append(f"concrete_object({_quote(object_name)}).")

    for action in abstract_plan:
        time_step = concrete_time_step(action.time_step)

        # A switch per step, so the search can give up the abstract plan one action at a time.
        switch = f"switch({time_step})"
        rules.append(f"0 {{ {switch} }} 1.")

        # While the switch is on, some grounding of the abstract action occurs at its step.
        action_str, conds_str = _action_pattern(action, abstraction)
        rules.append(f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}.")

    # Mark the odd time steps as gaps so the encoding lets them stay empty.
    for t in range(1, concrete_horizon + 1, 2):
        rules.append(f"gap({t}).")

    return "\n".join(rules)


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
