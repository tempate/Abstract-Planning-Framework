"""Fast Downward abstract-plan refinement strategy."""

from core.asp import format_abstract_plan, join_asp
from core.execution import timed_phase
from core.planning.mapping import build_mapping
from core.planning.refinement.base import BaseRefinement


class FastDownwardRefinement(BaseRefinement):
    """Try to realize the single abstract plan produced by Fast Downward."""

    def refine(self):
        context = self.context
        context.logger.info("Using Fast Downward plan")

        with timed_phase(context.logger, "Abstract plan generation time"):
            abstract_atoms = self.plan_to_abstract_atoms(context.abstract_task["planFile"])
            abstract_plan = format_abstract_plan(abstract_atoms)

        mapping = build_mapping(abstract_plan, context.abstraction)
        success, plan, _ = self.solve_concrete(join_asp(abstract_plan, mapping))

        if success:
            self.log_success(plan)
        else:
            context.logger.info("No concrete plan found at the selected horizon.")
            context.logger.info("FAILED")

        return self.build_result(success=success, plan=plan)

    def plan_to_abstract_atoms(self, plan_file_path):
        """Convert a Fast Downward plan into ``occurs_abstract`` facts."""
        abstract_atoms = []
        with open(plan_file_path, "r") as plan_file:
            time_step = 1
            for line in plan_file:
                line = line.strip()
                if not line or line.startswith(";"):
                    continue
                action_name, *arguments = line.strip("()").split()
                if arguments:
                    quoted_arguments = ",".join(f'"{argument}"' for argument in arguments)
                    action = f'action(("{action_name}",{quoted_arguments}))'
                else:
                    action = f'action("{action_name}")'
                abstract_atoms.append(f"occurs_abstract({action}, {time_step}).")
                time_step += 1

        return abstract_atoms
