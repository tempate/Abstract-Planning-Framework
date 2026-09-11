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

Then pull with `fetch_benchmarks`, which refuses while `squeue` is non-empty,
rsyncs, and collects in one step:

```bash
python -m scripts.fetch_benchmarks --remote-dir <dir>/benchmark-results/ --into <scratch> --csv benchmarks/results.csv
```

`--into` must point **outside the repo**. Only `benchmark-results/` is
gitignored, and rsync without `--delete` merges whatever is already there — two
runs in one directory collect into one unreadable CSV.

## Merging a gap-filling run

Collecting a partial run straight into `results.csv` **silently drops the
existing abstract rows**: `_preserved_concrete_rows` keeps only `concrete` rows
the run did not cover. Merge the raw trees instead, then collect once:

1. rsync both result directories into one scratch directory
2. write a manifest whose `expected_results` is the union of both manifests
3. `collect_benchmarks.main(<merged dir>, "benchmarks/results.csv")`

Confirm the collect prints no `Incomplete benchmark run` line and that the row
count matches problems × 2.

## Submitting

```bash
python -m scripts.run_benchmarks --with-concrete
```

`--with-concrete` is almost always right: `report_benchmarks` pairs the two
pipelines and drops any problem missing one, so abstract-only problems appear in
no table.

`main()` calls `_reset_results_dir()`, which **deletes the whole results tree**
before submitting. Move it aside first, or confirm the results are already
pulled.

To submit a subset, cut the problem files the runner reads down to the wanted
problems, submit, then `git checkout --` them. Workers get explicit problem
paths, so restoring the files mid-run is safe. Say plainly that such a run is
not reproducible from a SHA, since the committed code submits the whole set.

## Before reporting on a run

```bash
awk -F, '$4=="running"' benchmarks/results.csv | wc -l
```

`running` rows are jobs killed without a terminal status, not live work. They
cluster at one `last_completed_phase` when a limit killed them. Report a run as
partial rather than averaging over them, and check `status` for `error` and
`killed (signal 9)` too — a domain can contribute nothing while the totals still
look healthy.

## Closing the loop

When results land, do all four without being asked:

1. collect into `benchmarks/results.csv`
2. `python -m scripts.report_benchmarks` to regenerate `benchmarks/reports.md`
3. commit both with the message `Update results`
4. push
