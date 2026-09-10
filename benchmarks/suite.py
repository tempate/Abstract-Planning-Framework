"""Project benchmark suite and the problems an abstraction source accepts.

``SUITE`` holds every domain variant selected from downward-benchmarks'
``suite_satisficing_strips()``. A problem is only worth submitting when some
source can abstract it, so ``SYMMETRIC_PROBLEMS`` lists the ones PDDL Symmetries
reports a class for, read from ``symmetries.txt``, and ``LADDER_PROBLEMS`` lists
the ones the ladder scan accepts, read from ``ladders.txt``. Each file header
carries the command that regenerates it.

``NON_PNF_DOMAINS`` stays out of both files: those domains are not in positive
normal form, so relaxing deletes is not an overapproximation there.
"""

from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent / "downward-benchmarks"
SYMMETRIC_PROBLEMS_FILE = Path(__file__).parent / "symmetries.txt"
LADDER_PROBLEMS_FILE = Path(__file__).parent / "ladders.txt"

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
    "organic-synthesis-sat18-strips",
    "organic-synthesis-split-sat18-strips",
    # "pathways", Excluded: potassco/plasp/issues/14.
    "parcprinter-sat11-strips",
    "parking-sat14-strips",
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
    "spider-sat18-strips",
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

NON_PNF_DOMAINS = [
    "hiking-sat14-strips",
    "mprime",
    "openstacks-sat14-strips",
    "organic-synthesis-sat18-strips",
    "organic-synthesis-split-sat18-strips",
    "quantum-layout-sat23-strips",
]


def _read_problems(path):
    problems = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            domain, _, problem = line.partition("/")
            problems.add((domain, problem))
    return frozenset(problems)


SYMMETRIC_PROBLEMS = _read_problems(SYMMETRIC_PROBLEMS_FILE)
LADDER_PROBLEMS = _read_problems(LADDER_PROBLEMS_FILE)
ABSTRACTABLE_PROBLEMS = SYMMETRIC_PROBLEMS | LADDER_PROBLEMS
