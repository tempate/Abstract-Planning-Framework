# Examples

Complete CLI commands for a Driverlog task from the
[Downward benchmark collection](https://github.com/aibasel/downward-benchmarks).
Run them from the repository root after initializing the submodules.

| Script | Purpose |
| --- | --- |
| `concrete.sh` | Solve `driverlog/p07.pddl` directly |
| `abstract.sh` | Discover and solve an object abstraction of the same task |

```bash
./examples/concrete.sh
./examples/abstract.sh
```

The abstraction pays off on this task: it collapses two interchangeable packages
and its horizon already matches the concrete plan length, so the guided search
finds a plan in a single solver call.

`abstract.sh` selects the object class automatically, which needs the pybliss
setup described in the main README.
