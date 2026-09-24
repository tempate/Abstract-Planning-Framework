# Benchmark report

2026-09-24 10:54 — experiments/plan/results.csv

665 problems compared over abstract, concrete, lama; 2 dropped as unfinished

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline         LAMA-first
---------------------------------------------------------------------------------------------------
Plans found                                       127 (19.1%)        112 (16.8%)        600 (90.2%)
Timeouts                                          526 (79.1%)        541 (81.4%)          41 (6.2%)
Out of memory                                       12 (1.8%)          12 (1.8%)          23 (3.5%)
Others                                               0 (0.0%)           0 (0.0%)           1 (0.2%)
Total problems                                            665                665                665
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both                                       110                110
Faster when both found a plan                      32 (29.1%)         78 (70.9%)
Plan found when the other did not                          17                  2
Median runtime when both found a plan                  8.16 s            10.10 s
Total runtime across shared solves                 5,728.63 s         9,308.41 s
```

## Head to head: abstract vs LAMA-first

```
Metric                                      Abstract pipeline         LAMA-first
--------------------------------------------------------------------------------
Plans found by both                                       127                127
Faster when both found a plan                        1 (0.8%)        126 (99.2%)
Plan found when the other did not                           0                473
Median runtime when both found a plan                 12.57 s             2.43 s
Total runtime across shared solves                15,220.70 s           507.33 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     464 (88%)
Abstract plan discarded                               33 (6%)
Guided concrete search                                29 (6%)
Total                                                     526
```

## How the successes were solved

```
How the 127 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       80 (63%)
Refined after switching some actions off             38 (30%)
Abstract plan discarded, solved above it               9 (7%)
Total                                                     127
```

## Deletes relaxed, over the 118 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 12 (10%)
1 to 4                                               75 (64%)
5 to 9                                                 7 (6%)
10 to 19                                             18 (15%)
20 or more                                             6 (5%)
Total                                                     118
```
