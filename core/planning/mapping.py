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
    limits the choices to grounded actions that actually exist.

    The abstract actions are spread over the even time steps, leaving a gap
    before the first one, between consecutive ones, and after the last one.
    Each gap holds one concrete action or none.
    """
    mapping_rules = []

    # Add all objects of the abstraction to the concrete ASP program.
    for object_name in abstraction.objects:
        mapping_rules.append(f"concrete_object({_quote(object_name)}).")

    # Mark the odd time steps as gaps so the encoding lets them stay empty.
    for time_step in range(1, mapped_horizon(_abstract_horizon(abstract_plan)) + 1, 2):
        mapping_rules.append(f"gap({time_step}).")

    for action in sorted(abstract_plan, key=lambda action: action.time_step):
        time_step = concrete_time_step(action.time_step)

        # Add a switch for each time step to allow the abstract plan to be disabled.
        switch = f"switch({time_step})"
        mapping_rules.append(f"0 {{ {switch} }} 1.")

        # Add a rule to map the abstract action to a concrete candidate action.
        # If the switch is on, then the action at the time step must hold for some grounding.
        action_str, conds_str = _action_pattern(action, abstraction)
        rule = f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}."
        mapping_rules.append(rule)

    return "\n".join(mapping_rules)


def _abstract_horizon(abstract_plan):
    """Return the last time step of the abstract plan."""
    horizon = 0
    for action in abstract_plan:
        horizon = max(horizon, action.time_step)
    return horizon


def _action_pattern(action, abstraction):
    """Extract the action pattern and independent variables from an abstract action."""
    # Find the arguments and the abstract variables of the action
    variables = []
    args = []
    for arg in action.args:
        if arg.casefold() == abstraction.name.casefold():
            # Replace the abstract variable with a new independent variable for the concrete action.
            variable = f"ConcreteObject{len(variables) + 1}"
            variables.append(variable)
            args.append(variable)
        else:
            args.append(_quote(arg))

    # Build the action string for the new arguments.
    action_str = f"action(({','.join((_quote(action.name), *args))}))"

    # Build the conditions for the independent variables and the action.
    conds = []
    for variable in variables:
        conds.append(f"concrete_object({variable})")
    conds.append(f"action({action_str})")
    conds_str = ", ".join(conds)

    return action_str, conds_str


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
