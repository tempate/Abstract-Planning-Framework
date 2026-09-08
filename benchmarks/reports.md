# Benchmark report

2026-09-08 13:44 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        83 (21.8%)         75 (19.7%)
Timeouts                                          295 (77.6%)        305 (80.3%)
Total problems                                            380                380
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              72                 72
Faster when both found a plan                      17 (23.6%)         55 (76.4%)
Plan found when the other did not                          11                  3
Median runtime when both found a plan                  7.46 s             8.99 s
Total runtime across shared solves                 5,332.50 s         6,815.32 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     271 (92%)
Extended concrete search                              17 (6%)
Guided concrete search                                 7 (2%)
Total                                                     295
```

## How the successes were solved

```
How the 83 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       56 (67%)
Refined after switching some actions off             22 (27%)
Abstract plan discarded, solved above it               5 (6%)
Total                                                      83
```

## Deletes relaxed, over the 78 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (14%)
1 to 4                                               39 (50%)
5 to 9                                               13 (17%)
10 to 19                                             15 (19%)
20 or more                                             0 (0%)
Total                                                      78
```
