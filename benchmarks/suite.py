"""Project benchmark suite.

The suite contains the latest satisficing STRIPS formulation of each named
domain selected from downward-benchmarks. The classification comes from
downward-benchmarks' ``suite_satisficing_strips()`` rather than directory-name
suffixes. Distinct named variants such as ``organic-synthesis-split`` are
retained.
"""

from pathlib import Path

BENCHMARKS_DIR = Path(__file__).parent / "downward-benchmarks"

SUITE = [
    # IPC 2023
    "quantum-layout-sat23-strips",
    # IPC 2018
    "agricola-sat18-strips",
    "data-network-sat18-strips",
    "organic-synthesis-sat18-strips",
    "organic-synthesis-split-sat18-strips",
    "snake-sat18-strips",
    "spider-sat18-strips",
    "termes-sat18-strips",
    # IPC 2014
    "barman-sat14-strips",
    "childsnack-sat14-strips",
    "floortile-sat14-strips",
    "ged-sat14-strips",
    "hiking-sat14-strips",
    "openstacks-sat14-strips",
    "parking-sat14-strips",
    "tetris-sat14-strips",
    "thoughtful-sat14-strips",
    "transport-sat14-strips",
    "visitall-sat14-strips",
    # IPC 2011 (no newer satisficing STRIPS formulation)
    "elevators-sat11-strips",
    "nomystery-sat11-strips",
    "parcprinter-sat11-strips",
    "pegsol-sat11-strips",
    "scanalyzer-sat11-strips",
    "sokoban-sat11-strips",
    "tidybot-sat11-strips",
    "woodworking-sat11-strips",
    # IPC 2006 (no newer satisficing STRIPS formulation)
    "pathways",
    "pipesworld-tankage",
    "rovers",
    "storage",
    "tpp",
    "trucks-strips",
    # IPC 1998--2004 (no newer satisficing STRIPS formulation)
    "airport",
    "blocks",
    "depot",
    "driverlog",
    "freecell",
    "grid",
    "gripper",
    "logistics00",
    "logistics98",
    "miconic",
    "movie",
    "mprime",
    "mystery",
    "pipesworld-notankage",
    "psr-small",
    "satellite",
    "zenotravel",
]
