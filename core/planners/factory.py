from core.planners.BelugaPlanner import BelugaPlanner
from core.planners.NoMysteryPlanner import NoMysteryPlanner


PLANNER_TYPES = {
    planner.profile_name: planner
    for planner in (BelugaPlanner, NoMysteryPlanner)
}


def get_planner(name):
    """Return the planner implementation selected by a CLI profile name."""
    try:
        return PLANNER_TYPES[name]()
    except KeyError as error:
        valid_profiles = ", ".join(PLANNER_TYPES)
        raise ValueError(
            f"Unknown profile: {name}. Choose one of: {valid_profiles}"
        ) from error
