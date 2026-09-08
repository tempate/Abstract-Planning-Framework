"""Generic mapping from an abstract plan to concrete actions."""

import json


def concrete_time_step(abstract_time_step):
    """Place an abstract action after the gap that precedes it."""
    return 2 * abstract_time_step


def mapped_horizon(abstract_horizon):
    """Return the concrete horizon holding every abstract action and its gaps."""
    return concrete_time_step(abstract_horizon) + 1


def build_mapping(abstract_plan, abstractions):
    """Map an abstract plan to compatible grounded concrete actions.

    args equal to an abstract symbol become independent variables ranging over
    that symbol's objects.  The concrete ASP ``action/1`` relation then limits
    the choices to grounded actions that actually exist.  The actions take the
    even time steps, leaving a gap around each for one action or none.
    """
    abstractions_by_name = {}
    for abstraction in abstractions:
        abstractions_by_name[abstraction.name.casefold()] = abstraction

    mapping_rules = []

    # Key the objects by their abstract symbol so a variable standing for one
    # collapsed class cannot ground to another class's object.
    for abstraction in abstractions:
        for object_name in abstraction.objects:
            mapping_rules.append(f"concrete_object({_quote(abstraction.name)},{_quote(object_name)}).")

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
        action_str, conds_str = _action_pattern(action, abstractions_by_name)
        rule = f"1 {{ occurs({action_str},{time_step}) : {conds_str} }} 1 :- {switch}."
        mapping_rules.append(rule)

    return "\n".join(mapping_rules)


def _abstract_horizon(abstract_plan):
    """Return the last time step of the abstract plan."""
    horizon = 0
    for action in abstract_plan:
        horizon = max(horizon, action.time_step)
    return horizon


def _action_pattern(action, abstractions_by_name):
    """Extract the action pattern and independent variables from an abstract action."""
    # Find the arguments and the abstract variables of the action
    variables = []
    args = []
    for arg in action.args:
        abstraction = abstractions_by_name.get(arg.casefold())
        if abstraction is not None:
            # Replace the abstract variable with a new independent variable for the concrete action.
            variable = f"ConcreteObject{len(variables) + 1}"
            variables.append((variable, abstraction))
            args.append(variable)
        else:
            args.append(_quote(arg))

    # Build the action string for the new arguments.
    action_str = f"action(({','.join((_quote(action.name), *args))}))"

    # Build the conditions for the independent variables and the action.
    conds = []
    for variable, abstraction in variables:
        conds.append(f"concrete_object({_quote(abstraction.name)},{variable})")
    conds.append(f"action({action_str})")
    conds_str = ", ".join(conds)

    return action_str, conds_str


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
