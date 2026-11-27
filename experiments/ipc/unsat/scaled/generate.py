"""Grow the largest class of every problem both M&S and M&S-alpha prove unsolvable, by copying one of its objects.

Each copy gets every initial-state and goal atom of the object it copies, and a
copy of every domain action that names it, so it is interchangeable with that
object. Collapsing the grown class then gives the same abstract task as
collapsing the original one, so a problem M&S-alpha proves unsolvable stays
unsolvable at every size.
"""

import csv
import re
from collections import defaultdict

from experiments.ipc.unsat.scaled.suite import BENCHMARKS_DIR, SIZES
from experiments.report import solved
from experiments.tracks import TRACKS
from scripts.utils.arguments import find_domain

BASE_TRACK = TRACKS["unsat/symmetries"]

ATOM = re.compile(r"\([^()]*\)")


def scale(problem, obj, copies):
    """The problem text with `copies` copies of `obj`, each named `<obj>-copy<i>`."""
    names = _names(obj, copies)
    mentions = _mentions(obj)

    def with_copies(atom):
        atom = atom.group(0)
        if not mentions.search(atom):
            return atom
        return " ".join([atom] + [mentions.sub(name, atom) for name in names])

    objects_start = problem.index("(:objects")
    init_start = problem.index("(:init")

    # The object's own entry in the objects section gains the copies right after it.
    # A domain constant has no entry here, and scale_domain declares its copies.
    objects = mentions.sub(lambda match: " ".join([match.group(0)] + names), problem[objects_start:init_start], count=1)
    facts = ATOM.sub(with_copies, problem[init_start:])
    return problem[:objects_start] + objects + facts


def scale_domain(domain, obj, copies):
    """The domain text with the copies of `obj` declared and given its actions, when it names `obj`."""
    names = _names(obj, copies)
    mentions = _mentions(obj)

    if "(:constants" in domain:
        start = domain.index("(:constants")
        end = _closing(domain, start)
        constants = mentions.sub(lambda match: " ".join([match.group(0)] + names), domain[start:end], count=1)
        domain = domain[:start] + constants + domain[end:]

    # cave-diving hires each diver with an action of its own, such as hire-diver-d0.
    action_name = re.compile(rf"(\(:action\s+\S*?)(?<![^\s-]){re.escape(obj)}(?=\s)")
    pieces = []
    position = 0

    for match in re.finditer(r"\(:action\b", domain):
        start = match.start()
        end = _closing(domain, start)
        action = domain[start:end]
        pieces.append(domain[position:end])
        if mentions.search(action):
            for name in names:
                copy = action_name.sub(lambda match: match.group(1) + name, action, count=1)
                if copy == action:
                    copy = re.sub(r"\(:action\s+(\S+)", rf"(:action \1-{name}", action, count=1)
                pieces.append("\n  " + mentions.sub(name, copy))
        position = end

    pieces.append(domain[position:])
    return "".join(pieces)


def _names(obj, copies):
    return [f"{obj}-copy{i}" for i in range(1, copies + 1)]


def _mentions(obj):
    return re.compile(rf"(?<![\w-]){re.escape(obj)}(?![\w-])")


def _closing(text, start):
    """The index just past the parenthesis that closes the one at `start`."""
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "(":
            depth += 1
        elif text[index] == ")":
            depth -= 1
            if depth == 0:
                return index + 1

    raise ValueError(f"Unbalanced parentheses from position {start}")


def proved_by_both(results_file):
    """The (domain, problem) pairs every mode of the base track proves unsolvable."""
    proved = defaultdict(set)
    with results_file.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if solved(row):
                proved[(row["domain"], row["problem"])].add(row["mode"])
    return sorted(key for key, modes in proved.items() if modes >= set(BASE_TRACK.modes))


def largest_classes(classes_file):
    """Each problem's largest class as sorted objects, the one the abstraction collapses without a class ID."""
    largest = {}
    for line in classes_file.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            name, _class_id, _type, _size, objects = line.split("\t")
            domain, _, problem = name.rpartition("/")
            objects = tuple(sorted(objects.split()))
            # Ties go to the first class in sorted order, as collapsible_classes breaks them.
            current = largest.get((domain, problem))
            if current is None or (-len(objects), objects) < (-len(current), current):
                largest[(domain, problem)] = objects
    return largest


def generate(domain_name, problem_name, objects):
    """Write the problem at its own class size and at every larger size of SIZES."""
    problem = BASE_TRACK.benchmarks_dir / domain_name / problem_name
    domain = find_domain(problem)
    base = problem.read_text()
    base_domain = domain.read_text()

    class_size = len(objects)
    for size in [class_size] + [size for size in SIZES if size > class_size]:
        directory = BENCHMARKS_DIR / domain_name / f"size-{size}"
        directory.mkdir(parents=True, exist_ok=True)

        copies = size - class_size
        (directory / domain.name).write_text(scale_domain(base_domain, objects[0], copies))
        (directory / problem.name).write_text(scale(base, objects[0], copies))


def main():
    largest = largest_classes(BASE_TRACK.classes_file)
    # PDDL Symmetries proves some problems unsolvable before it finds a class, which leaves none to grow.
    problems = [key for key in proved_by_both(BASE_TRACK.results_file) if key in largest]
    for domain_name, problem_name in problems:
        generate(domain_name, problem_name, largest[(domain_name, problem_name)])
    print(f"Grew {len(problems)} problems into {BENCHMARKS_DIR}")


if __name__ == "__main__":
    main()
