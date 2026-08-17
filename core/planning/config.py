"""User-facing configuration for concrete and abstract planning runs."""

from collections.abc import Sequence
from dataclasses import asdict, dataclass
from os import PathLike
from typing import Any

Path = str | PathLike[str]
DEFAULT_HORIZON = None
DEFAULT_ENCODING = "exact"
DEFAULT_TIME_STEP = False
DEFAULT_PLAN_SOURCE = "clingo"
DEFAULT_PROFILE_NAME = "beluga"


@dataclass(frozen=True)
class ConcretePlanningConfig:
    """Complete input configuration for a concrete planning run."""

    domain_path: Path
    problem_path: Path
    horizon: int | None = DEFAULT_HORIZON
    encoding: str = DEFAULT_ENCODING
    time_step: bool = DEFAULT_TIME_STEP

    def as_dict(self) -> dict[str, Any]:
        """Return a result- and log-friendly representation."""
        values = asdict(self)
        values["domain_path"] = str(self.domain_path)
        values["problem_path"] = str(self.problem_path)
        return values


@dataclass(frozen=True)
class AbstractPlanningConfig:
    """Complete input configuration for an abstraction-based planning run."""

    abstract_domain_path: Path
    abstract_problem_path: Path
    concrete_domain_path: Path
    concrete_problem_path: Path
    horizon: int | None = DEFAULT_HORIZON
    encoding: str = DEFAULT_ENCODING
    time_step: bool = DEFAULT_TIME_STEP
    plan_source: str = DEFAULT_PLAN_SOURCE
    profile_name: str = DEFAULT_PROFILE_NAME
    abstract_symbol: str | None = None
    concrete_objects: Sequence[str] | None = None

    def __post_init__(self):
        if self.concrete_objects is not None:
            object.__setattr__(self, "concrete_objects", tuple(self.concrete_objects))

    def as_dict(self) -> dict[str, Any]:
        """Return a result- and log-friendly representation."""
        values = asdict(self)
        values["abstract_domain_path"] = str(self.abstract_domain_path)
        values["abstract_problem_path"] = str(self.abstract_problem_path)
        values["concrete_domain_path"] = str(self.concrete_domain_path)
        values["concrete_problem_path"] = str(self.concrete_problem_path)
        return values
