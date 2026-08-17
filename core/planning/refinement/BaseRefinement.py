"""Shared state and behavior for abstract-plan refinement strategies."""

import logging
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from pprint import pformat

from core.execution import PhaseTiming, timed_phase
from core.planning.config import AbstractPlanningConfig
from core.planners.BasePlanner import BasePlanner
from core.solvers.decremental import solve_decrementally


@dataclass(frozen=True)
class PlanningPaths:
    """ASP files shared by the abstract planning and refinement phases."""

    concrete_asp: str
    abstract_asp: str
    occurrences: str
    mapping: str


@dataclass(frozen=True)
class RefinementContext:
    """Configuration and run state shared by refinement strategies."""

    config: AbstractPlanningConfig
    planner: BasePlanner
    paths: PlanningPaths
    abstract_task: dict
    horizon: int
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
    """Base class for strategies that use abstract plans to guide search."""

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
            context.planner.build_mapping(
                context.paths.occurrences,
                context.paths.mapping,
                context.config.abstract_symbol,
                context.config.concrete_objects,
            )
        return timing.elapsed

    def solve_concrete(self):
        """Run and time the selected concrete solver."""
        context = self.context
        asp_files = [
            context.paths.concrete_asp,
            context.paths.occurrences,
            context.paths.mapping,
        ]
        with timed_phase(context.logger, "Concrete solving time") as timing:
            success, plan, operation_count = solve_decrementally(
                asp_files,
                context.horizon,
            )
        self.concrete_solve_time += timing.elapsed
        self.solver_operations += operation_count
        return success, plan, timing.elapsed

    def build_result(self, *, success, plan):
        """Build the shared result representation and record total runtime."""
        context = self.context
        total_time = context.total_timing.elapsed
        context.logger.info(f"TOTAL TIME: {total_time:.3f}s")
        return {
            "configuration": context.config.as_dict(),
            "horizon": context.horizon,
            "plan": plan if success else None,
            "success": success,
            "timings": {
                "iterations": 1,
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

    def log_success(self, plan):
        logger = self.context.logger
        logger.info("SUCCESS: Concrete plan found.")
        logger.info("Plan:")
        logger.info(pformat(plan))
