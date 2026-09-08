# Benchmark report

2026-09-08 16:40 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        83 (21.8%)         75 (19.7%)
Timeouts                                          296 (77.7%)        305 (80.1%)
Total problems                                            381                381
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              72                 72
Faster when both found a plan                      23 (31.9%)         49 (68.1%)
Plan found when the other did not                          11                  3
Median runtime when both found a plan                  6.57 s             8.97 s
Total runtime across shared solves                 3,942.11 s         6,867.90 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     251 (85%)
Guided concrete search                                28 (9%)
Extended concrete search                              17 (6%)
Total                                                     296
```

## How the successes were solved

```
How the 83 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       52 (63%)
Refined after switching some actions off             26 (31%)
Abstract plan discarded, solved above it               5 (6%)
Total                                                      83
```

## Deletes relaxed, over the 78 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (14%)
1 to 4                                               39 (50%)
5 to 9                                                 5 (6%)
10 to 19                                             14 (18%)
20 or more                                            9 (12%)
Total                                                      78
```
