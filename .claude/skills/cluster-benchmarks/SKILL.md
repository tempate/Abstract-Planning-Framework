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
`experiments/benchmarks/downward-benchmarks` and `lib/plasp/bin` are symlinks into
`~/apf/.shared`, which holds the only built copy. A branch that vendors
`lib/numeric-fast-downward` gets that linked too. Nothing is built per worktree,
so a branch that moved a submodule pointer would silently run the shared
version — we build one copy because no branch here moves one.

## Pulling a finished run

`experiments.fetch` does the checking itself: it refuses while `squeue` still
holds the run's jobs, rsyncs the run into a fresh temporary directory, and
collects it only when this checkout holds the code the manifest says submitted
it (commits that only touch `results.csv` or `report.md` since do not count).
It prints the producing commit and the directory either way, so a pull states
its own provenance:

```bash
python -m experiments.fetch
```

`--remote-dir` defaults to `~/apf/<branch>/runs/` for the branch this checkout
is on, which is where `new-worktree.sh` puts it. Pass it explicitly for a run
that lives anywhere else. The CSV defaults to the one of the track the manifest
names.

## Merging a gap-filling run

A partial run collects straight into `results.csv`: a row is replaced only where
the run holds that (domain, problem, mode), so the rest stays. A problem that
left the suite keeps its old row until you delete it.

## Submitting

```bash
python -m experiments.submit --modes abstract concrete lama
```

Submit every mode you want compared: `experiments.report` pairs **all** of them
and drops any problem missing one, so a mode left out of a run shrinks every
table. `lama` is plain Fast Downward, the external baseline. Runs go to
`sunnycove` by default, one CPU generation, so timings are comparable across a
run. Only pass `--partition any` to fill a queue you do not intend to publish
timings from: it spans two CPU generations and caps each job at one hour.

`--track unsolvability` takes only `abstract` and `concrete`: `scripts.unsolvability`
has no `lama` subcommand, and its concrete mode already is a plain Fast Downward
search.

`--track unsolvability` swaps the suite for unsolve-ipc-2016 and the planner for
`scripts.unsolvability`, which reports a verdict instead of a plan. The CSV
carries it in the `verdict` column. Only the probNN problems run, the ones known
unsolvable; satprob and unknownprob are skipped.

`main()` calls `_set_aside_results_dir()`, which renames the previous `runs/` to
`runs-<timestamp>/` and prints where it went. The new run still starts on an
empty directory, because collect reads every result underneath. Nothing is
deleted, so those siblings accumulate until pruned by hand.

To submit a subset, name it:

```bash
python -m experiments.submit --domains driverlog gripper --problems p07 p08
```

`--problems` matches within every domain submitted, by file name or stem. A
domain not in the track's suite is refused rather than quietly submitting
nothing. The manifest records exactly what was submitted, so the run stays
reproducible from a SHA plus its flags.

`--dry-run` prints the job count, the CopperBench config and the first
instances, and returns before touching `runs/` or the queue. Check a submit-side
change with it rather than against a real run.

## Running two branches at once

One run per worktree, never two from one checkout. Submitting renames `runs/`
aside rather than deleting it, so the first run's results survive — but that
path is `PROJECT_ROOT`-relative, and the jobs still writing into it follow the
directory to its new name while the manifest they are collected against is the
new run's.

```bash
ssh -o BatchMode=yes copperhead '~/apf/new-worktree.sh <branch>'
```

That fetches, adds `~/apf/<branch>`, replaces each empty submodule directory
with a link into `~/apf/.shared`, and asserts every artifact is reachable before
it prints `ready:`. Two seconds, no build.

Plain `git worktree add` leaves `experiments/benchmarks/downward-benchmarks`,
`lib/downward` and `lib/pddl-symmetries` empty. Submitting now refuses and names
what is missing, rather than queueing jobs that all die the same way. None of
these are checked in:

| missing | how it fails |
|---|---|
| `pybind11_blissmodule.so` | every abstract job dies in symmetry discovery |
| `lib/downward/builds/release` | exit code 36, `Could not find build 'release'` |
| `lib/plasp/bin/plasp` | `plasp binary not found`, before any solving |
| `lib/numeric-fast-downward/builds/release64` | `numeric-fast-downward binary not found`, on every resources-track job |

Left unchecked, the tell for all of these is a queue that drains far faster than 30
minutes a job. Smoke-test anyway when the branch touches the pipeline itself,
which the preflight cannot judge:

```bash
./examples/abstract.sh   # driverlog p07: collapses three packages, plan length 15
```

Pick a problem the branch solves quickly. A refinement branch can time out on a
hard one for its own reasons, which says nothing about the worktree.

`experiments.fetch` guards on the run's own jobs — CopperBench names every array
task after the run — so a finished run can be pulled while another is still
queued. `--remote-dir` follows the branch each checkout is on.

Removing a worktree afterwards needs `--force`, since the symlinks read as
local modifications:

```bash
ssh -o BatchMode=yes copperhead 'git -C ~/apf/.bare worktree remove --force ~/apf/<branch>'
```

## Rebuilding numeric-fast-downward

`~/apf/.shared/numeric-fast-downward` is the vendored source at `fac7ce0` with
`lib/numeric-fast-downward.patch` applied. The patch is what makes it buildable
here at all: the cluster has no CPLEX, and unpatched the LP layer demands it.

COIN lives in its own prefix, `~/apf/.shared/coin`, and **not** in the `apf` env —
installing into `apf` would disturb whatever jobs are running. `FindOSI.cmake`
reads `DOWNWARD_COIN_ROOT`, and `build.py` has a bare `python` shebang that does
not resolve here:

```bash
conda create -y -p ~/apf/.shared/coin -c conda-forge coin-or-osi coin-or-clp coin-or-utils
export DOWNWARD_COIN_ROOT=~/apf/.shared/coin
cd ~/apf/.shared/numeric-fast-downward && python3 ./build.py release64 -j4
```

`ldd` on the built binary must resolve the COIN libraries through RPATH, or the
jobs need `LD_LIBRARY_PATH` too. Detection exits through the no-solution path and
aborts even on success, so `Found <n>/<m> resource variables` on stdout is the
only thing that says it worked.

## Watching a run

```bash
python -m experiments.status
```

Reports the run's own queued jobs, how many results are written against how many
the manifest expects, and what each result says so far. It reads the cluster in
place and pulls nothing, so it is the right thing to put on a background watch:
the queue count alone means opposite things depending on whether the worktree is
built.

Results still saying `running` with no job left running are flagged. Those jobs
were killed before they could write an outcome. runsolver's memory limit is not
one of them: the worker catches its SIGINT and writes `interrupted`.

## Before reporting on a run

```bash
awk -F, '$4=="running"' experiments/plan/symmetries/results.csv | wc -l
```

`running` rows are jobs killed without a terminal status, not live work. Report a
run as partial rather than averaging over them. `interrupted` is runsolver's
memory limit and `out of memory` is Fast Downward's own; both cluster at one
`last_completed_phase`. Check `status` for `error` and `killed (signal 9)` too —
a domain can contribute nothing while the totals still look healthy. In a CSV
collected before #101, a crash reads `no plan found` and a memory kill `running`.

## Closing the loop

When results land, do all five without being asked:

1. collect into `experiments/plan/symmetries/results.csv`
2. `python -m experiments.report` to regenerate `experiments/plan/symmetries/report.md`
3. commit both with the message `Update results`
4. push
5. rewrite the description of the branch's PR around the run's numbers, following **Writing the PR** in the `pull-requests` skill, and drop any numbers or run IDs from earlier runs
