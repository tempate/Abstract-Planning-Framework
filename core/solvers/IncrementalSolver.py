"""Incremental concrete solving strategy."""

from core.solvers.AbstractSolver import AbstractSolver


class IncrementalSolver(AbstractSolver):
    """Enable plan prefixes until an abstract action makes them inconsistent."""

    mode = "incremental"
    log_prefix = "INC"

    def _solve(self):
        active_switches = []
        for index, switch in enumerate(self.switches):
            active_switches.append(switch)
            self.operation_count += 1
            if index + 1 == len(self.switches):
                continue

            next_id = self.switch_ids[self.switches[index + 1]]
            if not self.switch_map[next_id]["is_abstract"]:
                continue

            self.logger.info(
                f"[{self.log_prefix}] Testing before abstract switch={next_id}"
            )
            if self.is_unsatisfiable(active_switches):
                failing_actions = self.mapped_abstract_actions(active_switches)
                self.logger.info(f"[{self.log_prefix}] UNSAT detected")
                self.logger.info(
                    f"[{self.log_prefix}] Failing abstract actions={failing_actions}"
                )
                return False, [], failing_actions

        self.logger.info(f"[{self.log_prefix}] All prefixes SAT. Solving full model.")
        plans = self.collect_models(self.switches)
        abstract_actions = self.mapped_abstract_actions(self.switches)
        self.logger.info(f"[{self.log_prefix}] Plans found={len(plans)}")
        return True, plans, abstract_actions
