# Unified Planning Pipeline Migration

## Decisions

- Split the work into three sequential PRs: Unified Planning, in-memory tool
  boundaries, then workflow cleanup.
- Keep Fast Downward and PDDL Symmetries as subprocesses. Do not depend on
  Fast Downward's private Python APIs.
- The abstraction core operates only on Unified Planning models. PDDL parsing
  and serialization live at adapters/entrypoints.
- Preserve the existing CLIs and generated-file behavior through PRs 1 and 2.
  Make intentional CLI breaks only in PR 3.
- End state: the abstract planner generates symmetric-object abstractions
  internally; `scripts.abstract_object` and the NoMystery abstract-planning
  workflow are removed. Concrete NoMystery planning remains supported.
- End state uses minimal disk: only Fast Downward's required files exist in a
  private `TemporaryDirectory`; SAS, plans, occurrences, mappings, and ASP are
  carried in memory. Logs and requested reports remain on disk.

## PR 1: Replace handwritten PDDL handling with Unified Planning

PR 1 must preserve current commands and downstream file contracts. Its commits
are:

1. `test: characterize current abstraction semantics`
   - Cover object replacement, class ranking, unary-delete relaxation, static
     applicability, equality, collisions, initial values, and Beluga outputs.
   - Compare models/semantics rather than formatting produced by a writer.
2. `build: add Unified Planning dependency and PDDL codec`
   - Pin `unified-planning==1.3.0` in `requirements.txt`.
   - Add a thin reader/writer adapter using `PDDLReader` and `PDDLWriter`.
   - Test parse/write/reparse on supported tasks and opt-in Fast Downward
     acceptance of the generated paired domain/problem.
3. `refactor: implement abstraction over Unified Planning models`
   - Public core API:
     `abstract_problem(problem, objects, abstract_name=None) -> AbstractionResult`.
   - Public ranking API:
     `rank_symmetry_classes(problem, classes) -> tuple[RankedSymmetryClass, ...]`.
   - Construct a fresh `Problem`; never mutate the input problem.
   - Preserve the current object/type/name validation, initial-state collision
     checks, false-inequality rejection, static applicability calculation, and
     selective unary-delete relaxation.
4. `refactor: replace legacy PDDL abstraction implementation`
   - Route ranking and abstraction through the model API.
   - Delete the handwritten tokenizer/parser/renderer and recursive raw-list
     rewriting.
   - Keep `scripts.abstract_object` temporarily as a thin UP parse/write wrapper.

### PR 1 model rules

- Parse with `PDDLReader.parse_problem(...)` or `parse_problem_string(...)`.
- Build a fresh problem with the same environment and initial defaults.
- Reuse immutable types and fluents; add every unselected object and one new
  quotient object of the selected objects' common type.
- Substitute object expressions in preconditions, effects, effect conditions
  and values, explicit initial-value keys and values, goals, constraints, and
  supported metric expressions.
- Rebuild action effects through public APIs. Skip only the unary Boolean
  deletes selected by the existing relaxation/static-applicability algorithm.
- Iterate `explicit_initial_values`, not `initial_values`, to avoid grounding all
  fluent applications and mutating/expanding the backing state.
- Rebuild action-cost metrics with the old-to-new action map.
- Keep provenance outside UP: selected original names/type, quotient name,
  domain constants, removed deletes, and writer name mapping.
- Resolve PDDL Symmetries names case-insensitively because UP lowercases PDDL
  identifiers.
- Promise semantic paired-PDDL output, not preservation of comments, order,
  case, exact requirements, headers, or untyped spelling.

### PR 1 supported scope

The production contract is the current classical Beluga corpus: instantaneous
actions, typing/hierarchies, equality/negation, constants, conditional/forall
discrete effects where accepted by UP, and standard PDDL action costs or plan
length. Reject unsupported problem kinds with `AbstractionError` before making
a partial transformation. In particular, reject named preferences,
oversubscription/multiple metrics, derived predicates, temporal constructs,
processes/events, HTN/contingent features, object-valued fluents, general
numeric updates beyond action costs, and selection of a domain constant.
Trajectory constraints may be unit-tested at the UP layer but are rejected by
the end-to-end Fast Downward path. Unused declared types/constants need not
retain lexical domain placement; current Beluga constants are action-referenced
and remain supported.

### PR 1 acceptance

- The original UP model remains unchanged.
- No selected object remains in any supported expression of the result.
- Abstraction metadata and removed-delete ordering match the existing behavior.
- Current Beluga abstractions remain semantically equivalent and translate with
  Fast Downward.
- Existing CLI behavior remains available.

## PR 2: Remove avoidable intermediate files

PR 2 preserves the existing CLI while changing internal boundaries:

1. `test: characterize translator and solver boundaries`.
2. `refactor: encapsulate Fast Downward temporary files` — accept UP problems,
   write required PDDL/SAS/plan files in one private temporary directory, and
   return typed SAS text, parsed plan steps, and horizon before cleanup.
3. `refactor: stream SAS through plasp into clingo` — plasp stdin/stdout,
   in-memory encoding composition, and `clingo.Control.add()`.
4. `refactor: keep refinement programs in memory` — occurrences, mappings, and
   decremental solver inputs become program values rather than paths.
5. `cleanup: remove path-based intermediate APIs`.

PR 2 acceptance: workflows produce the same plans; only original inputs, logs,
requested reports, and short-lived private Fast Downward files touch disk.

## PR 3: Integrate abstraction and remove legacy workflows

1. `feat: generate abstractions inside abstract planner`
   - CLI accepts `--domain`, `--problem`, exactly one of `--objects ...` or
     `--auto`, and optional `--abstract-name`/`--bliss-time-limit`.
   - Automatic mode runs PDDL Symmetries on original files, ranks classes over
     the UP model, abstracts the selected class, and derives mapping metadata.
2. `cleanup: remove obsolete abstraction entrypoints`
   - Remove `scripts.abstract_object`, the four-file abstract-planner interface,
     duplicate mapping arguments, and the NoMystery abstract-planning profile.
   - Retain concrete NoMystery planning and datasets.
3. `docs: document the unified in-memory workflow`
   - Update examples and add end-to-end Beluga tests for explicit/automatic
     selection and both plan sources.

## Final data flow

```text
Original PDDL files
  -> PDDL Symmetries subprocess when requested
  -> Unified Planning Problem
  -> project-owned model abstraction
  -> Fast Downward private temporary directory
  -> SAS text
  -> plasp stdin/stdout
  -> ASP programs in memory
  -> clingo Python API
```

## Verification and repository notes

- Test framework: `python -m unittest discover -s tests -v`.
- Real planner workflows are gated by `RUN_PLANNER_INTEGRATION=1`.
- CI targets Python 3.13 and installs `requirements-dev.txt`.
- At planning time, the worktree already showed an untracked/dirty state inside
  `lib/pddl-symmetries`; preserve it and do not include it in these PRs.
