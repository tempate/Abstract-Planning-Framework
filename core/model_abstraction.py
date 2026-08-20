"""Symmetric-object abstraction over Unified Planning models."""

import re
from dataclasses import dataclass

from unified_planning.model import InstantaneousAction, Object, Problem
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeSequentialPlanLength

_PDDL_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")


class AbstractionError(ValueError):
    """Raised when a requested model abstraction cannot be constructed safely."""


@dataclass(frozen=True)
class RelaxedDelete:
    action: str
    predicate: str
    variable: str
    parameter_type: str


@dataclass(frozen=True)
class RankedSymmetryClass:
    objects: tuple[str, ...]
    object_type: str
    removed_deletes: tuple[RelaxedDelete, ...]

    @property
    def unary_delete_score(self):
        return len(self.removed_deletes)


@dataclass(frozen=True)
class AbstractionResult:
    problem: Problem
    objects: tuple[str, ...]
    object_type: str
    abstract_name: str
    removed_deletes: tuple[RelaxedDelete, ...]

    @property
    def unary_delete_score(self):
        return len(self.removed_deletes)


@dataclass(frozen=True)
class _Selection:
    objects: tuple[Object, ...]
    abstract_object: Object

    @property
    def object_type(self):
        return self.objects[0].type

    @property
    def substitutions(self):
        return {item: self.abstract_object for item in self.objects}


@dataclass(frozen=True)
class _DeleteCandidate:
    action: InstantaneousAction
    fluent: object
    argument: object
    metadata: RelaxedDelete

    @property
    def key(self):
        return self.action.name.casefold(), self.fluent.name.casefold(), self.metadata.variable.casefold()


def abstract_problem(problem: Problem, objects, abstract_name=None):
    """Collapse same-typed objects in a fresh model and relax applicable unary deletes."""
    _validate_supported_problem(problem)
    selection = _prepare_selection(problem, objects, abstract_name)
    candidates = _applicable_deletes(problem, selection.object_type, selection.objects)
    allowed_deletes = {item.key for item in candidates}
    target, removed = _copy_problem(problem, selection, allowed_deletes)
    return AbstractionResult(
        problem=target,
        objects=tuple(item.name for item in selection.objects),
        object_type=selection.object_type.name,
        abstract_name=selection.abstract_object.name,
        removed_deletes=tuple(removed),
    )


def rank_symmetry_classes(problem: Problem, classes):
    """Rank abstractable symmetry classes by delete score, size, and names."""
    _validate_supported_problem(problem)
    known = {item.name.casefold(): item for item in problem.all_objects}
    constants = {item.name.casefold() for item in _domain_constants(problem)}
    ranked = []
    seen_classes = set()

    for symmetry_class in classes:
        requested = tuple(sorted(dict.fromkeys(str(name).casefold() for name in symmetry_class)))
        class_key = frozenset(requested)
        if len(class_key) < 2 or class_key in seen_classes:
            continue
        seen_classes.add(class_key)

        unknown = class_key - known.keys()
        if unknown:
            raise AbstractionError(f"PDDL Symmetries returned unknown object {sorted(unknown)[0]!r}")
        if class_key & constants:
            continue

        selected = tuple(known[name] for name in requested)
        if len({item.type for item in selected}) != 1:
            raise AbstractionError("A symmetry class contains objects of different types")
        removed = _applicable_deletes(problem, selected[0].type, selected)
        ranked.append(
            RankedSymmetryClass(
                objects=tuple(item.name for item in selected),
                object_type=selected[0].type.name,
                removed_deletes=tuple(item.metadata for item in removed),
            )
        )

    ranked.sort(
        key=lambda item: (item.unary_delete_score, -len(item.objects), tuple(name.casefold() for name in item.objects))
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


def _prepare_selection(problem, objects, abstract_name):
    known = {item.name.casefold(): item for item in problem.all_objects}
    requested = tuple(dict.fromkeys(str(name).casefold() for name in objects))
    if len(requested) < 2:
        raise AbstractionError("At least two distinct objects must be selected")

    missing = [name for name in requested if name not in known]
    if missing:
        raise AbstractionError(f"Unknown problem objects: {', '.join(missing)}")
    constants = {item.name.casefold() for item in _domain_constants(problem)}
    selected_constants = set(requested) & constants
    if selected_constants:
        raise AbstractionError(f"Cannot collapse domain constant: {sorted(selected_constants)[0]}")

    selected = tuple(known[name] for name in requested)
    if len({item.type for item in selected}) != 1:
        raise AbstractionError("Selected objects must have the same declared type")

    chosen_name = abstract_name or f"{selected[0].type.name}_abs"
    if _PDDL_NAME.fullmatch(chosen_name) is None:
        raise AbstractionError(f"Invalid PDDL object name: {chosen_name!r}")
    normalized_name = chosen_name.casefold()
    if normalized_name in constants:
        raise AbstractionError(f"Abstract object name is a domain constant: {chosen_name}")
    if normalized_name in known and normalized_name not in requested:
        raise AbstractionError(f"Abstract object name already exists: {chosen_name}")

    return _Selection(objects=selected, abstract_object=Object(chosen_name, selected[0].type, problem.environment))


def _copy_problem(source, selection, allowed_deletes):
    target = Problem(source.name, environment=source.environment, initial_defaults=source.initial_defaults)
    substitutions = selection.substitutions

    for fluent in source.fluents:
        target.add_fluent(fluent, default_initial_value=source.fluents_defaults.get(fluent))
    for item in source.all_objects:
        if item not in selection.objects:
            target.add_object(item)
    target.add_object(selection.abstract_object)

    action_map = {}
    removed = []
    for action in source.actions:
        copied = action.clone()
        copied.clear_preconditions()
        for precondition in action.preconditions:
            copied.add_precondition(_substitute(precondition, substitutions))
        copied.clear_effects()
        for effect in action.effects:
            candidate = _delete_candidate(action, effect, selection.object_type)
            if candidate is not None and candidate.key in allowed_deletes:
                removed.append(candidate.metadata)
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
    if _creates_false_inequality(expression, substitutions):
        raise AbstractionError("Object collapse creates a false '(not (= object object))' constraint")
    return expression.substitute(substitutions).simplify()


def _creates_false_inequality(expression, substitutions):
    if expression.is_not() and expression.arg(0).is_equals():
        equality = expression.arg(0)
        before = equality.arg(0) == equality.arg(1)
        rewritten = equality.substitute(substitutions)
        if not before and rewritten.arg(0) == rewritten.arg(1):
            return True
    return any(_creates_false_inequality(argument, substitutions) for argument in expression.args)


def _domain_constants(problem):
    constants = set()
    for action in problem.actions:
        expressions = [*action.preconditions]
        for effect in action.effects:
            expressions.extend((effect.fluent, effect.value, effect.condition))
        for expression in expressions:
            constants.update(_objects_in(expression))
    return constants


def _objects_in(expression):
    if expression.is_object_exp():
        return {expression.object()}
    result = set()
    for argument in expression.args:
        result.update(_objects_in(argument))
    return result


def _applicable_deletes(problem, object_type, objects):
    static_fluents = _static_fluents(problem)
    positive_initial = tuple(
        fluent
        for fluent, value in problem.explicit_initial_values.items()
        if value.type.is_bool_type() and value.is_true()
    )
    result = []
    for action in problem.actions:
        for effect in action.effects:
            candidate = _delete_candidate(action, effect, object_type)
            if candidate is not None and _action_possible(
                action, candidate.argument, objects, static_fluents, positive_initial
            ):
                result.append(candidate)
    return tuple(result)


def _delete_candidate(action, effect, object_type):
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
    if not _is_subtype(object_type, variable.type):
        return None
    metadata = RelaxedDelete(
        action=action.name,
        predicate=effect.fluent.fluent().name,
        variable=f"?{variable.name}",
        parameter_type=variable.type.name,
    )
    return _DeleteCandidate(action, effect.fluent.fluent(), argument, metadata)


def _is_subtype(child, parent):
    current = child
    while current is not None:
        if current == parent:
            return True
        current = current.father if current.is_user_type() else None
    return False


def _static_fluents(problem):
    changed = {effect.fluent.fluent() for action in problem.actions for effect in action.effects}
    return {fluent for fluent in problem.fluents if fluent not in changed}


def _action_possible(action, variable, objects, static_fluents, positive_initial):
    atoms = [
        atom
        for precondition in action.preconditions
        for atom in _static_variable_preconditions(precondition, variable, static_fluents)
    ]
    return not atoms or any(
        all(any(_matches_static_fact(atom, fact, variable, item) for fact in positive_initial) for atom in atoms)
        for item in objects
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
