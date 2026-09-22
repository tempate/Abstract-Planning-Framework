# Benchmark report

2026-09-22 09:39 — experiments/plan/results.csv

665 problems compared over abstract, concrete, lama; 2 dropped as unfinished

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                       135 (20.3%)        112 (16.8%)        600 (90.2%)
Timeouts                                          518 (77.9%)        541 (81.4%)          41 (6.2%)
Out of memory                                       12 (1.8%)          12 (1.8%)          23 (3.5%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.2%)
Total problems                                            665                665                665
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                       110                110
Faster when both found a plan                      39 (35.5%)         71 (64.5%)
Plan found when the other did not                          25                  2
Median runtime when both found a plan                  7.99 s            10.10 s
Total runtime across shared solves                 7,925.11 s        10,601.69 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                       135                135
Faster when both found a plan                        1 (0.7%)        134 (99.3%)
Plan found when the other did not                           0                465
Median runtime when both found a plan                 11.54 s             2.43 s
Total runtime across shared solves                20,380.81 s           533.75 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     452 (87%)
Guided concrete search                                33 (6%)
Abstract plan discarded                               33 (6%)
Total                                                     518
```

## How the successes were solved

```
How the 135 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       72 (53%)
Refined after switching some actions off             54 (40%)
Abstract plan discarded, solved above it               9 (7%)
Total                                                     135
```

## Deletes relaxed, over the 126 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 12 (10%)
1 to 4                                               77 (61%)
5 to 9                                                 9 (7%)
10 to 19                                             23 (18%)
20 or more                                             5 (4%)
Total                                                     126
```
