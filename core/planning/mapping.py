"""Generic mapping from an abstract plan to concrete actions."""

import json

from core.execution import get_logger

OCCURRENCE_VALIDATION_CONSTRAINT = ":- occurs(Action, T), not action(Action)."


def build_mapping(abstract_plan, abstraction):
    """Map an abstract plan to compatible grounded concrete actions.

    Arguments equal to the abstraction name become independent variables
    ranging over its objects.  The concrete ASP ``action/1`` relation then
    limits the choices to grounded actions that actually exist.
    """
    mapping_rules = []

    # Add all objects of the abstraction to the concrete ASP program.
    for object_name in abstraction.objects:
        mapping_rules.append(f"concrete_object({_quote(object_name)}).")

    for plan_action in sorted(abstract_plan, key=lambda action: action.time_step):
        # Add a switch for each time step to allow the abstract plan to be disabled.
        switch = f"switch({plan_action.time_step})"
        mapping_rules.append(f"0 {{ {switch} }} 1.")

        # Add a rule to map the abstract action to a concrete candidate action.
        variables = []
        arguments = []
        for argument in plan_action.arguments:
            if argument.casefold() == abstraction.name.casefold():
                variable = f"ConcreteObject{len(variables) + 1}"
                variables.append(variable)
                arguments.append(variable)
            else:
                arguments.append(_quote(argument))
        candidate = _action_term(plan_action.name, arguments)

        if variables:
            conditions = [*(f"concrete_object({variable})" for variable in variables), f"action({candidate})"]
            mapping_rules.append(
                f"1 {{ occurs({candidate},{plan_action.time_step}) : {', '.join(conditions)} }} 1 :- {switch}."
            )
        else:
            mapping_rules.append(f"occurs({candidate},{plan_action.time_step}) :- {switch}.")

    # Add a rule to ensure that only valid concrete actions are chosen.
    mapping_rules.append(OCCURRENCE_VALIDATION_CONSTRAINT)

    logger = get_logger()
    logger.info(f"[MAP] Abstract plan actions={len(abstract_plan)}")
    logger.info("[MAP] Mapping implementation=grounded-action compatibility")
    return mapping_rules


def _action_term(name, arguments):
    if not arguments:
        return f"action({_quote(name)})"
    return f"action(({','.join((_quote(name), *arguments))}))"


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
