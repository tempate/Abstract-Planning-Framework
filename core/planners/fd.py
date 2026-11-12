"""Plan and decide with Fast Downward."""

from dataclasses import dataclass, replace

from core.integrations.fast_downward import Search, find_plan, find_sas_plan, parse_plan_actions
from core.utilities.outcomes import SOLVABLE, UNSOLVABLE, UnsolvableTaskError
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run

LABEL = "fd"


@dataclass(frozen=True)
class FastDownward:
    """Fast Downward with one search, planning a concrete task or an abstract one."""

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

    def find_abstract_plan(self, _config, base_dir, abstract_sas, metrics):
        """Search the abstract task, returning its actions and its horizon."""
        with metrics.measure("abstract_fd_search"):
            plan = find_sas_plan(base_dir, abstract_sas, "abstract", self.search)
        # The abstraction over-approximates, so an abstract task without a plan
        # proves the concrete one has none either.
        if plan is None:
            raise UnsolvableTaskError("Fast Downward found no abstract plan")

        # Fast Downward counts from 0 and ASP from 1, where the mapping expects it.
        actions = tuple(replace(action, time_step=action.time_step + 1) for action in parse_plan_actions(plan))
        metrics.set_counter("abstract_plan_length", len(actions))
        return actions, len(actions)
