---
name: cluster-benchmarks
description: Submit benchmark runs to the SLURM cluster and pull the results back. Use when asked to run benchmarks on the cluster, submit a suite, pull or collect a run's results, fill in problems a run missed, or summarize how a run went.
---

# Cluster benchmark runs

Benchmarks run on `copperhead` over plain non-interactive ssh. The checkout is
`/home/guests/dquilez/Abstract-Planning-Framework`, and every command there needs
the conda env first:

```bash
source ~/miniconda3/etc/profile.d/conda.sh && conda activate apf
```

## Pulling a finished run

**Find the checkout that produced it before trusting anything.** An empty queue
says a run finished, not which code ran it. Past runs have lived in sibling
clones (`...-Framework-sas`) as well as the main checkout:

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
git worktree add ../apf-<branch> <branch>
cd ../apf-<branch> && git submodule update --init --recursive
make -C lib/pddl-symmetries/src/translate/pybliss-0.73
(cd lib/downward && ./build.py release)
python scripts/install_plasp.py
```

No step is optional. `git worktree add` leaves
`experiments/plan/downward-benchmarks`, `lib/downward` and `lib/pddl-symmetries` empty,
so the runner finds no problems and submits nothing without saying why. All
three of these are built or downloaded rather than checked in, so a fresh submodule
checkout has none of them:

| missing | how it fails |
|---|---|
| `pybind11_blissmodule.so` | every abstract job dies in symmetry discovery |
| `lib/downward/builds/release` | exit code 36, `Could not find build 'release'` |
| `lib/plasp/bin/plasp` | `plasp binary not found`, before any solving |

The tell for all three is a queue that drains far faster than 30 minutes a job.
Smoke-test one problem before submitting the set, which catches them in a
minute instead of after 142 dead jobs:

```bash
B=experiments/plan/downward-benchmarks/quantum-layout-sat23-strips
python -m scripts.planner abstract --domain $B/domain_p14.pddl --problem $B/p14.pddl
```

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
