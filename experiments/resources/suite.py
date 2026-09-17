"""The resource-abstraction track: the satisficing suite, restricted to tasks with a resource.

The problems are the symmetry track's, since both plan the same benchmarks.
What differs is which of them are worth submitting: ``RUNNABLE_PROBLEMS`` lists
the ones numeric-fast-downward's detector finds a resource variable for, read
from ``resources.txt``, whose header carries the command that regenerates it.
"""

from pathlib import Path

from experiments import DOWNWARD_BENCHMARKS_DIR, read_problems
from experiments.symmetries.suite import SUITE

__all__ = ["BENCHMARKS_DIR", "RUNNABLE_PROBLEMS", "SUITE"]

BENCHMARKS_DIR = DOWNWARD_BENCHMARKS_DIR
RUNNABLE_PROBLEMS_FILE = Path(__file__).parent / "resources.txt"
RUNNABLE_PROBLEMS = read_problems(RUNNABLE_PROBLEMS_FILE)
