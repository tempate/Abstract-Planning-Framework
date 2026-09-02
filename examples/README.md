# Examples

The examples contain complete CLI commands for the Gripper domain from the
[Downward benchmark collection](https://github.com/aibasel/downward-benchmarks).
Run them from the repository root after initializing the submodules.

| Script | Task | Purpose |
| --- | --- | --- |
| `concrete.sh` | `gripper/prob01.pddl` | Solve the concrete task directly |
| `abstract.sh` | `gripper/prob01.pddl` | Discover and solve an object abstraction |

## Planning

```bash
./examples/concrete.sh
./examples/abstract.sh
```

`abstract.sh` asks PDDL Symmetries to discover the symmetric object classes.
The selected ball class is collapsed into a temporary abstract object, the
abstraction is solved, and its plan guides the concrete search. Automatic
selection requires the pybliss setup described in the main README.

Abstract mode stops after trying to refine the first abstract plan. Because an
abstraction can have a shorter plan than the concrete problem, this example can
report that no concrete plan exists at the discovered abstract horizon.

The example paths are deliberately ordinary `--domain` and `--problem`
arguments. The framework does not otherwise depend on the benchmark layout;
the same commands accept any compatible PDDL task. The examples let Clingo
increase the horizon incrementally until it finds a plan. Run
`python -m scripts.planner --help` for the two planning modes and their complete
CLI reference.
