# Examples

The examples contain complete CLI commands for the Gripper domain from the
[Downward benchmark collection](https://github.com/aibasel/downward-benchmarks).
Run them from the repository root after initializing the submodules.

| Script | Task | Purpose |
| --- | --- | --- |
| `concrete.sh` | `gripper/prob01.pddl` | Solve the concrete task directly |
| `abstract.sh` | `gripper/prob01.pddl` | Discover and solve an object abstraction |
| `performance.sh` | `gripper/prob02.pddl` | Run the same comparison on a larger task |

## Planning

```bash
./examples/concrete.sh
./examples/abstract.sh
./examples/performance.sh
```

`abstract.sh` asks PDDL Symmetries to discover the symmetric object classes.
The selected ball class is collapsed into a temporary abstract object, the
abstraction is solved, and its plan guides the concrete search. Automatic
selection requires the pybliss setup described in the main README.

The example paths are deliberately ordinary `--domain` and `--problem`
arguments. The framework does not otherwise depend on the benchmark layout;
the same commands accept any compatible PDDL task. All examples use explicit
horizons. Run `python -m scripts.planner --help` for the two planning modes and
their complete CLI reference.
