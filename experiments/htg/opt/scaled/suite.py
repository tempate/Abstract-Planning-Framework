"""The scaled HTG opt suite, one <domain>/size-N directory per domain and class size. See README.md."""

from experiments.ipc.opt.scaled.suite import SIZES

# Up to three problems per domain of opt-htg/symmetries that LMcut and LMcutᵅ both
# solve with their best class, those with the smallest best class first. In
# pipesworld-tankage the copies never join the class, so it has none.
BASE_PROBLEMS = (
    "blocksworld-large-simple/goal-3/p-100-3.pddl",
    "blocksworld-large-simple/goal-4/p-100-4.pddl",
    "blocksworld-large-simple/goal-5/p-100-5.pddl",
    "childsnack-contents/parsize1-cham3/contentam1-p0.pddl",
    "childsnack-contents/parsize1-cham3/contentam3-p0.pddl",
    "childsnack-contents/parsize1-cham3/contentam3-p5.pddl",
    "logistics-large-simple/goal-2/p-a1-c1-s1000-p10-t1-g2.pddl",
    "logistics-large-simple/goal-3/p-a1-c1-s1000-p10-t1-g3.pddl",
    "logistics-large-simple/goal-4/p-a1-c1-s1000-p10-t1-g4.pddl",
    "organic-synthesis-alkene/p10.pddl",
    "organic-synthesis-alkene/p11.pddl",
    "organic-synthesis-alkene/p12.pddl",
    "rovers-large-simple/goal-2/p-r1-w1500-o1-1-g2.pddl",
    "rovers-large-simple/goal-4/p-r1-w1000-o1-1-g4.pddl",
    "rovers-large-simple/goal-4/p-r1-w1500-o1-1-g4.pddl",
)
# The class sizes the base problems start from beyond SIZES.
BASE_SIZES = (94, 95, 96, 985, 986, 987)
DOMAINS = sorted({problem.rsplit("/", 1)[0] for problem in BASE_PROBLEMS})
SUITE = [f"{domain}/size-{size}" for domain in DOMAINS for size in sorted(SIZES + BASE_SIZES)]
