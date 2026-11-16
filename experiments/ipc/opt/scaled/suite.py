"""The scaled opt suite, one <domain>/size-N directory per domain and class size. See README.md."""

SIZES = (2, 3, 5, 10, 20, 50, 100, 200, 500, 1000)
# Up to three problems per domain of opt/symmetries that LMcut and LMcutᵅ both solve
# with the largest class, the class each of them grows. In pipesworld, quantum-layout
# and satellite the copies never join the class, so those domains have none.
BASE_PROBLEMS = (
    "airport/p01-airport1-p1.pddl",
    "airport/p02-airport1-p1.pddl",
    "airport/p03-airport1-p2.pddl",
    "depot/p02.pddl",
    "depot/p04.pddl",
    "driverlog/p01.pddl",
    "driverlog/p02.pddl",
    "driverlog/p03.pddl",
    "gripper/prob01.pddl",
    "gripper/prob02.pddl",
    "gripper/prob03.pddl",
    "hiking-opt14-strips/ptesting-1-2-3.pddl",
    "hiking-opt14-strips/ptesting-1-2-4.pddl",
    "hiking-opt14-strips/ptesting-1-2-5.pddl",
    "logistics00/probLOGISTICS-11-0.pddl",
    "logistics00/probLOGISTICS-4-0.pddl",
    "logistics00/probLOGISTICS-4-1.pddl",
    "logistics98/prob05.pddl",
    "miconic/s7-0.pddl",
    "mprime/prob02.pddl",
    "mprime/prob05.pddl",
    "mprime/prob08.pddl",
    "mystery/prob09.pddl",
    "mystery/prob28.pddl",
    "nomystery-opt11-strips/p03.pddl",
    "nomystery-opt11-strips/p13.pddl",
    "sokoban-opt08-strips/p06.pddl",
    "sokoban-opt08-strips/p12.pddl",
    "sokoban-opt11-strips/p01.pddl",
    "sokoban-opt11-strips/p14.pddl",
    "tpp/p02.pddl",
    "tpp/p03.pddl",
    "tpp/p04.pddl",
    "transport-opt08-strips/p01.pddl",
    "transport-opt08-strips/p11.pddl",
    "transport-opt08-strips/p21.pddl",
    "transport-opt14-strips/p01.pddl",
    "visitall-opt11-strips/problem02-full.pddl",
    "zenotravel/p05.pddl",
    "zenotravel/p07.pddl",
    "zenotravel/p08.pddl",
)
# The class sizes the base problems start from beyond SIZES.
BASE_SIZES = (4, 6, 8)
DOMAINS = sorted({problem.split("/")[0] for problem in BASE_PROBLEMS})
SUITE = [f"{domain}/size-{size}" for domain in DOMAINS for size in sorted(SIZES + BASE_SIZES)]
