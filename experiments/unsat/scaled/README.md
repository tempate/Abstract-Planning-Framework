# Scaled track

Unsolvable problems whose symmetric class grows up to 1000 objects, to see how M&S and M&Sᵅ scale with the class. The base problems are the 22 that M&Sᵅ proves unsolvable by collapsing their largest class: 5 cave-diving, 1 document-transfer, 8 over-nomystery and 8 over-rovers.

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

## Layout

`experiments/benchmarks/scaled/<domain>/size-N/` holds the base problems of `<domain>` with a class of N objects, each beside its domain file. Each base problem starts at its own class size, between 2 and 12, and grows to the sizes in `suite.py` above it.

## Commands

```bash
# Regenerate one base problem at every size (the object to copy and the class size come from rank 0 of experiments/unsat/symmetries/classes.txt)
python -m experiments.unsat.scaled.generate \
  --problem experiments/benchmarks/unsolve-ipc-2016/over-nomystery/prob01.pddl --object p3 --class-size 2

# Submit both modes
python -m experiments.submit --track scaled --abstraction-source symmetries --modes abs-ms ms
```
