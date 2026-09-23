"""Generic mapping from an abstract plan to concrete actions."""

import json


def concrete_time_step(abstract_time_step):
    """Place an abstract action after the gap that precedes it."""
    return 2 * abstract_time_step


def mapped_horizon(abstract_horizon):
    """Return the concrete horizon holding every abstract action and its gaps."""
    return concrete_time_step(abstract_horizon) + 1


def build_mapping(abstract_plan, abstraction):
    """Map an abstract plan to compatible grounded concrete actions.

    args equal to the abstraction name become independent variables
    ranging over its objects.  The concrete ASP ``action/1`` relation then
    limits the choices to grounded actions that actually exist.  The actions
    take the even time steps, leaving a gap around each for one action or none.
    """
    mapping_rules = []

    for object_name in abstraction.objects:
        mapping_rules.append(f"concrete_object({_quote(object_name)}).")

    # Mark the odd time steps as gaps so the encoding lets them stay empty.
    abstract_horizon = max((action.time_step for action in abstract_plan), default=0)
    for time_step in range(1, mapped_horizon(abstract_horizon) + 1, 2):
        mapping_rules.append(f"gap({time_step}).")

    for action in sorted(abstract_plan, key=lambda action: action.time_step):
        time_step = concrete_time_step(action.time_step)

        # A switch per step, so the search can give up the abstract plan one action at a time.
        switch = f"switch({time_step})"
        mapping_rules.append(f"0 {{ {switch} }} 1.")

        # While the switch is on, some grounding of the abstract action occurs at its step.
        action_str, conds_str = _action_pattern(action, abstraction)
        rule = f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}."
        mapping_rules.append(rule)

    return "\n".join(mapping_rules)


def _action_pattern(action, abstraction):
    """Extract the action pattern and independent variables from an abstract action."""
    variables = []
    args = []
    for arg in action.args:
        if arg.casefold() == abstraction.name.casefold():
            variable = f"ConcreteObject{len(variables) + 1}"
            variables.append(variable)
            args.append(variable)
        else:
            args.append(_quote(arg))

    action_str = f"action(({','.join((_quote(action.name), *args))}))"

    conds = []
    for variable in variables:
        conds.append(f"concrete_object({variable})")
    conds.append(f"action({action_str})")
    conds_str = ", ".join(conds)

    return action_str, conds_str


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
