# Examples

The examples are organized by planning workflow. Each Bash script contains
the complete public CLI commands, making its arguments easy to inspect and
copy. Run them from the repository root after installing `requirements.txt`.

| Script | Default | Other choices |
| --- | --- | --- |
| `concrete.sh` | NoMystery | `beluga`, `all` |
| `abstract.sh` | NoMystery | `beluga`, `all` |
| `refinement.sh` | NoMystery | `beluga`, `all` |
| `performance.sh` | none | `no_mystery`, `beluga`, `all` |
| `abstract_object.sh` | explicit selection | `auto`, `all` |

## Concrete planning

Run direct planning without abstraction:

```bash
./examples/concrete.sh
./examples/concrete.sh no_mystery
./examples/concrete.sh beluga
```

## Abstract planning

Run a small, fully realizable abstract planning workflow:

```bash
./examples/abstract.sh
./examples/abstract.sh no_mystery
./examples/abstract.sh beluga
```

The NoMystery example uses a fuel abstraction. The Beluga example represents
the three concrete hangars with `hangarabs`.

## Refinement

Run the concrete problem followed by its abstraction and decremental
refinement:

```bash
./examples/refinement.sh
./examples/refinement.sh no_mystery
./examples/refinement.sh beluga
```

NoMystery uses benchmark `p01` at horizon 11. Its abstract fuel route cannot
be realized in full, so solving relaxes it before finding a concrete plan. The
exact positive decrement count can vary with Clingo's parallel model
selection.

Beluga uses the small `problem_3` instance at horizon 17. Its two Beluga
trailers are represented by `beluga_abs_trailer`, and the abstract plan also
requires decremental relaxation.

## Performance comparison

Performance runs require an explicit domain so they are not launched by
accident:

```bash
./examples/performance.sh no_mystery
./examples/performance.sh beluga
./examples/performance.sh all
```

NoMystery uses `p04` at horizon 19. Beluga uses standard `problem_38` at
horizon 26 with its three hangars collapsed into `hangarabs`. Both scripts run
the concrete and abstract workflows against the same problem. Expect
machine-dependent runtimes of a minute or longer.

## Object abstraction

Generate a Beluga hangar abstraction by selecting the objects explicitly:

```bash
./examples/abstract_object.sh
./examples/abstract_object.sh explicit
```

Generate the same abstraction using PDDL Symmetries to select and rank the
objects:

```bash
./examples/abstract_object.sh auto
```

Automatic selection requires the pybliss extension described in the main
README. Use `all` to run both variants. Outputs are kept separate under
`scripts/utils/temp/abstract_object/explicit/` and
`scripts/utils/temp/abstract_object/auto/`.

## Horizons and Fast Downward

All examples provide explicit horizons. Fast Downward therefore translates
PDDL to SAS but does not search for a plan that Clingo would discard. In the
general Python API, omitting a horizon with a Clingo plan source still asks
Fast Downward for a plan length as an automatic horizon. Selecting
`plan_source="fd"` runs Fast Downward planning because that workflow consumes
the actual FD plan.
