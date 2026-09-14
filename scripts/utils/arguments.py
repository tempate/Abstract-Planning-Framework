"""Argument types shared by planner command-line entry points."""

import argparse


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
    return parser
