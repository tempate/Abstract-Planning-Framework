"""Command-line entry point for abstraction-based planning."""

import argparse
from functools import partial

from core.execution import get_logger
from core.planning.abstract import refine_abstract_plan
from core.planners.factory import PLANNER_TYPES, get_planner

from .utils.abstract_plan_log import (
    get_plan_log_path,
    initialize_plan_log,
    record_plan_attempt,
)
from .utils.reporting import print_planning_result, save_result_summary


def _argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--profile",
        choices=sorted(PLANNER_TYPES),
        default="beluga",
        help="Domain-specific mapping and refinement configuration",
    )
    parser.add_argument("--abstract-domain", required=True)
    parser.add_argument("--abstract-problem", required=True)
    parser.add_argument("--concrete-domain", required=True)
    parser.add_argument("--concrete-problem", required=True)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")
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
    parser.add_argument("--mode", choices=["inc", "dec"], default="inc")
    parser.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default="clingo",
        help="Use a Fast Downward plan directly or compute one with Clingo",
    )
    return parser


def main():
    parser = _argument_parser()
    args = parser.parse_args()

    planner = get_planner(args.profile)
    try:
        planner.validate_configuration(args.abstract_symbol, args.concrete_objects)
    except ValueError as error:
        parser.error(str(error))

    print("Starting")
    result = compute_concrete_from_abstract(
        abstract_domain_path=args.abstract_domain,
        abstract_problem_path=args.abstract_problem,
        concrete_domain_path=args.concrete_domain,
        concrete_problem_path=args.concrete_problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
        abstract_symbol=args.abstract_symbol,
        concrete_objects=args.concrete_objects,
        solving_mode=args.mode,
        plan_source=args.plan_source,
        profile_name=args.profile,
    )

    print_planning_result(result, get_logger())
    save_result_summary(args.abstract_problem, "abstract", args.mode, result)


def compute_concrete_from_abstract(
    abstract_domain_path,
    abstract_problem_path,
    concrete_domain_path,
    concrete_problem_path,
    horizon=None,
    encoding="exact",
    time_step=False,
    abstract_symbol=None,
    concrete_objects=None,
    solving_mode="inc",
    plan_source="clingo",
    profile_name="beluga",
    refinement_filter=None,
):
    """Run core planning while persisting script-level experiment history."""
    planner = get_planner(profile_name)
    planner.validate_configuration(abstract_symbol, concrete_objects)

    plan_log_path, problem_hash = get_plan_log_path(
        abstract_problem_path,
        concrete_problem_path,
        planner.run_directory,
    )
    initialize_plan_log(
        plan_log_path,
        problem_hash,
        abstract_problem_path,
        concrete_problem_path,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects,
    )

    return refine_abstract_plan(
        abstract_domain_path=abstract_domain_path,
        abstract_problem_path=abstract_problem_path,
        concrete_domain_path=concrete_domain_path,
        concrete_problem_path=concrete_problem_path,
        horizon=horizon,
        encoding=encoding,
        time_step=time_step,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects,
        solving_mode=solving_mode,
        plan_source=plan_source,
        profile_name=profile_name,
        refinement_filter=refinement_filter,
        attempt_recorder=partial(record_plan_attempt, plan_log_path),
    )


if __name__ == "__main__":
    main()
