"""Collapse concrete objects in a Unified Planning problem."""

from unified_planning.model import InstantaneousAction, Object, Problem
from unified_planning.model.metrics import (
    MinimizeActionCosts,
    MinimizeExpressionOnFinalState,
    MinimizeSequentialPlanLength,
)

__all__ = ["AbstractionError", "collapse_objects", "validate_supported_problem"]


class AbstractionError(ValueError):
    """Raised when a requested model abstraction cannot be constructed safely."""


def validate_supported_problem(problem):
    """Reject a problem whose features the object collapse cannot copy."""
    kind = problem.kind
    checks = (
        (kind.has_time(), "temporal planning"),
        (kind.has_hierarchical(), "hierarchical planning"),
        (kind.has_contingent(), "contingent planning"),
        (kind.has_processes(), "processes"),
        (kind.has_events(), "events"),
        (kind.has_simulated_effects(), "simulated effects"),
        (kind.has_object_fluents(), "object-valued fluents"),
        (kind.has_oversubscription(), "oversubscription metrics"),
        (kind.has_temporal_oversubscription(), "temporal oversubscription metrics"),
    )
    for present, label in checks:
        if present:
            raise AbstractionError(f"Unsupported PDDL feature: {label}")
    if len(problem.quality_metrics) > 1:
        raise AbstractionError("Unsupported PDDL feature: multiple quality metrics")
    if problem.quality_metrics and not isinstance(
        problem.quality_metrics[0], (MinimizeActionCosts, MinimizeExpressionOnFinalState, MinimizeSequentialPlanLength)
    ):
        raise AbstractionError(f"Unsupported quality metric: {type(problem.quality_metrics[0]).__name__}")
    if any(not isinstance(action, InstantaneousAction) for action in problem.actions):
        raise AbstractionError("Unsupported PDDL feature: non-instantaneous actions")


def collapse_objects(problem, abstraction, relaxable_deletes):
    """Replace the abstraction's concrete objects in a fresh problem."""
    objects_to_collapse = tuple(problem.object(name) for name in abstraction.objects)
    deletes_to_relax = set(relaxable_deletes)
    collapsed_problem = Problem(
        problem.name, environment=problem.environment, initial_defaults=problem.initial_defaults
    )
    abstract_object = Object(abstraction.name, objects_to_collapse[0].type, problem.environment)
    object_substitutions = {item: abstract_object for item in objects_to_collapse}

    def rewrite(expression):
        return expression.substitute(object_substitutions).simplify()

    for fluent in problem.fluents:
        collapsed_problem.add_fluent(fluent, default_initial_value=problem.fluents_defaults.get(fluent))
    for item in problem.all_objects:
        if item not in objects_to_collapse:
            collapsed_problem.add_object(item)
    collapsed_problem.add_object(abstract_object)

    relaxed_deletes = _copy_actions(problem, collapsed_problem, rewrite, deletes_to_relax)
    _copy_initial_values(problem, collapsed_problem, rewrite)
    _copy_goals_and_constraints(problem, collapsed_problem, rewrite)
    _copy_quality_metric(problem, collapsed_problem)
    return collapsed_problem, relaxed_deletes


def _copy_actions(problem, collapsed_problem, rewrite, deletes_to_relax):
    relaxed_deletes = []
    for action in problem.actions:
        collapsed_action, action_relaxed_deletes = _copy_action(action, rewrite, deletes_to_relax)
        relaxed_deletes.extend(action_relaxed_deletes)
        # An action with no effect left changes nothing, and the writer gives it
        # no :effect, which Fast Downward's parser rejects.
        if not collapsed_action.effects:
            continue
        collapsed_problem.add_action(collapsed_action)
    return tuple(relaxed_deletes)


def _copy_action(action, rewrite, deletes_to_relax):
    collapsed_action = action.clone()
    collapsed_action.clear_preconditions()
    for precondition in action.preconditions:
        collapsed_action.add_precondition(rewrite(precondition))

    relaxed_deletes = []
    collapsed_action.clear_effects()
    for effect in action.effects:
        if (action.name, effect) in deletes_to_relax:
            relaxed_deletes.append((action.name, effect))
            continue

        fluent = rewrite(effect.fluent)
        value = rewrite(effect.value)
        condition = rewrite(effect.condition)
        if effect.is_assignment():
            collapsed_action.add_effect(fluent, value, condition, effect.forall)
        elif effect.is_increase():
            collapsed_action.add_increase_effect(fluent, value, condition, effect.forall)
        elif effect.is_decrease():
            collapsed_action.add_decrease_effect(fluent, value, condition, effect.forall)
        else:
            raise AbstractionError(f"Unsupported effect in action {action.name}: {effect}")
    return collapsed_action, relaxed_deletes


def _copy_initial_values(problem, collapsed_problem, rewrite):
    collapsed_initial_values = {}
    for fluent, value in problem.explicit_initial_values.items():
        collapsed_fluent = rewrite(fluent)
        collapsed_value = rewrite(value)
        existing_value = collapsed_initial_values.get(collapsed_fluent)
        if existing_value is not None and existing_value != collapsed_value:
            if not existing_value.type.is_bool_type() or not collapsed_value.type.is_bool_type():
                raise AbstractionError(f"Object collapse creates conflicting initial values for {collapsed_fluent}")
            # The collapsed objects disagree on a fact, so the abstract object
            # holds it: the abstract task only has to admit the concrete plans,
            # and a fact that stays true only makes more actions applicable. In
            # PNF the complement of a fluent disagrees wherever the fluent does,
            # so this is the common case, not an edge.
            collapsed_value = problem.environment.expression_manager.TRUE()
        collapsed_initial_values[collapsed_fluent] = collapsed_value
    for fluent, value in collapsed_initial_values.items():
        collapsed_problem.set_initial_value(fluent, value)


def _copy_goals_and_constraints(problem, collapsed_problem, rewrite):
    collapsed_goals = set()
    for goal in problem.goals:
        collapsed_goal = rewrite(goal)
        if collapsed_goal not in collapsed_goals:
            collapsed_problem.add_goal(collapsed_goal)
            collapsed_goals.add(collapsed_goal)
    for constraint in problem.trajectory_constraints:
        collapsed_problem.add_trajectory_constraint(rewrite(constraint))


def _copy_quality_metric(problem, collapsed_problem):
    # Only the plan length survives write_abstract_problem, which strips a cost
    # because the search asks for the shortest plan rather than the cheapest.
    if problem.quality_metrics and isinstance(problem.quality_metrics[0], MinimizeSequentialPlanLength):
        collapsed_problem.add_quality_metric(MinimizeSequentialPlanLength(environment=problem.environment))
