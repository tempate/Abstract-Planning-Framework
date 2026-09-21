"""Solve one PDDL task concretely or through an automatically generated abstraction."""

import argparse

from core.integrations.unified_planning import PddlError
from core.abstraction.factory import AbstractionError
from core.outcomes import PlanningOutcomeError
from core.planning.abstract import solve_via_abstraction
from core.planning.concrete import solve_with_asp
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.baseline import solve_directly

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
    common = {"domain_path": args.domain, "problem_path": args.problem}
    if args.mode == "concrete":
        return solve_with_asp(PlanningConfig(**common), on_update)
    if args.mode == "lama":
        return solve_directly(PlanningConfig(**common), on_update)
    if args.mode == "abstract":
        return solve_via_abstraction(
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
    print(f"Plan found: {'yes' if result['plan'] is not None else 'no'}")
    if result.get("plan_valid"):
        print(f"Plan valid: {result['plan_valid']}")

    # The horizon surrounds every abstract action with a gap for one optional
    # concrete action, so it roughly doubles the plan a reader wants to see.
    length = result["metrics"]["counters"].get("plan_length")
    if result["plan"] is not None:
        print(f"Plan length: {length}")
    print_metrics(result["metrics"])

    if result["plan"] is not None:
        print(f"\nPlan ({length} actions):")
        for action in _ordered_actions(result["plan"]):
            print(" ", action)


def _ordered_actions(plan):
    """Order a plan for reading: our own by time step, an external one as given."""
    occurrences = [atom for atom in plan if atom.startswith("occurs(")]
    return sorted(occurrences, key=_time_step) if occurrences else plan


def _time_step(atom):
    return int(str(atom).split(",")[-1].rstrip(")"))


def _argument_parser():
    shared = task_arguments()
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
        "lama",
        parents=[shared],
        help="Solve with plain Fast Downward as a baseline",
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
