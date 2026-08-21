# Abstract Planning Framework

An experimental framework for comparing classical planning with abstraction
and decremental refinement. It supports Beluga hangar/trailer abstractions and
NoMystery fuel abstraction using Fast Downward, Clingo, and PlanPilot.

The abstract workflow builds a symmetric-object abstraction directly from one
concrete PDDL task, solves it, maps its plan to the concrete task, and relaxes
abstract-plan constraints in reverse order until it finds a concrete plan.

## Setup

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

The examples contain complete, copyable CLI commands. Beluga is the default;
pass `no_mystery`, `beluga`, or `all` to choose the workflow.

```bash
./examples/concrete.sh
./examples/abstract.sh
./examples/refinement.sh

./examples/concrete.sh no_mystery
./examples/abstract.sh no_mystery
```

Performance comparisons can take a minute or longer:

```bash
./examples/performance.sh
./examples/performance.sh no_mystery
```

See [examples/README.md](examples/README.md) for the workflow and object
abstraction examples.

## Command-line tools

```bash
python -m scripts.concrete_planner --help
python -m scripts.abstract_planner --help
```

- `concrete_planner` solves a concrete PDDL task.
- `abstract_planner` generates an object abstraction from one concrete task,
  plans abstractly, and realizes the result concretely.

For example, generate the abstraction automatically and use it to guide the
concrete search:

```bash
python -m scripts.abstract_planner \
    --profile beluga \
    --domain data/beluga/concrete/standard/domain.pddl \
    --problem data/beluga/concrete/standard/problem_3_s45_j3_r2_oc44_f3.pddl \
    --horizon 17
```

The planner asks PDDL Symmetries to discover an object class by default. Use
`--objects NAME...` to select an explicit class. Generated abstract PDDL files
live only for the duration of the planning run.

Generated plans, encodings, and logs are written below `scripts/utils/temp/`.

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
- [Data layout](data/README.md)
