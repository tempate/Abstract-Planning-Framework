from core.planners.BelugaPlanner import BelugaPlanner
from core.planners.NoMysteryPlanner import NoMysteryPlanner

PLANNER_TYPES = ("beluga", "no_mystery")


def get_planner(name):
    if name == "beluga":
        return BelugaPlanner()
    elif name == "no_mystery":
        return NoMysteryPlanner()

    raise ValueError(f"Unknown profile: {name}.")
