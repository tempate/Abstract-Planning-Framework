"""Argument types shared by planner command-line entry points."""

import argparse

from core.planning.config import ABSTRACTION_SOURCES, SYMMETRIES, AbstractPlanningConfig, PlanningConfig


def positive_int(value):
    """Parse a positive integer for argparse."""
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return value


def task_arguments():
    """Parent parser for the concrete PDDL task every entry point takes."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--domain", required=True, default=argparse.SUPPRESS, help="Concrete domain PDDL")
    parser.add_argument("--problem", required=True, default=argparse.SUPPRESS, help="Concrete problem PDDL")
    return parser


def abstraction_arguments():
    """Parent parser for the options that choose the collapsed object class."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--objects-to-abstract", nargs="+", help="Objects to collapse; omit to use PDDL Symmetries")
    parser.add_argument("--abstract-name", help="Name of the collapsed object")
    parser.add_argument(
        "--symmetry-time-limit", type=positive_int, default=300, help="Symmetry discovery time limit in seconds"
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
        help="Find a shortest plan, without the doubling horizons and gaps that find one sooner",
    )
    return parser


def planning_config(args):
    """The configuration the task arguments describe."""
    optimize = getattr(args, "optimize", False)
    return PlanningConfig(args.domain, args.problem, planner=args.mode, optimize=optimize)


def abstract_planning_config(args):
    """The configuration the task and abstraction arguments describe."""
    return AbstractPlanningConfig(
        args.domain,
        args.problem,
        planner=args.mode.removeprefix("abs-"),
        optimize=getattr(args, "optimize", False),
        objects_to_abstract=args.objects_to_abstract,
        abstract_name=args.abstract_name,
        symmetry_time_limit=args.symmetry_time_limit,
        abstraction_source=args.abstraction_source,
        class_rank=args.class_rank,
    )
