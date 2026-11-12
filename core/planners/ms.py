"""Decide a concrete task with MS-unsat."""

from core.integrations.ms_unsat import has_plan
from core.utilities.outcomes import SOLVABLE, UNSOLVABLE
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run


class MsUnsat:
    """MS-unsat deciding a concrete task."""

    def check_solvability(self, config: PlanningConfig, on_update=None):
        """Search the concrete task, which settles it either way."""
        with planning_run("concrete", on_update) as run:
            with run.metrics.measure("fd_search"):
                found = has_plan(run.base_dir, config.domain_path, config.problem_path, "concrete")

        return run.verdict_result(config, SOLVABLE if found else UNSOLVABLE)
