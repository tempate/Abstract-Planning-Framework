"""Orchestrate concrete planning from PDDL translation through ASP solving."""

from core.execution import temp_run_dir
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import sas_to_asp
from core.metrics import PlanningMetrics
from core.planning.config import PlanningConfig


def compute_concrete_plan(config: PlanningConfig):
    """Translate and solve one concrete PDDL planning problem."""
    metrics = PlanningMetrics()
    with metrics.measure("total"):
        with temp_run_dir() as (base_dir, run_id):
            result = _compute_concrete_plan(config, base_dir, run_id, metrics)
    result["metrics"] = metrics.as_dict()
    return result


def _compute_concrete_plan(config, base_dir, run_id, metrics):
    # Translate the concrete problem into SAS. With no requested horizon,
    # Fast Downward also finds a plan whose length supplies the horizon.
    fd_task = "plan" if config.horizon is None else "translate"
    with metrics.measure("concrete_fd"):
        task = run_fast_downward(base_dir, config.domain_path, config.problem_path, "concrete", fd_task)

    effective_horizon = task["horizon"] if config.horizon is None else config.horizon
    # Generate the ASP representation of the concrete problem.
    with metrics.measure("concrete_asp"):
        asp = sas_to_asp(task["sasFile"], config.encoding, config.time_step)

    # Solve the concrete problem using Clingo.
    with metrics.measure("guided_concrete_solving"):
        plan = run_clingo(asp, effective_horizon)

    metrics.set_counter("final_horizon", effective_horizon)
    metrics.set_counter("concrete_solve_calls", 1)

    return {
        "configuration": config.as_dict(),
        "horizon": effective_horizon,
        "plan": plan,
        "success": plan is not None,
        "run_id": run_id,
    }
