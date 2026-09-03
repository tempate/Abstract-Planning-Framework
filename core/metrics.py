"""Structured duration and counter metrics for one planning run."""

import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field

DURATION_NAMES = (
    "total",
    "problem_reading",
    "symmetry_discovery",
    "abstraction",
    "abstract_pddl_writing",
    "concrete_fd",
    "abstract_fd",
    "concrete_asp",
    "abstract_asp",
    "abstract_solving",
    "guided_concrete_solving",
    "extended_concrete_solving",
)

COUNTER_NAMES = (
    "decrements",
    "increments",
    "abstract_horizon",
    "final_horizon",
    "abstract_solve_calls",
    "concrete_solve_calls",
)


@dataclass
class PlanningMetrics:
    """Collect measurements without coupling integrations to timing logic."""

    durations: dict[str, float] = field(default_factory=dict)
    counters: dict[str, int] = field(default_factory=dict)
    _clock: Callable[[], float] = field(default=time.perf_counter, repr=False)

    @contextmanager
    def measure(self, name: str) -> Iterator[None]:
        """Accumulate elapsed seconds for a named phase."""
        if name not in DURATION_NAMES:
            raise ValueError(f"Unknown duration metric: {name}")
        started_at = self._clock()
        try:
            yield
        finally:
            elapsed = self._clock() - started_at
            self.durations[name] = self.durations.get(name, 0.0) + elapsed

    def set_counter(self, name: str, value: int) -> None:
        """Set a named integer counter."""
        if name not in COUNTER_NAMES:
            raise ValueError(f"Unknown counter metric: {name}")
        self.counters[name] = value

    def as_dict(self) -> dict:
        """Return a JSON-serializable snapshot in a stable order."""
        durations = {name: self.durations[name] for name in DURATION_NAMES if name in self.durations}
        counters = {name: self.counters[name] for name in COUNTER_NAMES if name in self.counters}
        return {"durations": durations, "counters": counters}
