"""Find what the collapse would falsify, so that it can be relaxed instead."""


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
    if not _is_delete(effect):
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


def _is_delete(effect):
    return (
        effect.is_assignment()
        and effect.value.is_false()
        and effect.fluent.type.is_bool_type()
        and effect.fluent.is_fluent_exp()
    )


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
    relaxed_problem = problem.clone()

    relaxed = []
    for action in relaxed_problem.actions:
        kept = []
        for precondition in action.preconditions:
            condition = _without_inequalities(action, precondition, collapsed, collapsed_type, relaxed)
            if condition is not None:
                kept.append(condition)
        action.clear_preconditions()
        for condition in kept:
            action.add_precondition(condition)

    return relaxed_problem, tuple(relaxed)


def _without_inequalities(action, condition, collapsed, collapsed_type, relaxed):
    """Drop the relaxable inequalities from a condition, or None if nothing is left.

    The reader hands over a whole conjunction as one precondition, so the
    inequality usually sits inside an and rather than beside it.
    """
    if condition.is_not() and condition.arg(0).is_equals():
        if all(_can_be_collapsed(side, collapsed, collapsed_type) for side in condition.arg(0).args):
            relaxed.append((action.name, condition))
            return None
    if not condition.is_and():
        return condition

    kept = []
    for argument in condition.args:
        kept_argument = _without_inequalities(action, argument, collapsed, collapsed_type, relaxed)
        if kept_argument is not None:
            kept.append(kept_argument)
    if not kept:
        return None
    if len(kept) == 1:
        return kept[0]
    return condition.environment.expression_manager.And(kept)


def _can_be_collapsed(expression, collapsed, collapsed_type):
    if expression.is_object_exp():
        return expression.object() in collapsed
    return _is_variable_of(expression, collapsed_type)


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
