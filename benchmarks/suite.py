"""Project benchmark suite and the problems an abstraction source accepts.

``SUITE`` holds the domain variants from downward-benchmarks'
``suite_satisficing_strips()`` that the abstraction can actually run. A problem
is only worth submitting when some source can abstract it, so
``SYMMETRIC_PROBLEMS`` lists the ones PDDL Symmetries reports a class for, read
from ``symmetries.txt``, whose header carries the command that regenerates it
from a collected run, and ``LADDER_PROBLEMS`` lists the ones the ladder scan
accepts, read from ``ladders.txt``.

``NON_PNF_DOMAINS`` holds what ``SUITE`` leaves out, grouped by why.
``python -m scripts.scan_pnf`` derives both groups from the PDDL.
"""

from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent / "downward-benchmarks"
SYMMETRIC_PROBLEMS_FILE = Path(__file__).parent / "symmetries.txt"
LADDER_PROBLEMS_FILE = Path(__file__).parent / "ladders.txt"

SUITE = [
    "airport",
    "barman-sat14-strips",
    "blocks",
    "childsnack-sat14-strips",
    "depot",
    "driverlog",
    "elevators-sat11-strips",
    "floortile-sat14-strips",
    "freecell",
    "grid",
    "gripper",
    "logistics00",
    "logistics98",
    "miconic",
    "movie",
    "mystery",
    "nomystery-sat11-strips",
    "openstacks-sat14-strips",
    "parcprinter-sat11-strips",
    "parking-sat14-strips",
    # "pathways", Excluded: potassco/plasp/issues/14.
    "pegsol-sat11-strips",
    "pipesworld-notankage",
    "pipesworld-tankage",
    "psr-small",
    "rovers",
    "satellite",
    "scanalyzer-sat11-strips",
    "sokoban-sat11-strips",
    # "storage", Excluded: aiplan4eu/unified-planning/issues/817.
    "thoughtful-sat14-strips",
    "tpp",
    "transport-sat14-strips",
    "trucks-strips",
    "visitall-sat14-strips",
    "woodworking-sat11-strips",
    "zenotravel",
]

NON_PNF_DOMAINS = [
    # NEEDS_PNF: negates a predicate that some action also deletes, so relaxing
    # that delete can make the negation false and lose plans the concrete task
    # has. openstacks negates too, but nothing deletes what it negates, so it
    # stays in SUITE.
    # agricola also fails earlier: its fluent-valued costs round-trip to
    # :numeric-fluents, which the translator rejects.
    "agricola-sat18-strips",
    "data-network-sat18-strips",
    "quantum-layout-sat23-strips",
    "snake-sat18-strips",
    "spider-sat18-strips",
    "termes-sat18-strips",
    "tidybot-sat11-strips",
    # INEQUALITY: every negated condition is (not (= ?x ?y)), which relaxing a
    # delete cannot reach. Collapsing two objects into one symbol does reach it,
    # since it makes the two sides equal.
    "ged-sat14-strips",
    "hiking-sat14-strips",
    "mprime",
    "organic-synthesis-sat18-strips",
    "organic-synthesis-split-sat18-strips",
    "tetris-sat14-strips",
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
