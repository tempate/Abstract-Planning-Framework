"""Shared state and operations for concrete solving strategies."""

import time
from abc import ABC, abstractmethod

from core.integrations.clingo import collect_models, create_control
from core.runtime.run_artifacts import get_logger, log_phase


class AbstractSolver(ABC):
    """Base class for switch-based concrete solvers."""

    mode = ""
    log_prefix = "SOLVER"

    def solve(self, lp_files, horizon, switch_map):
        """Prepare the Clingo state and execute the concrete solving strategy."""
        self.logger = get_logger()
        self.started_at = time.perf_counter()
        self.switch_map = switch_map
        self.control = create_control(lp_files, horizon)
        self.switches, self.switch_ids = self._find_switches()

        self.logger.info(f"[{self.log_prefix}] Starting {self.mode} solve")
        self.logger.info(
            f"[{self.log_prefix}] Found switches={len(self.switches)}"
        )
        result = self._solve()
        log_phase(self.logger, f"[{self.log_prefix}] Runtime", self.started_at)
        return result

    @abstractmethod
    def _solve(self):
        """Run the strategy after common solver state has been initialized."""

    def assumptions(self, active_switches):
        return [
            (switch, switch in active_switches)
            for switch in self.switches
        ]

    def is_satisfiable(self, active_switches):
        result = self.control.solve(assumptions=self.assumptions(active_switches))
        return result.satisfiable

    def is_unsatisfiable(self, active_switches):
        result = self.control.solve(assumptions=self.assumptions(active_switches))
        return result.unsatisfiable

    def collect_models(self, active_switches):
        return collect_models(self.control, self.assumptions(active_switches))

    def mapped_abstract_actions(self, selected_switches):
        return [
            self.switch_map[self.switch_ids[switch]]["atom"]
            for switch in self.switches
            if (
                switch in selected_switches
                and self.switch_map[self.switch_ids[switch]]["is_abstract"]
            )
        ]

    def _find_switches(self):
        switch_ids = {
            atom.symbol: atom.symbol.arguments[0].number
            for atom in self.control.symbolic_atoms
            if atom.symbol.name == "switch"
        }
        switches = sorted(switch_ids, key=switch_ids.__getitem__)
        return switches, switch_ids
