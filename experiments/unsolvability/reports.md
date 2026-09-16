# Benchmark report

2026-09-16 09:56 — experiments/unsolvability/results.csv

## Verdicts

```
Verdict                                     Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Unsolvable                                          15 (8.9%)         45 (26.8%)
Unknown                                            36 (21.4%)           0 (0.0%)
Timeouts                                             3 (1.8%)           0 (0.0%)
Out of memory                                     113 (67.3%)        123 (73.2%)
No plan found                                        1 (0.6%)           0 (0.0%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            168                168
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Proved unsolvable by both pipelines                        12                 12
Faster when both proved it                          5 (41.7%)          7 (58.3%)
Proved it when the other did not                            3                 33
Median runtime when both proved it                    15.87 s            14.14 s
Total runtime across shared proofs                 1,090.49 s         1,761.18 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
abstract_pddl_writing                                3 (100%)
Total                                                       3
```
