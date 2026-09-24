"""Solve a task with plain Fast Downward, as an external baseline."""

from core.integrations.fast_downward import find_plan, has_plan, parse_plan_actions
from core.metrics import PlanningMetrics
from core.outcomes import SOLVABLE, UNSOLVABLE
from core.planning.config import PlanningConfig
from core.planning.execution import temp_run_dir
from core.planning.validation import validated

LABEL = "lama"


def solve_directly(config: PlanningConfig, on_update=None):
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
        # Outside the measured phases, so that checking a plan cannot move a
        # timing. Fast Downward is trusted, so this is the control that says the
        # check itself agrees with a planner we did not write.
        "plan_valid": validated(config, plan, parse_plan_actions),
        "metrics": metrics.as_dict(),
    }


def check_solvability_directly(config: PlanningConfig, on_update=None):
    """Search the concrete task, which settles it either way."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("concrete") as (base_dir, run_id):
            with metrics.measure("concrete_fd"):
                found = has_plan(base_dir, config.domain_path, config.problem_path, "concrete")

    return {
        "configuration": config.as_dict(),
        "verdict": SOLVABLE if found else UNSOLVABLE,
        "run_id": run_id,
        "metrics": metrics.as_dict(),
    }
