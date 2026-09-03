"""Structured duration and counter metrics for one planning run."""

import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field

DURATION_LABELS = {
    "total": "Total",
    "problem_reading": "Problem reading",
    "symmetry_discovery": "Symmetry discovery",
    "abstraction": "Abstraction",
    "abstract_pddl_writing": "Abstract PDDL writing",
    "concrete_fd": "Concrete Fast Downward",
    "abstract_fd": "Abstract Fast Downward",
    "concrete_asp": "Concrete SAS-to-ASP",
    "abstract_asp": "Abstract SAS-to-ASP",
    "abstract_solving": "Abstract plan solving",
    "guided_concrete_solving": "Guided concrete solving",
    "extended_concrete_solving": "Extended concrete solving",
}

COUNTER_LABELS = {
    "decrements": "Refinement decrements",
    "increments": "Horizon increments",
    "abstract_horizon": "Abstract horizon",
    "final_horizon": "Final horizon",
    "abstract_solve_calls": "Abstract solver calls",
    "concrete_solve_calls": "Concrete solver calls",
}


@dataclass
class PlanningMetrics:
    """Collect measurements without coupling integrations to timing logic."""

    durations: dict[str, float] = field(default_factory=dict)
    counters: dict[str, int] = field(default_factory=dict)
    _clock: Callable[[], float] = field(default=time.perf_counter, repr=False)
    on_phase_complete: Callable[[str, dict], None] | None = field(default=None, repr=False)

    @contextmanager
    def measure(self, name: str) -> Iterator[None]:
        """Accumulate elapsed seconds for a named phase."""
        if name not in DURATION_LABELS:
            raise ValueError(f"Unknown duration metric: {name}")
        started_at = self._clock()
        completed = False
        try:
            yield
            completed = True
        finally:
            elapsed = self._clock() - started_at
            self.durations[name] = self.durations.get(name, 0.0) + elapsed
            if completed and self.on_phase_complete is not None:
                self.on_phase_complete(name, self.as_dict())

    def set_counter(self, name: str, value: int) -> None:
        """Set a named integer counter."""
        if name not in COUNTER_LABELS:
            raise ValueError(f"Unknown counter metric: {name}")
        self.counters[name] = value

    def as_dict(self) -> dict:
        """Return a JSON-serializable snapshot in a stable order."""
        durations = {name: self.durations[name] for name in DURATION_LABELS if name in self.durations}
        counters = {name: self.counters[name] for name in COUNTER_LABELS if name in self.counters}
        return {"durations": durations, "counters": counters}
