"""Plan with cpddl's lifted search, guided by a heuristic on a homomorphic image of the task."""

from dataclasses import dataclass

from core.integrations.cpddl import ASTAR_LMCUT, GBFS_FF, find_plan
from core.integrations.fast_downward import actions_from_plan_file
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run

LABEL = "rnd-g"


@dataclass(frozen=True)
class Homomorphism:
    """Horčík, Fišer and Torralba's planner, optimal when the config asks for a shortest plan."""

    config: PlanningConfig

    def solve(self, on_update=None):
        """Search the PDDL task, reporting it like our own pipelines."""
        config = self.config
        search = ASTAR_LMCUT if config.optimize else GBFS_FF

        with planning_run(LABEL, on_update) as run:
            with run.metrics.measure("cpddl_search"):
                lines = find_plan(run.base_dir, config.domain_path, config.problem_path, search)

            # An already satisfied goal gives an empty plan, which is a solved task.
            plan = None
            if lines is not None:
                plan = actions_from_plan_file(lines)
                run.metrics.set_counter("plan_length", len(plan))

        return run.plan_result(config, plan)
