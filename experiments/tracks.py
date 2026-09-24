"""The benchmark tracks: the problems each one runs, the driver that runs them, and where the results go."""

import json
from dataclasses import dataclass
from pathlib import Path

from experiments.plan import suite as plan
from experiments.unsolvability import suite as unsolvability

# The benchmark collections. A track says which of their problems it runs; it
# does not own the PDDL, so that two tracks over one collection cannot drift
# onto different revisions of it.
BENCHMARKS = Path(__file__).parent / "benchmarks"


@dataclass(frozen=True)
class Track:
    directory: Path
    suite: list[str]
    benchmarks_dir: Path
    driver: str
    # The driver's modes, the first of them submitted by default.
    modes: tuple[str, ...]
    # Passed to the modes through an abstraction only; the others have no class to choose.
    abstract_arguments: tuple[str, ...] = ()

    @property
    def results_file(self):
        return self.directory / "results.csv"

    @property
    def classes_file(self):
        """Every symmetry class of each problem, as experiments.classes enumerates them."""
        return self.directory / "classes.json"

    @property
    def class_results_file(self):
        """The results of a run that collapses every class, kept apart from the track's own."""
        return self.directory / "classes" / "results.csv"

    def classes(self):
        """Map "<domain>/<problem>" to the object names of each class, or None where none were enumerated.

        A class is named by its position in its problem's list, so enumerating
        again renumbers the results.
        """
        if not self.classes_file.is_file():
            return None
        return json.loads(self.classes_file.read_text(encoding="utf-8"))["classes"]

    @property
    def runnable_file(self):
        return self.directory / "problems.txt"

    def runnable(self):
        """The (domain, problem) pairs worth submitting: those the runnable file lists."""
        problems = set()
        for line in self.runnable_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                domain, _, problem = line.partition("/")
                problems.add((domain, problem))
        return frozenset(problems)


# Keyed by the question a track asks, then by what it abstracts to answer it.
TRACKS = {
    "plan/symmetries": Track(
        directory=Path(plan.__file__).parent / "symmetries",
        suite=plan.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abstraction-asp", "abstraction-fd", "asp", "fd"),
    ),
    # The same suite, restricted to the problems numeric-fast-downward finds a
    # resource for, and planned from that resource's objects.
    "plan/resources": Track(
        directory=Path(plan.__file__).parent / "resources",
        suite=plan.SUITE,
        benchmarks_dir=BENCHMARKS / "downward-benchmarks",
        driver="scripts.planner",
        modes=("abstraction-asp", "abstraction-fd", "asp", "fd"),
        abstract_arguments=("--abstraction-source", "resources"),
    ),
    "unsolvability/symmetries": Track(
        directory=Path(unsolvability.__file__).parent / "symmetries",
        suite=unsolvability.SUITE,
        benchmarks_dir=BENCHMARKS / "unsolve-ipc-2016",
        driver="scripts.unsolvability",
        modes=("abstraction-fd", "fd"),
    ),
}
DEFAULT_TRACK = "plan/symmetries"
