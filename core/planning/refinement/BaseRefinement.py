"""Shared state and behavior for abstract-plan refinement strategies."""

import logging
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from pprint import pformat

from core.execution import PhaseTiming, timed_phase
from core.paths import OCCURRENCE_VALIDATION_ENCODING
from core.planners.AbstractPlanner import AbstractPlanner
from core.solvers.DecrementalSolver import DecrementalSolver


@dataclass(frozen=True)
class PlanningPaths:
    """ASP files shared by the abstract planning and refinement phases."""

    concrete_asp: str
    abstract_asp: str
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
    refinement_filter: Callable[[str], bool]
    fd_timings: dict
    concrete_asp_time: float
    abstract_asp_time: float
    asp_total_time: float
    total_timing: PhaseTiming
    base_dir: str
    debug_dir: str
    logger: logging.Logger
    attempt_recorder: Callable[..., None] | None = None


class BaseRefinement(ABC):
    """Base class for strategies that realize abstract plans concretely."""

    def __init__(self, context):
        self.context = context
        self.solver_operations = 0
        self.abstract_solve_time = 0.0
        self.concrete_solve_time = 0.0

    @abstractmethod
    def refine(self):
        """Run the refinement strategy and return a planning result."""

    def build_mapping(self):
        """Build and time the domain-specific abstract-to-concrete mapping."""
        context = self.context
        with timed_phase(context.logger, "Mapping generation time") as timing:
            switch_map = context.planner.build_mapping(
                context.paths.occurrences,
                context.paths.mapping,
                context.abstract_symbol,
                context.concrete_objects,
            )
        return switch_map, timing.elapsed

    def solve_concrete(self, switch_map):
        """Run and time the selected concrete solver."""
        context = self.context
        asp_files = [
            context.paths.concrete_asp,
            context.paths.occurrences,
            context.paths.mapping,
            OCCURRENCE_VALIDATION_ENCODING,
        ]
        with timed_phase(context.logger, "Concrete solving time") as timing:
            success, plan, bad_actions, operation_count = DecrementalSolver().solve(
                asp_files,
                context.horizon,
                switch_map,
            )
        self.concrete_solve_time += timing.elapsed
        self.solver_operations += operation_count
        return success, plan, bad_actions, timing.elapsed

    def build_result(self, *, success, plan, iteration_times):
        """Build the shared result representation and record total runtime."""
        context = self.context
        total_time = context.total_timing.elapsed
        context.logger.info(f"TOTAL TIME: {total_time:.3f}s")
        return {
            "horizon": context.horizon,
            "plan": plan if success else None,
            "success": success,
            "timings": {
                "iterations": len(iteration_times),
                "decrements": self.solver_operations,
                "fd_concrete_time": context.fd_timings["fd_concrete_time"],
                "fd_abstract_time": context.fd_timings["fd_abstract_time"],
                "fd_total_time": context.fd_timings["fd_total_time"],
                "asp_concrete_time": context.concrete_asp_time,
                "asp_abstract_time": context.abstract_asp_time,
                "asp_total_time": context.asp_total_time,
                "abstract_solve_time": self.abstract_solve_time,
                "concrete_solve_time": self.concrete_solve_time,
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

    def log_success(self, plan):
        logger = self.context.logger
        logger.info("SUCCESS: Concrete plan found.")
        logger.info("Plan:")
        logger.info(pformat(plan))

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
