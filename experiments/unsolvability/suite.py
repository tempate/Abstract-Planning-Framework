"""The unsolvability benchmark suite, the FINAL domains of unsolve-ipc-2016.

The problems known to be unsolvable are the probNN of each domain: satprobNN is
the solvable twin beside it and unknownprobNN was never settled. Both are skipped
by name in ``experiments.submit``. Of those, ``SYMMETRIC_PROBLEMS`` lists the
ones worth submitting, read from ``symmetries.txt``, whose header carries the
command that regenerates it from a collected run.
"""

from pathlib import Path

from experiments import UNSOLVE_IPC_DIR, read_problems

BENCHMARKS_DIR = UNSOLVE_IPC_DIR
SYMMETRIC_PROBLEMS_FILE = Path(__file__).parent / "symmetries.txt"

SUITE = [
    "bag-barman",
    "bag-gripper",
    "bag-transport",
    "bottleneck",
    "cave-diving",
    "chessboard-pebbling",
    "diagnosis",
    "document-transfer",
    "over-nomystery",
    "over-rovers",
    "over-tpp",
    "pegsol",
    "pegsol-row5",
    "sliding-tiles",
    "tetris",
]


SYMMETRIC_PROBLEMS = read_problems(SYMMETRIC_PROBLEMS_FILE)
