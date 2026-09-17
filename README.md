# Abstract Planning Framework

An experimental framework for comparing classical planning with abstraction and
decremental refinement across classical-planning benchmarks using Fast Downward,
plasp, and Clingo.

Fast Downward translates PDDL to SAS, plasp translates SAS to ASP facts, and the
repository-owned encoding drives Clingo's incremental plan search. The `abstract`
mode collapses a symmetric object class, solves the smaller task, and relaxes the
resulting plan constraints in reverse order until the concrete task is solvable.

## Setup

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -e ".[dev]"
python -m scripts.setup
```

`scripts/setup.py` initializes the submodules and builds the three things pip
does not install: the pybliss extension, the Fast Downward release build, and
the pinned plasp binary. It skips whatever is already there and fails naming
anything still missing, because all three otherwise fail at planning time
rather than at setup time.

For automatic formatting on commit:

```bash
pre-commit install
```

## Try it

```bash
./examples/concrete.sh
./examples/abstract.sh
```

Both solve the same task, so the runs are comparable. See
[examples/README.md](examples/README.md).

## Command-line tools

```bash
python -m scripts.planner --help
```

- `concrete` solves the PDDL task directly.
- `abstract` collapses a symmetric object class, solves the abstraction, and uses
  its plan to guide the concrete search.

The search allows exactly one action per step and raises the horizon until it
finds a plan. `abstract` mode spreads the abstract actions over the even steps,
leaving a gap before the first, between consecutive ones, and after the last,
where one further concrete action may occur or none. It asks PDDL Symmetries for
a symmetric object class; pass `--objects-to-abstract NAME...` to choose one
yourself. If no symmetric class is found, `abstract` exits instead of falling
back to concrete search.

## Benchmark suite

Submit the suite through a cluster
[CopperBench](https://github.com/tlyphed/copperbench) installation, as one
abstract Slurm task per problem, each capped at 30 minutes and 8192 MiB.
`--with-concrete` submits the concrete baseline alongside it:

```bash
python -m experiments.submit
```

`experiments/plan/suite.py` holds every domain variant in `SUITE`. A problem is only
submitted when it is listed in `experiments/plan/symmetries.txt`, where PDDL Symmetries
reported an abstraction class. That file header carries the command that
regenerates it from a collected run.

`--unsolvable` submits the other collection instead, `experiments/unsolvability/suite.py` over
`experiments/unsolvability/unsolve-ipc-2016`, through `scripts.unsolvability`, which reports a
solvability verdict rather than a plan. It runs the probNN problems, the ones
known to be unsolvable, and not the satprob twins or the unsettled
unknownprob ones.

Results and logs land in `runs/`, rewritten after every completed
phase so an interrupted worker keeps its partial timings. Collect them into
`experiments/plan/results.csv`, which the run replaces except for the concrete
results it did not cover:

```bash
python -m experiments.collect
```

Print the coverage, head-to-head, timeout-phase, and refinement-outcome tables
for a collected CSV, over the problems both pipelines finished. The report also
replaces `experiments/plan/reports.md`, which holds the latest one:

```bash
python -m experiments.report experiments/plan/results.csv
```

## Tests

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

See [tests/README.md](tests/README.md) for the opt-in integration layer.
