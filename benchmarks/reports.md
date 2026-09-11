# Benchmark report

2026-09-11 15:06 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        91 (20.7%)         78 (17.8%)
Timeouts                                          339 (77.2%)        359 (81.8%)
Total problems                                            439                439
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              75                 75
Faster when both found a plan                      21 (28.0%)         54 (72.0%)
Plan found when the other did not                          16                  3
Median runtime when both found a plan                  7.06 s             9.19 s
Total runtime across shared solves                 9,061.88 s        11,333.48 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     297 (88%)
Extended concrete search                             35 (10%)
Guided concrete search                                 7 (2%)
Total                                                     339
```

## How the successes were solved

```
How the 91 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       60 (66%)
Refined after switching some actions off             23 (25%)
Abstract plan discarded, solved above it               8 (9%)
Total                                                      91
```

## Deletes relaxed, over the 83 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (13%)
1 to 4                                               44 (53%)
5 to 9                                               13 (16%)
10 to 19                                             15 (18%)
20 or more                                             0 (0%)
Total                                                      83
```
