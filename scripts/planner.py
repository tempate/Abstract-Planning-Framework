"""Solve one PDDL task concretely or through an automatically generated abstraction."""

import argparse

from core.execution import get_logger
from core.integrations.pddl_symmetries import PddlSymmetriesError
from core.integrations.unified_planning import PddlError
from core.abstraction.model import AbstractionError
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from core.planning.config import (
    DEFAULT_ENCODING,
    DEFAULT_HORIZON,
    DEFAULT_PLAN_SOURCE,
    DEFAULT_PROFILE_NAME,
    DEFAULT_TIME_STEP,
    AbstractPlanningConfig,
    PlanningConfig,
)
from core.profiles.factory import PROFILE_TYPES

from .utils.arguments import nonnegative_int, positive_int
from .utils.reporting import print_planning_result


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    try:
        print("Starting")
        result = _compute(args)
    except (AbstractionError, PddlError, PddlSymmetriesError, OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    abstraction = result.get("abstraction")
    if abstraction is not None:
        print(
            f"Collapsed {abstraction['concrete_objects']} into {abstraction['abstract_symbol']} "
            f"(type={abstraction['object_type']})"
        )
    print_planning_result(result, get_logger())
    return 0 if result["success"] else 1


def _compute(args):
    common = {
        "domain_path": args.domain,
        "problem_path": args.problem,
        "horizon": args.horizon,
        "encoding": args.encoding,
        "time_step": args.time_step,
    }
    if args.mode == "concrete":
        return compute_concrete_plan(PlanningConfig(**common))
    if args.mode == "abstract":
        return compute_abstract_plan(
            AbstractPlanningConfig(
                **common,
                objects=args.objects,
                abstract_name=args.abstract_name,
                bliss_time_limit=args.bliss_time_limit,
                plan_source=args.plan_source,
                profile_name=args.profile,
            )
        )
    raise ValueError(f"Unknown planning mode: {args.mode}")


def _argument_parser():
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--domain", required=True, default=argparse.SUPPRESS, help="Concrete domain PDDL")
    shared.add_argument("--problem", required=True, default=argparse.SUPPRESS, help="Concrete problem PDDL")
    shared.add_argument(
        "--horizon",
        type=nonnegative_int,
        default=DEFAULT_HORIZON,
        help="Planning horizon; omit to infer it with Fast Downward",
    )
    shared.add_argument("--encoding", default=DEFAULT_ENCODING, help="ASP encoding type")
    shared.add_argument(
        "--time-step", action="store_true", default=DEFAULT_TIME_STEP, help="Enable time-step based encoding"
    )

    # Abstract planning arguments
    abstract = argparse.ArgumentParser(add_help=False)
    abstract.add_argument(
        "--profile",
        choices=sorted(PROFILE_TYPES),
        default=DEFAULT_PROFILE_NAME,
        help="Domain-specific mapping and refinement configuration",
    )
    abstract.add_argument("--objects", nargs="+", help="Objects to collapse; omit to use PDDL Symmetries")
    abstract.add_argument("--abstract-name", help="Name of the collapsed object")
    abstract.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default=DEFAULT_PLAN_SOURCE,
        help="Use a Fast Downward plan directly or compute one with Clingo",
    )
    abstract.add_argument(
        "--bliss-time-limit", type=positive_int, default=300, help="PDDL Symmetries search limit in seconds"
    )

    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest="mode", required=True, title="planning modes")
    modes.add_parser(
        "concrete",
        parents=[shared],
        help="Solve the task directly",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "abstract",
        parents=[shared, abstract],
        help="Solve through abstraction",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
