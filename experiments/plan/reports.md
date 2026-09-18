# Benchmark report

2026-09-18 09:37 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       119 (26.7%)         99 (22.2%)
Timeouts                                          315 (70.6%)        335 (75.1%)
Out of memory                                       12 (2.7%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              96                 96
Faster when both found a plan                      36 (37.5%)         60 (62.5%)
Plan found when the other did not                          23                  3
Median runtime when both found a plan                  8.19 s             9.77 s
Total runtime across shared solves                 6,217.06 s         8,695.48 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     263 (83%)
Guided concrete search                               32 (10%)
Extended concrete search                              20 (6%)
Total                                                     315
```

## How the successes were solved

```
How the 119 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       66 (55%)
Refined after switching some actions off             45 (38%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     119
```

## Deletes relaxed, over the 111 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               69 (62%)
5 to 9                                                 8 (7%)
10 to 19                                             18 (16%)
20 or more                                             5 (5%)
Total                                                     111
```
