"""Project benchmark suite grouped by observed object symmetries.

The domain variants come from downward-benchmarks'
``suite_satisficing_strips()``. ``SYMMETRIC_DOMAINS`` retains the variants for
which PDDL Symmetries produced a valid abstraction class for at least one task
in the benchmark results; ``NON_SYMMETRIC_DOMAINS`` contains the remaining
selected variants. ``SYMMETRIC_NON_PNF_DOMAINS`` holds symmetric variants kept out of the
experiments because they are not in positive normal form, so relaxing deletes
is not an overapproximation there. All three groups remain in ``SUITE``.

A symmetric domain still holds individual tasks without an abstraction class.
``NON_SYMMETRIC_PROBLEMS`` lists those, read from ``no-symmetries.txt``.
"""

from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent / "downward-benchmarks"
NON_SYMMETRIC_PROBLEMS_FILE = Path(__file__).parent / "no-symmetries.txt"

SYMMETRIC_DOMAINS = [
    "barman-sat14-strips",
    "childsnack-sat14-strips",
    "elevators-sat11-strips",
    "nomystery-sat11-strips",
    "sokoban-sat11-strips",
    "woodworking-sat11-strips",
    # "pathways", Excluded: potassco/plasp/issues/14.
    "pipesworld-tankage",
    "tpp",
    "airport",
    "depot",
    "driverlog",
    "gripper",
    "logistics00",
    "logistics98",
    "miconic",
    "mystery",
    "pipesworld-notankage",
    "satellite",
    "zenotravel",
]

SYMMETRIC_NON_PNF_DOMAINS = [
    "quantum-layout-sat23-strips",
    "organic-synthesis-sat18-strips",
    "organic-synthesis-split-sat18-strips",
    "hiking-sat14-strips",
    "openstacks-sat14-strips",
    "mprime",
]

NON_SYMMETRIC_DOMAINS = [
    "agricola-sat18-strips",
    "data-network-sat18-strips",
    "snake-sat18-strips",
    "spider-sat18-strips",
    "termes-sat18-strips",
    "floortile-sat14-strips",
    "ged-sat14-strips",
    "parking-sat14-strips",
    "tetris-sat14-strips",
    "thoughtful-sat14-strips",
    "transport-sat14-strips",
    "visitall-sat14-strips",
    "parcprinter-sat11-strips",
    "pegsol-sat11-strips",
    "scanalyzer-sat11-strips",
    "tidybot-sat11-strips",
    "rovers",
    # "storage", Excluded: aiplan4eu/unified-planning/issues/817.
    "trucks-strips",
    "blocks",
    "freecell",
    "grid",
    "movie",
    "psr-small",
]

SUITE = SYMMETRIC_DOMAINS + SYMMETRIC_NON_PNF_DOMAINS + NON_SYMMETRIC_DOMAINS


def _read_non_symmetric_problems(path=NON_SYMMETRIC_PROBLEMS_FILE):
    problems = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            domain, _, problem = line.partition("/")
            problems.add((domain, problem))
    return frozenset(problems)


NON_SYMMETRIC_PROBLEMS = _read_non_symmetric_problems()
