"""Collapse an explicit or automatically selected symmetric PDDL object set."""

import argparse
from pathlib import Path

from core.symmetry_abstraction import (
    AbstractionError,
    abstract_task,
    find_symmetric_object_sets,
    rank_symmetry_classes,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("domain", type=Path, help="Concrete domain PDDL")
    parser.add_argument("problem", type=Path, help="Concrete problem PDDL")
    parser.add_argument("output_domain", type=Path, help="Abstract domain to write")
    parser.add_argument("output_problem", type=Path, help="Abstract problem to write")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--objects", nargs="+", help="Objects to collapse")
    selection.add_argument(
        "--auto", action="store_true",
        help="Select one class using PDDL Symmetries",
    )
    parser.add_argument("--abstract-name", help="Name of the collapsed object")
    parser.add_argument(
        "--bliss-time-limit", type=int, default=300,
        help="PDDL Symmetries search limit in seconds",
    )
    args = parser.parse_args()

    if args.bliss_time_limit < 1:
        parser.error("--bliss-time-limit must be positive")
    if args.output_domain.resolve() == args.output_problem.resolve():
        parser.error("domain and problem outputs must be different files")
    for output in (args.output_domain, args.output_problem):
        if output.resolve() in (args.domain.resolve(), args.problem.resolve()):
            parser.error("output files must not overwrite the inputs")

    domain_text = args.domain.read_text(encoding="utf-8")
    problem_text = args.problem.read_text(encoding="utf-8")
    objects = args.objects
    if args.auto:
        try:
            classes = find_symmetric_object_sets(
                args.domain, args.problem, args.bliss_time_limit,
            )
        except RuntimeError as error:
            parser.error(str(error))
        try:
            ranked = rank_symmetry_classes(domain_text, problem_text, classes)
        except AbstractionError as error:
            parser.error(str(error))
        if not ranked:
            parser.error("PDDL Symmetries found no non-trivial object classes")
        objects = list(ranked[0].objects)
        print("Ranked symmetric object classes:")
        for rank, item in enumerate(ranked, start=1):
            print(
                f"  {rank}. {list(item.objects)} "
                f"(type={item.object_type}, unary deletes={item.unary_delete_score})"
            )

    try:
        result = abstract_task(
            domain_text, problem_text, objects or (), args.abstract_name,
        )
    except AbstractionError as error:
        parser.error(str(error))

    args.output_domain.parent.mkdir(parents=True, exist_ok=True)
    args.output_problem.parent.mkdir(parents=True, exist_ok=True)
    args.output_domain.write_text(result.domain_text, encoding="utf-8")
    args.output_problem.write_text(result.problem_text, encoding="utf-8")

    print(
        f"Collapsed {list(result.objects)} into {result.abstract_name} "
        f"(type={result.object_type})"
    )
    print(f"Relaxed {result.unary_delete_score} unary delete effects")
    for removed in result.removed_deletes:
        print(f"  {removed.action}: (not ({removed.predicate} {removed.variable}))")
    print(f"Written abstract domain to: {args.output_domain}")
    print(f"Written abstract problem to: {args.output_problem}")


if __name__ == "__main__":
    main()
