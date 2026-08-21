"""Generic mapping from an abstract plan to concrete actions."""

import json

from core.asp import join_asp
from core.execution import get_logger

OCCURRENCE_VALIDATION_CONSTRAINT = ":- occurs(Action, T), not action(Action)."


def build_mapping(abstract_plan, abstraction):
    """Map an abstract plan to compatible grounded concrete actions.

    args equal to the abstraction name become independent variables
    ranging over its objects.  The concrete ASP ``action/1`` relation then
    limits the choices to grounded actions that actually exist.
    """
    mapping_rules = []

    # Add all objects of the abstraction to the concrete ASP program.
    for object_name in abstraction.objects:
        mapping_rules.append(f"concrete_object({_quote(object_name)}).")

    for action in sorted(abstract_plan, key=lambda action: action.time_step):
        # Add a switch for each time step to allow the abstract plan to be disabled.
        switch = f"switch({action.time_step})"
        mapping_rules.append(f"0 {{ {switch} }} 1.")

        # Add a rule to map the abstract action to a concrete candidate action.
        # If the switch is on, then the action at the time step must hold for some grounding.
        action_str, conds_str = _action_pattern(action, abstraction)
        rule = f"1 {{ occurs({action_str},{action.time_step}) : {conds_str} }} 1 :- {switch}."
        mapping_rules.append(rule)

    # Add a rule to ensure that only valid concrete actions are chosen.
    mapping_rules.append(OCCURRENCE_VALIDATION_CONSTRAINT)

    logger = get_logger()
    logger.info(f"[MAP] Abstract plan actions={len(abstract_plan)}")
    logger.info("[MAP] Mapping implementation=grounded-action compatibility")
    return join_asp(*mapping_rules)


def _action_pattern(action, abstraction):
    """Extract the action pattern and independent variables from an abstract action."""
    # Find the arguments and the abstract variables of the action
    vars = []
    args = []
    for arg in action.args:
        if arg.casefold() == abstraction.name.casefold():
            # Replace the abstract variable with a new independent variable for the concrete action.
            var = f"ConcreteObject{len(vars) + 1}"
            vars.append(var)
            args.append(var)
        else:
            args.append(_quote(arg))

    # Build the action string for the new arguments.
    action_str = f"action(({','.join((_quote(action.name), *args))}))"

    # Build the conditions for the independent variables and the action.
    conds = []
    for var in vars:
        conds.append(f"concrete_object({var})")
    conds.append(f"action({action_str})")
    conds_str = ", ".join(conds)

    return action_str, conds_str


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
