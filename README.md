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

`scripts.setup` initializes the submodules and builds the five things pip does
not install: the pybliss extension, the Fast Downward release build, Silvan Sievers' structural
symmetries fork of it, numeric Fast Downward for resource detection, and the pinned plasp binary. Numeric Fast Downward
needs COIN's Clp and Osi, found through `DOWNWARD_COIN_ROOT`, or resource detection
has no LP solver. Skipping it fails at planning time rather than at setup
time.

Refinement first tries the abstract plan on a partial grounding, from a private Fast Downward fork that must be cloned by
hand into `lib/downward-partial-grounding` (gitignored). Without it, refinement grounds the whole task, and
`experiments.submit` refuses to run.

For automatic formatting on commit:

```bash
pre-commit install
```

## Try it

```bash
python -m scripts.planner lama --problem experiments/benchmarks/downward-benchmarks/driverlog/p07.pddl
python -m scripts.planner asp --problem experiments/benchmarks/downward-benchmarks/driverlog/p07.pddl
python -m scripts.planner abs-lama --problem experiments/benchmarks/downward-benchmarks/driverlog/p07.pddl
python -m scripts.planner abs-asp --problem experiments/benchmarks/downward-benchmarks/driverlog/p07.pddl
```

All four solve the same task, so the runs are comparable.

## Command-line tools

```bash
python -m scripts.planner --help
```

| Mode | Plans the task with | Abstract mode |
| --- | --- | --- |
| `lama` | Fast Downward's lama-first | `abs-lama` |
| `lmcut` | Fast Downward's A* with LM-cut, length-optimal | `abs-lmcut` |
| `asp` | ASP, length-optimal with `--optimize` | `abs-asp` |

An abstract mode collapses an object class, plans the abstract task with its
planner, and refines that plan with ASP. `abs-lmcut` always refines optimally, and
`abs-asp` does with `--optimize`. The class comes from PDDL Symmetries, or from
resource detection with `--abstraction-source resources`. Pass
`--objects-to-abstract NAME...` to choose one yourself. Finding no class is an
error, not a fallback to concrete search. `--domain` defaults to the domain file
beside the problem.

`lama-symmetry-pruning` and `abs-lama-symmetry-pruning` add orbit space search to
`lama` and `abs-lama`. Orbit space search in lazy search comes from
`lib/structural-symmetries.patch`, which `scripts.setup` applies before it builds.

## Benchmark suite

Submit the suite through a cluster
[CopperBench](https://github.com/tlyphed/copperbench) installation, as one
Slurm task per mode, problem and class, each capped at 30 minutes and 8192 MiB.
It submits every mode of the track unless `--modes` names some.

```bash
python -m experiments.submit
python -m experiments.collect
python -m experiments.report experiments/ipc/sat/symmetries/results.csv
python -m experiments.figure sat --base origin/main --out before-after.png
```

- `experiments/ipc/sat/suite.py` holds the domains, but a problem is submitted
  only when `experiments/ipc/sat/symmetries/problems.txt` records an abstraction
  class for it.
- `--abstraction-source resources` submits `experiments/ipc/sat/resources/`, the
  problems its `problems.txt` lists, and collapses a resource instead of a symmetry
  class.
- `--track opt` submits `experiments/ipc/opt/symmetries/`, the problems of the optimal
  suite with a symmetry class, refined without gaps so that every plan is optimal, with
  `asp` and `lmcut` as the baselines, and `abs-lmcut` in place of `abs-lama`. `lmcut-symmetry-pruning` and
  `abs-lmcut-symmetry-pruning` add orbit space search to both.
  `--abstraction-source resources` submits `experiments/ipc/opt/resources/` instead, whose list
  `python -m experiments.scan --track opt/resources` writes.
- `--track sat-htg` submits `experiments/htg/sat/` over the hard-to-ground
  benchmarks of [htg-domains](https://github.com/abcorrea/htg-domains), a
  submodule, with the sat track's modes.
- `--track opt-htg` submits `experiments/htg/opt/` over the same benchmarks,
  with `labyrinth/OPT` in place of `labyrinth/SAT`, and the opt track's modes.
- Results land in untracked `runs/`, rewritten after every completed phase, so an
  interrupted worker keeps its partial timings.
- `collect` rewrites the `results.csv` of the track the run's manifest names,
  replacing only the (domain, problem, mode, class) results the run holds, so a
  baseline or a gap-filling run can be collected on its own.
  `report` rewrites the `report.md` beside the CSV, comparing only the
  problems every mode finished and saying how many it dropped.
  It also rewrites `best_classes.csv`, the class each abstract mode did best
  with on each problem.

## Tests

The default suite uses inline PDDL models and test doubles for the external
planners. The integration tests are opt-in and run the real toolchain.

```bash
python -m unittest discover -s tests -p 'test_*.py'

RUN_PLANNER_INTEGRATION=1 python -m unittest discover -s tests -p 'test_*.py'
```
