"""Find object classes a static relation orders or counts, as resource ladders are."""

from dataclasses import dataclass

__all__ = ["Ladder", "find_ladders"]


@dataclass(frozen=True)
class Ladder:
    object_type: str
    relation: str
    shape: str
    objects: tuple[str, ...]


def find_ladders(problem):
    """Find static relations over a single object type that order or count that type."""
    static_names = _static_fluent_names(problem)
    ladders = []
    for fluent in problem.fluents:
        if fluent.name not in static_names or not _is_over_one_type(fluent):
            continue
        facts = _initial_facts(problem, fluent.name)
        if len(fluent.signature) == 2:
            shape = _shape(facts)
        else:
            shape = "an arithmetic relation"
        if shape is None:
            continue
        # In untyped PDDL every object shares one type, so the relation's own
        # extension is what names the rungs.
        objects = _objects_in_facts(facts)
        if len(objects) < 3:
            continue
        ladders.append(Ladder(str(fluent.signature[0].type), fluent.name, shape, objects))
    return tuple(ladders)


def _static_fluent_names(problem):
    """Name every fluent no action ever writes."""
    written = set()
    for action in problem.actions:
        for effect in action.effects:
            written.add(effect.fluent.fluent().name)
    names = set()
    for fluent in problem.fluents:
        if fluent.name not in written:
            names.add(fluent.name)
    return names


def _is_over_one_type(fluent):
    """Accept a boolean relation whose arguments all share one type."""
    if not fluent.type.is_bool_type() or len(fluent.signature) < 2:
        return False
    for parameter in fluent.signature:
        if parameter.type != fluent.signature[0].type:
            return False
    return True


def _initial_facts(problem, fluent_name):
    facts = []
    for atom, value in problem.explicit_initial_values.items():
        if not value.is_true() or atom.fluent().name != fluent_name:
            continue
        names = []
        for arg in atom.args:
            if arg.is_object_exp():
                names.append(arg.object().name)
        if len(names) == len(atom.args):
            facts.append(tuple(names))
    return facts


def _shape(edges):
    """Classify a binary relation as a successor chain, a total order, or neither."""
    nodes = set()
    outgoing = {}
    incoming = {}
    for tail, head in edges:
        nodes.add(tail)
        nodes.add(head)
        outgoing[tail] = outgoing.get(tail, 0) + 1
        incoming[head] = incoming.get(head, 0) + 1
    if len(nodes) < 3:
        return None

    if len(edges) == len(nodes) - 1 and max(outgoing.values()) == 1 and max(incoming.values()) == 1:
        return "a chain"
    if len(edges) == len(nodes) * (len(nodes) - 1) // 2:
        return "a total order"
    return None


def _objects_in_facts(facts):
    names = []
    for fact in facts:
        for name in fact:
            if name not in names:
                names.append(name)
    return tuple(names)
