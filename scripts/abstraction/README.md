# Problem abstraction generators

These deterministic scripts reproduce the project-specific abstraction of
concrete PDDL **problem files**:

```bash
python -m scripts.abstraction.collapse_hangars INPUT.pddl OUTPUT_abs.pddl
python -m scripts.abstraction.collapse_trailers INPUT.pddl OUTPUT_abs.pddl
python -m scripts.abstraction.collapse_fuel_levels INPUT.pddl OUTPUT.pddl
```

The Beluga scripts were recovered from the former
`data/beluga/TryMoreInstances/*Abstraction/` directories. The NoMystery script
was recovered from the former `data/nomystery/rewrite.py`. Their retained
outputs are under `data/benchmarks/`.

The scripts do not generate abstract domain files. NoMystery uses the same
domain at both levels. Beluga's abstract domains contain additional,
hand-maintained relaxations and corrections, so use the checked-in domains at
`data/benchmarks/beluga/abstract/{hangar,trailer}/domain.pddl`.
