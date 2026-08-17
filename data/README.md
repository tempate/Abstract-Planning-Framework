# Data

```text
data/
├── examples/no_mystery/   # Small concrete and abstract p02 inputs
└── benchmarks/            # Beluga and NoMystery benchmark collections
```

The small NoMystery inputs provide stable quick starts:

```bash
./examples/concrete.sh
./examples/abstract.sh
```

The refinement and performance scripts use matched problems from
`benchmarks/`. Input PDDL stays under `data/`; generated plans, encodings, and
logs belong under `scripts/utils/temp/`.

See [benchmarks/README.md](benchmarks/README.md) for the retained benchmark
variants.
