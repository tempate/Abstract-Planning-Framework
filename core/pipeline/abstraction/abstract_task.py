"""Build planning abstractions from the object classes PDDL Symmetries or resource detection finds."""

import tempfile
from dataclasses import dataclass
from pathlib import Path

from unified_planning.model import Problem

from core.pipeline.abstraction.collapse import AbstractionError, collapse_objects, validate_supported_problem
from core.pipeline.abstraction.relaxation import find_relaxable_deletes, relax_inequalities, split_actions
from core.integrations.numeric_fast_downward import detect_resources
from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import (
    negates_a_fluent,
    read_problem,
    to_positive_normal_form,
    without_action_costs,
    write_problem,
)
from core.utilities.classes import class_id
from core.utilities.metrics import PlanningMetrics
from core.utilities.outcomes import NoResourcesError, NoSymmetriesError
from core.utilities.config import RESOURCES, AbstractPlanningConfig

__all__ = ["AbstractTask", "AbstractionError", "CollapsedSet", "NoSymmetriesError", "build_abstract_task"]


@dataclass(frozen=True)
class CollapsedSet:
    name: str
    objects: tuple[str, ...]
    object_type: str

    @property
    def id(self):
        return class_id(self.object_type, self.objects)


@dataclass(frozen=True)
class AbstractTask:
    collapsed_set: CollapsedSet
    problem: Problem
    relaxed_deletes: tuple
    relaxed_inequalities: tuple


def build_abstract_task(config: AbstractPlanningConfig, metrics: PlanningMetrics | None = None):
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

    collapsed_set = _choose_abstraction(problem, config, metrics)

    with metrics.measure("abstraction"):
        # The class has to be chosen before the inequalities can be relaxed,
        # and they have to be relaxed before the collapse makes them false.
        # Split before relaxing any delete, so that the relaxation sees which
        # groundings of an action can take a collapsed object.
        problem = split_actions(problem, collapsed_set)
        problem, relaxed_inequalities = relax_inequalities(problem, collapsed_set)

    # Relaxing a delete is only an over-approximation while every condition is
    # positive, so reach PNF before any delete is relaxed.
    # With nothing to rewrite the translation still writes out the closed
    # world, which nomystery's ternary sum predicate turns into 240k initial
    # facts and 600 seconds, so skip what would only rebuild the problem.
    with metrics.measure("pnf_translation"):
        if negates_a_fluent(problem):
            problem = to_positive_normal_form(problem)

    with metrics.measure("abstraction"):
        relaxable_deletes = find_relaxable_deletes(problem, collapsed_set)
        collapsed_problem, relaxed_deletes = collapse_objects(problem, collapsed_set, relaxable_deletes)

    return AbstractTask(
        collapsed_set=collapsed_set,
        problem=collapsed_problem,
        relaxed_deletes=relaxed_deletes,
        relaxed_inequalities=relaxed_inequalities,
    )


def _choose_abstraction(problem, config, metrics):
    """The objects the config names, or else the candidate class with the config's ID, the largest without one."""
    if config.objects_to_abstract is not None:
        with metrics.measure("abstraction"):
            return _create_abstraction(problem, config.objects_to_abstract)

    candidate_classes = _candidate_classes(config, metrics)
    with metrics.measure("abstraction"):
        return _select_abstraction(problem, candidate_classes, config.class_id)


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
        symmetry_classes = find_symmetric_object_sets(config.domain_path, config.problem_path)

    if not symmetry_classes:
        raise NoSymmetriesError("PDDL Symmetries found no abstractable object classes")
    return symmetry_classes


def _select_abstraction(problem, candidate_classes, class_id=None):
    """Select the candidate class with this ID, or the largest without one."""
    abstractions = collapsible_classes(problem, candidate_classes)
    if class_id is None:
        return abstractions[0]

    for abstraction in abstractions:
        if abstraction.id == class_id:
            return abstraction
    found = ", ".join(abstraction.id for abstraction in abstractions)
    raise AbstractionError(f"No class {class_id} among those this run can collapse: {found}")


def collapsible_classes(problem, candidate_classes):
    """Every candidate class the problem can collapse, largest first.

    Collapsing more objects is what lowers the abstract horizon, so size alone decides.
    """
    abstractions = []
    rejection = None

    # PDDL Symmetries prints its classes in a varying order, so sort them by name
    # first. Two resources can share their objects, so drop repeated classes.
    ordered_classes = sorted({tuple(sorted(candidate_class)) for candidate_class in candidate_classes})

    for candidate_class in ordered_classes:
        try:
            abstractions.append(_create_abstraction(problem, candidate_class))
        except AbstractionError as error:
            # One unusable class does not make the others unusable, so keep the
            # reason for the case where none of them works.
            rejection = rejection or error

    if not abstractions:
        raise rejection

    abstractions.sort(key=lambda collapsed_set: -len(collapsed_set.objects))
    return abstractions


def _create_abstraction(problem, object_names):
    objects_by_name = {item.name.casefold(): item for item in problem.all_objects}

    # Lowercase, without repeats, and in order.
    object_names = sorted({str(name).casefold() for name in object_names})
    if len(object_names) < 2:
        raise AbstractionError("At least two distinct objects must be selected")

    unknown_names = [name for name in object_names if name not in objects_by_name]
    if unknown_names:
        raise AbstractionError(f"Unknown problem objects: {', '.join(unknown_names)}")

    objects_to_collapse = tuple(objects_by_name[name] for name in object_names)

    if len({item.type for item in objects_to_collapse}) != 1:
        raise AbstractionError("Selected objects must have the same declared type")

    abstract_name = f"{objects_to_collapse[0].type.name}_abs"

    # The abstract object cannot share a name with anything the task keeps.
    reserved_names = {item.name.casefold() for item in (*problem.actions, *problem.fluents, *problem.user_types)}
    reserved_names |= {item.name.casefold() for item in problem.all_objects if item not in objects_to_collapse}

    if abstract_name.casefold() in reserved_names:
        raise AbstractionError(f"Abstract object name is already used: {abstract_name}")

    return CollapsedSet(
        name=abstract_name,
        objects=tuple(item.name for item in objects_to_collapse),
        object_type=objects_to_collapse[0].type.name,
    )


def report_abstraction(abstract_problem, metrics):
    """Record the collapsed class and what relaxing it cost.

    Reported before solving, so a run that fails later still carries it: the
    metrics snapshot reaches the result file on every update, which is what
    survives a run killed at the benchmark timeout.
    """
    collapsed_set = abstract_problem.collapsed_set
    metrics.set_abstraction(collapsed_set.objects, collapsed_set.object_type)
    metrics.set_counters(
        {
            "relaxed_deletes": len(abstract_problem.relaxed_deletes),
            "relaxed_inequalities": len(abstract_problem.relaxed_inequalities),
        }
    )

    print(f"Collapsed {sorted(collapsed_set.objects)} into {collapsed_set.name} (type={collapsed_set.object_type})")


def write_abstract_problem(problem, base_dir):
    """Write the abstract problem to a temporary directory."""
    input_directory = Path(base_dir, "generated-abstraction")
    input_directory.mkdir(parents=True, exist_ok=True)

    serialized = write_problem(problem)

    domain_path = input_directory / "domain.pddl"
    domain_path.write_text(serialized.domain, encoding="utf-8")

    problem_path = input_directory / "problem.pddl"
    problem_path.write_text(serialized.problem, encoding="utf-8")

    return domain_path, problem_path, serialized.renamings
