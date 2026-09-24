# Examples

Complete CLI commands for a Driverlog task from the
[Downward benchmark collection](https://github.com/aibasel/downward-benchmarks).
Run them from the repository root.

| Script | Purpose |
| --- | --- |
| `fd.sh` | Solve `driverlog/p07.pddl` directly with Fast Downward's lama-first |
| `asp.sh` | Solve it directly with ASP |
| `abstraction-fd.sh` | Discover an object abstraction of the same task, plan it with Fast Downward, and refine that plan with ASP |
| `abstraction-asp.sh` | The same, planning the abstraction with ASP |

```bash
./examples/fd.sh
./examples/asp.sh
./examples/abstraction-fd.sh
./examples/abstraction-asp.sh
```
