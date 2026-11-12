"""Plan and decide with Fast Downward."""

import os
from dataclasses import dataclass

from core.integrations.fast_downward import Search, find_pddl_plan, find_sas_plan, parse_plan_actions
from core.utilities.outcomes import SOLVABLE, UNSOLVABLE
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run

LABEL = "fd"


@dataclass(frozen=True)
class FastDownward:
    """Fast Downward with one search, planning a PDDL task or one already translated to SAS."""

    search: Search
    config: PlanningConfig

    def solve(self, on_update=None):
        """Search the PDDL task, reporting it like our own pipelines."""
        config = self.config

        with planning_run(LABEL, on_update) as run:
            with run.metrics.measure("fd_search"):
                lines = find_pddl_plan(run.base_dir, config.domain_path, config.problem_path, LABEL, self.search)

            # An already satisfied goal gives an empty plan, which is a solved
            # task rather than a failure, so the length is set on any plan.
            plan = None
            if lines is not None:
                plan = parse_plan_actions(lines)
                run.metrics.set_counter("plan_length", len(plan))

        return run.plan_result(config, plan)

    def check_solvability(self, on_update=None):
        """Search the concrete task, which settles it either way."""
        config = self.config

        with planning_run(LABEL, on_update) as run:
            with run.metrics.measure("fd_search"):
                plan = find_pddl_plan(run.base_dir, config.domain_path, config.problem_path, LABEL, self.search)

        return run.verdict_result(config, SOLVABLE if plan is not None else UNSOLVABLE)

    def plan_sas(self, sas_file, metrics):
        """Search a translated task for a plan, or None when it has none."""
        with metrics.measure("fd_search"):
            # The plan file goes beside the task it solves.
            plan = find_sas_plan(os.path.dirname(sas_file), sas_file, LABEL, self.search)

        return None if plan is None else parse_plan_actions(plan)
