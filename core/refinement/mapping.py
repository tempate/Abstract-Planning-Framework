"""Generic mapping from an abstract plan to concrete actions."""

import json


def mapped_horizon(abstract_horizon):
    """Return the concrete horizon holding every abstract action and its gaps."""
    return 2 * abstract_horizon + 1


def build_mapping(abstract_plan, abstraction):
    """Map an abstract plan to compatible grounded concrete actions.

    args equal to the abstraction name become independent variables
    ranging over its objects.  The concrete ASP ``action/1`` relation then
    limits the choices to grounded actions that actually exist.  The abstract
    plan fixes the order of its actions, not the steps they take, so every step
    is a gap that holds one action or none.
    """
    mapping_rules = []

    # Add all objects of the abstraction to the concrete ASP program.
    for object_name in abstraction.objects:
        mapping_rules.append(f"concrete_object({_quote(object_name)}).")

    # Mark every time step as a gap, so the encoding lets any of them stay
    # empty and the abstract actions are free to take the ones they need.
    horizon = mapped_horizon(_abstract_horizon(abstract_plan))
    for time_step in range(1, horizon + 1):
        mapping_rules.append(f"gap({time_step}).")

    ordered_actions = sorted(abstract_plan, key=lambda action: action.time_step)
    for position, action in enumerate(ordered_actions, start=1):
        # Number the switches by position in the abstract plan, so the
        # decremental search still relaxes the plan from its end. A position
        # never suppresses the time step of the same number, because every step
        # is a gap.
        switch = f"switch({position})"
        mapping_rules.append(f"0 {{ {switch} }} 1.")

        # Place the action on one of the time steps, and map it to a concrete
        # candidate action there.
        mapping_rules.append(f"1 {{ abstract_step({position},T) : T = 1..{horizon} }} 1 :- {switch}.")
        action_str, conds_str = _action_pattern(action, abstraction)
        rule = f"1 {{ occurs({action_str},T) : {conds_str} }} 1 :- abstract_step({position},T)."
        mapping_rules.append(rule)

    # Keep the actions in the order the abstract plan put them in.
    mapping_rules.append(":- abstract_step(I,T1), abstract_step(J,T2), I < J, T1 >= T2.")

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
