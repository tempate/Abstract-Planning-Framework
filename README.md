# Abstract Planning Framework

An experimental framework for comparing classical planning with abstraction
and decremental refinement across classical-planning benchmarks using Fast
Downward, Clingo, and PlanPilot.

The abstract workflow builds a symmetric-object abstraction directly from one
concrete PDDL task, solves it, maps its plan to the concrete task, and relaxes
abstract-plan constraints in reverse order until it finds a concrete plan.

## Setup

The planner toolchain and benchmark collection are Git submodules. Initialize
them together with the repository:

```bash
git submodule update --init --recursive
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python lib/downward/build.py release
```

Automatic object selection additionally requires the pybliss extension:

```bash
make -C lib/pddl-symmetries/src/translate/pybliss-0.73
```

For development tools and automatic formatting, install the development
requirements and enable the pre-commit hook:

```bash
python -m pip install -r requirements-dev.txt
python -m pip install pre-commit
pre-commit install
```

## Try it

The examples contain complete, copyable CLI commands using Gripper tasks from
the Downward benchmark collection.

```bash
./examples/concrete.sh
./examples/abstract.sh
```

See [examples/README.md](examples/README.md) for the workflow and object
abstraction examples.

## Command-line tools

```bash
python -m scripts.planner --help
```

The planner has two modes:

- `concrete` solves the concrete PDDL task directly.
- `abstract` generates an object abstraction, solves it, and uses its plan to
  guide the concrete search.

For example, generate the abstraction automatically and use it to guide the
concrete search:

```bash
python -m scripts.planner abstract \
    --domain benchmarks/downward-benchmarks/gripper/domain.pddl \
    --problem benchmarks/downward-benchmarks/gripper/prob01.pddl \
    --abstract-name ball_abs \
    --horizon 11
```

The planner asks PDDL Symmetries to discover a symmetric set of objects by default. Use `--objects-to-abstract NAME...` to select them explicitly. If PDDL Symmetries does not discover a symmetric set of objects, `abstract` mode exits without running a concrete planning pipeline.

Generated plans, encodings, and logs are written below `scripts/utils/temp/`.

## Benchmark suite

On the cluster login node, use the cluster-provided
[CopperBench](https://github.com/tlyphed/copperbench) installation to submit the
complete benchmark suite:

```bash
python -m scripts.run_benchmarks
```

This submits one Slurm array task per PDDL problem. Each task gets 30 minutes
and 8192 MiB of memory. The abstract and concrete comparisons share the
30-minute limit. Running the command again submits the complete suite again.

JSON results and cluster logs are written below `benchmark-results/`. Collect
the JSON results into a CSV with:

```bash
python -m scripts.collect_benchmarks
```

This writes `benchmark-results/results.csv`.

## Tests

Run the normal suite:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Include the real planner and PDDL Symmetries workflows:

```bash
RUN_PLANNER_INTEGRATION=1 \
    python -m unittest discover -s tests -p 'test_*.py' -v
```

See [tests/README.md](tests/README.md) for the test layers.

## More information

- [Example commands](examples/README.md)
