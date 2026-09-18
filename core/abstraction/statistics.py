"""Describe one symmetry class: what it looks like and what relaxing it costs.

Every number here is a property of the class rather than of the search, so a run
that later times out still carries its whole description.
"""

from collections import Counter

from core.abstraction.relaxation import _collapsible_name, match_relaxable_delete

# Two objects of one class are alike when their atoms agree after both are
# blanked out. Blanking the focal object apart from the rest keeps a fact about
# the object itself distinct from a fact about one of its peers.
_FOCUS = "\0focus"
_PEER = "\0peer"


def describe_class(problem, abstraction):
    """Describe the class on the problem as read.

    The inequalities are counted here rather than beside the deletes because
    ``relax_inequalities`` has dropped them from every later problem.
    """
    objects_to_collapse = tuple(problem.object(name) for name in abstraction.objects)
    initial_atoms = _positive_initial_atoms(problem)
    collapsed_type = objects_to_collapse[0].type

    return {
        "counters": {
            "problem_object_count": len(problem.all_objects),
            "init_predicates_on_class": len(_predicates_on(initial_atoms, objects_to_collapse)),
            "actions_binding_class": sum(
                1
                for action in problem.actions
                if any(collapsed_type.is_subtype(parameter.type) for parameter in action.parameters)
            ),
            "class_inequalities": _count_class_inequalities(problem, objects_to_collapse),
        },
        "ratios": {
            "shared_initial_state": _shared_fraction(initial_atoms, objects_to_collapse),
            "shared_goal": _shared_fraction(_goal_atoms(problem), objects_to_collapse),
        },
    }


def describe_relaxation(problem, abstraction, relaxed_deletes):
    """Count the relaxed deletes and the deletes they were chosen from, as counters.

    Takes the problem the collapse read, so the class objects are still there
    and the deletes are the ones the relaxation decided over.
    """
    objects_to_collapse = tuple(problem.object(name) for name in abstraction.objects)
    return {
        "unary_relaxed_deletes": sum(1 for delete in relaxed_deletes if _is_unary(problem, delete)),
        "class_deletes": _count_class_deletes(problem, objects_to_collapse),
    }


def _shared_fraction(atoms, objects_to_collapse):
    """Report the share of the class that agrees on these atoms.

    Objects no atom mentions all carry the empty signature, so a class absent
    from the goal reads as one.
    """
    signatures = Counter(_signature(atoms, item, objects_to_collapse) for item in objects_to_collapse)
    return max(signatures.values()) / len(objects_to_collapse)


def _signature(atoms, focus, objects_to_collapse):
    signature = set()
    for atom in atoms:
        arguments = tuple(_blank(argument, focus, objects_to_collapse) for argument in atom.args)
        if _FOCUS in arguments:
            signature.add((atom.fluent().name, arguments))
    return frozenset(signature)


def _blank(argument, focus, objects_to_collapse):
    if not argument.is_object_exp():
        return str(argument)
    item = argument.object()
    if item == focus:
        return _FOCUS
    if item in objects_to_collapse:
        return _PEER
    return item.name


def _predicates_on(atoms, objects_to_collapse):
    collapsed = set(objects_to_collapse)
    return {
        atom.fluent().name
        for atom in atoms
        if any(argument.is_object_exp() and argument.object() in collapsed for argument in atom.args)
    }


def _is_unary(problem, relaxed_delete):
    """Tell whether a relaxed delete removed a fact about one object alone."""
    return len(problem.fluent(relaxed_delete.predicate).signature) == 1


def _count_class_deletes(problem, objects_to_collapse):
    """Count every delete that touches the class, relaxed or not.

    The matcher is the one the relaxation itself uses, so the difference between
    this and the relaxed deletes is what the static preconditions preserved.
    """
    return sum(
        1
        for action in problem.actions
        for effect in action.effects
        if match_relaxable_delete(action, effect, objects_to_collapse) is not None
    )


def _count_class_inequalities(problem, objects_to_collapse):
    """Count the inequalities with a side the collapse could reach.

    Relaxing one needs both sides collapsible, so this is the wider set.
    """
    collapsed_type = objects_to_collapse[0].type
    return sum(
        1
        for action in problem.actions
        for precondition in action.preconditions
        for inequality in _inequalities(precondition)
        if any(
            _collapsible_name(side, collapsed_type, objects_to_collapse) is not None for side in inequality.arg(0).args
        )
    )


def _inequalities(condition):
    """Walk a precondition for negated equalities, which usually sit inside an and."""
    if condition.is_not() and condition.arg(0).is_equals():
        yield condition
    elif condition.is_and():
        for argument in condition.args:
            yield from _inequalities(argument)


def _positive_initial_atoms(problem):
    return tuple(
        fluent
        for fluent, value in problem.explicit_initial_values.items()
        if value.type.is_bool_type() and value.is_true()
    )


def _goal_atoms(problem):
    atoms = []
    pending = list(problem.goals)
    while pending:
        goal = pending.pop()
        if goal.is_and():
            pending.extend(goal.args)
        elif goal.is_fluent_exp():
            atoms.append(goal)
    return tuple(atoms)
