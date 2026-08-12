"""Iterative Clingo abstract-plan refinement strategy."""

from itertools import count

from core.asp import write_abstract_occurrences, write_forbidden_actions
from core.execution import (
    copy_iteration_file,
    save_iteration_file,
    save_json_iteration_file,
    timed_phase,
)
from core.integrations.clingo import run_clingo
from core.planning.refinement.base import RefinementStrategy


class ClingoRefinement(RefinementStrategy):
    """Generate and reject abstract plans until one can be realized."""

    def __init__(self, context):
        super().__init__(context)
        self.forbidden_actions = []
        self.iteration_times = []

    def refine(self):
        for iteration in count(1):
            with timed_phase() as iteration_timing:
                self._log_iteration_start(iteration)

                abstract_atoms, abstract_solve_time = self._solve_abstract(iteration)
                if abstract_atoms is None:
                    self.context.logger.info("No abstract plan possible.")
                    self.context.logger.info("FAILED")
                    return self.build_result(
                        success=False,
                        plans=[],
                        iteration_times=self.iteration_times,
                        abstract_solve_time=abstract_solve_time,
                        concrete_solve_time=0.0,
                    )

                occurrence_time, mapping_time, switch_map = self._prepare_plan(
                    iteration,
                    abstract_atoms,
                )
                success, plans, bad_actions, concrete_solve_time = self.solve_concrete(
                    switch_map
                )
                if success:
                    return self._finish_success(
                        iteration=iteration,
                        abstract_atoms=abstract_atoms,
                        plans=plans,
                        abstract_solve_time=abstract_solve_time,
                        occurrence_time=occurrence_time,
                        mapping_time=mapping_time,
                        concrete_solve_time=concrete_solve_time,
                        iteration_timing=iteration_timing,
                    )

                self._refine_failed_plan(
                    iteration=iteration,
                    abstract_atoms=abstract_atoms,
                    bad_actions=bad_actions,
                    abstract_solve_time=abstract_solve_time,
                    occurrence_time=occurrence_time,
                    mapping_time=mapping_time,
                    concrete_solve_time=concrete_solve_time,
                    iteration_timing=iteration_timing,
                )

    def _solve_abstract(self, iteration):
        context = self.context
        lp_files = [context.paths.abstract_lp]

        with timed_phase(context.logger, "Abstract solving time") as timing:
            if self.forbidden_actions:
                write_forbidden_actions(
                    self.forbidden_actions,
                    context.paths.forbidden_actions,
                )
                lp_files.append(context.paths.forbidden_actions)
                save_iteration_file(
                    context.debug_dir,
                    iteration,
                    "forbidden.lp",
                    "\n".join(self.forbidden_actions),
                )

            models = run_clingo(lp_files, context.horizon)
        return (models[0] if models else None), timing.elapsed

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

        switch_map, mapping_time = self.build_mapping()
        copy_iteration_file(
            context.debug_dir,
            iteration,
            context.paths.mapping,
        )
        return occurrence_timing.elapsed, mapping_time, switch_map

    def _finish_success(
        self,
        *,
        iteration,
        abstract_atoms,
        plans,
        abstract_solve_time,
        occurrence_time,
        mapping_time,
        concrete_solve_time,
        iteration_timing,
    ):
        context = self.context
        self.log_success(plans)
        save_json_iteration_file(
            context.debug_dir,
            iteration,
            "concrete_plans.json",
            plans,
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
            plans=plans,
            iteration_times=self.iteration_times,
            abstract_solve_time=abstract_solve_time,
            concrete_solve_time=concrete_solve_time,
        )

    def _refine_failed_plan(
        self,
        *,
        iteration,
        abstract_atoms,
        bad_actions,
        abstract_solve_time,
        occurrence_time,
        mapping_time,
        concrete_solve_time,
        iteration_timing,
    ):
        context = self.context
        with timed_phase(context.logger, "Refinement time") as refinement_timing:
            context.logger.info("Concrete solve failed.")
            self.log_atoms("Bad abstract actions:", bad_actions)
            save_iteration_file(
                context.debug_dir,
                iteration,
                "bad_actions.lp",
                "\n".join(bad_actions),
            )

            new_forbidden = self._add_forbidden_actions(bad_actions)
            self.log_atoms("New forbidden atoms:", new_forbidden)
            save_iteration_file(
                context.debug_dir,
                iteration,
                "new_forbidden.lp",
                "\n".join(new_forbidden),
            )

        timing = self.iteration_timing(
            abstract_solve_time,
            occurrence_time,
            mapping_time,
            concrete_solve_time,
            refinement_timing.elapsed,
            iteration_timing.elapsed,
        )
        self.iteration_times.append(timing)
        self._log_iteration_summary(iteration, timing)
        self.record_attempt(
            abstract_atoms,
            success=False,
            bad_actions=bad_actions,
        )

    def _add_forbidden_actions(self, bad_actions):
        new_forbidden = []
        for atom in bad_actions:
            if (
                self.context.refinement_filter(atom)
                and atom not in self.forbidden_actions
            ):
                self.forbidden_actions.append(atom)
                new_forbidden.append(atom)
        return new_forbidden

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
            f"forbidden={len(self.forbidden_actions)} | "
            f"iter={timing['iter']:.3f}s"
        )
