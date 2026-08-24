"""Symmetric-object abstraction over Unified Planning models."""

from dataclasses import dataclass

from unified_planning.model import InstantaneousAction, Object, Problem
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeSequentialPlanLength


class AbstractionError(ValueError):
    """Raised when a requested model abstraction cannot be constructed safely."""


@dataclass(frozen=True)
class RelaxedDelete:
    action: str
    predicate: str
    variable: str
    parameter_type: str


@dataclass(frozen=True)
class Abstraction:
    name: str
    objects: tuple[str, ...]
    object_type: str


@dataclass(frozen=True)
class RankedSymmetryClass:
    abstraction: Abstraction
    removed_deletes: tuple[RelaxedDelete, ...]

    @property
    def unary_delete_score(self):
        return len(self.removed_deletes)


@dataclass(frozen=True)
class AbstractProblem:
    abstraction: Abstraction
    problem: Problem
    removed_deletes: tuple[RelaxedDelete, ...]

    @property
    def unary_delete_score(self):
        return len(self.removed_deletes)


def abstract_problem(problem: Problem, objects_to_abstract, abstract_name=None):
    """Collapse same-typed objects in a fresh model and relax applicable unary deletes."""
    _validate_supported_problem(problem)
    abstraction = _prepare_abstraction(problem, objects_to_abstract, abstract_name)
    selected_objects = tuple(problem.object(name) for name in abstraction.objects)
    candidates = _applicable_deletes(problem, selected_objects[0].type, selected_objects)
    allowed_deletes = {_delete_key(item) for item in candidates}
    target, removed = _copy_problem(problem, abstraction, selected_objects, allowed_deletes)
    return AbstractProblem(abstraction=abstraction, problem=target, removed_deletes=tuple(removed))


def rank_symmetry_classes(problem: Problem, classes):
    """Rank abstractable symmetry classes by delete score, size, and names."""
    ranked = []

    for symmetry_class in classes:
        requested = tuple(sorted(str(name).casefold() for name in symmetry_class))
        abstraction = _prepare_abstraction(problem, requested, None)
        selected = tuple(problem.object(name) for name in abstraction.objects)
        removed = _applicable_deletes(problem, selected[0].type, selected)
        ranked.append(RankedSymmetryClass(abstraction=abstraction, removed_deletes=removed))

    ranked.sort(
        key=lambda item: (
            item.unary_delete_score,
            -len(item.abstraction.objects),
            tuple(name.casefold() for name in item.abstraction.objects),
        )
    )
    return tuple(ranked)


def _validate_supported_problem(problem):
    kind = problem.kind
    unsupported = []
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
    unsupported.extend(label for present, label in checks if present)
    if unsupported:
        raise AbstractionError(f"Unsupported PDDL feature: {unsupported[0]}")
    if len(problem.quality_metrics) > 1:
        raise AbstractionError("Unsupported PDDL feature: multiple quality metrics")
    if problem.quality_metrics and not isinstance(
        problem.quality_metrics[0], (MinimizeActionCosts, MinimizeSequentialPlanLength)
    ):
        raise AbstractionError(f"Unsupported quality metric: {type(problem.quality_metrics[0]).__name__}")
    if any(not isinstance(action, InstantaneousAction) for action in problem.actions):
        raise AbstractionError("Unsupported PDDL feature: non-instantaneous actions")


def _prepare_abstraction(problem, objects_to_abstract, abstract_name):
    known = {item.name.casefold(): item for item in problem.all_objects}
    requested = tuple(dict.fromkeys(str(name).casefold() for name in objects_to_abstract))
    if len(requested) < 2:
        raise AbstractionError("At least two distinct objects must be selected")

    missing = [name for name in requested if name not in known]
    if missing:
        raise AbstractionError(f"Unknown problem objects: {', '.join(missing)}")
    selected = tuple(known[name] for name in requested)
    if len({item.type for item in selected}) != 1:
        raise AbstractionError("Selected objects must have the same declared type")

    chosen_name = abstract_name or f"{selected[0].type.name}_abs"
    return Abstraction(
        name=chosen_name, objects=tuple(item.name for item in selected), object_type=selected[0].type.name
    )


def _copy_problem(source, abstraction, selected_objects, allowed_deletes):
    target = Problem(source.name, environment=source.environment, initial_defaults=source.initial_defaults)
    abstract_object = Object(abstraction.name, selected_objects[0].type, source.environment)
    substitutions = {item: abstract_object for item in selected_objects}

    for fluent in source.fluents:
        target.add_fluent(fluent, default_initial_value=source.fluents_defaults.get(fluent))
    for item in source.all_objects:
        if item not in selected_objects:
            target.add_object(item)
    target.add_object(abstract_object)

    action_map = {}
    removed = []
    for action in source.actions:
        copied = action.clone()
        copied.clear_preconditions()
        for precondition in action.preconditions:
            copied.add_precondition(_substitute(precondition, substitutions))
        copied.clear_effects()
        for effect in action.effects:
            candidate = _relaxed_delete(action, effect, selected_objects[0].type)
            if candidate is not None:
                _, relaxed_delete = candidate
                if _delete_key(relaxed_delete) in allowed_deletes:
                    removed.append(relaxed_delete)
                    continue
            fluent = _substitute(effect.fluent, substitutions)
            value = _substitute(effect.value, substitutions)
            condition = _substitute(effect.condition, substitutions)
            if effect.is_assignment():
                copied.add_effect(fluent, value, condition, effect.forall)
            elif effect.is_increase():
                copied.add_increase_effect(fluent, value, condition, effect.forall)
            elif effect.is_decrease():
                copied.add_decrease_effect(fluent, value, condition, effect.forall)
            else:
                raise AbstractionError(f"Unsupported effect in action {action.name}: {effect}")
        target.add_action(copied)
        action_map[action] = copied

    rewritten_initial_values = {}
    for fluent, value in source.explicit_initial_values.items():
        rewritten_fluent = _substitute(fluent, substitutions)
        rewritten_value = _substitute(value, substitutions)
        previous = rewritten_initial_values.get(rewritten_fluent)
        if previous is not None and previous != rewritten_value:
            if previous.type.is_bool_type() and rewritten_value.type.is_bool_type():
                raise AbstractionError("Object collapse creates contradictory initial facts")
            raise AbstractionError(f"Object collapse creates conflicting initial values for {rewritten_fluent}")
        rewritten_initial_values[rewritten_fluent] = rewritten_value
    for fluent, value in rewritten_initial_values.items():
        target.set_initial_value(fluent, value)

    seen_goals = set()
    for goal in source.goals:
        rewritten = _substitute(goal, substitutions)
        if rewritten not in seen_goals:
            target.add_goal(rewritten)
            seen_goals.add(rewritten)
    for constraint in source.trajectory_constraints:
        target.add_trajectory_constraint(_substitute(constraint, substitutions))

    if source.quality_metrics:
        metric = source.quality_metrics[0]
        if isinstance(metric, MinimizeActionCosts):
            costs = {action_map[action]: _substitute(cost, substitutions) for action, cost in metric.costs.items()}
            default = _substitute(metric.default, substitutions) if metric.default is not None else None
            target.add_quality_metric(MinimizeActionCosts(costs, default=default, environment=source.environment))
        else:
            target.add_quality_metric(MinimizeSequentialPlanLength(environment=source.environment))
    return target, removed


def _substitute(expression, substitutions):
    return expression.substitute(substitutions).simplify()


def _applicable_deletes(problem, object_type, objects_to_abstract):
    static_fluents = problem.get_static_fluents()
    positive_initial = tuple(
        fluent
        for fluent, value in problem.explicit_initial_values.items()
        if value.type.is_bool_type() and value.is_true()
    )
    result = []
    for action in problem.actions:
        for effect in action.effects:
            candidate = _relaxed_delete(action, effect, object_type)
            if candidate is not None:
                argument, relaxed_delete = candidate
                if _action_possible(action, argument, objects_to_abstract, static_fluents, positive_initial):
                    result.append(relaxed_delete)
    return tuple(result)


def _relaxed_delete(action, effect, object_type):
    if not effect.is_assignment() or not effect.value.is_false() or not effect.fluent.type.is_bool_type():
        return None
    if not effect.fluent.is_fluent_exp() or len(effect.fluent.args) != 1:
        return None
    argument = effect.fluent.arg(0)
    if argument.is_parameter_exp():
        variable = argument.parameter()
    elif argument.is_variable_exp():
        variable = argument.variable()
    else:
        return None
    if not object_type.is_subtype(variable.type):
        return None
    relaxed_delete = RelaxedDelete(
        action=action.name,
        predicate=effect.fluent.fluent().name,
        variable=f"?{variable.name}",
        parameter_type=variable.type.name,
    )
    return argument, relaxed_delete


def _delete_key(relaxed_delete):
    return (relaxed_delete.action.casefold(), relaxed_delete.predicate.casefold(), relaxed_delete.variable.casefold())


def _action_possible(action, variable, objects_to_abstract, static_fluents, positive_initial):
    atoms = [
        atom
        for precondition in action.preconditions
        for atom in _static_variable_preconditions(precondition, variable, static_fluents)
    ]
    return not atoms or any(
        all(any(_matches_static_fact(atom, fact, variable, item) for fact in positive_initial) for atom in atoms)
        for item in objects_to_abstract
    )


def _static_variable_preconditions(expression, variable, static_fluents):
    if expression.is_and():
        return [
            atom
            for child in expression.args
            for atom in _static_variable_preconditions(child, variable, static_fluents)
        ]
    if expression.is_fluent_exp() and expression.fluent() in static_fluents and variable in expression.args:
        return [expression]
    return []


def _matches_static_fact(atom, fact, variable, object_value):
    if not fact.is_fluent_exp() or atom.fluent() != fact.fluent() or len(atom.args) != len(fact.args):
        return False
    for expected, actual in zip(atom.args, fact.args):
        if expected.is_parameter_exp() or expected.is_variable_exp():
            if expected == variable and (not actual.is_object_exp() or actual.object() != object_value):
                return False
        elif expected != actual:
            return False
    return True
