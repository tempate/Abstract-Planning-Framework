"""Grow a problem's symmetric class by copying one of its objects.

Each copy gets every initial-state and goal atom of the object it copies, so it is
interchangeable with that object. When the object has goals of its own, as a
package in over-nomystery does, a plan for the grown problem without the copies'
actions is a plan for the original, so an unsolvable problem stays unsolvable.
"""

import argparse
import re
import shutil
from pathlib import Path

from experiments.tracks import TRACKS, find_domain
from experiments.unsat.scaled.suite import SIZES

ATOM = re.compile(r"\([^()]*\)")


def scale(problem, obj, copies):
    """The problem text with `copies` copies of `obj`, each named `<obj>-copy<i>`."""
    names = [f"{obj}-copy{i}" for i in range(1, copies + 1)]
    mentions = re.compile(rf"(?<![\w-]){re.escape(obj)}(?![\w-])")

    def with_copies(atom):
        atom = atom.group(0)
        if not mentions.search(atom):
            return atom
        return " ".join([atom] + [mentions.sub(name, atom) for name in names])

    objects_start = problem.index("(:objects")
    init_start = problem.index("(:init")
    # The object's own entry in the objects section gains the copies right after it.
    objects = mentions.sub(lambda match: " ".join([match.group(0)] + names), problem[objects_start:init_start], count=1)
    facts = ATOM.sub(with_copies, problem[init_start:])
    return problem[:objects_start] + objects + facts


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
        help="Directory with one <domain>-size-N directory per domain and class size",
    )
    args = parser.parse_args()

    domain = find_domain(args.problem)
    base = args.problem.read_text()
    for size in args.sizes:
        directory = args.out / f"{args.problem.parent.name}-size-{size}"
        directory.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(domain, directory / "domain.pddl")
        path = directory / args.problem.name
        path.write_text(scale(base, args.object, size - args.class_size))
        print(path)


if __name__ == "__main__":
    main()
