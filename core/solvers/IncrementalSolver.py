"""Incremental concrete solving strategy."""

from core.solvers.AbstractSolver import AbstractSolver


class IncrementalSolver(AbstractSolver):
    """Enable plan prefixes until an abstract action makes them inconsistent."""

    mode = "incremental"
    log_prefix = "INC"

    def _solve(self):
        active_switches = []

        for switch in self.switches:
            active_switches.append(switch)
            self.operation_count += 1

            if self.is_satisfiable(active_switches):
                continue

            switch_id = self.switch_ids[switch]
            failing_actions = self.mapped_abstract_actions(active_switches)
            self.logger.info(
                f"[{self.log_prefix}] UNSAT after switch={switch_id}"
            )
            self.logger.info(
                f"[{self.log_prefix}] Failing abstract actions={failing_actions}"
            )
            return False, [], failing_actions

        plan = self.collect_plan(active_switches)
        abstract_actions = self.mapped_abstract_actions(active_switches)

        self.logger.info(f"[{self.log_prefix}] Plan found={plan is not None}")
        return plan is not None, plan, abstract_actions
