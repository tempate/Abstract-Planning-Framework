# Benchmark report

2026-09-17 13:07 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       120 (26.9%)         99 (22.2%)
Timeouts                                          314 (70.4%)        335 (75.1%)
Out of memory                                       12 (2.7%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              97                 97
Faster when both found a plan                      36 (37.1%)         61 (62.9%)
Plan found when the other did not                          23                  2
Median runtime when both found a plan                  8.50 s             9.75 s
Total runtime across shared solves                 6,184.68 s         8,720.46 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     260 (83%)
Guided concrete search                               34 (11%)
Extended concrete search                              20 (6%)
Total                                                     314
```

## How the successes were solved

```
How the 120 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       66 (55%)
Refined after switching some actions off             46 (38%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     120
```

## Deletes relaxed, over the 112 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               66 (59%)
5 to 9                                                 8 (7%)
10 to 19                                             22 (20%)
20 or more                                             5 (4%)
Total                                                     112
```
