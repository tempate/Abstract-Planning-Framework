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

The performance comparison uses `p04` at horizon 19. On the machine used to
select it, the abstract workflow completed in about 2 seconds while direct
concrete search did not finish within 60 seconds. This case does not normally
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

The performance comparison uses `problem_39` from the `more_trailers` set. Six
concrete Beluga trailers are collapsed into one abstract trailer. In the
selection run, concrete planning took about 55 seconds, while abstraction plus
refinement took about 20 seconds and performed 21 decrements. Timings and the
exact decrement count can vary, but both columns always refer to the same
domain variant, problem, and resulting horizon.
