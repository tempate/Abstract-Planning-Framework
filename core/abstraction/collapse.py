"""Collapse concrete objects in a Unified Planning problem."""

from unified_planning.model import InstantaneousAction, Object, Problem
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeSequentialPlanLength

from core.abstraction.relaxation import match_relaxable_delete

__all__ = ["AbstractionError", "collapse_objects"]


class AbstractionError(ValueError):
    """Raised when a requested model abstraction cannot be constructed safely."""


def collapse_objects(problem, abstraction, relaxable_deletes):
    """Replace the abstraction's concrete objects in a fresh problem."""
    _validate_supported_problem(problem)
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

    collapsed_actions, relaxed_deletes = _copy_actions(
        problem, collapsed_problem, rewrite, objects_to_collapse[0].type, deletes_to_relax
    )
    _copy_initial_values(problem, collapsed_problem, rewrite)
    _copy_goals_and_constraints(problem, collapsed_problem, rewrite)
    _copy_quality_metric(problem, collapsed_problem, collapsed_actions, rewrite)
    return collapsed_problem, relaxed_deletes


def _validate_supported_problem(problem):
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
        problem.quality_metrics[0], (MinimizeActionCosts, MinimizeSequentialPlanLength)
    ):
        raise AbstractionError(f"Unsupported quality metric: {type(problem.quality_metrics[0]).__name__}")
    if any(not isinstance(action, InstantaneousAction) for action in problem.actions):
        raise AbstractionError("Unsupported PDDL feature: non-instantaneous actions")


def _copy_actions(problem, collapsed_problem, rewrite, collapsed_type, deletes_to_relax):
    collapsed_actions = {}
    relaxed_deletes = []
    for action in problem.actions:
        collapsed_action, action_relaxed_deletes = _copy_action(action, rewrite, collapsed_type, deletes_to_relax)
        collapsed_problem.add_action(collapsed_action)
        collapsed_actions[action] = collapsed_action
        relaxed_deletes.extend(action_relaxed_deletes)
    return collapsed_actions, tuple(relaxed_deletes)


def _copy_action(action, rewrite, collapsed_type, deletes_to_relax):
    collapsed_action = action.clone()
    collapsed_action.clear_preconditions()
    for precondition in action.preconditions:
        collapsed_action.add_precondition(rewrite(precondition))

    relaxed_deletes = []
    collapsed_action.clear_effects()
    for effect in action.effects:
        match = match_relaxable_delete(action, effect, collapsed_type)
        if match is not None:
            _, relaxable_delete = match
            if relaxable_delete in deletes_to_relax:
                relaxed_deletes.append(relaxable_delete)
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
            if existing_value.type.is_bool_type() and collapsed_value.type.is_bool_type():
                raise AbstractionError("Object collapse creates contradictory initial facts")
            raise AbstractionError(f"Object collapse creates conflicting initial values for {collapsed_fluent}")
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


def _copy_quality_metric(problem, collapsed_problem, collapsed_actions, rewrite):
    if not problem.quality_metrics:
        return
    metric = problem.quality_metrics[0]
    if isinstance(metric, MinimizeActionCosts):
        action_costs = {collapsed_actions[action]: rewrite(cost) for action, cost in metric.costs.items()}
        default_cost = rewrite(metric.default) if metric.default is not None else None
        collapsed_problem.add_quality_metric(
            MinimizeActionCosts(action_costs, default=default_cost, environment=problem.environment)
        )
    else:
        collapsed_problem.add_quality_metric(MinimizeSequentialPlanLength(environment=problem.environment))
