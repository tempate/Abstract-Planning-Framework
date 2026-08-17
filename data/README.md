# Data

```text
data/
├── examples/no_mystery/   # Small concrete and abstract p02 inputs
└── benchmarks/            # Beluga and NoMystery benchmark collections
```

Run the small NoMystery inputs explicitly with:

```bash
./examples/concrete.sh no_mystery
./examples/abstract.sh no_mystery
```

The refinement and performance scripts use matched problems from
`benchmarks/`. Input PDDL stays under `data/`; generated plans, encodings, and
logs belong under `scripts/utils/temp/`.

See [benchmarks/README.md](benchmarks/README.md) for the retained benchmark
variants.
