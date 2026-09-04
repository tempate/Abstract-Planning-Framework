"""Build planning abstractions from PDDL Symmetries classes."""

from dataclasses import dataclass

from unified_planning.model import Problem

from core.abstraction.collapse import AbstractionError, collapse_objects
from core.abstraction.heuristic import abstraction_score
from core.abstraction.relaxation import find_relaxable_deletes
from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import read_problem
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.planning.outcomes import NoSymmetriesError

__all__ = ["Abstraction", "AbstractionError", "AbstractionResult", "NoSymmetriesError", "build_abstract_problem"]


@dataclass(frozen=True)
class Abstraction:
    name: str
    objects: tuple[str, ...]
    object_type: str


@dataclass(frozen=True)
class AbstractionResult:
    abstraction: Abstraction
    problem: Problem
    relaxed_deletes: tuple


def build_abstract_problem(config: AbstractPlanningConfig, metrics: PlanningMetrics | None = None):
    """Read one concrete task, select an object class, and abstract it."""
    metrics = metrics or PlanningMetrics()
    with metrics.measure("problem_reading"):
        problem = read_problem(config.domain_path, config.problem_path)

    if config.objects_to_abstract is None:
        with metrics.measure("symmetry_discovery"):
            symmetry_classes = find_symmetric_object_sets(
                config.domain_path, config.problem_path, config.symmetry_time_limit
            )
        if not symmetry_classes:
            raise NoSymmetriesError("PDDL Symmetries found no abstractable object classes")

    with metrics.measure("abstraction"):
        if config.objects_to_abstract is None:
            abstraction, relaxable_deletes = _select_abstraction(problem, symmetry_classes, config.abstract_name)
        else:
            abstraction = _create_abstraction(problem, config.objects_to_abstract, config.abstract_name)
            relaxable_deletes = find_relaxable_deletes(problem, abstraction)
        collapsed_problem, relaxed_deletes = collapse_objects(problem, abstraction, relaxable_deletes)
    return AbstractionResult(abstraction=abstraction, problem=collapsed_problem, relaxed_deletes=relaxed_deletes)


def _select_abstraction(problem, symmetry_classes, abstract_name=None):
    """Select the lowest-scoring class reported by PDDL Symmetries."""
    candidate = None
    candidate_relaxable_deletes = ()
    candidate_score = None

    for symmetry_class in symmetry_classes:
        abstraction = _create_abstraction(problem, symmetry_class, abstract_name)
        relaxable_deletes = find_relaxable_deletes(problem, abstraction)
        score = abstraction_score(problem, abstraction, relaxable_deletes)
        if candidate_score is None or score < candidate_score:
            candidate = abstraction
            candidate_relaxable_deletes = relaxable_deletes
            candidate_score = score

    return candidate, candidate_relaxable_deletes


def _create_abstraction(problem, object_names, abstract_name):
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

    if abstract_name is None:
        abstract_name = f"{objects_to_collapse[0].type.name}_abs"

    # Check if abstract_name is taken
    reserved_names = set()
    for item in problem.actions:
        reserved_names.add(item.name.casefold())
    for item in problem.fluents:
        reserved_names.add(item.name.casefold())
    for item in problem.user_types:
        reserved_names.add(item.name.casefold())
    for item in problem.all_objects:
        if item not in objects_to_collapse:
            reserved_names.add(item.name.casefold())
    if abstract_name.casefold() in reserved_names:
        raise AbstractionError(f"Abstract object name is already used: {abstract_name}")

    return Abstraction(
        name=abstract_name,
        objects=tuple(item.name for item in objects_to_collapse),
        object_type=objects_to_collapse[0].type.name,
    )


def _normalize_object_names(object_names):
    """Normalize object names to lowercase and remove duplicates."""
    return {str(name).casefold() for name in object_names}
