"""Clingo-guided decremental concrete planning."""

from core.asp import format_abstract_plan, join_asp
from core.execution import timed_phase
from core.integrations.clingo import run_clingo
from core.planning.refinement.base import BaseRefinement


class ClingoRefinement(BaseRefinement):
    """Use one abstract plan as constraints for decremental concrete search."""

    def refine(self):
        context = self.context
        context.logger.info("Abstract plan search")

        with timed_phase(context.logger, "Abstract solving time") as timing:
            abstract_atoms = run_clingo(context.abstract_asp, context.horizon)
        self.abstract_solve_time = timing.elapsed

        if abstract_atoms is None:
            context.logger.info("No abstract plan possible.")
            context.logger.info("FAILED")
            return self.build_result(success=False, plan=None)

        context.logger.info("Abstract plan:")
        for atom in abstract_atoms:
            context.logger.info(f"  {atom}")

        with timed_phase(context.logger, "Abstract plan generation time"):
            abstract_plan = format_abstract_plan(abstract_atoms)

        mapping, _ = self.build_mapping(abstract_plan)

        success, plan, _ = self.solve_concrete(join_asp(abstract_plan, mapping))
        if success:
            self.log_success(plan)
        else:
            context.logger.info("No concrete plan found at the selected horizon.")
            context.logger.info("FAILED")

        return self.build_result(success=success, plan=plan)
