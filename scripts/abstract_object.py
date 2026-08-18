"""Collapse an explicit or automatically selected symmetric PDDL object set."""

import argparse
from pathlib import Path

from core.integrations.pddl_symmetries import PddlSymmetriesError, find_symmetric_object_sets
from core.symmetry_abstraction import AbstractionError, abstract_task, rank_symmetry_classes
from .utils.arguments import positive_int


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    try:
        _validate_output_paths(args)
        domain_text = args.domain.read_text(encoding="utf-8")
        problem_text = args.problem.read_text(encoding="utf-8")

        ranked = []
        objects = args.objects
        if args.auto:
            classes = find_symmetric_object_sets(args.domain, args.problem, args.bliss_time_limit)
            ranked = rank_symmetry_classes(domain_text, problem_text, classes)
            if not ranked:
                raise AbstractionError("PDDL Symmetries found no abstractable object classes")
            objects = ranked[0].objects

        result = abstract_task(domain_text, problem_text, objects or (), args.abstract_name)
        for output in (args.output_domain, args.output_problem):
            output.parent.mkdir(parents=True, exist_ok=True)
        args.output_domain.write_text(result.domain_text, encoding="utf-8")
        args.output_problem.write_text(result.problem_text, encoding="utf-8")
    except (AbstractionError, PddlSymmetriesError, OSError, UnicodeError) as error:
        parser.error(str(error))
    _report(args, result, ranked)


def _validate_output_paths(args):
    inputs = {args.domain.resolve(), args.problem.resolve()}
    outputs = {args.output_domain.resolve(), args.output_problem.resolve()}
    if len(outputs) != 2:
        raise AbstractionError("Domain and problem outputs must be different files")
    if inputs & outputs:
        raise AbstractionError("Output files must not overwrite the inputs")


def _report(args, result, ranked):
    if ranked:
        print("Ranked symmetric object classes:")
        for rank, item in enumerate(ranked, start=1):
            print(
                f"  {rank}. {list(item.objects)} " f"(type={item.object_type}, unary deletes={item.unary_delete_score})"
            )
            for removed in item.removed_deletes:
                print(f"    {removed.action}: (not ({removed.predicate} {removed.variable}))")
    print(f"Collapsed {list(result.objects)} into {result.abstract_name} " f"(type={result.object_type})")
    print(f"Relaxed {result.unary_delete_score} unary delete effects")
    for removed in result.removed_deletes:
        print(f"  {removed.action}: (not ({removed.predicate} {removed.variable}))")
    print(f"Written abstract domain to: {args.output_domain}")
    print(f"Written abstract problem to: {args.output_problem}")


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--domain", type=Path, required=True, default=argparse.SUPPRESS, help="Concrete domain PDDL")
    parser.add_argument("--problem", type=Path, required=True, default=argparse.SUPPRESS, help="Concrete problem PDDL")
    parser.add_argument(
        "--output-domain", type=Path, required=True, default=argparse.SUPPRESS, help="Abstract domain to write"
    )
    parser.add_argument(
        "--output-problem", type=Path, required=True, default=argparse.SUPPRESS, help="Abstract problem to write"
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--objects", nargs="+", help="Objects to collapse")
    selection.add_argument("--auto", action="store_true", help="Select one class using PDDL Symmetries")
    parser.add_argument("--abstract-name", help="Name of the collapsed object")
    parser.add_argument(
        "--bliss-time-limit", type=positive_int, default=300, help="PDDL Symmetries search limit in seconds"
    )
    return parser


if __name__ == "__main__":
    main()
