"""Decide one PDDL task with Fast Downward, directly or through its abstraction.

The abstraction over-approximates, so the two modes answer different questions.
``concrete`` settles the task: solvable or unsolvable. ``abstract`` searches the
abstraction instead, where no plan proves the concrete task unsolvable but a plan
may exist only because of the relaxation, and is reported as unknown.
"""

import argparse

from core.integrations.unified_planning import PddlError
from core.abstraction.factory import AbstractionError
from core.outcomes import PlanningOutcomeError
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.abstract import check_solvability_via_abstraction
from core.planning.baseline import check_solvability_directly

from .utils.arguments import abstraction_arguments, task_arguments
from .utils.reporting import print_metrics, progress_callback


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    try:
        print("Starting")
        result = _compute(args)
    except PlanningOutcomeError as error:
        print(f"{error.label}: {error}")
        return error.exit_code
    except (AbstractionError, PddlError, OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    print_verdict(result)
    return 0


def _compute(args):
    on_update = progress_callback()
    common = {"domain_path": args.domain, "problem_path": args.problem}
    if args.mode == "concrete":
        return check_solvability_directly(PlanningConfig(**common), on_update)
    if args.mode == "abstract":
        return check_solvability_via_abstraction(
            AbstractPlanningConfig(
                **common,
                objects_to_abstract=args.objects_to_abstract,
                abstract_name=args.abstract_name,
                symmetry_time_limit=args.symmetry_time_limit,
            ),
            on_update,
        )
    raise ValueError(f"Unknown decision mode: {args.mode}")


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
        "concrete",
        parents=[shared],
        help="Search the task itself",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "abstract",
        parents=[shared, abstract],
        help="Search its abstraction",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
