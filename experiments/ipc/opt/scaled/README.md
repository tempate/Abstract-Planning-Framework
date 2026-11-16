# Scaled opt track

Problems of opt/symmetries whose largest class grows up to 1000 objects, to see how LMcut and LMcutᵅ scale with the class. The base problems are up to three per domain that both solve with the largest class, 41 over 18 domains, listed in `suite.py`.

## Example

In nomystery `p03`, packages `p3` and `p4` form a class of size 2. `nomystery-opt11-strips/size-3/p03.pddl` adds one copy of `p3` with the same start and goal:

```diff
-p0 p1 p2 p3 p4 - package
+p0 p1 p2 p3 p3-copy1 p4 - package
-(at p3 l3)
+(at p3 l3) (at p3-copy1 l3)
-(at p3 l2)
+(at p3 l2) (at p3-copy1 l2)
```

A copied domain constant, such as an airport segment, is also declared in the domain, with a copy of every action that names it.

Collapsing the grown class gives the same abstract task as collapsing the original one. The grown class stays the largest, so LMcutᵅ collapses it as rank 0 at every size. A copy joins the class only when the class members share no atom with each other or a fact only one object can hold, which rules out pipesworld, quantum-layout and satellite.

## Layout

`experiments/benchmarks/scaled/<domain>/size-N/` holds the base problems of `<domain>` with a class of N objects, each beside its domain file. Each base problem starts at its own class size, between 2 and 8, and grows to the sizes in `suite.py` above it.

## Commands

```bash
# Regenerate every problem and problems.txt from the base problems and opt/symmetries/classes.txt
python -m experiments.ipc.opt.scaled.generate

# Submit both modes; the track has no results to pick a best class from, and its grown class is rank 0
python -m experiments.submit --track opt-scaled --modes abs-lmcut lmcut --classes all

# Draw the share of problems each mode solves per class size
python -m experiments.figure opt-scaled --out scaled.png
```
