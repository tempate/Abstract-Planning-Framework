"""Structured planning actions shared by plan sources and refinement."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanAction:
    name: str
    arguments: tuple[str, ...]
    time_step: int
