"""Find what the collapse would falsify, so that it can be relaxed instead."""

import itertools
from collections import OrderedDict

from unified_planning.model import Fluent, InstantaneousAction

# A split action keeps the name it came from, so the refinement can still find
# it in the concrete task, and carries the separator to mark what it is.
SPLIT_SEPARATOR = "--abs-"


def split_actions(problem, abstraction):
    """Split each action on whether its collapsible parameters take a collapsed object.

    Relaxing a delete or an inequality on the schema relaxes it in every
    grounding, including the ones that name no collapsed object. Each copy of an
    action fixes, through static markers, which of its parameters take a
    collapsed object, so the relaxation that follows reaches only the groundings
    that need it.
    """
    collapsed = _collapsed_objects(problem, abstraction)
    collapsed_type = _collapsed_type(problem, abstraction)
    static_fluents = problem.get_static_fluents()
    true_facts = [fluent for fluent, value in problem.explicit_initial_values.items() if value.is_true()]

    split_problem = problem.clone()
    collapsed_marker, kept_marker = _add_markers(split_problem, abstraction, collapsed)
    split_problem.clear_actions()
    for action in problem.actions:
        if SPLIT_SEPARATOR in action.name:
            raise ValueError(f"Action name already holds the split separator: {action.name}")
        parameters = _split_parameters(problem, action, collapsed, collapsed_type, static_fluents, true_facts)
        if not parameters:
            split_problem.add_action(action)
            continue
        for index, takes_collapsed in enumerate(itertools.product((False, True), repeat=len(parameters))):
            name = f"{action.name}{SPLIT_SEPARATOR}{index}" if any(takes_collapsed) else action.name
            markers = [
                (collapsed_marker if is_collapsed else kept_marker)(parameter)
                for parameter, is_collapsed in zip(parameters, takes_collapsed)
            ]
            split_problem.add_action(_with_preconditions(action, name, markers))
    return split_problem


def _add_markers(problem, abstraction, collapsed):
    """Static facts telling the collapsed objects apart from every other object of their type tree."""
    root = _collapsed_type(problem, abstraction)
    while root.father is not None:
        root = root.father

    boolean = problem.environment.type_manager.BoolType()
    collapsed_marker = Fluent(f"{abstraction.name}-collapsed", boolean, environment=problem.environment, x=root)
    kept_marker = Fluent(f"{abstraction.name}-kept", boolean, environment=problem.environment, x=root)
    problem.add_fluent(collapsed_marker, default_initial_value=False)
    problem.add_fluent(kept_marker, default_initial_value=False)
    for item in problem.all_objects:
        if item.type != root and not item.type.is_subtype(root):
            continue
        marker = collapsed_marker if item in collapsed else kept_marker
        problem.set_initial_value(marker(item), True)
    return collapsed_marker, kept_marker


def _split_parameters(problem, action, collapsed, collapsed_type, static_fluents, true_facts):
    """The parameters that reach an effect or an inequality and can take both a collapsed object and another one."""
    candidates = []
    for effect in action.effects:
        candidates.extend(effect.fluent.args)
    for atom in _conjuncts(action.preconditions):
        if atom.is_not() and atom.arg(0).is_equals():
            candidates.extend(atom.arg(0).args)

    parameters = []
    for candidate in candidates:
        if not candidate.is_parameter_exp() or candidate in parameters:
            continue
        if not _is_variable_of(candidate, collapsed_type):
            continue
        # A parameter that only ever takes collapsed objects, as when the class
        # is a whole type, relaxes in every grounding, so a split gains nothing.
        others = {
            item
            for item in problem.all_objects
            if item not in collapsed and (item.type == candidate.type or item.type.is_subtype(candidate.type))
        }
        if _can_bind(action, candidate, collapsed, static_fluents, true_facts) and _can_bind(
            action, candidate, others, static_fluents, true_facts
        ):
            parameters.append(candidate)
    return parameters


def _with_preconditions(action, name, conditions):
    parameters = OrderedDict((parameter.name, parameter.type) for parameter in action.parameters)
    copy = InstantaneousAction(name, parameters, action.environment)
    for precondition in action.preconditions:
        copy.add_precondition(precondition)
    for condition in conditions:
        copy.add_precondition(condition)
    for effect in action.effects:
        if effect.is_assignment():
            copy.add_effect(effect.fluent, effect.value, effect.condition, effect.forall)
        elif effect.is_increase():
            copy.add_increase_effect(effect.fluent, effect.value, effect.condition, effect.forall)
        elif effect.is_decrease():
            copy.add_decrease_effect(effect.fluent, effect.value, effect.condition, effect.forall)
        else:
            raise ValueError(f"Unsupported effect in action {action.name}: {effect}")
    return copy


def find_relaxable_deletes(problem, abstraction):
    """Find the deletes that could remove a fact other collapsed objects still hold.

    Returns them as (action name, effect) pairs.
    """
    collapsed = _collapsed_objects(problem, abstraction)
    collapsed_type = _collapsed_type(problem, abstraction)
    static_fluents = problem.get_static_fluents()
    true_facts = [fluent for fluent, value in problem.explicit_initial_values.items() if value.is_true()]

    relaxable = []
    for action in problem.actions:
        for effect in action.effects:
            if _deletes_a_collapsed_fact(action, effect, collapsed, collapsed_type, static_fluents, true_facts):
                relaxable.append((action.name, effect))
    return tuple(relaxable)


def _deletes_a_collapsed_fact(action, effect, collapsed, collapsed_type, static_fluents, true_facts):
    is_delete = (
        effect.is_assignment()
        and effect.value.is_false()
        and effect.fluent.type.is_bool_type()
        and effect.fluent.is_fluent_exp()
    )
    if not is_delete:
        return False

    for argument in effect.fluent.args:
        if argument.is_object_exp() and argument.object() in collapsed:
            # The delete names a collapsed object outright, so it always applies.
            return True

    # A single argument that can bind a collapsed object is enough to make the
    # delete remove a fact the other collapsed objects may still support.
    for argument in effect.fluent.args:
        if not _is_variable_of(argument, collapsed_type):
            continue
        if _can_bind(action, argument, collapsed, static_fluents, true_facts):
            return True
    return False


def _can_bind(action, variable, collapsed, static_fluents, true_facts):
    """Whether the action's static preconditions still let the variable take a collapsed object."""
    candidates = set(collapsed)
    for atom in _conjuncts(action.preconditions):
        is_static_on_variable = atom.is_fluent_exp() and atom.fluent() in static_fluents and variable in atom.args
        if is_static_on_variable:
            candidates &= _objects_satisfying(atom, variable, true_facts)
    return bool(candidates)


def _conjuncts(conditions):
    pending = list(conditions)
    while pending:
        condition = pending.pop()
        if condition.is_and():
            pending.extend(condition.args)
        else:
            yield condition


def _objects_satisfying(atom, variable, true_facts):
    """The objects that, bound to the variable, make the atom one of the true facts."""
    objects = set()
    for fact in true_facts:
        bound = _binding(atom, fact, variable)
        if bound is not None:
            objects.add(bound)
    return objects


def _binding(atom, fact, variable):
    """The object the fact binds the variable to, or None if the fact does not match the atom."""
    if not fact.is_fluent_exp() or fact.fluent() != atom.fluent():
        return None

    bound = None
    for expected, actual in zip(atom.args, fact.args):
        if expected == variable:
            if bound is not None and bound != actual.object():
                return None
            bound = actual.object()
        elif expected.is_parameter_exp() or expected.is_variable_exp():
            # Another variable, which this check leaves free.
            continue
        elif expected != actual:
            return None
    return bound


def relax_inequalities(problem, abstraction):
    """Drop the inequalities the collapse would make false.

    Collapsing two objects into one symbol makes (not (= ?x ?y)) false wherever
    both sides can bind a collapsed object, which loses every ground action the
    concrete task reaches through them. Dropping the condition keeps those
    actions, in the same sense that relaxing a delete keeps a fact the concrete
    task removes. Returns the relaxed problem and the (action name, inequality)
    pairs it dropped.
    """
    collapsed = _collapsed_objects(problem, abstraction)
    collapsed_type = _collapsed_type(problem, abstraction)
    static_fluents = problem.get_static_fluents()
    true_facts = [fluent for fluent, value in problem.explicit_initial_values.items() if value.is_true()]

    def can_be_collapsed(action, side):
        if side.is_object_exp():
            return side.object() in collapsed
        return _is_variable_of(side, collapsed_type) and _can_bind(action, side, collapsed, static_fluents, true_facts)

    relaxed_problem = problem.clone()

    relaxed = []
    for action in relaxed_problem.actions:
        kept = []
        for precondition in action.preconditions:
            condition = _without_inequalities(action, precondition, can_be_collapsed, relaxed)
            if condition is not None:
                kept.append(condition)
        action.clear_preconditions()
        for condition in kept:
            action.add_precondition(condition)

    return relaxed_problem, tuple(relaxed)


def _without_inequalities(action, condition, can_be_collapsed, relaxed):
    """Drop the relaxable inequalities from a condition, or None if nothing is left.

    The reader hands over a whole conjunction as one precondition, so the
    inequality usually sits inside an and rather than beside it.
    """
    if condition.is_not() and condition.arg(0).is_equals():
        if all(can_be_collapsed(action, side) for side in condition.arg(0).args):
            relaxed.append((action.name, condition))
            return None
    if not condition.is_and():
        return condition

    kept = []
    for argument in condition.args:
        kept_argument = _without_inequalities(action, argument, can_be_collapsed, relaxed)
        if kept_argument is not None:
            kept.append(kept_argument)
    if not kept:
        return None
    if len(kept) == 1:
        return kept[0]
    return condition.environment.expression_manager.And(kept)


def _is_variable_of(expression, collapsed_type):
    """Whether the expression is a parameter or variable that can take an object of the collapsed type."""
    if expression.is_parameter_exp():
        variable = expression.parameter()
    elif expression.is_variable_exp():
        variable = expression.variable()
    else:
        return False
    return collapsed_type.is_subtype(variable.type)


def _collapsed_objects(problem, abstraction):
    return frozenset(problem.object(name) for name in abstraction.objects)


def _collapsed_type(problem, abstraction):
    return problem.object(abstraction.objects[0]).type
