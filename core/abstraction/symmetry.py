"""Build symmetric-object abstractions for planning workflows."""

from core.integrations.pddl_symmetries import find_symmetric_object_sets
from core.integrations.unified_planning import read_problem
from core.abstraction.model import AbstractionError, abstract_problem, rank_symmetry_classes


def prepare_abstraction(
    domain_path, problem_path, *, objects_to_abstract=None, abstract_name=None, bliss_time_limit=300
):
    """Read one concrete task, select an object class, and abstract it."""
    problem = read_problem(domain_path, problem_path)
    ranked = ()
    selected = objects_to_abstract
    if selected is None:
        classes = find_symmetric_object_sets(domain_path, problem_path, bliss_time_limit)
        ranked = rank_symmetry_classes(problem, classes)
        if not ranked:
            raise AbstractionError("PDDL Symmetries found no abstractable object classes")
        selected = ranked[0].abstraction.objects

    return abstract_problem(problem, selected, abstract_name)
