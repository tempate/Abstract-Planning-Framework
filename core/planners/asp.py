"""Plan with ASP: a concrete task directly, or the abstract task for a refinement to follow."""

from dataclasses import dataclass

from core.integrations.clingo import parse_plan_actions
from core.integrations.fast_downward import pddl_to_sas
from core.integrations.plasp import sas_to_asp
from core.utilities.config import PlanningConfig
from core.utilities.execution import planning_run
from core.asp.solver import Solver


@dataclass(frozen=True)
class Asp:
    """ASP planning a PDDL task, or one already translated to SAS."""

    config: PlanningConfig

    def solve(self, on_update=None):
        """Translate and solve the PDDL task."""
        config = self.config
        with planning_run("concrete", on_update) as run:
            with run.metrics.measure("concrete_fd"):
                sas_file = pddl_to_sas(run.base_dir, config.domain_path, config.problem_path, "concrete")
            plan = self.plan_sas(sas_file, run.metrics.prefixed("concrete_"))
            run.metrics.set_counter("plan_length", len(plan))

        return run.plan_result(config, plan)

    def plan_sas(self, sas_file, metrics):
        """Search a translated task for a plan, raising the horizon until one exists."""
        with metrics.measure("asp"):
            program = sas_to_asp(sas_file, self.config.optimize)

        def record_attempt(horizon, _dropped, solve_calls):
            metrics.set_counters({"horizon": horizon, "solve_calls": solve_calls})

        with metrics.measure("solving"):
            solver = Solver(program, optimize=self.config.optimize)
            solve_result = solver.search(on_attempt=record_attempt)

        metrics.set_counter("solve_calls", solve_result.attempts)
        return parse_plan_actions(solve_result.plan)
