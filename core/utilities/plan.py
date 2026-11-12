"""Structured planning actions shared by plan sources and refinement."""

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class PlanAction:
    name: str
    args: tuple[str, ...]
    time_step: int


def one_action_per_step(actions):
    """The actions in order on steps 1, 2, ..., the layout refinement maps onto the concrete steps."""
    return tuple(replace(action, time_step=step) for step, action in enumerate(actions, 1))
