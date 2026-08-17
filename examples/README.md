# Examples

Examples are organized by workflow and contain complete CLI commands. Run them
from the repository root.

| Script | Default | Choices |
| --- | --- | --- |
| `concrete.sh` | NoMystery | `no_mystery`, `beluga`, `all` |
| `abstract.sh` | NoMystery | `no_mystery`, `beluga`, `all` |
| `refinement.sh` | NoMystery | `no_mystery`, `beluga`, `all` |
| `performance.sh` | none | `no_mystery`, `beluga`, `all` |
| `abstract_object.sh` | explicit | `explicit`, `auto`, `all` |

## Planning

```bash
./examples/concrete.sh [no_mystery|beluga|all]
./examples/abstract.sh [no_mystery|beluga|all]
./examples/refinement.sh [no_mystery|beluga|all]
./examples/performance.sh {no_mystery|beluga|all}
```

`refinement.sh` first runs the concrete task, then an abstract version that
requires decremental relaxation. `performance.sh` uses larger matched tasks
and requires an explicit domain to avoid launching a long run accidentally.

## Object abstraction

```bash
./examples/abstract_object.sh explicit
./examples/abstract_object.sh auto
```

The explicit example collapses three Beluga hangars. Automatic mode uses PDDL
Symmetries to choose an object class and requires the pybliss setup described
in the main README. Generated PDDL is written below
`scripts/utils/temp/abstract_object/`.

All examples use explicit horizons. Pass `--help` to the underlying Python
modules in `scripts/` for the complete CLI reference.
