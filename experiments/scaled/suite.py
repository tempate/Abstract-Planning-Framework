"""The scaled suite: over-nomystery problems whose symmetric class grows from 2 to 1000 packages.

Each domain is one unsat-track problem that both ms and abs-ms prove unsolvable,
and each of its classNNNN problems copies one package of its class {a, b} until
the class has NNNN packages. Regenerate a domain with:
  python -m experiments.scale --domain experiments/benchmarks/unsolve-ipc-2016/over-nomystery/domain.pddl \
    --problem experiments/benchmarks/unsolve-ipc-2016/over-nomystery/probNN.pddl --object a --class-size 2 \
    --sizes 2 3 5 10 20 50 100 200 500 1000 --out experiments/benchmarks/scaled-over-nomystery/over-nomystery-probNN
"""

SUITE = [f"over-nomystery-prob{n:02d}" for n in (1, 2, 6, 7, 11, 12, 16, 17)]
