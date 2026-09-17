"""The satisficing benchmark suite and the problems an abstraction source accepts.

``SUITE`` holds the domain variants from downward-benchmarks'
``suite_satisficing_strips()`` the experiments run, with what the abstraction
cannot read commented out. Two markers flag a domain whose results are not
sound yet, both derived from the PDDL by ``python -m scripts.scan_pnf``:
``# PNF.`` negates a predicate some action also deletes, so relaxing that
delete can falsify the negation and lose plans, and the problem has to reach
PNF first; ``# Inequality.`` negates only ``(= ?x ?y)``, which
no relaxed delete reaches, but which collapsing two objects into one symbol
does, by making the two sides equal.

A problem is only worth submitting when some source can abstract it, so
``SYMMETRIC_PROBLEMS`` lists the ones PDDL Symmetries reports a class for, read
from ``symmetries.txt``, whose header carries the command that regenerates it
from a collected run.
"""

from pathlib import Path

from experiments import read_problems

BENCHMARKS_DIR = Path(__file__).parent / "downward-benchmarks"
SYMMETRIC_PROBLEMS_FILE = Path(__file__).parent / "symmetries.txt"

SUITE = [
    "agricola-sat18-strips",
    "airport",
    "barman-sat14-strips",
    "blocks",
    "childsnack-sat14-strips",
    "data-network-sat18-strips",
    "depot",
    "driverlog",
    "elevators-sat11-strips",
    "floortile-sat14-strips",
    "freecell",
    "ged-sat14-strips",
    "grid",
    "gripper",
    "hiking-sat14-strips",
    "logistics00",
    "logistics98",
    "miconic",
    "movie",
    "mprime",
    "mystery",
    "nomystery-sat11-strips",
    "openstacks-sat14-strips",
    # "organic-synthesis-sat18-strips", and
    # "organic-synthesis-split-sat18-strips", Excluded: both declare element
    # types they never instantiate, and unified-planning refuses to translate
    # (not (= ?x ?y)) over a type with no objects to expand the pair over.
    "parcprinter-sat11-strips",
    "parking-sat14-strips",
    # "pathways", Excluded: potassco/plasp/issues/14.
    "pegsol-sat11-strips",
    "pipesworld-notankage",
    "pipesworld-tankage",
    "psr-small",
    "quantum-layout-sat23-strips",
    "rovers",
    "satellite",
    "scanalyzer-sat11-strips",
    "snake-sat18-strips",
    "sokoban-sat11-strips",
    # "spider-sat18-strips", Excluded: uses (when ...).
    # "storage", Excluded: aiplan4eu/unified-planning/issues/817.
    "termes-sat18-strips",
    "tetris-sat14-strips",
    "thoughtful-sat14-strips",
    "tidybot-sat11-strips",
    "tpp",
    "transport-sat14-strips",
    "trucks-strips",
    "visitall-sat14-strips",
    "woodworking-sat11-strips",
    "zenotravel",
]


SYMMETRIC_PROBLEMS = read_problems(SYMMETRIC_PROBLEMS_FILE)
