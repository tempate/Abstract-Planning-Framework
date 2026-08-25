"""Find delete effects that can be relaxed after collapsing objects."""

from dataclasses import dataclass


@dataclass(frozen=True)
class _RelaxableDelete:
    action: str
    predicate: str
    variable: str


def find_relaxable_deletes(problem, abstraction):
    """Find unary deletes that can be relaxed for the selected objects."""
    objects_to_collapse = tuple(problem.object(name) for name in abstraction.objects)
    collapsed_type = objects_to_collapse[0].type
    static_fluents = problem.get_static_fluents()
    positive_initial_facts = tuple(
        fluent
        for fluent, value in problem.explicit_initial_values.items()
        if value.type.is_bool_type() and value.is_true()
    )

    relaxable_deletes = []
    for action in problem.actions:
        action_relaxable_deletes = _find_action_relaxable_deletes(
            action, collapsed_type, static_fluents, positive_initial_facts, objects_to_collapse
        )
        relaxable_deletes.extend(action_relaxable_deletes)
    return tuple(relaxable_deletes)


def _find_static_preconditions(expression, variable_expression, static_fluents):
    static_preconditions = []
    pending_expressions = [expression]
    while pending_expressions:
        current_expression = pending_expressions.pop()
        if current_expression.is_and():
            pending_expressions.extend(reversed(current_expression.args))
        elif (
            current_expression.is_fluent_exp()
            and current_expression.fluent() in static_fluents
            and variable_expression in current_expression.args
        ):
            static_preconditions.append(current_expression)
    return static_preconditions


def _matching_object(atom, fact, variable_expression):
    if not fact.is_fluent_exp() or atom.fluent() != fact.fluent() or len(atom.args) != len(fact.args):
        return None

    matching_object = None
    for expected, actual in zip(atom.args, fact.args):
        if expected.is_parameter_exp() or expected.is_variable_exp():
            if expected != variable_expression:
                continue
            if not actual.is_object_exp():
                return None
            if matching_object is not None and matching_object != actual.object():
                return None
            matching_object = actual.object()
        elif expected != actual:
            return None
    return matching_object


def _objects_supported_by_condition(atom, variable_expression, positive_initial_facts):
    supported_objects = set()
    for fact in positive_initial_facts:
        matching_object = _matching_object(atom, fact, variable_expression)
        if matching_object is not None:
            supported_objects.add(matching_object)
    return supported_objects


def _collect_static_preconditions(action, variable_expression, static_fluents):
    static_preconditions = []
    for precondition in action.preconditions:
        static_preconditions.extend(_find_static_preconditions(precondition, variable_expression, static_fluents))
    return static_preconditions


def _find_action_relaxable_deletes(action, collapsed_type, static_fluents, positive_initial_facts, objects_to_collapse):
    action_relaxable_deletes = []
    for effect in action.effects:
        relaxable_delete = _relaxable_delete_for_effect(
            action, effect, collapsed_type, static_fluents, positive_initial_facts, objects_to_collapse
        )
        if relaxable_delete is not None:
            action_relaxable_deletes.append(relaxable_delete)
    return action_relaxable_deletes


def _relaxable_delete_for_effect(
    action, effect, collapsed_type, static_fluents, positive_initial_facts, objects_to_collapse
):
    match = match_relaxable_delete(action, effect, collapsed_type)
    if match is None:
        return None

    variable_expression, relaxable_delete = match
    static_conditions = _collect_static_preconditions(action, variable_expression, static_fluents)
    applicable_objects = set(objects_to_collapse)
    for condition in static_conditions:
        supported_objects = _objects_supported_by_condition(condition, variable_expression, positive_initial_facts)
        applicable_objects &= supported_objects
        if not applicable_objects:
            return None
    return relaxable_delete


def match_relaxable_delete(action, effect, collapsed_type):
    """Match a unary delete effect that refers to the collapsed object type."""
    if not effect.is_assignment() or not effect.value.is_false() or not effect.fluent.type.is_bool_type():
        return None
    if not effect.fluent.is_fluent_exp() or len(effect.fluent.args) != 1:
        return None
    variable_expression = effect.fluent.arg(0)
    if variable_expression.is_parameter_exp():
        variable = variable_expression.parameter()
    elif variable_expression.is_variable_exp():
        variable = variable_expression.variable()
    else:
        return None
    if not collapsed_type.is_subtype(variable.type):
        return None
    relaxable_delete = _RelaxableDelete(
        action=action.name, predicate=effect.fluent.fluent().name, variable=f"?{variable.name}"
    )
    return variable_expression, relaxable_delete
