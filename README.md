# Abstract Planning Framework

An experimental framework for comparing classical planning with and without
abstraction across classical-planning benchmarks, built on Fast Downward, plasp,
and Clingo.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m scripts.setup
```

`scripts.setup` initializes the submodules and builds the three things pip does
not install: the pybliss extension, the Fast Downward release build, and the
pinned plasp binary. Skipping it fails at planning time rather than at setup
time.

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
  its plan to guide the concrete search. It asks PDDL Symmetries for the class;
  pass `--objects-to-abstract NAME...` to choose one yourself. Finding no
  symmetric class is an error, not a fallback to concrete search.

## Benchmark suite

Submit the suite through a cluster
[CopperBench](https://github.com/tlyphed/copperbench) installation, as one
abstract Slurm task per problem, each capped at 30 minutes and 8192 MiB.
`--with-concrete` submits the baseline alongside it.

```bash
python -m experiments.submit
python -m experiments.collect
python -m experiments.report experiments/plan/results.csv
```

- `experiments/plan/suite.py` holds the domains, but a problem is submitted only
  when `experiments/plan/symmetries.txt` records an abstraction class for it.
  That file's header carries the command that regenerates it.
- `--unsolvable` submits `experiments/unsolvability/` over unsolve-ipc-2016
  through `scripts.unsolvability`, which reports a solvability verdict instead of
  a plan. Only the probNN problems run, the ones known to be unsolvable.
- Results land in untracked `runs/`, rewritten after every completed phase, so an
  interrupted worker keeps its partial timings.
- `collect` rewrites `experiments/plan/results.csv`, keeping only the concrete
  results the run did not cover. `report` rewrites `experiments/plan/reports.md`.

## Tests

The default suite uses inline PDDL models and test doubles for the external
planners. The integration tests are opt-in and run the real toolchain.

```bash
python -m unittest discover -s tests -p 'test_*.py'

RUN_PLANNER_INTEGRATION=1 python -m unittest discover -s tests -p 'test_*.py'
```
