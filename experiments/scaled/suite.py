"""The scaled suite: over-nomystery problems whose symmetric class grows from 2 to 1000 packages.

Each domain size-N holds the unsat-track problems that both ms and abs-ms prove
unsolvable, under their own names, with one package of their class {a, b} copied
until the class has N packages. Regenerate a problem's sizes with:
  python -m experiments.scale --domain experiments/benchmarks/unsolve-ipc-2016/over-nomystery/domain.pddl \
    --problem experiments/benchmarks/unsolve-ipc-2016/over-nomystery/probNN.pddl --object a --class-size 2 \
    --sizes 2 3 5 10 20 50 100 200 500 1000 --out experiments/benchmarks/scaled-over-nomystery
"""

SIZES = (2, 3, 5, 10, 20, 50, 100, 200, 500, 1000)
SUITE = [f"size-{size}" for size in SIZES]
