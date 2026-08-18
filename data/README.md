# Data

```text
data/
├── beluga/
│   ├── concrete/   # Standard and modified concrete variants
│   └── abstract/   # Hangar and trailer abstractions
└── no_mystery/
    ├── concrete/   # Exact-fuel domain and problems
    └── abstract/   # Fuel-abstracted domain and problems
```

The NoMystery quick examples use `p02`; refinement uses `p01`. Beluga quick
examples use the small standard `problem_3` instance.

Input PDDL stays under `data/`. Generated plans, encodings, and logs belong
under `scripts/utils/temp/`.
