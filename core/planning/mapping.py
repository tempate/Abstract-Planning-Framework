"""Generic mapping from an abstract plan to concrete actions."""

import csv
import json
import re

from core.asp import join_asp, parse_abstract_actions
from core.execution import get_logger

OCCURRENCE_VALIDATION_CONSTRAINT = ":- occurs(Action, T), not action(Action)."
_TUPLE_ACTION = re.compile(r"^action\(\((.*)\)\)$")


def build_mapping(abstract_plan, abstract_name, objects):
    """Map an abstract plan to compatible grounded concrete actions.

    Arguments equal to ``abstract_name`` become independent variables ranging
    over the selected symmetry class.  The concrete ASP ``action/1`` relation
    then limits the choices to grounded actions that actually exist.
    """
    abstract_actions = parse_abstract_actions(abstract_plan)
    mapping_rules = [f"concrete_object({_quote(name)})." for name in objects]

    for abstract_action, time_step in abstract_actions:
        switch = f"switch({time_step})"
        mapping_rules.append(f"0 {{ {switch} }} 1.")
        candidate, variables = _concrete_candidate(abstract_action, abstract_name)

        if variables:
            conditions = [*(f"concrete_object({variable})" for variable in variables), f"action({candidate})"]
            mapping_rules.append(
                f"1 {{ occurs({candidate},{time_step}) : {', '.join(conditions)} }} 1 :- "
                f"occurs_abstract({abstract_action},{time_step}), {switch}."
            )
        else:
            mapping_rules.append(
                f"occurs({abstract_action},{time_step}) :- "
                f"occurs_abstract({abstract_action},{time_step}), {switch}."
            )

    logger = get_logger()
    logger.info(f"[MAP] Abstract plan actions={len(abstract_actions)}")
    logger.info("[MAP] Mapping implementation=grounded-action compatibility")
    return join_asp(*mapping_rules, OCCURRENCE_VALIDATION_CONSTRAINT)


def _concrete_candidate(abstract_action, abstract_name):
    """Return an action pattern and its independently grounded variables."""
    match = _TUPLE_ACTION.fullmatch(abstract_action)
    if match is None:
        return abstract_action, ()

    fields = next(csv.reader([match.group(1)], skipinitialspace=True))
    if not fields:
        return abstract_action, ()

    variables = []
    rendered = [_quote(fields[0])]
    for argument in fields[1:]:
        if argument.casefold() == abstract_name.casefold():
            variable = f"ConcreteObject{len(variables) + 1}"
            variables.append(variable)
            rendered.append(variable)
        else:
            rendered.append(_quote(argument))
    return f"action(({','.join(rendered)}))", tuple(variables)


def _quote(value):
    return json.dumps(str(value), ensure_ascii=False)
