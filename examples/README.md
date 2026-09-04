# Examples

The examples contain complete CLI commands for the Driverlog domain from the
[Downward benchmark collection](https://github.com/aibasel/downward-benchmarks).
Run them from the repository root after initializing the submodules.

| Script | Task | Purpose |
| --- | --- | --- |
| `concrete.sh` | `driverlog/p07.pddl` | Solve the concrete task directly |
| `abstract.sh` | `driverlog/p07.pddl` | Discover and solve an object abstraction |

Both scripts solve the same task, so the two runs are directly comparable. The
abstraction pays off here: it collapses two interchangeable packages, its
abstract horizon of 13 already matches the concrete plan length, and the guided
concrete search then finds a plan in a single solver call instead of raising the
horizon 14 times.

## Planning

```bash
./examples/concrete.sh
./examples/abstract.sh
```

`abstract.sh` asks PDDL Symmetries to discover the symmetric object classes.
The selected package class is collapsed into a temporary abstract object, the
abstraction is solved, and its plan guides the concrete search. Automatic
selection requires the pybliss setup described in the main README.

The example paths are deliberately ordinary `--domain` and `--problem`
arguments. The framework does not otherwise depend on the benchmark layout;
the same commands accept any compatible PDDL task. The examples let Clingo
increase the horizon incrementally until it finds a plan. Run
`python -m scripts.planner --help` for the two planning modes and their complete
CLI reference.
