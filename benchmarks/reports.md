# Benchmark report

2026-09-15 14:48 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       116 (27.1%)         99 (23.1%)
Timeouts                                          310 (72.4%)        329 (76.9%)
Total problems                                            428                428
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              97                 97
Faster when both found a plan                      30 (30.9%)         67 (69.1%)
Plan found when the other did not                          19                  2
Median runtime when both found a plan                  8.48 s             9.75 s
Total runtime across shared solves                 7,942.12 s         8,720.46 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     255 (82%)
Guided concrete search                               32 (10%)
Extended concrete search                              19 (6%)
pnf_translation                                        4 (1%)
Total                                                     310
```

## How the successes were solved

```
How the 116 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       67 (58%)
Refined after switching some actions off             41 (35%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     116
```

## Deletes relaxed, over the 108 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               64 (59%)
5 to 9                                                10 (9%)
10 to 19                                             19 (18%)
20 or more                                             4 (4%)
Total                                                     108
```
