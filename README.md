# Abstract Planning Framework

An experimental framework for comparing classical planning with abstraction
and decremental refinement. It supports Beluga hangar/trailer abstractions and
NoMystery fuel abstraction using Fast Downward, Clingo, and PlanPilot.

The abstract workflow computes an abstract plan, maps it to the concrete task,
and relaxes abstract-plan constraints in reverse order until it finds a
concrete plan.

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
./examples/abstract_object.sh auto
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
python -m scripts.abstract_object --help
```

- `concrete_planner` solves a concrete PDDL task.
- `abstract_planner` plans abstractly and realizes the result concretely.
- `abstract_object` collapses an explicit or automatically selected symmetric
  object set into one abstract object.

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
