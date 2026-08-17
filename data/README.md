# Data layout

The small, verified inputs under `examples/` are the best place to start:

```text
examples/
└── no_mystery/
    ├── abstract/
    │   ├── domain.pddl
    │   └── problem.pddl
    └── concrete/
        ├── domain.pddl
        └── problem.pddl
```

Both problems describe the same NoMystery `p02` instance. The abstract version
collapses the concrete fuel levels, while the concrete version contains the
full fuel arithmetic. This instance is intentionally duplicated here so that
the example remains stable if the benchmark archive is reorganized.

From the repository root, run:

```bash
./examples/concrete.sh
./examples/abstract.sh
./examples/refinement.sh
```

The first two commands run concrete and fully realizable abstract cases for
`p02`. The third solves benchmark `p01` concretely and through refinement.
Every case should find a plan. Generated plans, ASP files, and debug logs are
written below `scripts/utils/temp/`; they do not belong in `data/`.

`./examples/refinement.sh no_mystery` uses benchmark `p01` at horizon 11 to
demonstrate actual decremental relaxation and runs its concrete counterpart
first. The `p02` abstract plan is fully realizable without any decrements.

`./examples/performance.sh no_mystery` uses the matched concrete and abstract
`p04` inputs at horizon 19. It is intentionally slow on the concrete side.

`benchmarks/` contains the larger Beluga and NoMystery PDDL collections. It is
intended for experiments after the quick-start example; historical outputs,
generated planner files, caches, and obsolete batch scripts have been removed.
See [`benchmarks/README.md`](benchmarks/README.md) for the retained inputs.
