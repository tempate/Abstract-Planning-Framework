"""Plan with ASP: a concrete task directly, or the abstract task for a refinement to follow."""

from dataclasses import replace

from core.integrations.clingo import parse_plan_actions, plan_length
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run
from core.asp.solver import Solver


class Asp:
    """ASP planning a concrete task, or the abstract task for a refinement to follow."""

    def solve(self, config: PlanningConfig, on_update=None):
        """Translate and solve one concrete PDDL planning problem."""
        with planning_run("concrete", on_update) as run:
            with run.metrics.measure("concrete_fd"):
                sas_file = pddl_to_sas(run.base_dir, config.domain_path, config.problem_path, "concrete")
            with run.metrics.measure("concrete_asp"):
                asp = sas_to_asp(sas_file, config.optimize)
            plan = _search(asp, config, run.metrics)

        return run.plan_result(config, plan)

    def find_abstract_plan(self, config, _base_dir, abstract_sas, metrics):
        """Search for an abstract plan."""
        with metrics.measure("abstract_asp"):
            abstract_asp = sas_to_asp(abstract_sas, config.optimize)

        def record_attempt(horizon, _dropped, solve_calls):
            metrics.set_counters({"abstract_plan_length": horizon, "abstract_solve_calls": solve_calls})

        with metrics.measure("abstract_solving"):
            solver = Solver(abstract_asp, optimize=config.optimize)
            solve_result = solver.search(on_attempt=record_attempt)

        # An exponential horizon can leave steps empty. Closing them up keeps an abstract action on
        # every step, which is the layout refinement maps onto the concrete steps.
        actions = []
        for step, action in enumerate(parse_plan_actions(solve_result.plan), 1):
            actions.append(replace(action, time_step=step))

        metrics.set_counters({"abstract_plan_length": len(actions), "abstract_solve_calls": solve_result.attempts})
        return tuple(actions), len(actions)


def _search(asp, config, metrics):
    """Solve the program, raising the horizon until a plan is found."""

    def record_attempt(_horizon, _dropped, solve_calls):
        metrics.set_counter("concrete_solve_calls", solve_calls)

    with metrics.measure("guided_concrete_solving"):
        solver = Solver(asp, optimize=config.optimize)
        solve_result = solver.search(on_attempt=record_attempt)

    metrics.set_counter("concrete_solve_calls", solve_result.attempts)
    if solve_result.plan is not None:
        metrics.set_counter("plan_length", plan_length(solve_result.plan))
    return solve_result.plan
