---
name: cluster-benchmarks
description: Submit benchmark runs to the SLURM cluster, watch them, and pull the results back into a PR. Use when asked to run benchmarks on the cluster, submit a suite or a subset of it, check how the cluster is going, pull or collect a run's results, fill in problems a run missed, or report on a run.
---

# Cluster benchmark runs

Benchmarks run on `copperhead`, reached over plain non-interactive ssh through the
`vivaldi` jump host. Every command there needs the conda env first:

```bash
source ~/miniconda3/etc/profile.d/conda.sh && conda activate apf
```

A run belongs to a PR. The PR is a draft from the moment its run is submitted until
its results are pushed, and ready from then on (see **Closing the loop**).

## Checkouts

Every run has its own checkout, a worktree of the bare repo `~/apf/.bare` at
`~/apf/<branch>`. Its `lib/downward`, `lib/pddl-symmetries`, `lib/plasp/bin`,
`experiments/benchmarks/downward-benchmarks` and, where vendored,
`lib/numeric-fast-downward` are symlinks into `~/apf/.shared`, the only built copy.
Nothing is built per checkout, so a branch that moved a submodule pointer would
silently run the shared version. No branch here moves one.

```bash
ssh -o BatchMode=yes copperhead '~/apf/new-worktree.sh <branch>'
```

The script fetches, adds the worktree, links the shared tools, and checks every
artifact before it prints `ready:`. It takes two seconds.

One run per checkout. Submitting renames `runs/` aside, and jobs still writing into
it follow it to its new name while the new manifest no longer matches them. A
branch that runs on several tracks therefore needs one checkout per track. Give
each extra one a branch name of its own at the same commit:

```bash
ssh -o BatchMode=yes copperhead 'git -C ~/apf/.bare fetch -q origin \
  && git -C ~/apf/.bare branch <branch>-<track> origin/<branch> \
  && ~/apf/new-worktree.sh <branch>-<track>'
```

Plain `git worktree add` leaves the linked directories empty. Submitting refuses
and names what is missing, rather than queueing jobs that all die the same way:

| missing | how it fails |
|---|---|
| `pybind11_blissmodule.so` | every abstract job dies in symmetry discovery |
| `lib/downward/builds/release` | exit code 36, `Could not find build 'release'` |
| `lib/plasp/bin/plasp` | `plasp binary not found`, before any solving |
| `lib/numeric-fast-downward/builds/release64` | `numeric-fast-downward binary not found`, on every resources-track job |

Smoke-test a branch that changes the pipeline, which the checks above cannot
judge. Run each mode it touches on a problem it solves fast and expect a valid plan:

```bash
python -m scripts.planner abs-asp \
  --domain experiments/benchmarks/downward-benchmarks/gripper/domain.pddl \
  --problem experiments/benchmarks/downward-benchmarks/gripper/prob01.pddl
```

Removing a checkout needs `--force`, since the symlinks read as local changes:

```bash
ssh -o BatchMode=yes copperhead 'git -C ~/apf/.bare worktree remove --force ~/apf/<branch>'
```

Setting up checkouts, smoke-testing and submitting can take minutes. Chain them in
one background command.

## Submitting

```bash
python -m experiments.submit --track sat --abstraction-source symmetries --modes abs-asp abs-lama asp lama
```

| track | modes | baseline |
|---|---|---|
| `sat` | `asp`, `abs-asp`, `lama`, `abs-lama` | `lama`, Fast Downward's lama-first |
| `opt` | `asp`, `abs-asp`, `lmcut`, `abs-lmcut` | `lmcut`, A* with LM-cut |
| `unsat` | `ms`, `abs-ms` | `ms`, A* with merge-and-shrink |

`--abstraction-source resources` collapses resources instead of symmetric objects.
`--track unsat` runs `scripts.unsolvability` over the probNN problems of
unsolve-ipc-2016 and records a `verdict` instead of a plan. Submit refuses a mode
its track does not run.

`experiments.report` compares only problems every mode in the CSV finished, so a
mode left out of a run shrinks every table. Leave a mode out only when its results
from an earlier run still hold, such as the baselines under a refinement change.

Runs go to `sunnycove`, one CPU generation, so timings compare across runs. Pass
`--partition any` only to fill a queue whose timings you will not publish. It spans
two CPU generations and caps each job at one hour.

An abstract mode runs, by default, the class it did best with in the track's
`results.csv`, plus every class `classes.txt` lists for a problem without a result.
`--classes all` runs every class.

To submit a subset, name it:

```bash
python -m experiments.submit --domains driverlog gripper --problems p07 p08
```

`--problems` matches by file name in every domain submitted, so the run is the cross
product of the two lists. A subset that picks different problems per domain runs
more than asked whenever names repeat across domains, as `p01` does. Keep the
intended (domain, problem) pairs and report on those alone. `--dry-run` prints the
job count without touching `runs/` or the queue, so compare it with the pairs first.

When the run is for an open PR, make the PR a draft in the same step:

```bash
gh pr ready <n> --undo
```

Then start a background watch (see **Watching a run**).

## The queue

Pending jobs start by priority. Fairshare and job size are equal across your own
jobs, so among them the one that has waited longest starts first. Two things bend
that order. Backfill starts a later job early when it fits a gap. A requeued task
restarts its age and falls behind. To put one run ahead of your others, lower the
others, which only touches your own jobs:

```bash
scontrol update job=<array job id> nice=300
```

`sacct` shows some tasks as FAILED with exit code `4:0`. Those are CopperBench
refusing to start a finished task twice, and their stdout says
`Solver already finished before`. Their results are intact.

## Watching a run

Every run in the queue gets a background watch without being asked, including runs
submitted in an earlier session. One watch per PR, polling every ten minutes. Open a
fresh ssh for each poll, and treat a failed ssh as no answer, never as an empty
queue:

```bash
while true; do
  queue=$(ssh -o BatchMode=yes -o ConnectTimeout=20 copperhead 'squeue -u dquilez -h -o "%j"') \
    || { sleep 60; continue; }
  grep -qE '<run-name>|<other-run-name>' <<<"$queue" || break
  sleep 600
done
```

Start the loop as a background command, never in the foreground. A run takes hours,
and a foreground loop blocks the session for all of them, while a background one
reports back when the run drains.

The run's name is the `run-<timestamp>` directory submit wrote. For progress, count
states per run:

```bash
ssh copperhead 'sacct -u dquilez -S <date> -X -n -P --name=<run-name> -o State | sort | uniq -c'
```

`python -m experiments.status` reports the run's queued and running jobs and what
its results say so far. It opens its own ssh, so run it locally from a checkout of
the branch, never on copperhead.

## Pulling a finished run

```bash
python -m experiments.fetch --remote-dir '~/apf/<checkout>/runs/'
```

`fetch` refuses while the run still has jobs queued, rsyncs it into a fresh
temporary directory, and collects it into the CSV of the track the manifest names.
It prints the producing commit and the directory, which holds the run's
`manifest.json`. The rsync can take minutes, so pull in the background too.
`--remote-dir` defaults to the checkout named after the current branch.

`fetch` collects only into a checkout whose code matches the commit that produced
the run. Commits that touch only `results.csv` or `report.md` do not count. When the
branch has moved on with code changes that cannot change behavior, collect in a
detached checkout of the producing commit and copy the CSVs to the branch tip.

Collect replaces a row only where the run holds its (domain, problem, mode, class),
so the rest stays. A best-class run therefore lands next to the other classes an
earlier every-class run left, and `experiments.report` takes the best class across
both runs. For the PR's numbers, keep only the abstract rows the run's manifest
lists, and compare against the base on the same problems and classes. A problem
that left the suite keeps its old row until you delete it.

That merge is only right when the PR leaves the classes it did not rerun alone. When
it changes what every class does, as #139 changed refinement, the old rows measure
code that no longer exists, and both the report and the next run's best-class choice
read them. Then delete the abstract rows the run's manifest does not list before
committing the results, or run every class.

## Before reporting on a run

```bash
awk -F, '$5=="running"' experiments/<track>/<source>/results.csv | wc -l
```

A `running` row is a job killed without a terminal status, not live work. Report the
run as partial rather than averaging over them. `interrupted` is runsolver's memory
limit and `out of memory` is Fast Downward's own. Both are results. Check `status`
for `error` and `killed (signal 9)` too, since one domain can contribute nothing
while the totals look healthy. In a CSV collected before #101, a crash reads
`no plan found` and a memory kill `running`.

## Mode names before #135

Delete this section once no open branch predates #135. Branches that left `main` before #135 still call the modes `fd`, `abs-fd`,
`fd-lmcut` and so on. Their CSVs need the new names after a rebase onto `main`,
or the report ignores those rows. The mode is column 3, and the files are CRLF,
which `awk` keeps:

```bash
awk -F, -v OFS=, 'NR>1 && $3=="fd"{$3="lama"} NR>1 && $3=="abs-fd"{$3="abs-lama"} {print}' results.csv > tmp && mv tmp results.csv
```

| track | old | new |
|---|---|---|
| sat | `fd`, `abs-fd` | `lama`, `abs-lama` |
| opt | `fd-lmcut`, `abs-fd` | `lmcut`, `abs-lmcut` |
| unsat | `fd`, `abs-fd` | `ms`, `abs-ms` |

## Closing the loop

When a watch reports a run done, do all of this without being asked:

1. Pull every run of the PR into its branch.
2. Regenerate each touched track's report with `python -m experiments.report <results.csv>`.
3. Commit the CSVs and reports as `Update results`.
4. Push, and mark the PR ready with `gh pr ready <n>` in the same step.
5. Rewrite the description around the run's numbers and figures, following **Experiment PRs** in the `pull-requests` skill, and drop numbers from earlier runs.

## Rebuilding numeric-fast-downward

`~/apf/.shared/numeric-fast-downward` is the vendored source at `fac7ce0` with
`lib/numeric-fast-downward.patch` applied. The patch makes it build without CPLEX,
which the cluster lacks.

COIN lives in its own prefix, `~/apf/.shared/coin`, not in the `apf` env, where
installing would disturb running jobs. `FindOSI.cmake` reads `DOWNWARD_COIN_ROOT`,
and `build.py` has a bare `python` shebang that does not resolve here:

```bash
conda create -y -p ~/apf/.shared/coin -c conda-forge coin-or-osi coin-or-clp coin-or-utils
export DOWNWARD_COIN_ROOT=~/apf/.shared/coin
cd ~/apf/.shared/numeric-fast-downward && python3 ./build.py release64 -j4
```

`ldd` on the binary must resolve the COIN libraries through RPATH, or the jobs need
`LD_LIBRARY_PATH` too. Detection exits through the no-solution path even on success,
so `Found <n>/<m> resource variables` on stdout is the only sign it worked.
