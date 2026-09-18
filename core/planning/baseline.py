"""Solve a task with plain Fast Downward, as an external baseline."""

from core.integrations.fast_downward import find_plan
from core.metrics import PlanningMetrics
from core.planning.config import PlanningConfig
from core.planning.execution import temp_run_dir

LABEL = "lama"


def compute_baseline_plan(config: PlanningConfig, on_update=None):
    """Search one PDDL task with LAMA-first, reporting it like our own pipelines."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir(LABEL) as (base_dir, run_id):
            with metrics.measure("lama_fd"):
                plan = find_plan(base_dir, config.domain_path, config.problem_path, LABEL)

            # An already satisfied goal gives an empty plan, which is a solved
            # task rather than a failure, so the length is set on any plan.
            if plan is not None:
                metrics.set_counter("plan_length", len(plan))

    return {
        "configuration": config.as_dict(),
        "plan": plan,
        "success": plan is not None,
        "run_id": run_id,
        "metrics": metrics.as_dict(),
    }
