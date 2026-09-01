"""Project benchmark suite grouped by observed object symmetries.

The domain variants come from downward-benchmarks'
``suite_satisficing_strips()``. ``SYMMETRIC_DOMAINS`` retains the variants for
which PDDL Symmetries produced a valid abstraction class for at least one task
in the benchmark results; ``NON_SYMMETRIC_DOMAINS`` contains the remaining
selected variants. Both groups remain in ``SUITE``.
"""

from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent / "downward-benchmarks"

SYMMETRIC_DOMAINS = [
    # IPC 2023
    "quantum-layout-sat23-strips",
    # IPC 2018
    "organic-synthesis-sat18-strips",
    "organic-synthesis-split-sat18-strips",
    # IPC 2014
    "barman-sat14-strips",
    "childsnack-sat14-strips",
    "hiking-sat14-strips",
    "openstacks-sat14-strips",
    # IPC 2011 (no newer satisficing STRIPS formulation)
    "elevators-sat11-strips",
    "nomystery-sat11-strips",
    "sokoban-sat11-strips",
    "woodworking-sat11-strips",
    # IPC 2006 (no newer satisficing STRIPS formulation)
    "pathways",
    "pipesworld-tankage",
    "tpp",
    # IPC 1998--2004 (no newer satisficing STRIPS formulation)
    "airport",
    "depot",
    "driverlog",
    "gripper",
    "logistics00",
    "logistics98",
    "miconic",
    "mprime",
    "mystery",
    "pipesworld-notankage",
    "satellite",
    "zenotravel",
]

NON_SYMMETRIC_DOMAINS = [
    # IPC 2018
    "agricola-sat18-strips",
    "data-network-sat18-strips",
    "snake-sat18-strips",
    "spider-sat18-strips",
    "termes-sat18-strips",
    # IPC 2014
    "floortile-sat14-strips",
    "ged-sat14-strips",
    "parking-sat14-strips",
    "tetris-sat14-strips",
    "thoughtful-sat14-strips",
    "transport-sat14-strips",
    "visitall-sat14-strips",
    # IPC 2011 (no newer satisficing STRIPS formulation)
    "parcprinter-sat11-strips",
    "pegsol-sat11-strips",
    "scanalyzer-sat11-strips",
    "tidybot-sat11-strips",
    # IPC 2006 (no newer satisficing STRIPS formulation)
    "rovers",
    # Temporarily excluded: Unified Planning cannot convert standard
    # ``(either ...)`` parameter types (aiplan4eu/unified-planning#817).
    # "storage",
    "trucks-strips",
    # IPC 1998--2004 (no newer satisficing STRIPS formulation)
    "blocks",
    "freecell",
    "grid",
    "movie",
    "psr-small",
]

SUITE = SYMMETRIC_DOMAINS + NON_SYMMETRIC_DOMAINS
