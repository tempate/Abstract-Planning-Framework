"""Grow the symmetric class of every base problem of the scaled opt suite by copying one of its objects.

Each copy gets every initial-state and goal atom of the object it copies, and a
copy of every domain action that names it, so it is interchangeable with that
object. Collapsing the grown class then gives the same abstract task as
collapsing the original one at every size.
"""

import re

from experiments.ipc.opt.scaled.suite import BASE_PROBLEMS, SIZES
from experiments.tracks import TRACKS, find_domain

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


def main():
    source = TRACKS["opt/symmetries"]
    scaled = TRACKS["opt-scaled/symmetries"]

    # Rank 0 of classes.txt is the largest class, the one each base problem grows.
    largest = {}
    for line in source.classes_file.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            problem, rank, _type, size, objects = line.split("\t")
            if rank == "0":
                largest[problem] = (int(size), objects.split()[0])

    runnable = []
    for name in BASE_PROBLEMS:
        class_size, obj = largest[name]
        problem = source.benchmarks_dir / name
        domain = find_domain(problem)
        base = problem.read_text()
        base_domain = domain.read_text()

        # The base problem sits at its own class size, and the larger sizes grow from it.
        for size in [class_size] + [size for size in SIZES if size > class_size]:
            directory = scaled.benchmarks_dir / problem.parent.name / f"size-{size}"
            directory.mkdir(parents=True, exist_ok=True)

            copies = size - class_size
            (directory / domain.name).write_text(scale_domain(base_domain, obj, copies))
            (directory / problem.name).write_text(scale(base, obj, copies))
            runnable.append(f"{problem.parent.name}/size-{size}/{problem.name}")

    header = "# Every problem of the suite. Regenerate with:\n#   python -m experiments.ipc.opt.scaled.generate\n"
    scaled.runnable_file.write_text(header + "\n".join(sorted(runnable)) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
