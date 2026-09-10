# Benchmark report

2026-09-10 08:51 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        78 (20.5%)         75 (19.7%)
Timeouts                                          300 (78.9%)        305 (80.3%)
Total problems                                            380                380
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              70                 70
Faster when both found a plan                      16 (22.9%)         54 (77.1%)
Plan found when the other did not                           8                  5
Median runtime when both found a plan                  7.98 s             7.60 s
Total runtime across shared solves                 5,260.12 s         5,188.27 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     270 (90%)
Extended concrete search                              17 (6%)
Guided concrete search                                13 (4%)
Total                                                     300
```

## How the successes were solved

```
How the 78 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       66 (85%)
Refined after switching some actions off               7 (9%)
Abstract plan discarded, solved above it               5 (6%)
Total                                                      78
```

## Deletes relaxed, over the 73 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (15%)
1 to 4                                               39 (53%)
5 to 9                                               10 (14%)
10 to 19                                             13 (18%)
20 or more                                             0 (0%)
Total                                                      73
```
