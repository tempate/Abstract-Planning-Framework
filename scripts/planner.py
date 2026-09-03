"""Solve one PDDL task concretely or through an automatically generated abstraction."""

import argparse

from core.integrations.unified_planning import PddlError
from core.abstraction.factory import AbstractionError
from core.metrics import COUNTER_LABELS, DURATION_LABELS
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from core.planning.config import (
    DEFAULT_ENCODING,
    DEFAULT_HORIZON,
    DEFAULT_PLAN_SOURCE,
    DEFAULT_TIME_STEP,
    AbstractPlanningConfig,
    PlanningConfig,
)
from core.planning.outcomes import PlanningOutcomeError

from .utils.arguments import nonnegative_int, positive_int


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

    abstraction = result.get("abstraction")
    if abstraction is not None:
        print(
            f"Collapsed {sorted(abstraction['objects_to_abstract'])} into {abstraction['abstract_symbol']} "
            f"(type={abstraction['object_type']})"
        )
    print_planning_result(result)
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
                objects_to_abstract=args.objects_to_abstract,
                abstract_name=args.abstract_name,
                symmetry_time_limit=args.symmetry_time_limit,
                plan_source=args.plan_source,
            )
        )
    raise ValueError(f"Unknown planning mode: {args.mode}")


def print_planning_result(result):
    """Print a planning result."""
    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plan found: {'yes' if result['plan'] is not None else 'no'}")
    _print_metrics(result["metrics"])

    if result["plan"] is not None:
        print("\nPlan:")
        plan_actions = [atom for atom in result["plan"] if atom.startswith("occurs(")]
        for atom in sorted(plan_actions, key=_time_step):
            print(" ", atom)


def _time_step(atom):
    return int(str(atom).split(",")[-1].rstrip(")"))


def _print_metrics(metrics):
    print("\nMetrics:")
    _print_metric_group("Durations (seconds)", metrics["durations"], DURATION_LABELS, lambda value: f"{value:.6f}")
    _print_metric_group("Solver activity", metrics["counters"], COUNTER_LABELS, lambda value: str(int(value)))


def _print_metric_group(title, values, labels, format_value):
    present = [(labels[name], format_value(values[name])) for name in labels if name in values]
    if not present:
        return

    width = max(len(label) for label, _ in present)
    print(f"  {title}:")
    for label, value in present:
        print(f"    {label:<{width}}  {value}")


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
    abstract.add_argument("--objects-to-abstract", nargs="+", help="Objects to collapse; omit to use PDDL Symmetries")
    abstract.add_argument("--abstract-name", help="Name of the collapsed object")
    abstract.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default=DEFAULT_PLAN_SOURCE,
        help="Use a Fast Downward plan directly or compute one with Clingo",
    )
    abstract.add_argument(
        "--symmetry-time-limit", type=positive_int, default=300, help="Symmetry discovery time limit in seconds"
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
