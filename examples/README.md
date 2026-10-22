# Examples

Complete CLI commands for a Driverlog task from the
[Downward benchmark collection](https://github.com/aibasel/downward-benchmarks).
Run them from the repository root.

| Script | Purpose |
| --- | --- |
| `lama.sh` | Solve `driverlog/p07.pddl` directly with Fast Downward's lama-first |
| `asp.sh` | Solve it directly with ASP |
| `abs-lama.sh` | Discover an object abstraction of the same task, plan it with Fast Downward, and refine that plan with ASP |
| `abs-asp.sh` | The same, planning the abstraction with ASP |

```bash
./examples/lama.sh
./examples/asp.sh
./examples/abs-lama.sh
./examples/abs-asp.sh
```
