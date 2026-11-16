"""Argument types shared by planner command-line entry points."""

import argparse
from pathlib import Path

from core.utilities.config import ABSTRACTION_SOURCES, SYMMETRIES, AbstractPlanningConfig, PlanningConfig


def positive_int(value):
    """Parse a positive integer for argparse."""
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return value


def task_arguments():
    """Parent parser for the concrete PDDL task every entry point takes."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--domain", help="Concrete domain PDDL; omit to use the domain file beside the problem")
    parser.add_argument("--problem", required=True, default=argparse.SUPPRESS, help="Concrete problem PDDL")
    return parser


def abstraction_arguments():
    """Parent parser for the options that choose the collapsed object class."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--objects-to-abstract", nargs="+", help="Objects to collapse; omit to take them from the abstraction source"
    )
    parser.add_argument(
        "--abstraction-source",
        choices=ABSTRACTION_SOURCES,
        default=SYMMETRIES,
        help="Where the collapsed class comes from",
    )
    parser.add_argument(
        "--class-rank",
        type=int,
        default=0,
        help="Collapse the candidate class at this rank, counting from the largest (0)",
    )
    return parser


def optimize_arguments():
    """Parent parser for the modes that can find a shortest plan."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--optimize",
        action="store_true",
        help="Find a shortest plan",
    )
    return parser


def planning_config(args):
    """The configuration the task arguments describe."""
    optimize = getattr(args, "optimize", False)
    return PlanningConfig(_domain(args), args.problem, planner=args.mode, optimize=optimize)


def abstract_planning_config(args):
    """The configuration the task and abstraction arguments describe."""
    # An optimal abstract plan is wasted on a refinement with gaps, so both abs-lmcut modes always optimize.
    optimize = args.mode in ("abs-lmcut", "abs-lmcut-symmetry-pruning") or getattr(args, "optimize", False)
    return AbstractPlanningConfig(
        _domain(args),
        args.problem,
        planner=args.mode.removeprefix("abs-"),
        optimize=optimize,
        objects_to_abstract=args.objects_to_abstract,
        abstraction_source=args.abstraction_source,
        class_rank=args.class_rank,
    )


def _domain(args):
    return args.domain if args.domain is not None else find_domain(Path(args.problem))


def find_domain(problem):
    """Find the domain file using the naming conventions of the benchmark collections."""
    candidates = [
        "domain.pddl",
        f"{problem.stem}-domain{problem.suffix}",
        f"{problem.name[:3]}-domain.pddl",
        f"domain_{problem.name}",
        f"domain-{problem.name}",
    ]

    for name in candidates:
        domain = problem.parent / name
        if domain.is_file():
            return domain

    raise FileNotFoundError(f"No domain file found for {problem}")
