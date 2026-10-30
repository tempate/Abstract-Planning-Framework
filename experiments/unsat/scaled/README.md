# Scaled track

Unsolvable over-nomystery problems whose symmetric class grows from 2 to 1000 packages, to see how M&S and M&Sᵅ scale with the class.

## Example

In `prob01`, packages `p3` and `p4` both start at `l1` and must reach `l0`, so they form a symmetric class of size 2. `over-nomystery-size-3/prob01.pddl` adds one copy of `p3` with the same start and goal:

```diff
-p0 p1 p2 p3 p4 p5 p6 p7 - package
+p0 p1 p2 p3 p3-copy1 p4 p5 p6 p7 - package
-(at p3 l1)
+(at p3 l1) (at p3-copy1 l1)
-(at p3 l0)
+(at p3 l0) (at p3-copy1 l0)
```

A plan for the grown problem without the copy's actions is a plan for the original, so every size stays unsolvable. M&Sᵅ collapses all copies into one package, so its abstract task is the same at every size.

## Layout

`experiments/benchmarks/scaled/over-nomystery-size-N/probNN.pddl` is base problem `probNN` with a class of N packages. `over-nomystery-size-2` holds the originals. The base problems are the 8 over-nomystery problems both modes prove unsolvable.

## Commands

```bash
# Regenerate one base problem at every size (the copied package comes from experiments/unsat/symmetries/classes.txt)
python -m experiments.unsat.scaled.generate \
  --problem experiments/benchmarks/unsolve-ipc-2016/over-nomystery/prob01.pddl --object p3 --class-size 2

# Submit both modes
python -m experiments.submit --track scaled --abstraction-source symmetries --modes abs-ms ms
```
