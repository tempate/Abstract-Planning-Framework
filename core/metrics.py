"""Structured duration and counter metrics for one planning run."""

import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field

DURATION_LABELS = {
    "total": "Total",
    "problem_reading": "Problem reading",
    "pnf_translation": "PNF translation",
    "symmetry_discovery": "Symmetry discovery",
    "abstraction": "Abstraction",
    "abstract_pddl_writing": "Abstract PDDL writing",
    "concrete_fd": "Concrete Fast Downward",
    "abstract_fd": "Abstract Fast Downward",
    "lama_fd": "LAMA-first Fast Downward",
    "concrete_asp": "Concrete SAS-to-ASP",
    "abstract_asp": "Abstract SAS-to-ASP",
    "abstract_solving": "Abstract plan solving",
    "guided_concrete_solving": "Guided concrete solving",
    # No longer measured: the guided search now raises the horizon itself. Kept
    # so collecting a run made before that still writes the column it recorded.
    "extended_concrete_solving": "Extended concrete solving",
}

COUNTER_LABELS = {
    "relaxed_deletes": "Relaxed deletes",
    "relaxed_inequalities": "Relaxed inequalities",
    "decrements": "Refinement decrements",
    "increments": "Horizon increments",
    "abstract_plan_length": "Abstract plan length",
    "plan_length": "Plan length",
    "abstract_solve_calls": "Abstract solver calls",
    "concrete_solve_calls": "Concrete solver calls",
    "problem_object_count": "Problem objects",
    "init_predicates_on_class": "Initial predicates on the class",
    "actions_binding_class": "Actions binding the class",
    "unary_relaxed_deletes": "Relaxed unary deletes",
    "class_deletes": "Deletes on the class",
    "class_inequalities": "Inequalities on the class",
    "concrete_sas_variables": "Concrete SAS variables",
    "concrete_sas_operators": "Concrete SAS operators",
    "abstract_sas_variables": "Abstract SAS variables",
    "abstract_sas_operators": "Abstract SAS operators",
}

RATIO_LABELS = {"shared_initial_state": "Shared initial state", "shared_goal": "Shared goal"}


@dataclass
class PlanningMetrics:
    """Collect measurements without coupling integrations to timing logic."""

    durations: dict[str, float] = field(default_factory=dict)
    counters: dict[str, int] = field(default_factory=dict)
    ratios: dict[str, float] = field(default_factory=dict)
    abstraction: dict | None = None
    _clock: Callable[[], float] = field(default=time.perf_counter, repr=False)
    on_update: Callable[[dict, dict], None] | None = field(default=None, repr=False)

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
            if completed:
                self._report({"kind": "phase_completed", "phase": name})

    def set_counter(self, name: str, value: int) -> None:
        """Set a named integer counter."""
        if name not in COUNTER_LABELS:
            raise ValueError(f"Unknown counter metric: {name}")
        self.counters[name] = value
        self._report({"kind": "counter_updated", "counter": name})

    def set_ratio(self, name: str, value: float) -> None:
        """Set a named fraction between zero and one."""
        if name not in RATIO_LABELS:
            raise ValueError(f"Unknown ratio metric: {name}")
        self.ratios[name] = value
        self._report({"kind": "ratio_updated", "ratio": name})

    def set_abstraction(self, objects, object_type: str) -> None:
        """Record the collapsed object class."""
        self.abstraction = {"objects": sorted(objects), "object_type": object_type}
        self._report({"kind": "abstraction_selected"})

    def as_dict(self) -> dict:
        """Return a JSON-serializable snapshot in a stable order."""
        durations = {name: self.durations[name] for name in DURATION_LABELS if name in self.durations}
        counters = {name: self.counters[name] for name in COUNTER_LABELS if name in self.counters}
        ratios = {name: self.ratios[name] for name in RATIO_LABELS if name in self.ratios}
        snapshot = {"durations": durations, "counters": counters, "ratios": ratios}
        if self.abstraction is not None:
            snapshot["abstraction"] = self.abstraction
        return snapshot

    def _report(self, event: dict) -> None:
        if self.on_update is not None:
            self.on_update(event, self.as_dict())
