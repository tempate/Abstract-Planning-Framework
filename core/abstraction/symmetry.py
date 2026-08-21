"""Build symmetric-object abstractions for planning workflows."""

from dataclasses import dataclass

from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import read_problem
from core.abstraction.model import (
    AbstractionError,
    AbstractionResult,
    RankedSymmetryClass,
    abstract_problem,
    rank_symmetry_classes,
)


@dataclass(frozen=True)
class PreparedAbstraction:
    """An abstract model together with any automatic-selection ranking."""

    result: AbstractionResult
    ranked: tuple[RankedSymmetryClass, ...] = ()


def prepare_abstraction(domain_path, problem_path, *, objects=None, abstract_name=None, bliss_time_limit=300):
    """Read one concrete task, select an object class, and abstract it."""
    problem = read_problem(domain_path, problem_path)
    ranked = ()
    selected = objects
    if selected is None:
        classes = find_symmetric_object_sets(domain_path, problem_path, bliss_time_limit)
        ranked = rank_symmetry_classes(problem, classes)
        if not ranked:
            raise AbstractionError("PDDL Symmetries found no abstractable object classes")
        selected = ranked[0].objects

    return PreparedAbstraction(result=abstract_problem(problem, selected, abstract_name), ranked=ranked)
