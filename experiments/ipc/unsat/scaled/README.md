# Scaled track

Unsolvable problems whose largest symmetric class grows up to 1000 objects, to see how M&S and M&Sᵅ scale with the class. The base problems are those of `unsat/symmetries` (unsolve-ipc-2016) that both prove unsolvable at their original size.

## Example

In over-nomystery `prob01`, packages `p3` and `p4` both start at `l1` and must reach `l0`, so they form a symmetric class of size 2. `over-nomystery/size-3/prob01.pddl` adds one copy of `p3` with the same start and goal:

```diff
-p0 p1 p2 p3 p4 p5 p6 p7 - package
+p0 p1 p2 p3 p3-copy1 p4 p5 p6 p7 - package
-(at p3 l1)
+(at p3 l1) (at p3-copy1 l1)
-(at p3 l0)
+(at p3 l0) (at p3-copy1 l0)
```

A copied domain constant, such as a cave-diving diver, is also declared in the domain and gets a copy of every action that names it, such as `hire-diver-d0`.

Collapsing the grown class gives the same abstract task as collapsing the original one. M&Sᵅ proves that task unsolvable, so every size stays unsolvable, and M&Sᵅ searches the same abstract task at every size.

## Commands

`experiments/benchmarks/scaled/<domain>/size-N/` is generated, not tracked. Generate it in every checkout before submitting the track.

```bash
# 1. Find the classes of unsolve-ipc-2016, then run both modes on the largest class of each problem
python -m experiments.scan --track unsat/symmetries --submit   # then --collect
python -m experiments.submit --track unsat --classes largest

# 2. Grow the problems both modes prove unsolvable, from experiments/ipc/unsat/symmetries/{results.csv,classes.txt}
python -m experiments.ipc.unsat.scaled.generate
python -m experiments.submit --track scaled --classes largest

# 3. Median time against class size
python -m experiments.ipc.unsat.scaled.figure --out scaled.png
```
