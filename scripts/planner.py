"""Solve one PDDL task concretely or through an automatically generated abstraction."""

import argparse

from core.planning import abstraction, asp, fd
from core.planning.config import AbstractPlanningConfig, PlanningConfig

from .utils.arguments import abstraction_arguments, task_arguments
from .utils.entry import run
from .utils.reporting import print_metrics, progress_callback


def main():
    return run(_argument_parser(), _compute, _report)


def _report(result):
    print_planning_result(result)
    return 0 if result["success"] else 1


def _compute(args):
    on_update = progress_callback()
    common = {"domain_path": args.domain, "problem_path": args.problem}
    config = PlanningConfig(**common)

    if args.mode == "asp":
        return asp.solve(config, on_update)
    if args.mode == "fd":
        return fd.solve(config, on_update)

    config = AbstractPlanningConfig(
        **common,
        objects_to_abstract=args.objects_to_abstract,
        abstract_name=args.abstract_name,
        symmetry_time_limit=args.symmetry_time_limit,
        abstraction_source=args.abstraction_source,
    )

    if args.mode == "abstraction-asp":
        return abstraction.solve(config, asp.find_abstract_plan, on_update)
    if args.mode == "abstraction-fd":
        return abstraction.solve(config, fd.find_abstract_plan, on_update)


def print_planning_result(result):
    """Print a planning result."""
    print("\n=== RESULT ===")
    print(f"Plan found: {'yes' if result['plan'] is not None else 'no'}")
    if result.get("plan_valid"):
        print(f"Plan valid: {result['plan_valid']}")

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
        "asp",
        parents=[shared],
        help="Solve the task with ASP",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "fd",
        parents=[shared],
        help="Solve the task with Fast Downward's lama-first",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "abstraction-asp",
        parents=[shared, abstract],
        help="Find an abstract plan with ASP, then refine it with ASP",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    modes.add_parser(
        "abstraction-fd",
        parents=[shared, abstract],
        help="Find an abstract plan with Fast Downward's lama-first, then refine it with ASP",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
