# Examples

Each domain has quick workflows and matched concrete-versus-abstraction
comparisons. Run these commands from the repository root after installing
`requirements.txt`.

| Mode | What it runs |
| --- | --- |
| `concrete` | Small concrete baseline |
| `abstract` | Small, fully realizable abstract baseline |
| `refinement` | A matched concrete and abstract pair that requires refinement |
| `performance` | A matched pair selected to expose the cost of concrete search |
| `quick` | Both baselines and the refinement comparison; this is the default |
| `all` | `quick` followed by the deliberately long `performance` comparison |

Both comparison modes print the two complete results followed by a
side-by-side table containing plan status, horizon, refinement decrements,
total runtime, and the end-to-end runtime ratio.

## NoMystery

```bash
python -m examples.no_mystery refinement
python -m examples.no_mystery performance
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
python -m examples.beluga refinement
python -m examples.beluga performance
```

The refinement comparison uses the small `problem_3` instance. It solves the
same problem directly and with its two Beluga trailers represented by
`beluga_abs_trailer`; the abstract plan requires decremental relaxation.

The performance comparison uses `problem_39` from the `more_hangars` set. Five
concrete hangars are collapsed into `hangarabs`. After removing the redundant
Fast Downward planning pass, the selection run took about 24 seconds concretely
and 17 seconds through the abstraction. This plan is fully realizable without
decrements; the separate trailer comparison above demonstrates refinement.
Timings can vary, but both columns always refer to the same domain variant,
problem, and horizon.

## Horizons and Fast Downward

All examples provide explicit horizons. Fast Downward therefore translates
PDDL to SAS but does not search for a plan that Clingo would discard. In the
general Python API, omitting a horizon with a Clingo plan source still asks Fast
Downward for a plan length as an automatic horizon. Selecting `plan_source="fd"`
runs Fast Downward planning because that workflow consumes the actual FD plan.
