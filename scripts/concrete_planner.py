import argparse

from core.execution import get_logger
from core.planning.config import (
    DEFAULT_ENCODING,
    DEFAULT_HORIZON,
    DEFAULT_TIME_STEP,
    ConcretePlanningConfig,
)
from core.planning.concrete import compute_concrete_plan

from .utils.arguments import nonnegative_int
from .utils.reporting import print_planning_result


def main():
    parser = _argument_parser()
    args = parser.parse_args()

    print("Starting")

    config = ConcretePlanningConfig(
        domain_path=args.domain,
        problem_path=args.problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
    )
    result = compute_concrete_plan(config)

    print_planning_result(result, get_logger())


def _argument_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--domain",
        required=True,
        default=argparse.SUPPRESS,
        help="Concrete domain file",
    )
    parser.add_argument(
        "--problem",
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
    return parser


if __name__ == "__main__":
    main()
