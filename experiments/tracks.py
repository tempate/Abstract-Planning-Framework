"""The benchmark tracks: the problems each one runs, and where the results go."""

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from experiments.htg.opt import suite as htg_opt
from experiments.htg.sat import suite as htg
from experiments.ipc.opt import suite as opt
from experiments.ipc.sat import suite as sat

# The benchmark collections. A track says which of their problems it runs; it
# does not own the PDDL, so that two tracks over one collection cannot drift
# onto different revisions of it.
EXPERIMENTS = Path(__file__).parent
BENCHMARKS = EXPERIMENTS / "benchmarks"


@dataclass(frozen=True)
class Track:
    # What the track asks of each problem, then what it abstracts to answer it, such as sat/symmetries.
    name: str
    directory: Path
    suite: list[str]
    benchmarks_dir: Path
    # The modes, the first of them submitted by default.
    modes: tuple[str, ...]
    # Passed to the modes through an abstraction only; the others have no class to choose.
    abstract_arguments: tuple[str, ...] = ()
    # Passed to the modes that can find a shortest plan.
    optimizing_arguments: tuple[str, ...] = ()

    @property
    def kind(self):
        return self.name.partition("/")[0]

    @property
    def source(self):
        return self.name.partition("/")[2]

    @property
    def results_file(self):
        return self.directory / "results.csv"

    @property
    def runnable_file(self):
        return self.directory / "problems.txt"

    @property
    def classes_file(self):
        return self.directory / "classes.txt"

    def class_ids(self):
        """The ID of every class each problem can collapse, as classes.txt lists them, or None without one."""
        if not self.classes_file.is_file():
            return None

        ids = defaultdict(list)
        for line in self.classes_file.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                name, class_id = line.split("\t")[:2]
                domain, _, problem = name.rpartition("/")
                ids[(domain, problem)].append(class_id)

        return dict(ids)

    def runnable(self):
        """The (domain, problem) pairs worth submitting: those the runnable file lists."""
        problems = set()
        for line in self.runnable_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                domain, _, problem = line.rpartition("/")
                problems.add((domain, problem))

        return frozenset(problems)


# Keyed by the question a track asks, then, for sat, by what it abstracts to answer it.
TRACKS = {
    track.name: track
    for track in (
        Track(
            name="sat/symmetries",
            directory=EXPERIMENTS / "ipc" / "sat" / "symmetries",
            suite=sat.SUITE,
            benchmarks_dir=BENCHMARKS / "downward-benchmarks",
            modes=("abs-asp", "abs-lama", "asp", "lama", "lama-symmetry-pruning"),
        ),
        # The same suite, restricted to the problems numeric-fast-downward finds a
        # resource for, and planned from that resource's objects.
        Track(
            name="sat/resources",
            directory=EXPERIMENTS / "ipc" / "sat" / "resources",
            suite=sat.SUITE,
            benchmarks_dir=BENCHMARKS / "downward-benchmarks",
            modes=("abs-asp", "abs-lama", "asp", "lama", "lama-symmetry-pruning"),
            abstract_arguments=("--abstraction-source", "resources"),
        ),
        # The hard-to-ground benchmarks, refined with gaps like sat/symmetries.
        Track(
            name="sat-htg/symmetries",
            directory=EXPERIMENTS / "htg" / "sat",
            suite=htg.SUITE,
            benchmarks_dir=BENCHMARKS / "htg-domains",
            modes=(
                "abs-asp",
                "abs-lama",
                "asp",
                "lama",
                "abs-powerlifted",
                "powerlifted",
                "lama-symmetry-pruning",
            ),
        ),
        # The hard-to-ground benchmarks, refined without gaps like opt/symmetries.
        Track(
            name="opt-htg/symmetries",
            directory=EXPERIMENTS / "htg" / "opt",
            suite=htg_opt.SUITE,
            benchmarks_dir=BENCHMARKS / "htg-domains",
            modes=(
                "abs-asp",
                "abs-lmcut",
                "asp",
                "lmcut",
                "abs-powerlifted",
                "powerlifted",
                "lmcut-symmetry-pruning",
            ),
            optimizing_arguments=("--optimize",),
        ),
        # The optimal suite, refined without gaps so that every plan is optimal, with
        # abs-lmcut searching the abstract task optimally like its lmcut baseline.
        Track(
            name="opt/symmetries",
            directory=EXPERIMENTS / "ipc" / "opt" / "symmetries",
            suite=opt.SUITE,
            benchmarks_dir=BENCHMARKS / "downward-benchmarks",
            modes=("abs-asp", "abs-lmcut", "asp", "lmcut", "lmcut-symmetry-pruning"),
            optimizing_arguments=("--optimize",),
        ),
        Track(
            name="opt/resources",
            directory=EXPERIMENTS / "ipc" / "opt" / "resources",
            suite=opt.SUITE,
            benchmarks_dir=BENCHMARKS / "downward-benchmarks",
            modes=("abs-asp", "abs-lmcut", "asp", "lmcut", "lmcut-symmetry-pruning"),
            abstract_arguments=("--abstraction-source", "resources"),
            optimizing_arguments=("--optimize",),
        ),
    )
}
DEFAULT_TRACK = "sat/symmetries"


def is_domain_file(name):
    """Tell a domain file from a problem file by name."""
    return "domain" in name
