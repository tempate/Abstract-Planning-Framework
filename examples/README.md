# Examples

Each domain has a Bash quick-start containing the complete planner commands.
Run them from the repository root after installing `requirements.txt`.

| Mode | What it runs |
| --- | --- |
| `concrete` | Small concrete baseline |
| `abstract` | Small, fully realizable abstract baseline |
| `refinement` | A matched concrete and abstract pair that requires refinement |
| `performance` | A matched pair selected to expose the cost of concrete search |
| `quick` | Both baselines and the refinement comparison; this is the default |
| `all` | `quick` followed by the deliberately long `performance` comparison |

The scripts execute the public `scripts.concrete_planner` and
`scripts.abstract_planner` entry points directly, making their arguments easy
to inspect and copy.

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

## NoMystery

```bash
./examples/no_mystery.sh
./examples/no_mystery.sh refinement
./examples/no_mystery.sh performance
```

The refinement comparison solves benchmark `p01` concretely and through the
fuel abstraction at the same horizon, 11. The abstract fuel route cannot be
realized in full, so decremental solving relaxes it before finding a concrete
plan. The exact positive decrement count can vary with Clingo's parallel model
selection.

The performance comparison uses `p04` at horizon 19. After removing the
redundant Fast Downward planning pass, the abstract workflow completed in
about 6 seconds while direct concrete Clingo search did not finish within 90
seconds. This case does not normally
need decrements; its purpose is to isolate the search-space reduction supplied
by the fuel abstraction. Expect machine-dependent runtimes, and use `quick`
for a short demonstration.

## Beluga

```bash
./examples/beluga.sh
./examples/beluga.sh refinement
./examples/beluga.sh performance
```

The refinement comparison uses the small `problem_3` instance. It solves the
same problem directly and with its two Beluga trailers represented by
`beluga_abs_trailer`; the abstract plan requires decremental relaxation.

The performance comparison uses standard `problem_38` at horizon 26. Its three
concrete hangars are collapsed into `hangarabs`. Fast Downward produces the
abstract plan, and Clingo realizes it against the concrete task. In three
paired validation runs, direct concrete planning took 20.8–30.2 seconds while
the abstract workflow took 12.28–12.33 seconds, a 1.69x–2.45x speedup. This
abstract plan was fully realizable without decrements; the separate trailer
comparison above demonstrates refinement.

## Horizons and Fast Downward

All examples provide explicit horizons. Fast Downward therefore translates
PDDL to SAS but does not search for a plan that Clingo would discard. In the
general Python API, omitting a horizon with a Clingo plan source still asks Fast
Downward for a plan length as an automatic horizon. Selecting `plan_source="fd"`
runs Fast Downward planning because that workflow consumes the actual FD plan.
