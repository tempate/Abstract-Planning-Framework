"""Build planning abstractions from PDDL Symmetries classes."""

import tempfile
from dataclasses import dataclass
from pathlib import Path

from unified_planning.model import Problem

from core.abstraction.collapse import AbstractionError, collapse_objects, validate_supported_problem
from core.abstraction.relaxation import find_relaxable_deletes, relax_inequalities
from core.integrations.numeric_fast_downward import detect_resources
from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import (
    read_problem,
    to_positive_normal_form,
    without_action_costs,
    write_problem,
)
from core.metrics import PlanningMetrics
from core.outcomes import NoResourcesError, NoSymmetriesError
from core.planning.config import RESOURCES, AbstractPlanningConfig

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
    relaxed_inequalities: tuple


def build_abstract_problem(config: AbstractPlanningConfig, metrics: PlanningMetrics | None = None):
    """Read one concrete task, select an object class, and abstract it."""
    metrics = metrics or PlanningMetrics()
    with metrics.measure("problem_reading"):
        problem = read_problem(config.domain_path, config.problem_path)

    # Reject unsupported models before anything walks the actions, which only
    # the instantaneous ones are shaped for.
    validate_supported_problem(problem)

    # The search wants any plan, not a cheap one, so the costs go before the
    # collapse, which would otherwise merge the values that price actions.
    problem = without_action_costs(problem)

    if config.objects_to_abstract is None:
        candidate_classes = _candidate_classes(config, metrics)

    with metrics.measure("abstraction"):
        if config.objects_to_abstract is None:
            abstraction = _select_abstraction(problem, candidate_classes, config.abstract_name)
        else:
            abstraction = _create_abstraction(problem, config.objects_to_abstract, config.abstract_name)

        # The class has to be chosen before the inequalities can be relaxed,
        # and they have to be relaxed before the translation, which rewrites
        # every one of them into a disjunction over pairs of objects.
        problem, relaxed_inequalities = relax_inequalities(problem, abstraction)

    # Relaxing a delete is only an over-approximation while every condition is
    # positive, so reach PNF before any delete is relaxed.
    # With nothing to rewrite the translation still writes out the closed
    # world, which nomystery's ternary sum predicate turns into 240k initial
    # facts and 600 seconds, so skip what would only rebuild the problem.
    with metrics.measure("pnf_translation"):
        if problem.kind.has_negative_conditions():
            problem = to_positive_normal_form(problem)

    with metrics.measure("abstraction"):
        relaxable_deletes = find_relaxable_deletes(problem, abstraction)
        collapsed_problem, relaxed_deletes = collapse_objects(problem, abstraction, relaxable_deletes)
    return AbstractionResult(
        abstraction=abstraction,
        problem=collapsed_problem,
        relaxed_deletes=relaxed_deletes,
        relaxed_inequalities=relaxed_inequalities,
    )


def _candidate_classes(config, metrics):
    """Find the object classes this run may collapse, from the source it was given."""
    if config.abstraction_source == RESOURCES:
        with metrics.measure("resource_detection"):
            with tempfile.TemporaryDirectory(prefix="apf-resources-") as directory:
                resources = detect_resources(directory, config.domain_path, config.problem_path)
        if not resources:
            raise NoResourcesError("Resource detection found no abstractable object classes")
        return [resource.objects for resource in resources]

    with metrics.measure("symmetry_discovery"):
        symmetry_classes = find_symmetric_object_sets(
            config.domain_path, config.problem_path, config.symmetry_time_limit
        )
    if not symmetry_classes:
        raise NoSymmetriesError("PDDL Symmetries found no abstractable object classes")
    return symmetry_classes


def _select_abstraction(problem, symmetry_classes, abstract_name=None):
    """Select the largest of the candidate classes.

    Collapsing more objects is what lowers the abstract horizon, so size alone decides.
    """
    candidate = None
    rejection = None

    # PDDL Symmetries prints its classes in an order that varies between
    # processes, and the first of the largest wins, so two runs of one problem
    # could collapse different classes of the same size.
    ordered_classes = sorted(sorted(symmetry_class) for symmetry_class in symmetry_classes)

    for symmetry_class in ordered_classes:
        try:
            abstraction = _create_abstraction(problem, symmetry_class, abstract_name)
        except AbstractionError as error:
            # One unusable class does not make the others unusable, so keep the
            # reason for the case where none of them works.
            rejection = rejection or error
            continue
        if candidate is None or len(abstraction.objects) > len(candidate.objects):
            candidate = abstraction

    if candidate is None:
        raise rejection
    return candidate


def _create_abstraction(problem, object_names, abstract_name):
    objects_by_name = {item.name.casefold(): item for item in problem.all_objects}

    object_names = _normalize_object_names(object_names)
    if len(object_names) < 2:
        raise AbstractionError("At least two distinct objects must be selected")

    unknown_names = [name for name in object_names if name not in objects_by_name]
    if unknown_names:
        raise AbstractionError(f"Unknown problem objects: {', '.join(unknown_names)}")
    objects_to_collapse = tuple(objects_by_name[name] for name in object_names)

    if len({item.type for item in objects_to_collapse}) != 1:
        raise AbstractionError("Selected objects must have the same declared type")

    if abstract_name is None:
        abstract_name = f"{objects_to_collapse[0].type.name}_abs"

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
    """Normalize object names to lowercase, remove duplicates, and order them."""
    return sorted({str(name).casefold() for name in object_names})


def report_abstraction(abstract_problem, metrics):
    """Record the collapsed class and what relaxing it cost.

    Reported before solving, so a run that fails later still carries it: the
    metrics snapshot reaches the result file on every update, which is what
    survives a run killed at the benchmark timeout.
    """
    abstraction = abstract_problem.abstraction
    metrics.set_abstraction(abstraction.objects, abstraction.object_type)
    metrics.set_counters(
        {
            "relaxed_deletes": len(abstract_problem.relaxed_deletes),
            "relaxed_inequalities": len(abstract_problem.relaxed_inequalities),
        }
    )
    print(f"Collapsed {sorted(abstraction.objects)} into {abstraction.name} (type={abstraction.object_type})")


def write_abstract_problem(problem, base_dir):
    """Write the abstract problem to a temporary directory."""
    input_directory = Path(base_dir, "generated-abstraction")
    input_directory.mkdir(parents=True, exist_ok=True)

    serialized = write_problem(problem)

    domain_path = input_directory / "domain.pddl"
    domain_path.write_text(serialized.domain, encoding="utf-8")

    problem_path = input_directory / "problem.pddl"
    problem_path.write_text(serialized.problem, encoding="utf-8")

    return domain_path, problem_path
