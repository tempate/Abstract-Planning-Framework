"""Fast Downward abstract-plan refinement strategy."""

import time

from core.execution import log_phase
from core.integrations.fast_downward import fast_downward_plan_to_abstract_atoms
from core.planning.refinement.base import RefinementStrategy


class FastDownwardRefinement(RefinementStrategy):
    """Try to realize the single abstract plan produced by Fast Downward."""

    def refine(self):
        context = self.context
        context.logger.info("Using Fast Downward plan")

        occurrence_start = time.perf_counter()
        abstract_atoms = fast_downward_plan_to_abstract_atoms(
            context.abstract_task["planFile"],
            context.paths.occurrences,
        )
        occurrence_time = log_phase(
            context.logger,
            "Abstract occurrences from Fast Downward",
            occurrence_start,
        )

        iteration_start = time.perf_counter()
        iteration_times = []
        switch_map, mapping_time = self.build_mapping()
        success, plans, bad_actions, concrete_solve_time = self.solve_concrete(
            switch_map
        )

        if success:
            self.log_success(plans)
            iteration_times.append(
                self.iteration_timing(
                    0,
                    occurrence_time,
                    mapping_time,
                    concrete_solve_time,
                    0.0,
                    time.perf_counter() - iteration_start,
                )
            )
            bad_actions = []
        else:
            context.logger.info("Concrete solve failed.")
            self.log_atoms("Bad abstract actions:", bad_actions)
            context.logger.info("No abstract plan possible.")
            context.logger.info("FAILED")

        self.record_attempt(
            abstract_atoms,
            success=success,
            bad_actions=bad_actions,
        )
        self.log_iteration_totals(iteration_times)
        return self.build_result(
            success=success,
            plans=plans,
            iteration_times=iteration_times,
            abstract_solve_time=0.0,
            concrete_solve_time=concrete_solve_time,
        )
