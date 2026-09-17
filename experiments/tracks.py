"""The benchmark tracks the drivers can run."""

from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

from experiments.resources import suite as resources_suite
from experiments.symmetries import suite as symmetries_suite
from experiments.unsolvability import suite as unsolvability_suite


@dataclass(frozen=True)
class Track:
    """One track: the problems it submits and the driver that runs them."""

    suite: ModuleType
    pipeline: str

    @property
    def directory(self):
        return Path(self.suite.__file__).parent

    @property
    def results_file(self):
        return self.directory / "results.csv"


TRACKS = {
    "symmetries": Track(suite=symmetries_suite, pipeline="plan"),
    "resources": Track(suite=resources_suite, pipeline="resources"),
    "unsolvability": Track(suite=unsolvability_suite, pipeline="decide"),
}
DEFAULT_TRACK = "symmetries"
