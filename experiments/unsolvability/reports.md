# Benchmark report

2026-09-16 09:15 — experiments/unsolvability/results.csv

## Verdicts

```
Verdict                                     Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Unsolvable                                          15 (7.5%)         67 (33.3%)
Unknown                                            36 (17.9%)           0 (0.0%)
Solvable                                             0 (0.0%)           0 (0.0%)
No verdict                                        150 (74.6%)        134 (66.7%)
Total problems                                            201                201
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Proved unsolvable                                          15                 67
Proved unsolvable by both                                  12                 12
Faster when both proved it                          5 (41.7%)          7 (58.3%)
Median runtime when both proved it                    15.87 s            14.14 s
Proved it when the other did not                            3                 55
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
abstract_pddl_writing                                3 (100%)
Total                                                       3
```
