"""Plan with ASP: a concrete task directly, or the abstract task for a refinement to follow."""

from dataclasses import replace

from core.integrations.clingo import parse_plan_actions, plan_length
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.metrics import PlanningMetrics
from core.planning.config import PlanningConfig
from core.planning.execution import temp_run_dir
from core.planning.validation import validated
from core.search.incremental import IncrementalSolver

ONE_ACTION_PER_STEP = "1 {occurs(Action, t) : action(Action)} 1."
AT_MOST_ONE_ACTION_PER_STEP = "{occurs(Action, t) : action(Action)} 1."


def solve(config: PlanningConfig, on_update=None, exp_horizon=False):
    """Translate and solve one concrete PDDL planning problem."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir() as (base_dir, run_id):
            result = _translate_and_solve(config, base_dir, run_id, metrics, exp_horizon)
    # Outside the measured phases, so that checking a plan cannot move a timing.
    result["plan_valid"] = validated(config, result.get("plan"), parse_plan_actions)
    result["metrics"] = metrics.as_dict()
    return result


def _translate_and_solve(config, base_dir, run_id, metrics, exp_horizon):
    sas_file = _to_sas(base_dir, config, metrics)
    asp = _to_asp(sas_file, metrics)
    return _search(asp, config, run_id, metrics, exp_horizon)


def _to_sas(base_dir, config, metrics):
    """Translate the task and return its SAS file."""
    with metrics.measure("concrete_fd"):
        return pddl_to_sas(base_dir, config.domain_path, config.problem_path, "concrete")


def _to_asp(sas_file, metrics):
    """Translate the SAS file into its ASP program."""
    with metrics.measure("concrete_asp"):
        return sas_to_asp(sas_file)


def _search(asp, config, run_id, metrics, exp_horizon):
    """Solve the program, raising the horizon until a plan is found."""

    def record_attempt(_horizon, solve_calls):
        metrics.set_counter("concrete_solve_calls", solve_calls)

    with metrics.measure("guided_concrete_solving"):
        solve_result = _horizon_search(asp, exp_horizon, record_attempt)

    metrics.set_counter("concrete_solve_calls", solve_result.attempts)
    if solve_result.plan is not None:
        metrics.set_counter("plan_length", plan_length(solve_result.plan))

    return {
        "configuration": config.as_dict(),
        "plan": solve_result.plan,
        "success": solve_result.plan is not None,
        "run_id": run_id,
    }


def find_abstract_plan(_base_dir, abstract_sas, metrics, exp_horizon=False):
    """Search for an abstract plan, the shortest unless the horizon grows exponentially, returning its actions and its length."""
    with metrics.measure("abstract_asp"):
        abstract_asp = sas_to_asp(abstract_sas)

    def record_attempt(horizon, solve_calls):
        metrics.set_counters({"abstract_plan_length": horizon, "abstract_solve_calls": solve_calls})

    with metrics.measure("abstract_solving"):
        solve_result = _horizon_search(abstract_asp, exp_horizon, record_attempt)

    # An exponential horizon can leave steps empty. Closing them up keeps an abstract action on
    # every step, which is the layout refinement maps onto the concrete steps.
    actions = tuple(
        replace(action, time_step=step) for step, action in enumerate(parse_plan_actions(solve_result.plan), 1)
    )
    metrics.set_counters({"abstract_plan_length": len(actions), "abstract_solve_calls": solve_result.attempts})
    return actions, len(actions)


def _horizon_search(asp, exp_horizon, on_attempt):
    """Search the horizons one by one, or by doubling them over a program that lets a step stay empty."""
    if exp_horizon:
        asp = asp.replace(ONE_ACTION_PER_STEP, AT_MOST_ONE_ACTION_PER_STEP)
    return IncrementalSolver(asp, exp_horizon=exp_horizon).search(on_attempt=on_attempt)
