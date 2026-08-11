"""Decremental concrete solving strategy."""

from core.solvers.AbstractSolver import AbstractSolver


class DecrementalSolver(AbstractSolver):
    """Disable switches in reverse until the remaining plan becomes consistent."""

    mode = "decremental"
    log_prefix = "DEC"

    def _solve(self):
        active_switches = set(self.switches)
        if self.is_satisfiable(active_switches):
            self.logger.info(f"[{self.log_prefix}] Full model SAT")
            plans = self.collect_models(active_switches)
            abstract_actions = self.mapped_abstract_actions(active_switches)
            return True, plans, abstract_actions

        self.logger.info(
            f"[{self.log_prefix}] Full model UNSAT. Reverse disabling begins."
        )
        for switch in reversed(self.switches):
            switch_id = self.switch_ids[switch]
            self.logger.info(f"[{self.log_prefix}] Disabled switch={switch_id}")
            active_switches.remove(switch)
            if not self.switch_map[switch_id]["is_abstract"]:
                continue
            if self.is_satisfiable(active_switches):
                self.logger.info(
                    f"[{self.log_prefix}] SAT after disabling switch={switch_id}"
                )
                plans = self.collect_models(active_switches)
                failing_actions = self.mapped_abstract_actions(active_switches)
                failing_actions.append(self.switch_map[switch_id]["atom"])
                return False, plans, list(dict.fromkeys(failing_actions))

        earliest_abstract = next(
            (
                self.switch_map[self.switch_ids[switch]]["atom"]
                for switch in self.switches
                if self.switch_map[self.switch_ids[switch]]["is_abstract"]
            ),
            None,
        )
        self.logger.info(
            f"[{self.log_prefix}] Minimal failing action={earliest_abstract}"
        )
        return False, [], [earliest_abstract]
