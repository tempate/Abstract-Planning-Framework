"""Score candidate abstractions to pick the one that costs the least precision."""


def abstraction_score(problem, abstraction, relaxable_deletes):
    """Score one candidate abstraction, lowest first.

    Collapsing objects the goal mentions merges goal conjuncts, which costs far
    more abstract-horizon slack than relaxing an extra delete does, so goal
    conjuncts outrank deletes. Larger classes break the remaining ties.
    """
    return (_count_collapsed_goal_conjuncts(problem, abstraction), len(relaxable_deletes), -len(abstraction.objects))


def _count_collapsed_goal_conjuncts(problem, abstraction):
    """Count the goal conjuncts that mention one of the collapsed objects."""
    collapsed_names = {name.casefold() for name in abstraction.objects}

    collapsed_conjuncts = 0
    for goal in problem.goals:
        for conjunct in _goal_conjuncts(goal):
            if _mentions_collapsed_object(conjunct, collapsed_names):
                collapsed_conjuncts += 1
    return collapsed_conjuncts


def _goal_conjuncts(goal):
    """Flatten a goal into its top-level conjuncts."""
    if not goal.is_and():
        return [goal]

    conjuncts = []
    for arg in goal.args:
        conjuncts.extend(_goal_conjuncts(arg))
    return conjuncts


def _mentions_collapsed_object(expression, collapsed_names):
    """Check whether an expression refers to one of the collapsed objects."""
    pending_expressions = [expression]
    while pending_expressions:
        current_expression = pending_expressions.pop()
        if current_expression.is_object_exp() and current_expression.object().name.casefold() in collapsed_names:
            return True
        pending_expressions.extend(current_expression.args)
    return False
