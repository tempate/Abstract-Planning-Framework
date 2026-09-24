# Benchmark report

2026-09-24 11:30 — experiments/plan/symmetries/results.csv

667 problems compared over abstract, concrete, lama

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                       135 (20.2%)        113 (16.9%)        602 (90.3%)
Timeouts                                          519 (77.8%)        541 (81.1%)          42 (6.3%)
Out of memory                                       13 (1.9%)          13 (1.9%)          22 (3.3%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.1%)
Total problems                                            667                667                667
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                       111                111
Faster when both found a plan                      43 (38.7%)         68 (61.3%)
Plan found when the other did not                          24                  2
Median runtime when both found a plan                  8.09 s            10.35 s
Total runtime across shared solves                 8,268.69 s        12,840.20 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                       135                135
Faster when both found a plan                        4 (3.0%)        131 (97.0%)
Plan found when the other did not                           0                467
Median runtime when both found a plan                 11.07 s             3.11 s
Total runtime across shared solves                21,616.50 s           626.21 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     454 (87%)
Abstract plan discarded                               33 (6%)
Guided concrete search                                32 (6%)
Total                                                     519
```

## How the successes were solved

```
How the 135 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       72 (53%)
Refined after switching some actions off             54 (40%)
Abstract plan discarded, solved above it               9 (7%)
Total                                                     135
```

## Deletes relaxed, over the 126 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 12 (10%)
1 to 4                                               77 (61%)
5 to 9                                                 9 (7%)
10 to 19                                             23 (18%)
20 or more                                             5 (4%)
Total                                                     126
```
