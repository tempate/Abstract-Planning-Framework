"""Plan and decide with Fast Downward."""

from dataclasses import dataclass

from core.integrations.fast_downward import Search, find_plan, find_sas_plan, parse_plan_actions
from core.utilities.outcomes import SOLVABLE, UNSOLVABLE
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run

LABEL = "fd"


@dataclass(frozen=True)
class FastDownward:
    """Fast Downward with one search, planning a PDDL task or one already translated to SAS."""

    search: Search

    def solve(self, config: PlanningConfig, on_update=None):
        """Search one PDDL task, reporting it like our own pipelines."""
        with planning_run(LABEL, on_update) as run:
            with run.metrics.measure("fd_search"):
                plan = find_plan(run.base_dir, config.domain_path, config.problem_path, LABEL, self.search)

            # An already satisfied goal gives an empty plan, which is a solved
            # task rather than a failure, so the length is set on any plan.
            if plan is not None:
                run.metrics.set_counter("plan_length", len(plan))

        return run.plan_result(config, plan)

    def check_solvability(self, config: PlanningConfig, on_update=None):
        """Search the concrete task, which settles it either way."""
        with planning_run(LABEL, on_update) as run:
            with run.metrics.measure("fd_search"):
                plan = find_plan(run.base_dir, config.domain_path, config.problem_path, LABEL, self.search)

        return run.verdict_result(config, SOLVABLE if plan is not None else UNSOLVABLE)

    def plan_sas(self, _config, base_dir, sas_file, metrics):
        """Search a translated task for a plan, or None when it has none."""
        with metrics.measure("abstract_fd_search"):
            plan = find_sas_plan(base_dir, sas_file, "abstract", self.search)
        return None if plan is None else parse_plan_actions(plan)
