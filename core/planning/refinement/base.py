"""Shared state and behavior for abstract-plan refinement strategies."""

import logging
import time
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from pprint import pformat

from core.execution import log_phase
from core.planners.AbstractPlanner import AbstractPlanner
from core.solvers.factory import get_solver


@dataclass(frozen=True)
class PlanningPaths:
    """ASP files shared by the abstract planning and refinement phases."""

    concrete_lp: str
    abstract_lp: str
    occurrences: str
    mapping: str
    forbidden_actions: str


@dataclass(frozen=True)
class RefinementContext:
    """Configuration and run state shared by refinement strategies."""

    planner: AbstractPlanner
    paths: PlanningPaths
    abstract_task: dict
    horizon: int
    abstract_symbol: str | None
    concrete_objects: list[str] | None
    solving_mode: str
    refinement_filter: Callable[[str], bool]
    fd_timings: dict
    concrete_lp_time: float
    abstract_lp_time: float
    lp_total_time: float
    total_start: float
    base_dir: str
    debug_dir: str
    logger: logging.Logger
    attempt_recorder: Callable[..., None] | None = None


class RefinementStrategy(ABC):
    """Base class for strategies that realize abstract plans concretely."""

    def __init__(self, context):
        self.context = context

    @abstractmethod
    def refine(self):
        """Run the refinement strategy and return a planning result."""

    def build_mapping(self):
        """Build and time the domain-specific abstract-to-concrete mapping."""
        context = self.context
        start = time.perf_counter()
        switch_map = context.planner.build_mapping(
            context.paths.occurrences,
            context.paths.mapping,
            context.abstract_symbol,
            context.concrete_objects,
        )
        elapsed = log_phase(context.logger, "Mapping generation time", start)
        return switch_map, elapsed

    def solve_concrete(self, switch_map):
        """Run and time the selected concrete solver."""
        context = self.context
        lp_files = [
            context.paths.concrete_lp,
            context.paths.occurrences,
            context.paths.mapping,
        ]
        start = time.perf_counter()
        success, plans, bad_actions = get_solver(context.solving_mode).solve(
            lp_files,
            context.horizon,
            switch_map,
        )
        elapsed = log_phase(context.logger, "Concrete solving time", start)
        return success, plans, bad_actions, elapsed

    def build_result(
        self,
        *,
        success,
        plans,
        iteration_times,
        abstract_solve_time,
        concrete_solve_time,
    ):
        """Build the shared result representation and record total runtime."""
        context = self.context
        total_time = time.perf_counter() - context.total_start
        context.logger.info(f"TOTAL TIME: {total_time:.3f}s")
        return {
            "horizon": context.horizon,
            "numPlans": len(plans) if success else 0,
            "plans": plans if success else [],
            "success": success,
            "timings": {
                "iterations": len(iteration_times),
                "fd_concrete_time": context.fd_timings["fd_concrete_time"],
                "fd_abstract_time": context.fd_timings["fd_abstract_time"],
                "fd_total_time": context.fd_timings["fd_total_time"],
                "lp_concrete_time": context.concrete_lp_time,
                "lp_abstract_time": context.abstract_lp_time,
                "lp_total_time": context.lp_total_time,
                "abstract_solve_time": abstract_solve_time,
                "concrete_solve_time": concrete_solve_time,
                "total_time": total_time,
                "run_id": context.base_dir,
            },
        }

    def record_attempt(self, abstract_atoms, *, success, bad_actions):
        """Send an attempt to the optional experiment recorder."""
        recorder = self.context.attempt_recorder
        if recorder:
            recorder(
                abstract_atoms,
                success=success,
                bad_actions=bad_actions,
                mode=self.context.solving_mode,
            )

    @staticmethod
    def iteration_timing(abstract, occurs, mapping, concrete, refinement, total):
        return {
            "abs": abstract,
            "occ": occurs,
            "map": mapping,
            "conc": concrete,
            "ref": refinement,
            "iter": total,
        }

    def log_success(self, plans):
        logger = self.context.logger
        logger.info("SUCCESS: Concrete plan found.")
        logger.info("Plans:")
        logger.info(pformat(plans))

    def log_atoms(self, heading, atoms):
        logger = self.context.logger
        logger.info(heading)
        for atom in atoms:
            logger.info(f"  {atom}")

    def log_iteration_totals(self, iteration_times):
        totals = {
            phase: sum(timing[phase] for timing in iteration_times)
            for phase in ("abs", "occ", "map", "conc", "ref", "iter")
        }
        logger = self.context.logger
        logger.info("=" * 70)
        logger.info(
            "ITERATIONS TOTAL SUMMARY | "
            f"iters={len(iteration_times)} | "
            f"abs={totals['abs']:.3f}s | occ={totals['occ']:.3f}s | "
            f"map={totals['map']:.3f}s | conc={totals['conc']:.3f}s | "
            f"ref={totals['ref']:.3f}s | iter_total={totals['iter']:.3f}s"
        )
