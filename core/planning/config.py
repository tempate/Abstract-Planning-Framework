"""User-facing configuration for concrete and abstract planning runs."""

from collections.abc import Sequence
from dataclasses import asdict, dataclass
from os import PathLike

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

    def as_dict(self):
        values = asdict(self)
        values["domain_path"] = str(self.domain_path)
        values["problem_path"] = str(self.problem_path)
        return values


@dataclass(frozen=True)
class AbstractPlanningConfig:
    """Complete input configuration for an abstraction-based planning run."""

    domain_path: Path
    problem_path: Path
    objects: Sequence[str] | None = None
    abstract_name: str | None = None
    horizon: int | None = DEFAULT_HORIZON
    encoding: str = DEFAULT_ENCODING
    time_step: bool = DEFAULT_TIME_STEP
    plan_source: str = DEFAULT_PLAN_SOURCE
    profile_name: str = DEFAULT_PROFILE_NAME
    bliss_time_limit: int = 300

    def __post_init__(self):
        if self.objects is not None:
            object.__setattr__(self, "objects", tuple(self.objects))

    def as_dict(self):
        values = asdict(self)
        values["domain_path"] = str(self.domain_path)
        values["problem_path"] = str(self.problem_path)
        return values
