"""Grow a problem's symmetric class by copying one of its objects.

Each copy gets every initial-state and goal atom of the object it copies, and a
copy of every domain action that names it, so it is interchangeable with that
object. Collapsing the grown class then gives the same abstract task as
collapsing the original one, so a problem M&S-alpha proves unsolvable stays
unsolvable at every size.
"""

import argparse
import re
from pathlib import Path

from experiments.tracks import TRACKS, find_domain
from experiments.unsat.scaled.suite import SIZES

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
    for start in [match.start() for match in re.finditer(r"\(:action\b", domain)]:
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
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--problem", required=True, type=Path, help="The base problem PDDL")
    parser.add_argument("--object", required=True, help="The object of the symmetric class to copy")
    parser.add_argument("--class-size", type=int, required=True, help="Size of the class in the base problem")
    parser.add_argument("--sizes", type=int, nargs="+", default=SIZES, help="Class sizes to generate")
    parser.add_argument(
        "--out",
        type=Path,
        default=TRACKS["scaled/symmetries"].benchmarks_dir,
        help="Directory with one <domain>/size-N directory per domain and class size",
    )
    args = parser.parse_args()

    domain = find_domain(args.problem)
    base = args.problem.read_text()
    base_domain = domain.read_text()
    # The base problem sits at its own class size, and the larger sizes grow from it.
    sizes = [args.class_size] + [size for size in args.sizes if size > args.class_size]
    for size in sizes:
        directory = args.out / args.problem.parent.name / f"size-{size}"
        directory.mkdir(parents=True, exist_ok=True)
        copies = size - args.class_size
        (directory / domain.name).write_text(scale_domain(base_domain, args.object, copies))
        path = directory / args.problem.name
        path.write_text(scale(base, args.object, copies))
        print(path)


if __name__ == "__main__":
    main()
