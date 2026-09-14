# Benchmark report

2026-09-14 11:37 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        90 (23.7%)         75 (19.7%)
Timeouts                                          288 (75.8%)        305 (80.3%)
Total problems                                            380                380
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              75                 75
Faster when both found a plan                      29 (38.7%)         46 (61.3%)
Plan found when the other did not                          15                  0
Median runtime when both found a plan                  6.81 s             9.57 s
Total runtime across shared solves                 4,331.64 s         9,445.54 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     238 (83%)
Guided concrete search                               30 (10%)
Extended concrete search                              20 (7%)
Total                                                     288
```

## How the successes were solved

```
How the 90 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       48 (53%)
Refined after switching some actions off             35 (39%)
Abstract plan discarded, solved above it               7 (8%)
Total                                                      90
```

## Deletes relaxed, over the 83 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (13%)
1 to 4                                               43 (52%)
5 to 9                                                8 (10%)
10 to 19                                             19 (23%)
20 or more                                             2 (2%)
Total                                                      83
```
