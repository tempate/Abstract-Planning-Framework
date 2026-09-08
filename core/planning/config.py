"""User-facing configuration for concrete and abstract planning runs."""

from dataclasses import asdict, dataclass
from os import PathLike

Path = str | PathLike[str]
DEFAULT_TIME_STEP = False


@dataclass(frozen=True)
class PlanningConfig:
    """Input configuration shared by all planning modes."""

    domain_path: Path
    problem_path: Path
    time_step: bool = DEFAULT_TIME_STEP

    def as_dict(self):
        values = asdict(self)
        values["domain_path"] = str(self.domain_path)
        values["problem_path"] = str(self.problem_path)
        return values


@dataclass(frozen=True)
class AbstractPlanningConfig(PlanningConfig):
    """Complete input configuration for an abstraction-based planning run."""

    symmetry_time_limit: int = 300
