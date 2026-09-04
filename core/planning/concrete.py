"""Orchestrate concrete planning from PDDL translation through ASP solving."""

import os

from core.execution import temp_run_dir
from core.integrations.clingo import solve
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.integrations.unified_planning import read_problem, write_problem_files
from core.metrics import PlanningMetrics
from core.planning.config import PlanningConfig


def compute_concrete_plan(config: PlanningConfig, on_update=None):
    """Translate and solve one concrete PDDL planning problem."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir() as (base_dir, run_id):
            result = _compute_concrete_plan(config, base_dir, run_id, metrics)
    result["metrics"] = metrics.as_dict()
    return result


def _compute_concrete_plan(config, base_dir, run_id, metrics):
    # Read the concrete problem through Unified Planning and write it back out, so
    # this baseline translates the same PDDL the abstract workflow translates.
    with metrics.measure("problem_reading"):
        problem = read_problem(config.domain_path, config.problem_path)

    with metrics.measure("concrete_pddl_writing"):
        domain_path, problem_path = write_problem_files(problem, os.path.join(base_dir, "generated-concrete"))

    # Translate the concrete problem into SAS.
    with metrics.measure("concrete_fd"):
        task = pddl_to_sas(base_dir, domain_path, problem_path, "concrete")

    # Generate the ASP representation of the concrete problem.
    with metrics.measure("concrete_asp"):
        asp = sas_to_asp(task["sasFile"], abstract_time_steps=config.time_step)

    # Solve the concrete problem, raising the horizon until a plan is found.
    def record_attempt(horizon, solve_calls):
        metrics.set_counter("final_horizon", horizon)
        metrics.set_counter("concrete_solve_calls", solve_calls)

    with metrics.measure("guided_concrete_solving"):
        solve_result = solve(asp, on_attempt=record_attempt)

    metrics.set_counter("final_horizon", solve_result.horizon)
    metrics.set_counter("concrete_solve_calls", solve_result.attempts)

    return {
        "configuration": config.as_dict(),
        "horizon": solve_result.horizon,
        "plan": solve_result.plan,
        "success": solve_result.plan is not None,
        "run_id": run_id,
    }
