"""Plan with ASP: a concrete task directly, or the abstract task for a refinement to follow."""

from core.integrations.clingo import parse_plan_actions, plan_length
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run
from core.asp.solver import Solver


class Asp:
    """ASP planning a PDDL task, or one already translated to SAS."""

    def solve(self, config: PlanningConfig, on_update=None):
        """Translate and solve one concrete PDDL planning problem."""
        with planning_run("concrete", on_update) as run:
            with run.metrics.measure("concrete_fd"):
                sas_file = pddl_to_sas(run.base_dir, config.domain_path, config.problem_path, "concrete")

            with run.metrics.measure("concrete_asp"):
                asp = sas_to_asp(sas_file, config.optimize)

            def record_attempt(_horizon, _dropped, solve_calls):
                run.metrics.set_counter("concrete_solve_calls", solve_calls)

            with run.metrics.measure("guided_concrete_solving"):
                solver = Solver(asp, optimize=config.optimize)
                solve_result = solver.search(on_attempt=record_attempt)

            run.metrics.set_counter("concrete_solve_calls", solve_result.attempts)
            plan = solve_result.plan
            if plan is not None:
                run.metrics.set_counter("plan_length", plan_length(plan))

        return run.plan_result(config, plan)

    def plan_sas(self, config, _base_dir, sas_file, metrics):
        """Search a translated task for a plan, raising the horizon until one exists."""
        with metrics.measure("abstract_asp"):
            program = sas_to_asp(sas_file, config.optimize)

        def record_attempt(horizon, _dropped, solve_calls):
            metrics.set_counters({"abstract_plan_length": horizon, "abstract_solve_calls": solve_calls})

        with metrics.measure("abstract_solving"):
            solver = Solver(program, optimize=config.optimize)
            solve_result = solver.search(on_attempt=record_attempt)

        metrics.set_counter("abstract_solve_calls", solve_result.attempts)
        return parse_plan_actions(solve_result.plan)
