"""Fast Downward abstract-plan refinement strategy."""

from core.execution import timed_phase
from core.planning.refinement.BaseRefinement import BaseRefinement


class FastDownwardRefinement(BaseRefinement):
    """Try to realize the single abstract plan produced by Fast Downward."""

    def refine(self):
        context = self.context
        context.logger.info("Using Fast Downward plan")

        iteration_times = []
        with timed_phase() as iteration_timing:
            with timed_phase(
                context.logger,
                "Abstract occurrences from Fast Downward",
            ) as occurrence_timing:
                abstract_atoms = self.plan_to_abstract_atoms(
                    context.abstract_task["planFile"],
                    context.paths.occurrences,
                )

            switch_map, mapping_time = self.build_mapping()
            success, plan, bad_actions, concrete_solve_time = self.solve_concrete(
                switch_map
            )

            if success:
                self.log_success(plan)
                bad_actions = []
            else:
                context.logger.info("Concrete solve failed.")
                self.log_atoms("Bad abstract actions:", bad_actions)
                context.logger.info("No abstract plan possible.")
                context.logger.info("FAILED")

            iteration_times.append(
                self.iteration_timing(
                    0,
                    occurrence_timing.elapsed,
                    mapping_time,
                    concrete_solve_time,
                    0.0,
                    iteration_timing.elapsed,
                )
            )

        self.record_attempt(
            abstract_atoms,
            success=success,
            bad_actions=bad_actions,
        )
        self.log_iteration_totals(iteration_times)
        return self.build_result(
            success=success,
            plan=plan,
            iteration_times=iteration_times,
        )

    def plan_to_abstract_atoms(self, plan_file_path, output_path):
        """Convert a Fast Downward plan into ``occurs_abstract`` facts."""
        abstract_atoms = []
        with open(plan_file_path, "r") as plan_file:
            time_step = 1
            for line in plan_file:
                line = line.strip()
                if not line or line.startswith(";"):
                    continue
                action_name, *arguments = line.strip("()").split()
                quoted_arguments = ",".join(f'"{argument}"' for argument in arguments)
                abstract_atoms.append(
                    f'occurs_abstract(action(("{action_name}",{quoted_arguments})), {time_step}).'
                )
                time_step += 1

        with open(output_path, "w") as output_file:
            output_file.write("\n".join(abstract_atoms))
        return abstract_atoms
