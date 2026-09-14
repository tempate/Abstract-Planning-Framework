"""Find resource ladders in the finite-domain representation of a task.

The translator already groups mutually exclusive atoms into one variable, so a
ladder shows up as a variable whose domain dwarfs the rest. A resource is either
one nothing puts back, whose domain transition graph has no cycle, or a
renewable counter, which cycles but only ever steps to an adjacent count. A
position cycles too and moves anywhere, which is what tells the two apart.
"""

import statistics
from dataclasses import dataclass
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

from core.integrations.sas import parse_atom, read_sas

__all__ = ["SasLadder", "find_ladder_classes"]


@dataclass(frozen=True)
class SasLadder:
    predicate: str
    objects: tuple[str, ...]


def find_ladder_classes(problem, concrete_sas):
    """Report the objects of every resource ladder the translated task holds."""
    if concrete_sas is None:
        return []

    task = read_sas(Path(concrete_sas).read_text(encoding="utf-8"))
    classes = []
    for ladder in _find_sas_ladders(task):
        classes.append(_whole_ladder(problem, ladder.objects))
    return classes


def _whole_ladder(problem, objects):
    """Extend the reachable objects the translator kept to every object of their type.

    Relaxed reachability drops values no plan can visit, and collapsing all but
    those leaves the rest of the ladder standing, which the refinement then pays
    for. The declared type is the whole ladder, unless the task is untyped and
    that type is every object there is.
    """
    names = set()
    for name in objects:
        names.add(name.casefold())

    types = set()
    for item in problem.all_objects:
        if item.name.casefold() in names:
            types.add(item.type)
    if len(types) != 1:
        return list(objects)

    whole = []
    count = 0
    for item in problem.all_objects:
        count += 1
        if item.type in types:
            whole.append(item.name)
    if len(whole) == count:
        return list(objects)
    return whole


def _find_sas_ladders(task, outlier_ratio=3.0):
    """Report the variables whose domain is an outlier and whose transitions hold a resource."""
    if len(task.variables) < 2:
        return ()
    threshold = outlier_ratio * _median_domain_size(task.variables)

    ladders = []
    for index, variable in enumerate(task.variables):
        if len(variable.values) < 3 or len(variable.values) < threshold:
            continue
        if _has_cycle(task.transitions[index]) and not _is_counter(task.transitions[index], len(variable.values)):
            continue
        found = _ladder_objects(variable.values)
        if found is None:
            continue
        predicate, objects = found
        ladders.append(SasLadder(predicate, objects))
    return tuple(ladders)


def _median_domain_size(variables):
    sizes = []
    for variable in variables:
        sizes.append(len(variable.values))
    return statistics.median(sizes)


def _has_cycle(edges):
    """Tell whether the transitions ever return to a value they left."""
    predecessors = {}
    for tail, head in edges:
        predecessors.setdefault(head, set()).add(tail)
    try:
        TopologicalSorter(predecessors).prepare()
    except CycleError:
        return True
    return False


def _is_counter(edges, size):
    """Tell whether the values form a simple path, which is how a counter moves up and down."""
    neighbours = {}
    for tail, head in edges:
        if tail != head:
            neighbours.setdefault(tail, set()).add(head)
            neighbours.setdefault(head, set()).add(tail)
    if len(neighbours) != size:
        return False

    start = None
    for value, near in neighbours.items():
        if len(near) > 2:
            return False
        if len(near) == 1:
            start = value
    if start is None:
        return False

    # Every value has at most two neighbours, so walking from an end is the path.
    seen = set()
    current = start
    while current is not None:
        seen.add(current)
        current = _next_value(neighbours[current], seen)
    return len(seen) == size


def _next_value(neighbours, seen):
    for value in neighbours:
        if value not in seen:
            return value
    return None


def _ladder_objects(values):
    """Name the predicate and the objects a variable's atoms differ in."""
    predicate = None
    argument_lists = []
    for value in values:
        atom = parse_atom(value)
        if atom is None:
            continue
        if predicate is None:
            predicate = atom[0]
        elif atom[0] != predicate:
            return None
        argument_lists.append(atom[1])

    if len(argument_lists) < 3:
        return None

    # Which argument the atoms range over shows in any two of them, and the
    # caller takes the whole type from the lifted task anyway.
    varying = None
    for position in range(len(argument_lists[0])):
        if argument_lists[0][position] == argument_lists[1][position]:
            continue
        if varying is not None:
            return None
        varying = position
    if varying is None:
        return None

    objects = []
    for arguments in argument_lists:
        objects.append(arguments[varying])
    return predicate, tuple(objects)
