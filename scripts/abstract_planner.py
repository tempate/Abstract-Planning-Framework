"""Command-line entry point for abstraction-based planning."""

import argparse

from core.execution import get_logger
from core.integrations.pddl_symmetries import PddlSymmetriesError
from core.integrations.unified_planning import PddlError
from core.model_abstraction import AbstractionError
from core.planning.config import (
    DEFAULT_ENCODING,
    DEFAULT_HORIZON,
    DEFAULT_PLAN_SOURCE,
    DEFAULT_PROFILE_NAME,
    DEFAULT_TIME_STEP,
    AbstractPlanningConfig,
)
from core.planning.abstract import compute_abstract_plan
from core.planners.factory import PLANNER_TYPES

from .utils.arguments import nonnegative_int, positive_int
from .utils.reporting import print_planning_result


def main():
    parser = _argument_parser()
    args = parser.parse_args()
    try:
        print("Starting")
        config = AbstractPlanningConfig(
            domain_path=args.domain,
            problem_path=args.problem,
            objects=args.objects,
            abstract_name=args.abstract_name,
            horizon=args.horizon,
            encoding=args.encoding,
            time_step=args.time_step,
            bliss_time_limit=args.bliss_time_limit,
            plan_source=args.plan_source,
            profile_name=args.profile,
        )
        result = compute_abstract_plan(config)
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


def _argument_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--profile",
        choices=sorted(PLANNER_TYPES),
        default=DEFAULT_PROFILE_NAME,
        help="Domain-specific mapping and refinement configuration",
    )
    parser.add_argument("--domain", required=True, default=argparse.SUPPRESS, help="Concrete domain PDDL")
    parser.add_argument("--problem", required=True, default=argparse.SUPPRESS, help="Concrete problem PDDL")
    parser.add_argument(
        "--objects", nargs="+", help="Concrete objects to collapse; omit to select a class using PDDL Symmetries"
    )
    parser.add_argument(
        "--horizon",
        type=nonnegative_int,
        default=DEFAULT_HORIZON,
        help="Planning horizon; omit to infer it with Fast Downward",
    )
    parser.add_argument("--encoding", default=DEFAULT_ENCODING, help="ASP encoding type")
    parser.add_argument(
        "--time-step", action="store_true", default=DEFAULT_TIME_STEP, help="Enable time-step based encoding"
    )
    parser.add_argument("--abstract-name", default=None, help="Name of the collapsed object")
    parser.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default=DEFAULT_PLAN_SOURCE,
        help="Use a Fast Downward plan directly or compute one with Clingo",
    )
    parser.add_argument(
        "--bliss-time-limit", type=positive_int, default=300, help="PDDL Symmetries search limit in seconds"
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
