"""Build planning abstractions from PDDL Symmetries classes."""

from dataclasses import dataclass

from unified_planning.model import Problem

from core.abstraction.collapse import AbstractionError, collapse_objects
from core.abstraction.relaxation import find_relaxable_deletes
from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import read_problem
from core.metrics import PlanningMetrics
from core.outcomes import NoSymmetriesError
from core.planning.config import AbstractPlanningConfig

__all__ = ["Abstraction", "AbstractionError", "AbstractionResult", "NoSymmetriesError", "build_abstract_problem"]


@dataclass(frozen=True)
class Abstraction:
    name: str
    objects: tuple[str, ...]
    object_type: str


@dataclass(frozen=True)
class AbstractionResult:
    abstractions: tuple[Abstraction, ...]
    problem: Problem
    relaxed_deletes: tuple


def build_abstract_problem(config: AbstractPlanningConfig, metrics: PlanningMetrics | None = None):
    """Read one concrete task, find its symmetric object classes, and abstract it."""
    metrics = metrics or PlanningMetrics()
    with metrics.measure("problem_reading"):
        problem = read_problem(config.domain_path, config.problem_path)

    with metrics.measure("symmetry_discovery"):
        symmetry_classes = find_symmetric_object_sets(
            config.domain_path, config.problem_path, config.symmetry_time_limit
        )
    if not symmetry_classes:
        raise NoSymmetriesError("PDDL Symmetries found no abstractable object classes")

    with metrics.measure("abstraction"):
        abstractions, relaxable_deletes = _build_abstractions(problem, symmetry_classes)
        collapsed_problem, relaxed_deletes = collapse_objects(problem, abstractions, relaxable_deletes)
    return AbstractionResult(abstractions=abstractions, problem=collapsed_problem, relaxed_deletes=relaxed_deletes)


def _build_abstractions(problem, symmetry_classes):
    """Collapse every class PDDL Symmetries reported, skipping the ones that cannot be."""
    collapsed_names = set()
    for symmetry_class in symmetry_classes:
        collapsed_names.update(_normalize_object_names(symmetry_class))
    reserved_names = _reserved_names(problem, collapsed_names)

    abstractions = []
    relaxable_deletes = []
    for symmetry_class in symmetry_classes:
        try:
            abstraction = _create_abstraction(problem, symmetry_class, reserved_names=reserved_names)
        except AbstractionError:
            # One unusable class must not cost the run every other class.
            continue
        reserved_names.add(abstraction.name.casefold())
        abstractions.append(abstraction)
        relaxable_deletes.extend(find_relaxable_deletes(problem, abstraction))

    if not abstractions:
        raise NoSymmetriesError("No symmetry class reported by PDDL Symmetries could be collapsed")

    # The same delete can be relaxable for two classes; relaxing it once is enough.
    return tuple(abstractions), tuple(dict.fromkeys(relaxable_deletes))


def _create_abstraction(problem, object_names, abstract_name=None, reserved_names=None):
    objects_by_name = {item.name.casefold(): item for item in problem.all_objects}

    # Normalize names and remove duplicates.
    object_names = _normalize_object_names(object_names)
    if len(object_names) < 2:
        raise AbstractionError("At least two distinct objects must be selected")

    # Find the objects to collapse
    unknown_names = [name for name in object_names if name not in objects_by_name]
    if unknown_names:
        raise AbstractionError(f"Unknown problem objects: {', '.join(unknown_names)}")
    objects_to_collapse = tuple(objects_by_name[name] for name in object_names)

    # Check that all selected objects have the same declared type
    if len({item.type for item in objects_to_collapse}) != 1:
        raise AbstractionError("Selected objects must have the same declared type")

    if reserved_names is None:
        reserved_names = _reserved_names(problem, set(object_names))

    if abstract_name is None:
        abstract_name = _unique_abstract_name(objects_to_collapse[0].type.name, reserved_names)
    elif abstract_name.casefold() in reserved_names:
        raise AbstractionError(f"Abstract object name is already used: {abstract_name}")

    return Abstraction(
        name=abstract_name,
        objects=tuple(item.name for item in objects_to_collapse),
        object_type=objects_to_collapse[0].type.name,
    )


def _reserved_names(problem, collapsed_names):
    """Names an abstract object cannot take; the collapsed objects free theirs."""
    reserved_names = set()
    for item in problem.actions:
        reserved_names.add(item.name.casefold())
    for item in problem.fluents:
        reserved_names.add(item.name.casefold())
    for item in problem.user_types:
        reserved_names.add(item.name.casefold())
    for item in problem.all_objects:
        if item.name.casefold() not in collapsed_names:
            reserved_names.add(item.name.casefold())
    return reserved_names


def _unique_abstract_name(type_name, reserved_names):
    """Two classes can share a declared type, so suffix the name until it is free."""
    abstract_name = f"{type_name}_abs"
    suffix = 1
    while abstract_name.casefold() in reserved_names:
        suffix += 1
        abstract_name = f"{type_name}_abs{suffix}"
    return abstract_name


def _normalize_object_names(object_names):
    """Normalize object names to lowercase, remove duplicates, and order them."""
    return sorted({str(name).casefold() for name in object_names})
