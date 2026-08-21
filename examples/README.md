# Examples

Examples are organized by workflow and contain complete CLI commands. Run them
from the repository root.

| Script | Default | Choices |
| --- | --- | --- |
| `concrete.sh` | Beluga | `no_mystery`, `beluga`, `all` |
| `abstract.sh` | Beluga | `no_mystery`, `beluga`, `all` |
| `refinement.sh` | Beluga | `no_mystery`, `beluga`, `all` |
| `performance.sh` | Beluga | `no_mystery`, `beluga`, `all` |

## Planning

```bash
./examples/concrete.sh [no_mystery|beluga|all]
./examples/abstract.sh [no_mystery|beluga|all]
./examples/refinement.sh [no_mystery|beluga|all]
./examples/performance.sh [no_mystery|beluga|all]
```

`refinement.sh` first runs a concrete task and then its abstraction.
`performance.sh` uses larger matched tasks and can take a minute or longer.

The Beluga workflow in `abstract.sh` demonstrates the integrated path: it
takes one concrete domain/problem pair, lets PDDL Symmetries select the
hangars, builds a temporary abstraction, solves it, and uses that plan to guide
concrete search.
Omit `--objects` to let PDDL Symmetries discover and rank the object classes,
as the NoMystery examples do. Automatic selection requires the pybliss setup
described in the main README.

All examples use explicit horizons. Run `python -m scripts.planner --help` for
the two planning modes and their complete CLI reference.
