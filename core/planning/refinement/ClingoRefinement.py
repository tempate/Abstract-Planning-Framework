"""Clingo-guided decremental concrete planning."""

from core.asp import write_abstract_occurrences
from core.execution import (
    copy_iteration_file,
    save_json_iteration_file,
    timed_phase,
)
from core.integrations.clingo import run_clingo
from core.planning.refinement.BaseRefinement import BaseRefinement


class ClingoRefinement(BaseRefinement):
    """Use one abstract plan as constraints for decremental concrete search."""

    def __init__(self, context):
        super().__init__(context)
        self.iteration_times = []

    def refine(self):
        iteration = 1
        with timed_phase() as iteration_timing:
            self._log_iteration_start(iteration)

            abstract_atoms, abstract_solve_time = self._solve_abstract()
            if abstract_atoms is None:
                return self._finish_no_abstract_plan(
                    iteration,
                    abstract_solve_time,
                    iteration_timing,
                )

            occurrence_time, mapping_time = self._prepare_plan(
                iteration,
                abstract_atoms,
            )
            success, plan, concrete_solve_time = self.solve_concrete()
            if success:
                return self._finish_success(
                    iteration=iteration,
                    abstract_atoms=abstract_atoms,
                    plan=plan,
                    abstract_solve_time=abstract_solve_time,
                    occurrence_time=occurrence_time,
                    mapping_time=mapping_time,
                    concrete_solve_time=concrete_solve_time,
                    iteration_timing=iteration_timing,
                )
            return self._finish_failure(
                iteration=iteration,
                abstract_atoms=abstract_atoms,
                abstract_solve_time=abstract_solve_time,
                occurrence_time=occurrence_time,
                mapping_time=mapping_time,
                concrete_solve_time=concrete_solve_time,
                iteration_timing=iteration_timing,
            )

    def _solve_abstract(self):
        context = self.context

        with timed_phase(context.logger, "Abstract solving time") as timing:
            plan = run_clingo([context.paths.abstract_asp], context.horizon)
        self.abstract_solve_time += timing.elapsed
        return plan, timing.elapsed

    def _finish_no_abstract_plan(
        self,
        iteration,
        abstract_solve_time,
        iteration_timing,
    ):
        timing = self.iteration_timing(
            abstract_solve_time,
            0.0,
            0.0,
            0.0,
            0.0,
            iteration_timing.elapsed,
        )
        self.iteration_times.append(timing)
        self._log_iteration_summary(iteration, timing)

        self.context.logger.info("No abstract plan possible.")
        self.context.logger.info("FAILED")
        self.log_iteration_totals(self.iteration_times)
        return self.build_result(
            success=False,
            plan=None,
            iteration_times=self.iteration_times,
        )

    def _prepare_plan(self, iteration, abstract_atoms):
        context = self.context
        self.log_atoms("Abstract plan:", abstract_atoms)

        with timed_phase(
            context.logger,
            "Abstract occurrence generation time",
        ) as occurrence_timing:
            write_abstract_occurrences(abstract_atoms, context.paths.occurrences)
        copy_iteration_file(
            context.debug_dir,
            iteration,
            context.paths.occurrences,
        )

        mapping_time = self.build_mapping()
        copy_iteration_file(
            context.debug_dir,
            iteration,
            context.paths.mapping,
        )
        return occurrence_timing.elapsed, mapping_time

    def _finish_success(
        self,
        *,
        iteration,
        abstract_atoms,
        plan,
        abstract_solve_time,
        occurrence_time,
        mapping_time,
        concrete_solve_time,
        iteration_timing,
    ):
        context = self.context
        self.log_success(plan)
        save_json_iteration_file(
            context.debug_dir,
            iteration,
            "concrete_plans.json",
            plan,
        )

        self.iteration_times.append(
            self.iteration_timing(
                abstract_solve_time,
                occurrence_time,
                mapping_time,
                concrete_solve_time,
                0.0,
                iteration_timing.elapsed,
            )
        )
        self.record_attempt(abstract_atoms, success=True, bad_actions=[])
        self.log_iteration_totals(self.iteration_times)
        return self.build_result(
            success=True,
            plan=plan,
            iteration_times=self.iteration_times,
        )

    def _finish_failure(
        self,
        *,
        iteration,
        abstract_atoms,
        abstract_solve_time,
        occurrence_time,
        mapping_time,
        concrete_solve_time,
        iteration_timing,
    ):
        context = self.context
        context.logger.info("No concrete plan found at the selected horizon.")
        context.logger.info("FAILED")

        timing = self.iteration_timing(
            abstract_solve_time,
            occurrence_time,
            mapping_time,
            concrete_solve_time,
            0.0,
            iteration_timing.elapsed,
        )
        self.iteration_times.append(timing)
        self._log_iteration_summary(iteration, timing)
        self.record_attempt(
            abstract_atoms,
            success=False,
            bad_actions=[],
        )
        self.log_iteration_totals(self.iteration_times)
        return self.build_result(
            success=False,
            plan=None,
            iteration_times=self.iteration_times,
        )

    def _log_iteration_start(self, iteration):
        logger = self.context.logger
        logger.info("")
        logger.info("=" * 50)
        logger.info(f"ITERATION {iteration}")
        logger.info("=" * 50)

    def _log_iteration_summary(self, iteration, timing):
        self.context.logger.info(
            f"ITER {iteration} SUMMARY | "
            f"abs={timing['abs']:.3f}s | "
            f"occ={timing['occ']:.3f}s | "
            f"map={timing['map']:.3f}s | "
            f"conc={timing['conc']:.3f}s | "
            f"ref={timing['ref']:.3f}s | "
            f"iter={timing['iter']:.3f}s"
        )
