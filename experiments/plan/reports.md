# Benchmark report

2026-09-16 12:19 — experiments/plan/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       109 (24.4%)         99 (22.2%)
Timeouts                                          324 (72.6%)        335 (75.1%)
Out of memory                                       13 (2.9%)          12 (2.7%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            446                446
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                              94                 94
Faster when both found a plan                      26 (27.7%)         68 (72.3%)
Plan found when the other did not                          15                  5
Median runtime when both found a plan                  8.02 s             8.61 s
Total runtime across shared solves                 7,592.01 s         8,262.67 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     266 (82%)
Guided concrete search                               39 (12%)
Extended concrete search                              19 (6%)
Total                                                     324
```

## How the successes were solved

```
How the 109 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                       74 (68%)
Refined after switching some actions off             27 (25%)
Abstract plan discarded, solved above it               8 (7%)
Total                                                     109
```

## Deletes relaxed, over the 101 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                 11 (11%)
1 to 4                                               64 (63%)
5 to 9                                               10 (10%)
10 to 19                                             14 (14%)
20 or more                                             2 (2%)
Total                                                     101
```
