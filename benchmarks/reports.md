# Benchmark report

2026-09-07 14:19 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                        99 (21.7%)        111 (24.3%)
Timeouts                                          356 (77.9%)        345 (75.5%)
Total problems                                            457                457
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              97                 97
Faster when both found a plan                        5 (5.2%)         92 (94.8%)
Plan found when the other did not                           2                 14
Median runtime when both found a plan                 13.24 s             8.86 s
Total runtime across shared solves                10,600.99 s         4,446.11 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     310 (87%)
Extended concrete search                              30 (8%)
Guided concrete search                                16 (4%)
Total                                                     356
```

## How the successes were solved

```
How the 99 successes were solved                     Problems
-------------------------------------------------------------
Abstract plan refined directly                       55 (56%)
Refined after switching some actions off             12 (12%)
Abstract plan discarded, solved above it             32 (32%)
Total                                                      99
```

## Deletes relaxed

```
This CSV predates the relaxed-deletes counter
```
