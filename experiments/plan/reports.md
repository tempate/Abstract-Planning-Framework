# Benchmark report

2026-09-17 09:20 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       113 (25.3%)         99 (22.2%)
Timeouts                                          321 (72.0%)        335 (75.1%)
Out of memory                                       12 (2.7%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              95                 95
Faster when both found a plan                      33 (34.7%)         62 (65.3%)
Plan found when the other did not                          18                  4
Median runtime when both found a plan                  8.42 s             9.09 s
Total runtime across shared solves                 5,733.45 s         8,293.16 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     267 (83%)
Guided concrete search                               34 (11%)
Extended concrete search                              20 (6%)
Total                                                     321
```

## How the successes were solved

```
How the 113 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       71 (63%)
Refined after switching some actions off             34 (30%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     113
```

## Deletes relaxed, over the 105 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               67 (64%)
5 to 9                                               11 (10%)
10 to 19                                             13 (12%)
20 or more                                             3 (3%)
Total                                                     105
```
