"""Command-line entry point for abstraction-based planning."""

import argparse
from functools import partial

from core.execution import get_logger
from core.planning.config import (
    DEFAULT_ENCODING,
    DEFAULT_HORIZON,
    DEFAULT_PLAN_SOURCE,
    DEFAULT_PROFILE_NAME,
    DEFAULT_TIME_STEP,
    AbstractPlanningConfig,
)
from core.planning.abstract import compute_abstract_plan
from core.planners.factory import PLANNER_TYPES, get_planner

from .utils.arguments import nonnegative_int
from .utils.abstract_plan_log import (
    get_plan_log_path,
    initialize_plan_log,
    record_plan_attempt,
)
from .utils.reporting import print_planning_result


def main():
    parser = _argument_parser()
    args = parser.parse_args()

    planner = get_planner(args.profile)
    planner.validate_configuration(args.abstract_symbol, args.concrete_objects)

    print("Starting")
    plan_log_path, problem_hash = get_plan_log_path(
        args.abstract_problem,
        args.concrete_problem,
        planner.run_directory,
    )
    initialize_plan_log(
        plan_log_path,
        problem_hash,
        args.abstract_problem,
        args.concrete_problem,
        abstract_symbol=args.abstract_symbol,
        concrete_objects=args.concrete_objects,
    )

    config = AbstractPlanningConfig(
        abstract_domain_path=args.abstract_domain,
        abstract_problem_path=args.abstract_problem,
        concrete_domain_path=args.concrete_domain,
        concrete_problem_path=args.concrete_problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
        abstract_symbol=args.abstract_symbol,
        concrete_objects=args.concrete_objects,
        plan_source=args.plan_source,
        profile_name=args.profile,
    )
    result = compute_abstract_plan(
        config,
        attempt_recorder=partial(record_plan_attempt, plan_log_path),
    )

    print_planning_result(result, get_logger())


def _argument_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--profile",
        choices=sorted(PLANNER_TYPES),
        default=DEFAULT_PROFILE_NAME,
        help="Domain-specific mapping and refinement configuration",
    )
    parser.add_argument(
        "--abstract-domain",
        required=True,
        default=argparse.SUPPRESS,
        help="Abstract domain file",
    )
    parser.add_argument(
        "--abstract-problem",
        required=True,
        default=argparse.SUPPRESS,
        help="Abstract problem file",
    )
    parser.add_argument(
        "--concrete-domain",
        required=True,
        default=argparse.SUPPRESS,
        help="Concrete domain file",
    )
    parser.add_argument(
        "--concrete-problem",
        required=True,
        default=argparse.SUPPRESS,
        help="Concrete problem file",
    )
    parser.add_argument(
        "--horizon",
        type=nonnegative_int,
        default=DEFAULT_HORIZON,
        help="Planning horizon; omit to infer it with Fast Downward",
    )
    parser.add_argument(
        "--encoding",
        default=DEFAULT_ENCODING,
        help="ASP encoding type",
    )
    parser.add_argument(
        "--time-step",
        action="store_true",
        default=DEFAULT_TIME_STEP,
        help="Enable time-step based encoding",
    )
    parser.add_argument(
        "--abstract-symbol",
        default=None,
        help="Abstract symbol used in abstraction mapping",
    )
    parser.add_argument(
        "--concrete-objects",
        nargs="+",
        default=None,
        help=(
            "One or more concrete objects mapped to the abstract symbol "
            "(required by the beluga profile)"
        ),
    )
    parser.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default=DEFAULT_PLAN_SOURCE,
        help="Use a Fast Downward plan directly or compute one with Clingo",
    )
    return parser


if __name__ == "__main__":
    main()
