---
name: cluster-benchmarks
description: Submit benchmark runs to the SLURM cluster and pull the results back. Use when asked to run benchmarks on the cluster, submit a suite, pull or collect a run's results, fill in problems a run missed, or summarize how a run went.
---

# Cluster benchmark runs

Benchmarks run on `copperhead` over plain non-interactive ssh, and every command
there needs the conda env first:

```bash
source ~/miniconda3/etc/profile.d/conda.sh && conda activate apf
```

Checkouts are worktrees of the bare repo `~/apf/.bare`, one per branch at
`~/apf/<branch>`. In each of them `lib/downward`, `lib/pddl-symmetries`,
`experiments/plan/downward-benchmarks` and `lib/plasp/bin` are symlinks into
`~/apf/.shared`, which holds the only built copy. Nothing is built per worktree,
so a branch that moved a submodule pointer would silently run the shared
version — we build one copy because no branch here moves one.

## Pulling a finished run

**Find the worktree that produced it before trusting anything.** An empty queue
says a run finished, not which code ran it:

```bash
ssh -o BatchMode=yes copperhead 'cd <dir> && git rev-parse --abbrev-ref HEAD && git rev-parse --short HEAD'
```

Compare that HEAD to the local branch. A mismatch means the results are not this
branch's run.

Then pull with `experiments.fetch`, which refuses while `squeue` is non-empty,
rsyncs, and collects in one step:

```bash
python -m experiments.fetch --remote-dir <dir>/runs/ --into <scratch> --csv experiments/plan/results.csv
```

`--into` must point **outside the repo**. Only `runs/` is
gitignored, and rsync without `--delete` merges whatever is already there — two
runs in one directory collect into one unreadable CSV.

## Merging a gap-filling run

Collecting a partial run straight into `results.csv` **silently drops the
existing abstract rows**: `_preserved_concrete_rows` keeps only `concrete` rows
the run did not cover. Merge the raw trees instead, then collect once:

1. rsync both result directories into one scratch directory
2. write a manifest whose `expected_results` is the union of both manifests
3. `experiments.collect.main(<merged dir>, "experiments/plan/results.csv")`

Confirm the collect prints no `Incomplete benchmark run` line and that the row
count matches problems × 2.

## Submitting

```bash
python -m experiments.submit --with-concrete
```

`--with-concrete` is almost always right: `experiments.report` pairs the two
pipelines and drops any problem missing one, so abstract-only problems appear in
no table.

`--unsolvable` swaps the suite for unsolve-ipc-2016 and the planner for
`scripts.unsolvability`, which reports a verdict instead of a plan. The CSV
carries it in the `verdict` column. Only the probNN problems run, the ones known
unsolvable; satprob and unknownprob are skipped.

`main()` calls `_reset_results_dir()`, which **deletes the whole results tree**
before submitting. Move it aside first, or confirm the results are already
pulled.

To submit a subset, cut the problem files the runner reads down to the wanted
problems, submit, then `git checkout --` them. Workers get explicit problem
paths, so restoring the files mid-run is safe. Say plainly that such a run is
not reproducible from a SHA, since the committed code submits the whole set.

## Running two branches at once

One run per worktree, never two from one checkout. `_reset_results_dir()` deletes
`runs/` before submitting and that path is `PROJECT_ROOT`-relative,
so a second submission from the same directory wipes the first run's results and
its manifest while those jobs are still writing into it.

```bash
ssh -o BatchMode=yes copperhead '~/apf/new-worktree.sh <branch>'
```

That fetches, adds `~/apf/<branch>`, replaces the three empty submodule
directories with links into `~/apf/.shared`, and asserts every artifact is
reachable before it prints `ready:`. Two seconds, no build.

Plain `git worktree add` leaves `experiments/plan/downward-benchmarks`,
`lib/downward` and `lib/pddl-symmetries` empty, so the runner finds no problems
and submits nothing without saying why. None of these are checked in:

| missing | how it fails |
|---|---|
| `pybind11_blissmodule.so` | every abstract job dies in symmetry discovery |
| `lib/downward/builds/release` | exit code 36, `Could not find build 'release'` |
| `lib/plasp/bin/plasp` | `plasp binary not found`, before any solving |

The tell for all three is a queue that drains far faster than 30 minutes a job.
Smoke-test before submitting the set, which catches them in a minute instead of
after 142 dead jobs:

```bash
./examples/abstract.sh   # driverlog p07: collapses three packages, plan length 15
```

Pick a problem the branch solves quickly. A refinement branch can time out on a
hard one for its own reasons, which says nothing about the worktree.

`experiments.fetch` guards on `squeue -u "$USER"`, the whole user rather than one
run, so neither run can be pulled until both drain. Give each its own `--into`.

## Before reporting on a run

```bash
awk -F, '$4=="running"' experiments/plan/results.csv | wc -l
```

`running` rows are jobs killed without a terminal status, not live work. They
cluster at one `last_completed_phase` when a limit killed them. Report a run as
partial rather than averaging over them, and check `status` for `error` and
`killed (signal 9)` too — a domain can contribute nothing while the totals still
look healthy.

## Closing the loop

When results land, do all four without being asked:

1. collect into `experiments/plan/results.csv`
2. `python -m experiments.report` to regenerate `experiments/plan/reports.md`
3. commit both with the message `Update results`
4. push
