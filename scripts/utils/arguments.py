"""Argument types shared by planner command-line entry points."""

import argparse


def positive_int(value):
    """Parse a positive integer for argparse."""
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be positive")
    return value
