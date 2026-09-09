# Abstract Planning Framework

An experimental framework for comparing classical planning with abstraction and
decremental refinement across classical-planning benchmarks using Fast Downward,
plasp, and Clingo.

Fast Downward translates PDDL to SAS, plasp translates SAS to ASP facts, and the
repository-owned encoding drives Clingo's incremental plan search. The `abstract`
mode collapses a symmetric object class, solves the smaller task, and relaxes the
resulting plan constraints in reverse order until the concrete task is solvable.

## Setup

Fast Downward, PDDL Symmetries, and the benchmark collection are Git submodules.
Initialize them, install the pinned plasp release, and build Fast Downward:

```bash
git submodule update --init --recursive
python scripts/install_plasp.py
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python lib/downward/build.py release
```

Automatic object selection additionally requires the pybliss extension:

```bash
make -C lib/pddl-symmetries/src/translate/pybliss-0.73
```

For development tools and automatic formatting:

```bash
python -m pip install -r requirements-dev.txt
python -m pip install pre-commit
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
finds a plan. `abstract` mode fixes the order of the abstract actions, not the
steps they take: every step holds one action or none, and the horizon leaves a
further step for each abstract action, plus one. It asks PDDL Symmetries for
a symmetric object class; pass `--objects-to-abstract NAME...` to choose one
yourself. If no symmetric class is found, `abstract` exits instead of falling
back to concrete search.

## Benchmark suite

Submit the suite through a cluster
[CopperBench](https://github.com/tlyphed/copperbench) installation, as one
abstract and one concrete Slurm task per problem, each capped at 30 minutes and
8192 MiB:

```bash
python -m scripts.run_benchmarks
```

Both modes are skipped for the problems listed in `benchmarks/no-symmetries.txt`,
where PDDL Symmetries found no abstraction class. That file header carries the
command that regenerates it from a collected run.

Results and logs land in `benchmark-results/`, rewritten after every completed
phase so an interrupted worker keeps its partial timings. Collect them into
`benchmarks/results.csv`, which the run replaces except for the concrete
results it did not cover:

```bash
python -m scripts.collect_benchmarks
```

Print the coverage, head-to-head, timeout-phase, and refinement-outcome tables
for a collected CSV, over the problems both pipelines finished. The report also
replaces `benchmarks/reports.md`, which holds the latest one:

```bash
python -m scripts.report_benchmarks benchmarks/results.csv
```

## Tests

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

See [tests/README.md](tests/README.md) for the opt-in integration layer.
