"""Find what the collapse would falsify, so that it can be relaxed instead."""


def action_inequalities(problem):
    """Each action's inequalities, by action name, before any is relaxed or compiled away."""
    return {action.name: _inequalities(action) for action in problem.actions}


def find_relaxable_deletes(problem, abstraction, inequalities):
    """Find the deletes that could remove a fact other collapsed objects still hold.

    A grounding has to satisfy the action's original inequalities too, which the
    translation to positive normal form has rewritten by now, so they come from
    action_inequalities. Returns the deletes as (action name, effect) pairs.
    """
    collapsed = _collapsed_objects(problem, abstraction)
    collapsed_type = _collapsed_type(problem, abstraction)
    static_facts = _static_facts(problem)

    relaxable = []
    for action in problem.actions:
        action_inequalities = inequalities.get(action.name, ())
        for effect in action.effects:
            if _deletes_a_collapsed_fact(
                problem, action, effect, collapsed, collapsed_type, static_facts, action_inequalities
            ):
                relaxable.append((action.name, effect))
    return tuple(relaxable)


def _deletes_a_collapsed_fact(problem, action, effect, collapsed, collapsed_type, static_facts, inequalities):
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

    # A single argument that some grounding binds to a collapsed object is enough
    # to make the delete remove a fact the other collapsed objects may still support.
    for argument in effect.fluent.args:
        if not _is_variable_of(argument, collapsed_type):
            continue
        if not argument.is_parameter_exp():
            # A variable of a quantified effect, which no precondition binds.
            return True
        restricted = {argument.parameter(): collapsed}
        if _grounding_exists(problem, action, static_facts, inequalities, restricted):
            return True
    return False


def _grounding_exists(problem, action, static_facts, inequalities, restricted):
    """Whether a grounding meets the static preconditions and the inequalities, with restricted parameters in their sets."""
    atoms = [
        atom for atom in _conjuncts(action.preconditions) if atom.is_fluent_exp() and atom.fluent() in static_facts
    ]
    if not all(_holds(atom, {}, static_facts) for atom in atoms if not _parameters(atom.args)):
        return False
    if any(left == right for left, right in inequalities if not _parameters((left, right))):
        return False

    # Only the parameters something constrains need a value. Every other one
    # can take any object of its type.
    constrained = set(restricted)
    for atom in atoms:
        constrained |= _parameters(atom.args)
    for pair in inequalities:
        constrained |= _parameters(pair)

    domains = {}
    for parameter in constrained:
        objects = set(problem.objects(parameter.type))
        domains[parameter] = objects & restricted[parameter] if parameter in restricted else objects

    def extend(binding):
        unbound = [parameter for parameter in domains if parameter not in binding]
        if not unbound:
            return True

        # Bind the parameter with the fewest values left first, so that a dead
        # end shows up before the search branches on it.
        options = {
            parameter: _options(parameter, binding, domains, atoms, inequalities, static_facts) for parameter in unbound
        }
        parameter = min(unbound, key=lambda unbound_parameter: len(options[unbound_parameter]))
        return any(extend({**binding, parameter: value}) for value in options[parameter])

    return extend({})


def _options(parameter, binding, domains, atoms, inequalities, static_facts):
    """The values the parameter can take next to the binding without breaking a static precondition or an inequality."""
    options = set(domains[parameter])
    for atom in atoms:
        if parameter in _parameters(atom.args):
            options &= _values_in_facts(atom, parameter, binding, static_facts[atom.fluent()])

    for left, right in inequalities:
        for side, other in ((left, right), (right, left)):
            other_value = _value(other, binding)
            if side.is_parameter_exp() and side.parameter() == parameter and other_value is not None:
                options.discard(other_value)
    return options


def _values_in_facts(atom, parameter, binding, facts):
    """The objects that, bound to the parameter, make the atom one of the facts."""
    values = set()
    for fact in facts:
        value = None
        matches = True
        for expected, actual in zip(atom.args, fact.args):
            if expected.is_parameter_exp() and expected.parameter() == parameter:
                matches = value is None or value == actual.object()
                value = actual.object()
            elif expected.is_object_exp() or (expected.is_parameter_exp() and expected.parameter() in binding):
                matches = _value(expected, binding) == actual.object()
            if not matches:
                break
        if matches:
            values.add(value)
    return values


def _holds(atom, binding, static_facts):
    values = tuple(_value(argument, binding) for argument in atom.args)
    return any(tuple(argument.object() for argument in fact.args) == values for fact in static_facts[atom.fluent()])


def _value(expression, binding):
    """The object the expression stands for under the binding, or None while it is unbound."""
    if expression.is_object_exp():
        return expression.object()
    if expression.is_parameter_exp():
        return binding.get(expression.parameter())
    return None


def _parameters(expressions):
    return {expression.parameter() for expression in expressions if expression.is_parameter_exp()}


def _static_facts(problem):
    """The true facts of every static fluent, by fluent."""
    static_facts = {fluent: [] for fluent in problem.get_static_fluents()}
    for fact, value in problem.explicit_initial_values.items():
        if value.is_true() and fact.is_fluent_exp() and fact.fluent() in static_facts:
            static_facts[fact.fluent()].append(fact)
    return static_facts


def _inequalities(action):
    return [
        tuple(condition.arg(0).args)
        for condition in _conjuncts(action.preconditions)
        if condition.is_not() and condition.arg(0).is_equals()
    ]


def _conjuncts(conditions):
    pending = list(conditions)
    while pending:
        condition = pending.pop()
        if condition.is_and():
            pending.extend(condition.args)
        else:
            yield condition


def relax_inequalities(problem, abstraction):
    """Drop the inequalities the collapse would make false.

    Collapsing two objects into one symbol makes (not (= ?x ?y)) false wherever
    some grounding binds both sides to collapsed objects, which loses every
    ground action the concrete task reaches through them. Dropping the condition
    keeps those actions, in the same sense that relaxing a delete keeps a fact
    the concrete task removes. Returns the relaxed problem and the (action name,
    inequality) pairs it dropped.
    """
    collapsed = _collapsed_objects(problem, abstraction)
    collapsed_type = _collapsed_type(problem, abstraction)
    static_facts = _static_facts(problem)
    relaxed_problem = problem.clone()

    relaxed = []
    for action in relaxed_problem.actions:
        inequalities = _inequalities(action)

        def collapses_both_sides(inequality):
            return _collapses_both_sides(
                relaxed_problem, action, inequality, collapsed, collapsed_type, static_facts, inequalities
            )

        kept = []
        for precondition in action.preconditions:
            condition = _without_inequalities(action, precondition, collapses_both_sides, relaxed)
            if condition is not None:
                kept.append(condition)
        action.clear_preconditions()
        for condition in kept:
            action.add_precondition(condition)

    return relaxed_problem, tuple(relaxed)


def _collapses_both_sides(problem, action, inequality, collapsed, collapsed_type, static_facts, inequalities):
    """Whether some grounding binds both sides of the inequality to collapsed objects."""
    restricted = {}
    for side in inequality.args:
        if side.is_object_exp():
            if side.object() not in collapsed:
                return False
        elif not _is_variable_of(side, collapsed_type):
            return False
        elif side.is_parameter_exp():
            restricted[side.parameter()] = collapsed
    return _grounding_exists(problem, action, static_facts, inequalities, restricted)


def _without_inequalities(action, condition, collapses_both_sides, relaxed):
    """Drop the relaxable inequalities from a condition, or None if nothing is left.

    The reader hands over a whole conjunction as one precondition, so the
    inequality usually sits inside an and rather than beside it.
    """
    if condition.is_not() and condition.arg(0).is_equals():
        if collapses_both_sides(condition.arg(0)):
            relaxed.append((action.name, condition))
            return None
    if not condition.is_and():
        return condition

    kept = []
    for argument in condition.args:
        kept_argument = _without_inequalities(action, argument, collapses_both_sides, relaxed)
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
