# Problem abstraction generators

These deterministic scripts reproduce the project-specific abstraction of
concrete PDDL **problem files**:

```bash
python -m scripts.abstraction.collapse_hangars INPUT.pddl OUTPUT_abs.pddl
python -m scripts.abstraction.collapse_trailers INPUT.pddl OUTPUT_abs.pddl
python -m scripts.abstraction.collapse_fuel_levels INPUT.pddl OUTPUT.pddl
```

## Generic object abstraction

The generic transformer writes both an abstract domain and problem. It
collapses one same-typed collection of problem objects, replaces their problem
references with one abstract object, and removes compatible unary delete
effects from the domain:

```bash
python -m scripts.abstraction.abstract_objects \
    DOMAIN.pddl PROBLEM.pddl ABSTRACT_DOMAIN.pddl ABSTRACT_PROBLEM.pddl \
    --objects hangar1 hangar2 hangar3 \
    --abstract-name hangarabs
```

The output paths must differ from the inputs. If `--abstract-name` is omitted,
the generated name is `<object-type>_abs`. Output is valid, canonically
formatted PDDL; comments and input whitespace are not retained.

Unary-delete relaxation is type-wide: it removes every negative unary effect
whose action parameter can accept the selected object type. This matches the
legacy Beluga trailer abstraction. The corrected checked-in trailer domain
uses hand-specialized factory-side and Beluga-side actions and is intentionally
more precise than this generic transformation.

## Automatic selection with PDDL Symmetries

Initialize and build the pinned dependency once:

```bash
git submodule update --init --recursive
python -m pip install -r requirements.txt
make -C lib/pddl-symmetries/src/translate/pybliss-0.73
```

Then use `--auto` instead of `--objects`:

```bash
python -m scripts.abstraction.abstract_objects \
    DOMAIN.pddl PROBLEM.pddl ABSTRACT_DOMAIN.pddl ABSTRACT_PROBLEM.pddl \
    --auto --bliss-time-limit 300
```

Candidate symmetry classes are ranked by the number of compatible unary
delete occurrences in domain action schemas. Ties prefer the largest class,
then lexicographic object order. Exactly one class is abstracted per run. The
command prints every ranked class, the selected objects, and each relaxed
effect.

The Beluga scripts were recovered from the former
`data/beluga/TryMoreInstances/*Abstraction/` directories. The NoMystery script
was recovered from the former `data/nomystery/rewrite.py`. Their retained
outputs are under `data/benchmarks/`.

The three project-specific scripts above do not generate abstract domain files.
NoMystery uses the same domain at both levels. Beluga's retained abstract
domains contain manually maintained relaxations and corrections; the generic
tool is the path for generating new object abstractions.
