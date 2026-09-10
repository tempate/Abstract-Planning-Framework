# Benchmark report

2026-09-10 08:55 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        79 (20.8%)         75 (19.7%)
Timeouts                                          299 (78.7%)        305 (80.3%)
Total problems                                            380                380
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              72                 72
Faster when both found a plan                      20 (27.8%)         52 (72.2%)
Plan found when the other did not                           7                  3
Median runtime when both found a plan                  6.55 s             8.99 s
Total runtime across shared solves                 5,672.79 s         6,815.32 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     270 (90%)
Extended concrete search                              17 (6%)
Guided concrete search                                12 (4%)
Total                                                     299
```

## How the successes were solved

```
How the 79 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       72 (91%)
Refined after switching some actions off               2 (3%)
Abstract plan discarded, solved above it               5 (6%)
Total                                                      79
```

## Deletes relaxed, over the 74 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (15%)
1 to 4                                               39 (53%)
5 to 9                                               10 (14%)
10 to 19                                             14 (19%)
20 or more                                             0 (0%)
Total                                                      74
```
