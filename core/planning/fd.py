"""Plan and decide with Fast Downward."""

from dataclasses import replace

from core.integrations.fast_downward import find_plan, find_sas_plan, has_plan, parse_plan_actions
from core.metrics import PlanningMetrics
from core.outcomes import SOLVABLE, UNSOLVABLE, UnsolvableTaskError
from core.planning.config import PlanningConfig
from core.planning.execution import temp_run_dir
from core.planning.validation import validated

LABEL = "fd"


def solve(config: PlanningConfig, on_update=None):
    """Search one PDDL task with LAMA-first, reporting it like our own pipelines."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir(LABEL) as (base_dir, run_id):
            with metrics.measure("fd_search"):
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


def find_abstract_plan(base_dir, abstract_sas, metrics):
    """Search the abstract task with LAMA-first, returning its actions and its horizon."""
    with metrics.measure("abstract_fd_search"):
        plan = find_sas_plan(base_dir, abstract_sas, "abstract")
    # The abstraction over-approximates, so an abstract task without a plan
    # proves the concrete one has none either.
    if plan is None:
        raise UnsolvableTaskError("Fast Downward found no abstract plan")

    # Fast Downward counts from 0 and ASP from 1, where the mapping expects it.
    actions = tuple(replace(action, time_step=action.time_step + 1) for action in parse_plan_actions(plan))
    metrics.set_counter("abstract_plan_length", len(actions))
    return actions, len(actions)
