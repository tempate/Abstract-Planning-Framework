# Benchmark report

2026-09-11 12:16 — benchmarks/results.csv

## Coverage

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found                                       157 (19.0%)        144 (17.4%)
Timeouts                                          618 (74.6%)        680 (82.1%)
Total problems                                            828                828
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Plans found by both pipelines                             137                137
Faster when both found a plan                      45 (32.8%)         92 (67.2%)
Plan found when the other did not                          20                  7
Median runtime when both found a plan                  6.51 s             5.87 s
Total runtime across shared solves                 8,541.27 s        14,636.30 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
Searching for the abstract plan                     437 (71%)
Extended concrete search                            138 (22%)
Guided concrete search                                43 (7%)
Total                                                     618
```

## How the successes were solved

```
How the 157 successes were solved                    Problems
-------------------------------------------------------------
Abstract plan refined directly                      107 (68%)
Refined after switching some actions off             36 (23%)
Abstract plan discarded, solved above it              14 (9%)
Total                                                     157
```

## Deletes relaxed, over the 143 successes whose abstract plan was used

```
Deletes relaxed                                      Problems
-------------------------------------------------------------
None                                                  11 (8%)
1 to 4                                               95 (66%)
5 to 9                                                13 (9%)
10 to 19                                             24 (17%)
20 or more                                             0 (0%)
Total                                                     143
```
