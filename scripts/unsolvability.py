"""Decide one PDDL task with MS-unsat, directly or through its abstraction.

The abstraction over-approximates, so the modes answer different questions.
``ms`` settles the task: solvable or unsolvable. So does ``oss``, which runs blind
A* with structural symmetry pruning instead of MS-unsat. ``abs-ms`` searches the
abstraction instead, where no plan proves the concrete task unsolvable but a plan
may exist only because of the relaxation, and is reported as unknown.
"""

import argparse

from core.pipeline import pipeline
from core.planners.registry import PLANNERS

from .utils.arguments import abstract_planning_config, abstraction_arguments, planning_config, task_arguments
from .utils.entry import run
from .utils.reporting import print_metrics, progress_callback


def main():
    return run(_argument_parser(), _compute, _report)


def _report(result):
    print_verdict(result)
    return 0


def _compute(args):
    on_update = progress_callback()

    if args.mode in ("ms", "oss"):
        return PLANNERS[args.mode](planning_config(args)).check_solvability(on_update)
    if args.mode == "abs-ms":
        return pipeline.check_solvability(abstract_planning_config(args), on_update)


def print_verdict(result):
    """Print a decision result."""
    print("\n=== RESULT ===")
    print(f"Verdict: {result['verdict']}")
    print_metrics(result["metrics"])


def _argument_parser():
    shared = task_arguments()
    abstract = abstraction_arguments()

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    modes = parser.add_subparsers(dest="mode", required=True, title="decision modes")
    modes.add_parser(
        "ms",
        parents=[shared],
        help="Search the task itself",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "oss",
        parents=[shared],
        help="Search the task itself with blind A*, pruning symmetric states",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "abs-ms",
        parents=[shared, abstract],
        help="Search its abstraction",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
