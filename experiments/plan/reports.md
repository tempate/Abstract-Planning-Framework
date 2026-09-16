# Benchmark report

2026-09-16 10:25 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       114 (25.6%)         99 (22.2%)
Timeouts                                          319 (71.5%)        335 (75.1%)
Out of memory                                       13 (2.9%)          12 (2.7%)
No plan found                                        0 (0.0%)           0 (0.0%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              96                 96
Faster when both found a plan                      29 (30.2%)         67 (69.8%)
Plan found when the other did not                          18                  3
Median runtime when both found a plan                  8.12 s             9.42 s
Total runtime across shared solves                 7,112.92 s         8,318.14 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     266 (83%)
Guided concrete search                               34 (11%)
Extended concrete search                              19 (6%)
Total                                                     319
```

## How the successes were solved

```
How the 114 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       68 (60%)
Refined after switching some actions off             38 (33%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     114
```

## Deletes relaxed, over the 106 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               64 (60%)
5 to 9                                                 9 (8%)
10 to 19                                             19 (18%)
20 or more                                             3 (3%)
Total                                                     106
```
