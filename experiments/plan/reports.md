# Benchmark report

2026-09-17 09:20 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       117 (26.2%)         99 (22.2%)
Timeouts                                          318 (71.3%)        335 (75.1%)
Out of memory                                       11 (2.5%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              96                 96
Faster when both found a plan                      32 (33.3%)         64 (66.7%)
Plan found when the other did not                          21                  3
Median runtime when both found a plan                  8.38 s             9.77 s
Total runtime across shared solves                 7,006.55 s         8,695.48 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     266 (84%)
Guided concrete search                               33 (10%)
Extended concrete search                              19 (6%)
Total                                                     318
```

## How the successes were solved

```
How the 117 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       70 (60%)
Refined after switching some actions off             38 (32%)
Abstract plan discarded, solved above it               9 (8%)
Total                                                     117
```

## Deletes relaxed, over the 108 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (10%)
1 to 4                                               67 (62%)
5 to 9                                               13 (12%)
10 to 19                                             13 (12%)
20 or more                                             4 (4%)
Total                                                     108
```
