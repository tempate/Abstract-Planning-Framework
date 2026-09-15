"""Solve one PDDL task concretely or through an automatically generated abstraction."""

import argparse

from core.integrations.unified_planning import PddlError
from core.abstraction.factory import AbstractionError
from core.outcomes import PlanningOutcomeError
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from core.planning.config import DEFAULT_TIME_STEP, AbstractPlanningConfig, PlanningConfig

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

    print_planning_result(result)
    return 0 if result["success"] else 1


def _compute(args):
    on_update = progress_callback()
    common = {"domain_path": args.domain, "problem_path": args.problem, "time_step": args.time_step}
    if args.mode == "concrete":
        return compute_concrete_plan(PlanningConfig(**common), on_update)
    if args.mode == "abstract":
        return compute_abstract_plan(
            AbstractPlanningConfig(
                **common,
                objects_to_abstract=args.objects_to_abstract,
                abstract_name=args.abstract_name,
                symmetry_time_limit=args.symmetry_time_limit,
            ),
            on_update,
        )
    raise ValueError(f"Unknown planning mode: {args.mode}")


def print_planning_result(result):
    """Print a planning result."""
    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plan found: {'yes' if result['plan'] is not None else 'no'}")
    print_metrics(result["metrics"])

    if result["plan"] is not None:
        print(f"\nPlan ({result['plan_length']} actions):")
        plan_actions = [atom for atom in result["plan"] if atom.startswith("occurs(")]
        for atom in sorted(plan_actions, key=_time_step):
            print(" ", atom)


def _time_step(atom):
    return int(str(atom).split(",")[-1].rstrip(")"))


def _argument_parser():
    shared = task_arguments()
    shared.add_argument(
        "--time-step", action="store_true", default=DEFAULT_TIME_STEP, help="Enable time-step based encoding"
    )
    abstract = abstraction_arguments()

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
