"""Fast Downward SAS boundary for reading a translated task back."""

import re
from dataclasses import dataclass

ATOM_PATTERN = re.compile(r"^Atom ([\w-]+)\(([^)]*)\)$")


@dataclass(frozen=True)
class SasVariable:
    """One finite-domain variable and the atoms it ranges over."""

    name: str
    values: tuple[str, ...]


@dataclass(frozen=True)
class SasTask:
    """The variables of a translated task and the value changes its operators make."""

    variables: tuple[SasVariable, ...]
    transitions: dict


def read_sas(sas_text):
    """Read the variables and the per-variable transitions of a translated task."""
    lines = sas_text.split("\n")
    variables = _read_variables(lines)
    return SasTask(variables=variables, transitions=_read_transitions(lines, variables))


def parse_atom(value):
    """Split a variable's value into its predicate and arguments, if it names an atom."""
    match = ATOM_PATTERN.match(value)
    if match is None:
        # Values such as "<none of those>" name no atom.
        return None
    arguments = []
    for argument in match.group(2).split(","):
        arguments.append(argument.strip())
    return match.group(1), tuple(arguments)


def _read_variables(lines):
    variables = []
    index = 0
    while index < len(lines):
        if lines[index] != "begin_variable":
            index += 1
            continue
        size = int(lines[index + 3])
        variables.append(SasVariable(lines[index + 1], tuple(lines[index + 4 : index + 4 + size])))
        index += 4 + size
    return tuple(variables)


def _read_transitions(lines, variables):
    transitions = {}
    for index in range(len(variables)):
        transitions[index] = set()

    index = 0
    while index < len(lines):
        if lines[index] != "begin_operator":
            index += 1
            continue
        prevail_count = int(lines[index + 2])
        effect_index = index + 3 + prevail_count
        effect_count = int(lines[effect_index])
        for offset in range(effect_count):
            parts = lines[effect_index + 1 + offset].split()
            condition_count = int(parts[0])
            variable = int(parts[1 + condition_count])
            before = int(parts[2 + condition_count])
            after = int(parts[3 + condition_count])
            if before == after:
                continue
            if before != -1:
                transitions[variable].add((before, after))
                continue
            # An effect without a precondition applies to every other value.
            for value in range(len(variables[variable].values)):
                if value != after:
                    transitions[variable].add((value, after))
        index = effect_index + 1 + effect_count
    return transitions
