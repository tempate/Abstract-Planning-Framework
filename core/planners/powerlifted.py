"""Plan with Powerlifted, which searches the lifted task without grounding it."""

from dataclasses import dataclass

from core.integrations.fast_downward import actions_from_plan_file
from core.integrations.powerlifted import ALT_BFWS, HMAX, find_plan
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run

LABEL = "powerlifted"


@dataclass(frozen=True)
class Powerlifted:
    """Powerlifted planning a PDDL task, optimally when the config asks for a shortest plan."""

    config: PlanningConfig

    def solve(self, on_update=None):
        """Search the PDDL task, reporting it like our own pipelines."""
        config = self.config

        with planning_run(LABEL, on_update) as run:
            plan = self.plan_pddl(run.base_dir, config.domain_path, config.problem_path, run.metrics)

            # An already satisfied goal gives an empty plan, which is a solved task.
            if plan is not None:
                run.metrics.set_counter("plan_length", len(plan))

        return run.plan_result(config, plan)

    def plan_pddl(self, base_dir, domain_path, problem_path, metrics):
        """Search a PDDL task for a plan, or None when it has none."""
        search = HMAX if self.config.optimize else ALT_BFWS
        with metrics.measure("powerlifted_search"):
            lines = find_plan(base_dir, domain_path, problem_path, search)

        return None if lines is None else actions_from_plan_file(lines)
