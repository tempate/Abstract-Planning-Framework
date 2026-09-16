# Benchmark report

2026-09-16 16:15 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       116 (26.0%)         99 (22.2%)
Timeouts                                          318 (71.3%)        335 (75.1%)
Out of memory                                       12 (2.7%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              93                 93
Faster when both found a plan                      29 (31.2%)         64 (68.8%)
Plan found when the other did not                          23                  6
Median runtime when both found a plan                  8.23 s             8.13 s
Total runtime across shared solves                 2,823.72 s         7,664.04 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     281 (88%)
Extended concrete search                              20 (6%)
Guided concrete search                                17 (5%)
Total                                                     318
```

## How the successes were solved

```
How the 116 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       84 (72%)
Refined after switching some actions off             24 (21%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     116
```

## Deletes relaxed, over the 108 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 94 (87%)
1 to 4                                                 5 (5%)
5 to 9                                                 6 (6%)
10 to 19                                               1 (1%)
20 or more                                             2 (2%)
Total                                                     108
```
