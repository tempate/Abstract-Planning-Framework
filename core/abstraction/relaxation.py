"""Find delete effects that can be relaxed after collapsing objects."""

from dataclasses import dataclass


@dataclass(frozen=True)
class _RelaxableInequality:
    action: str
    variables: tuple[str, ...]


@dataclass(frozen=True)
class _RelaxableDelete:
    action: str
    predicate: str
    variables: tuple[str, ...]


def match_relaxable_delete(action, effect, objects_to_collapse):
    """Match a delete effect that refers to the collapsed objects."""
    if (
        not effect.is_assignment()
        or not effect.value.is_false()
        or not effect.fluent.type.is_bool_type()
        or not effect.fluent.is_fluent_exp()
    ):
        return None

    collapsed_type = objects_to_collapse[0].type
    variable_expressions = []
    variable_names = []

    for arg in effect.fluent.args:
        if arg.is_object_exp():
            if arg.object() in objects_to_collapse:
                variable_names.append(arg.object().name)
            continue

        if arg.is_parameter_exp():
            variable = arg.parameter()
        elif arg.is_variable_exp():
            variable = arg.variable()
        else:
            continue

        if not collapsed_type.is_subtype(variable.type):
            continue

        variable_expressions.append(arg)
        variable_names.append(f"?{variable.name}")

    if not variable_names:
        return None

    relaxable_delete = _RelaxableDelete(
        action=action.name, predicate=effect.fluent.fluent().name, variables=tuple(variable_names)
    )
    return tuple(variable_expressions), relaxable_delete


def find_relaxable_deletes(problem, abstraction):
    """Find deletes that can be relaxed for the selected objects."""
    objects_to_collapse = tuple(problem.object(name) for name in abstraction.objects)
    static_fluents = problem.get_static_fluents()
    positive_initial_facts = tuple(
        fluent
        for fluent, value in problem.explicit_initial_values.items()
        if value.type.is_bool_type() and value.is_true()
    )

    relaxable_deletes = []
    for action in problem.actions:
        action_relaxable_deletes = _find_action_relaxable_deletes(
            action, static_fluents, positive_initial_facts, objects_to_collapse
        )
        relaxable_deletes.extend(action_relaxable_deletes)
    return tuple(relaxable_deletes)


def _find_action_relaxable_deletes(action, static_fluents, positive_initial_facts, objects_to_collapse):
    action_relaxable_deletes = []
    for effect in action.effects:
        relaxable_delete = _relaxable_delete_for_effect(
            action, effect, static_fluents, positive_initial_facts, objects_to_collapse
        )
        if relaxable_delete is not None:
            action_relaxable_deletes.append(relaxable_delete)
    return action_relaxable_deletes


def _relaxable_delete_for_effect(action, effect, static_fluents, positive_initial_facts, objects_to_collapse):
    match = match_relaxable_delete(action, effect, objects_to_collapse)
    if match is None:
        return None

    variable_expressions, relaxable_delete = match
    if _names_a_collapsed_object(effect, objects_to_collapse):
        # The delete names a collapsed object outright, so it always applies.
        return relaxable_delete

    # A single argument that can bind a collapsed object is enough to make the
    # delete remove a fact the other collapsed objects may still support.
    for variable_expression in variable_expressions:
        if _binds_a_collapsed_object(
            action, variable_expression, static_fluents, positive_initial_facts, objects_to_collapse
        ):
            return relaxable_delete
    return None


def _names_a_collapsed_object(effect, objects_to_collapse):
    for arg in effect.fluent.args:
        if arg.is_object_exp() and arg.object() in objects_to_collapse:
            return True
    return False


def _binds_a_collapsed_object(action, variable_expression, static_fluents, positive_initial_facts, objects_to_collapse):
    """Check whether static preconditions still let the variable take a collapsed object."""
    static_conditions = _collect_static_preconditions(action, variable_expression, static_fluents)
    applicable_objects = set(objects_to_collapse)
    for condition in static_conditions:
        supported_objects = _objects_supported_by_condition(condition, variable_expression, positive_initial_facts)
        applicable_objects &= supported_objects
        if not applicable_objects:
            return False
    return True


def _collect_static_preconditions(action, variable_expression, static_fluents):
    static_preconditions = []
    for precondition in action.preconditions:
        static_preconditions.extend(_find_static_preconditions(precondition, variable_expression, static_fluents))
    return static_preconditions


def _objects_supported_by_condition(atom, variable_expression, positive_initial_facts):
    supported_objects = set()
    for fact in positive_initial_facts:
        matching_object = _matching_object(atom, fact, variable_expression)
        if matching_object is not None:
            supported_objects.add(matching_object)
    return supported_objects


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


def relax_inequalities(problem, abstraction):
    """Drop the inequalities the collapse would make false.

    Collapsing two objects into one symbol makes (not (= ?x ?y)) false wherever
    both sides can bind a collapsed object, which loses every ground action the
    concrete task reaches through them. Dropping the condition keeps those
    actions, in the same sense that relaxing a delete keeps a fact the concrete
    task removes.
    """
    objects_to_collapse = tuple(problem.object(name) for name in abstraction.objects)
    relaxed_problem = problem.clone()

    relaxed_inequalities = []
    for action in relaxed_problem.actions:
        kept_preconditions = []
        for precondition in action.preconditions:
            kept = _without_relaxable_inequalities(action, precondition, objects_to_collapse, relaxed_inequalities)
            if kept is not None:
                kept_preconditions.append(kept)
        action.clear_preconditions()
        for precondition in kept_preconditions:
            action.add_precondition(precondition)

    return relaxed_problem, tuple(relaxed_inequalities)


def _without_relaxable_inequalities(action, condition, objects_to_collapse, relaxed_inequalities):
    """Drop the relaxable inequalities from a condition, or None if nothing is left.

    The reader hands over a whole conjunction as one precondition, so the
    inequality usually sits inside an and rather than beside it.
    """
    relaxable_inequality = _match_relaxable_inequality(action, condition, objects_to_collapse)
    if relaxable_inequality is not None:
        relaxed_inequalities.append(relaxable_inequality)
        return None
    if not condition.is_and():
        return condition

    kept = []
    for argument in condition.args:
        kept_argument = _without_relaxable_inequalities(action, argument, objects_to_collapse, relaxed_inequalities)
        if kept_argument is not None:
            kept.append(kept_argument)
    if not kept:
        return None
    if len(kept) == 1:
        return kept[0]
    return condition.environment.expression_manager.And(kept)


def _match_relaxable_inequality(action, precondition, objects_to_collapse):
    """Match a precondition that the collapse would turn into (not (= x x))."""
    if not precondition.is_not() or not precondition.arg(0).is_equals():
        return None

    collapsed_type = objects_to_collapse[0].type
    variable_names = []
    for side in precondition.arg(0).args:
        name = _collapsible_name(side, collapsed_type, objects_to_collapse)
        if name is None:
            return None
        variable_names.append(name)

    return _RelaxableInequality(action=action.name, variables=tuple(variable_names))


def _collapsible_name(expression, collapsed_type, objects_to_collapse):
    """Name the side of an equality when it can take a collapsed object."""
    if expression.is_object_exp():
        if expression.object() in objects_to_collapse:
            return expression.object().name
        return None
    if expression.is_parameter_exp():
        parameter = expression.parameter()
    elif expression.is_variable_exp():
        parameter = expression.variable()
    else:
        return None
    if not collapsed_type.is_subtype(parameter.type):
        return None
    return f"?{parameter.name}"
