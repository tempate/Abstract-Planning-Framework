# Benchmark report

2026-09-08 11:33 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       118 (25.8%)        110 (24.1%)
Timeouts                                          335 (73.3%)        345 (75.5%)
Total problems                                            457                457
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                             103                103
Faster when both found a plan                      18 (17.5%)         85 (82.5%)
Plan found when the other did not                          15                  7
Median runtime when both found a plan                 11.42 s             9.86 s
Total runtime across shared solves                 9,215.24 s         8,333.96 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     310 (93%)
Extended concrete search                              17 (5%)
Guided concrete search                                 8 (2%)
Total                                                     335
```

## How the successes were solved

```
How the 118 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       89 (75%)
Refined after switching some actions off             24 (20%)
Abstract plan discarded, solved above it               5 (4%)
Total                                                     118
```

## Deletes relaxed, over the 113 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               69 (61%)
5 to 9                                               13 (12%)
10 to 19                                             15 (13%)
20 or more                                             5 (4%)
Total                                                     113
```
