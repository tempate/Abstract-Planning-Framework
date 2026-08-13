"""Decremental concrete solving strategy."""

from core.solvers.BaseSolver import BaseSolver


class DecrementalSolver(BaseSolver):
    """Relax plan constraints in reverse until a concrete plan is found."""

    mode = "decremental"
    log_prefix = "DEC"

    def _solve(self):
        active_switches = set(self.switches)
        plan = self.collect_plan(active_switches)
        if plan is not None:
            self.logger.info(f"[{self.log_prefix}] Full plan SAT")
            return True, plan

        self.logger.info(
            f"[{self.log_prefix}] Full plan UNSAT. Reverse disabling begins."
        )
        for switch in reversed(self.switches):
            switch_id = self.switch_ids[switch]
            self.logger.info(f"[{self.log_prefix}] Disabled switch={switch_id}")
            active_switches.remove(switch)
            self.operation_count += 1
            plan = self.collect_plan(active_switches)
            if plan is not None:
                self.logger.info(
                    f"[{self.log_prefix}] SAT after disabling switch={switch_id}"
                )
                return True, plan

        self.logger.info(f"[{self.log_prefix}] No concrete plan found")
        return False, None
