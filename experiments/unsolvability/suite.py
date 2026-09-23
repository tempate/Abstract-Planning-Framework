"""The unsolvability benchmark suite, the FINAL domains of unsolve-ipc-2016.

The problems known to be unsolvable are the probNN of each domain: satprobNN is
the solvable twin beside it and unknownprobNN was never settled. Both are skipped
by name in ``experiments.submit``. Of those, ``symmetries.txt`` lists the
ones worth submitting, whose header carries the
command that regenerates it from a collected run.
"""

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
