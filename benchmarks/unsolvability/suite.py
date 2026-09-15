"""The unsolvability benchmark suite, the FINAL domains of unsolve-ipc-2016.

There is no symmetries file for this collection, so every problem known to be
unsolvable runs, which is the probNN of each domain: satprobNN is the solvable
twin beside it and unknownprobNN was never settled. Both are skipped by name in
``scripts.experiments.submit``.
"""

from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent / "unsolve-ipc-2016"

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
