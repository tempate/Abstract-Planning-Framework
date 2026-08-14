import argparse

from core.execution import get_logger
from core.planning.concrete import compute_concrete_plan

from .utils.arguments import nonnegative_int
from .utils.reporting import print_planning_result


def main():
    parser = _argument_parser()
    args = parser.parse_args()

    print("Starting")

    result = compute_concrete_plan(
        domain_path=args.domain,
        problem_path=args.problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
    )

    print_planning_result(result, get_logger())


def _argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--horizon", type=nonnegative_int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")
    return parser


if __name__ == "__main__":
    main()
