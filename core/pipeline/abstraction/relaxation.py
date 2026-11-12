"""Find what the collapse would falsify, so that it can be relaxed instead."""

import itertools
from collections import OrderedDict
from dataclasses import dataclass

from unified_planning.model import Fluent, InstantaneousAction

from core.integrations.unified_planning import add_effect_like

# A split action keeps the name it came from, so the refinement can still find
# it in the concrete task, and carries the separator to mark what it is.
SPLIT_SEPARATOR = "--abs-"


@dataclass(frozen=True)
class _Reach:
    """The collapsed class, and the static facts that decide which objects an action's variables can take."""

    collapsed: frozenset
    collapsed_type: object
    static_fluents: set
    true_facts: list


def _reach(problem, abstraction):
    collapsed = frozenset(problem.object(name) for name in abstraction.objects)
    true_facts = [fluent for fluent, value in problem.explicit_initial_values.items() if value.is_true()]
    return _Reach(collapsed, _collapsed_type(problem, abstraction), problem.get_static_fluents(), true_facts)


def split_actions(problem, abstraction):
    """Split each action on whether its collapsible parameters take a collapsed object.

    Relaxing a delete on the schema relaxes it in every grounding, including
    the ones that name no collapsed object. Each copy of an
    action fixes, through static markers, which of its parameters take a
    collapsed object, so the relaxation that follows reaches only the groundings
    that need it.
    """
    reach = _reach(problem, abstraction)

    split_problem = problem.clone()
    collapsed_marker, kept_marker = _add_markers(split_problem, abstraction, reach.collapsed)

    split_problem.clear_actions()
    for action in problem.actions:
        if SPLIT_SEPARATOR in action.name:
            raise ValueError(f"Action name already holds the split separator: {action.name}")

        parameters = _split_parameters(problem, action, reach)
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
    root = _root_type(problem, abstraction)

    boolean = problem.environment.type_manager.BoolType()
    collapsed_marker = Fluent(f"{abstraction.name}-collapsed", boolean, environment=problem.environment, x=root)
    kept_marker = Fluent(f"{abstraction.name}-kept", boolean, environment=problem.environment, x=root)
    problem.add_fluent(collapsed_marker, default_initial_value=False)
    problem.add_fluent(kept_marker, default_initial_value=False)

    for item in problem.all_objects:
        if not item.type.is_subtype(root):
            continue
        marker = collapsed_marker if item in collapsed else kept_marker
        problem.set_initial_value(marker(item), True)

    return collapsed_marker, kept_marker


def _split_parameters(problem, action, reach):
    """The parameters that reach an effect and can take both a collapsed object and another one."""
    candidates = []
    for effect in action.effects:
        candidates.extend(effect.fluent.args)

    parameters = []
    for candidate in candidates:
        if not candidate.is_parameter_exp() or candidate in parameters:
            continue
        if not _is_variable_of(candidate, reach.collapsed_type):
            continue

        # A parameter that only ever takes collapsed objects, as when the class
        # is a whole type, relaxes in every grounding, so a split gains nothing.
        others = {
            item for item in problem.all_objects if item not in reach.collapsed and item.type.is_subtype(candidate.type)
        }
        if _can_bind(action, candidate, reach.collapsed, reach) and _can_bind(action, candidate, others, reach):
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
        add_effect_like(copy, effect, effect.fluent, effect.value, effect.condition)

    return copy


def find_relaxable_deletes(problem, abstraction):
    """Find the deletes that could remove a fact other collapsed objects still hold.

    Returns them as (action name, effect) pairs.
    """
    reach = _reach(problem, abstraction)

    relaxable = []
    for action in problem.actions:
        for effect in action.effects:
            if _deletes_a_collapsed_fact(action, effect, reach):
                relaxable.append((action.name, effect))

    return tuple(relaxable)


def _deletes_a_collapsed_fact(action, effect, reach):
    is_delete = (
        effect.is_assignment()
        and effect.value.is_false()
        and effect.fluent.type.is_bool_type()
        and effect.fluent.is_fluent_exp()
    )
    if not is_delete:
        return False

    for argument in effect.fluent.args:
        if argument.is_object_exp() and argument.object() in reach.collapsed:
            # The delete names a collapsed object outright, so it always applies.
            return True

    # A single argument that can bind a collapsed object is enough to make the
    # delete remove a fact the other collapsed objects may still support.
    for argument in effect.fluent.args:
        if not _is_variable_of(argument, reach.collapsed_type):
            continue
        if _can_bind(action, argument, reach.collapsed, reach):
            return True

    return False


def _can_bind(action, variable, objects, reach):
    """Whether the action's static preconditions still let the variable take one of the objects."""
    candidates = set(objects)
    for atom in _conjuncts(action.preconditions):
        is_static_on_variable = atom.is_fluent_exp() and atom.fluent() in reach.static_fluents and variable in atom.args
        if is_static_on_variable:
            candidates &= _objects_satisfying(atom, variable, reach.true_facts)

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
    """Replace the inequalities the collapse would make false with a static distinct predicate.

    Collapsing two objects into one symbol makes (not (= ?x ?y)) false wherever
    both sides bind a collapsed object, which loses every ground action the
    concrete task reaches through them. The replacement (distinct ?x ?y) holds
    for every pair of different objects, so the collapse turns any two collapsed
    objects into (distinct C C) and keeps exactly those actions, while two kept
    objects still have to differ. Returns the relaxed problem and the
    (action name, inequality) pairs it replaced.
    """
    reach = _reach(problem, abstraction)

    def can_be_collapsed(action, side):
        if side.is_object_exp():
            return side.object() in reach.collapsed
        return _is_variable_of(side, reach.collapsed_type) and _can_bind(action, side, reach.collapsed, reach)

    relaxed_problem = problem.clone()

    root = _root_type(problem, abstraction)
    boolean = problem.environment.type_manager.BoolType()
    distinct = Fluent(f"{abstraction.name}-distinct", boolean, environment=problem.environment, x=root, y=root)

    relaxed = []
    for action in relaxed_problem.actions:
        conditions = [
            _with_distinct(action, precondition, can_be_collapsed, distinct, relaxed)
            for precondition in action.preconditions
        ]
        action.clear_preconditions()
        for condition in conditions:
            action.add_precondition(condition)

    if relaxed:
        relaxed_problem.add_fluent(distinct, default_initial_value=False)

        # The distinct facts cover every object a side of a relaxed inequality can take.
        side_types = set()
        for _, inequality in relaxed:
            for side in inequality.arg(0).args:
                side_types.add(_type_of(side))

        objects = []
        for item in relaxed_problem.all_objects:
            if any(item.type.is_subtype(side_type) for side_type in side_types):
                objects.append(item)

        for first, second in itertools.permutations(objects, 2):
            relaxed_problem.set_initial_value(distinct(first, second), True)

    return relaxed_problem, tuple(relaxed)


def _with_distinct(action, condition, can_be_collapsed, distinct, relaxed):
    """Replace the relaxable inequalities in a condition with the distinct predicate.

    The reader hands over a whole conjunction as one precondition, so the
    inequality usually sits inside an and rather than beside it.
    """
    if condition.is_not() and condition.arg(0).is_equals():
        sides = condition.arg(0).args
        if all(can_be_collapsed(action, side) for side in sides):
            relaxed.append((action.name, condition))
            return distinct(*sides)
        return condition

    if not condition.is_and():
        return condition
    arguments = [_with_distinct(action, argument, can_be_collapsed, distinct, relaxed) for argument in condition.args]
    return condition.environment.expression_manager.And(arguments)


def _type_of(expression):
    if expression.is_object_exp():
        return expression.object().type
    if expression.is_parameter_exp():
        return expression.parameter().type
    return expression.variable().type


def _is_variable_of(expression, collapsed_type):
    """Whether the expression is a parameter or variable that can take an object of the collapsed type."""
    if expression.is_parameter_exp():
        variable = expression.parameter()
    elif expression.is_variable_exp():
        variable = expression.variable()
    else:
        return False

    return collapsed_type.is_subtype(variable.type)


def _root_type(problem, abstraction):
    root = _collapsed_type(problem, abstraction)
    while root.father is not None:
        root = root.father
    return root


def _collapsed_type(problem, abstraction):
    return problem.object(abstraction.objects[0]).type
