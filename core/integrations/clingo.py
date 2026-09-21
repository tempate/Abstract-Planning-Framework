"""Reading Clingo's models back as plan actions."""

import clingo

from core.outcomes import IntegrationError
from core.plan import PlanAction


def parse_plan_actions(atoms):
    """Convert shown ``occurs/2`` atoms into chronological plan actions."""
    actions = []
    for atom in atoms:
        action = _plan_action(clingo.parse_term(atom.rstrip(".")))
        if action is not None:
            actions.append(action)

    return tuple(sorted(actions, key=lambda action: action.time_step))


def plan_length(atoms):
    """Count the actions in a plan, which gaps leave below the horizon."""
    return len(parse_plan_actions(atoms))


def _plan_action(symbol):
    """Read one occurs/2 atom, or None when it is some other atom."""
    if not _is_function(symbol, "occurs", 2):
        return None

    # Past this point the atom is a step of the plan, so a shape this cannot
    # read is a step gone missing rather than an atom to pass over. Dropping it
    # would shorten the plan the caller reports and weaken the guidance the
    # refinement builds from it.
    action, time_step = symbol.arguments
    fields = _action_fields(action.arguments[0]) if _is_function(action, "action", 1) else None
    if fields is None or time_step.type != clingo.SymbolType.Number:
        raise IntegrationError(f"Clingo returned a plan step this parser cannot read: {symbol}")
    return PlanAction(fields[0], fields[1:], time_step.number)


def _action_fields(payload):
    """Read an action's name and arguments from its string or tuple payload."""
    if payload.type == clingo.SymbolType.String:
        return (payload.string,)
    if payload.type != clingo.SymbolType.Function or payload.name != "" or not payload.arguments:
        return None

    fields = []
    for item in payload.arguments:
        if item.type != clingo.SymbolType.String:
            return None
        fields.append(item.string)
    return tuple(fields)


def _is_function(symbol, name, arity):
    return symbol.type == clingo.SymbolType.Function and symbol.name == name and len(symbol.arguments) == arity
