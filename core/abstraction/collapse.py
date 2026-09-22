"""Collapse concrete objects in a Unified Planning problem."""

import itertools
from dataclasses import dataclass

from unified_planning.model import Fluent, InstantaneousAction, Object, Problem
from unified_planning.model.metrics import (
    MinimizeActionCosts,
    MinimizeExpressionOnFinalState,
    MinimizeSequentialPlanLength,
)

from core.abstraction.relaxation import match_relaxable_delete

__all__ = ["AbstractionError", "RELAXED_VARIANT_SEPARATOR", "collapse_objects", "validate_supported_problem"]

# A relaxed variant keeps the action name it came from, so the refinement can
# still recognise it, and carries the separator to mark what it is.
RELAXED_VARIANT_SEPARATOR = "--relaxed-"

# Each collapsible parameter doubles the variants. Past this the schema-level
# drop is cheaper than the precision it buys.
MAX_COLLAPSIBLE_PARAMETERS = 3


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

    markers = _add_markers(collapsed_problem, abstraction.name, abstract_object, objects_to_collapse[0].type)

    relaxed_deletes = _copy_actions(problem, collapsed_problem, rewrite, objects_to_collapse, deletes_to_relax, markers)
    _copy_initial_values(problem, collapsed_problem, rewrite)
    _copy_goals_and_constraints(problem, collapsed_problem, rewrite)
    _copy_quality_metric(problem, collapsed_problem)
    return collapsed_problem, relaxed_deletes


@dataclass(frozen=True)
class _Markers:
    """Static fluents telling the abstract object apart from the rest."""

    abstract: Fluent
    plain: Fluent


def _add_markers(collapsed_problem, abstract_name, abstract_object, collapsed_type):
    """Mark which objects of the collapsed type stand for several concrete ones."""
    environment = collapsed_problem.environment
    boolean = environment.type_manager.BoolType()
    markers = _Markers(
        abstract=Fluent(f"{abstract_name}-is-abstract", boolean, environment=environment, x=collapsed_type),
        plain=Fluent(f"{abstract_name}-is-plain", boolean, environment=environment, x=collapsed_type),
    )
    collapsed_problem.add_fluent(markers.abstract, default_initial_value=False)
    collapsed_problem.add_fluent(markers.plain, default_initial_value=False)
    collapsed_problem.set_initial_value(markers.abstract(abstract_object), True)
    for item in collapsed_problem.all_objects:
        if item != abstract_object and (item.type == collapsed_type or item.type.is_subtype(collapsed_type)):
            collapsed_problem.set_initial_value(markers.plain(item), True)
    return markers


def _copy_actions(problem, collapsed_problem, rewrite, objects_to_collapse, deletes_to_relax, markers):
    relaxed_deletes = []
    for action in problem.actions:
        variants, action_relaxed_deletes = _action_variants(
            action, rewrite, objects_to_collapse, deletes_to_relax, markers
        )
        relaxed_deletes.extend(action_relaxed_deletes)
        for variant in variants:
            # An action with no effect left changes nothing, and the writer gives
            # it no :effect, which Fast Downward's parser rejects.
            if not variant.effects:
                continue
            collapsed_problem.add_action(variant)
    return tuple(relaxed_deletes)


def _action_variants(action, rewrite, objects_to_collapse, deletes_to_relax, markers):
    """Split an action so a delete survives the groundings that do not collapse.

    Dropping a relaxable delete from the schema drops it for every grounding,
    including the ones whose atom mentions no collapsed object. Splitting the
    action on whether its collapsible parameters take the abstract object keeps
    the delete exactly where the concrete task still needs it.
    """
    if RELAXED_VARIANT_SEPARATOR in action.name:
        raise AbstractionError(f"Action name already holds the variant separator: {action.name}")

    matches = []
    for effect in action.effects:
        match = match_relaxable_delete(action, effect, objects_to_collapse)
        if match is None:
            continue
        parameters, relaxable_delete = match
        if relaxable_delete not in deletes_to_relax:
            continue
        # A delete naming a collapsed object outright mentions one in every
        # grounding, whatever its parameters take.
        always = any(not variable.startswith("?") for variable in relaxable_delete.variables)
        matches.append((effect, () if always else parameters, relaxable_delete, always))

    if not matches:
        return [_variant(action, rewrite, set(), ())], []

    collapsible = []
    for _, parameters, _, _ in matches:
        for parameter in parameters:
            if parameter not in collapsible:
                collapsible.append(parameter)

    relaxed_deletes = [relaxable_delete for _, _, relaxable_delete, _ in matches]

    # With no collapsible parameter every grounding mentions a collapsed object
    # outright, so the schema-level drop is already exact.
    if not collapsible or len(collapsible) > MAX_COLLAPSIBLE_PARAMETERS:
        return [_variant(action, rewrite, {id(effect) for effect, _, _, _ in matches}, ())], relaxed_deletes

    variants = []
    for index, assignment in enumerate(itertools.product((False, True), repeat=len(collapsible))):
        abstract_parameters = {id(parameter) for parameter, is_abstract in zip(collapsible, assignment) if is_abstract}
        dropped = {
            id(effect)
            for effect, parameters, _, always in matches
            if always or any(id(parameter) in abstract_parameters for parameter in parameters)
        }
        conditions = tuple(
            (markers.abstract if is_abstract else markers.plain)(parameter)
            for parameter, is_abstract in zip(collapsible, assignment)
        )
        name = action.name if not any(assignment) else f"{action.name}{RELAXED_VARIANT_SEPARATOR}{index}"
        variants.append(_variant(action, rewrite, dropped, conditions, name))
    return variants, relaxed_deletes


def _variant(action, rewrite, dropped_effects, conditions, name=None):
    variant = action.clone()
    if name is not None and name != action.name:
        variant._name = name
    variant.clear_preconditions()
    for precondition in action.preconditions:
        variant.add_precondition(rewrite(precondition))
    for condition in conditions:
        variant.add_precondition(condition)

    variant.clear_effects()
    for effect in action.effects:
        if id(effect) in dropped_effects:
            continue
        fluent = rewrite(effect.fluent)
        value = rewrite(effect.value)
        condition = rewrite(effect.condition)
        if effect.is_assignment():
            variant.add_effect(fluent, value, condition, effect.forall)
        elif effect.is_increase():
            variant.add_increase_effect(fluent, value, condition, effect.forall)
        elif effect.is_decrease():
            variant.add_decrease_effect(fluent, value, condition, effect.forall)
        else:
            raise AbstractionError(f"Unsupported effect in action {action.name}: {effect}")
    return variant


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
            # and a fact that stays true only makes more actions applicable.
            # In PNF the complement of a fluent disagrees
            # wherever the fluent does, so this is the common case, not an edge.
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
