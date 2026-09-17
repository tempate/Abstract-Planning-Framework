# Benchmark report

2026-09-17 13:11 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       118 (26.5%)         99 (22.2%)
Timeouts                                          316 (70.9%)        335 (75.1%)
Out of memory                                       12 (2.7%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              96                 96
Faster when both found a plan                      29 (30.2%)         67 (69.8%)
Plan found when the other did not                          22                  3
Median runtime when both found a plan                  7.66 s             9.77 s
Total runtime across shared solves                 5,864.07 s         8,695.48 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     262 (83%)
Guided concrete search                               34 (11%)
Extended concrete search                              20 (6%)
Total                                                     316
```

## How the successes were solved

```
How the 118 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       66 (56%)
Refined after switching some actions off             44 (37%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     118
```

## Deletes relaxed, over the 110 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               68 (62%)
5 to 9                                                 8 (7%)
10 to 19                                             18 (16%)
20 or more                                             5 (5%)
Total                                                     110
```
