"""Orchestrate concrete planning from PDDL translation through ASP solving."""

from core.integrations.clingo import plan_length
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.metrics import PlanningMetrics
from core.planning.config import PlanningConfig
from core.planning.execution import temp_run_dir
from core.search.incremental import IncrementalSolver


def solve_with_asp(config: PlanningConfig, on_update=None):
    """Translate and solve one concrete PDDL planning problem."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir() as (base_dir, run_id):
            result = _translate_and_solve(config, base_dir, run_id, metrics)
    result["metrics"] = metrics.as_dict()
    return result


def _translate_and_solve(config, base_dir, run_id, metrics):
    sas_file = _to_sas(base_dir, config, metrics)
    asp = _to_asp(sas_file, metrics)
    return _search(asp, config, run_id, metrics)


def _to_sas(base_dir, config, metrics):
    """Translate the task and return its SAS file."""
    with metrics.measure("concrete_fd"):
        return pddl_to_sas(base_dir, config.domain_path, config.problem_path, "concrete")


def _to_asp(sas_file, metrics):
    """Translate the SAS file into its ASP program."""
    with metrics.measure("concrete_asp"):
        return sas_to_asp(sas_file)


def _search(asp, config, run_id, metrics):
    """Solve the program, raising the horizon until a plan is found."""

    def record_attempt(_horizon, solve_calls):
        metrics.set_counter("concrete_solve_calls", solve_calls)

    with metrics.measure("guided_concrete_solving"):
        solver = IncrementalSolver(asp)
        solve_result = solver.search(on_attempt=record_attempt)

    metrics.set_counter("concrete_solve_calls", solve_result.attempts)
    if solve_result.plan is not None:
        metrics.set_counter("plan_length", plan_length(solve_result.plan))

    return {
        "configuration": config.as_dict(),
        "plan": solve_result.plan,
        "success": solve_result.plan is not None,
        "run_id": run_id,
    }
