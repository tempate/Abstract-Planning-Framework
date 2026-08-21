"""Fast Downward abstract-plan refinement strategy."""

from core.asp import join_asp
from core.execution import timed_phase
from core.planning.mapping import build_mapping
from core.planning.plan import PlanAction
from core.planning.refinement.base import BaseRefinement


class FastDownwardRefinement(BaseRefinement):
    """Try to realize the single abstract plan produced by Fast Downward."""

    def refine(self):
        context = self.context
        context.logger.info("Using Fast Downward plan")

        with timed_phase(context.logger, "Abstract plan generation time"):
            abstract_plan = self.read_abstract_plan(context.abstract_task["planFile"])

        mapping = build_mapping(abstract_plan, context.abstraction)
        success, plan, _ = self.solve_concrete(join_asp(*mapping))

        if success:
            self.log_success(plan)
        else:
            context.logger.info("No concrete plan found at the selected horizon.")
            context.logger.info("FAILED")

        return self.build_result(success=success, plan=plan)

    def read_abstract_plan(self, plan_file_path):
        """Read a Fast Downward plan into chronological plan actions."""
        abstract_plan = []
        with open(plan_file_path, "r") as plan_file:
            time_step = 1
            for line in plan_file:
                line = line.strip()
                if not line or line.startswith(";"):
                    continue
                action_name, *arguments = line.strip("()").split()
                abstract_plan.append(PlanAction(action_name, tuple(arguments), time_step))
                time_step += 1

        return tuple(abstract_plan)
