"""Decide a concrete task with MS-unsat."""

from core.integrations.ms_unsat import has_plan
from core.utilities.metrics import PlanningMetrics
from core.utilities.outcomes import SOLVABLE, UNSOLVABLE
from core.utilities.config import PlanningConfig
from core.utilities.execution import temp_run_dir


def check_solvability(config: PlanningConfig, on_update=None):
    """Search the concrete task, which settles it either way."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("concrete") as (base_dir, run_id):
            with metrics.measure("fd_search"):
                found = has_plan(base_dir, config.domain_path, config.problem_path, "concrete")

    return {
        "configuration": config.as_dict(),
        "verdict": SOLVABLE if found else UNSOLVABLE,
        "run_id": run_id,
        "metrics": metrics.as_dict(),
    }
