# Benchmark report

2026-09-10 08:44 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        80 (21.1%)         75 (19.7%)
Timeouts                                          298 (78.4%)        305 (80.3%)
Total problems                                            380                380
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              71                 71
Faster when both found a plan                      19 (26.8%)         52 (73.2%)
Plan found when the other did not                           9                  4
Median runtime when both found a plan                  7.40 s             8.80 s
Total runtime across shared solves                 4,379.32 s         6,613.59 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     271 (91%)
Extended concrete search                              17 (6%)
Guided concrete search                                10 (3%)
Total                                                     298
```

## How the successes were solved

```
How the 80 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       62 (78%)
Refined after switching some actions off             16 (20%)
Abstract plan discarded, solved above it               2 (2%)
Total                                                      80
```

## Deletes relaxed, over the 78 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (14%)
1 to 4                                               39 (50%)
5 to 9                                               15 (19%)
10 to 19                                             13 (17%)
20 or more                                             0 (0%)
Total                                                      78
```
