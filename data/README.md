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
python -m examples.no_mystery
```

The example runs the concrete case followed by abstract-plan refinement. Both
cases should find a plan. Generated plans, ASP files, and debug logs are
written below `scripts/utils/temp/`; they do not belong in `data/`.

`benchmarks/` contains the larger Beluga and NoMystery PDDL collections. It is
intended for experiments after the quick-start example; historical outputs,
generated planner files, caches, and obsolete batch scripts have been removed.
See [`benchmarks/README.md`](benchmarks/README.md) for the retained inputs.
