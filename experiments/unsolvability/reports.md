# Benchmark report

2026-09-16 09:47 — experiments/unsolvability/results.csv

## Verdicts

```
Verdict                                     Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Unsolvable                                          15 (7.5%)         67 (33.3%)
Unknown                                            36 (17.9%)           0 (0.0%)
Timeouts                                             3 (1.5%)           0 (0.0%)
Out of memory                                      98 (48.8%)        114 (56.7%)
Others                                             49 (24.4%)         20 (10.0%)
Total problems                                            201                201
```

## Head to head

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Proved unsolvable by both pipelines                        12                 12
Faster when both proved it                          5 (41.7%)          7 (58.3%)
Proved it when the other did not                            3                 55
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
