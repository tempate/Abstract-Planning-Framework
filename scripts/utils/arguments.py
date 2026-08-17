"""Argument types shared by planner command-line entry points."""

import argparse


def nonnegative_int(value):
    """Parse a nonnegative integer for argparse."""
    value = int(value)
    if value < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return value


def positive_int(value):
    """Parse a positive integer for argparse."""
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return value
