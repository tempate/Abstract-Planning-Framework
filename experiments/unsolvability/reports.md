# Benchmark report

2026-09-18 11:18 — experiments/unsolvability/results.csv

168 problems compared over abstract, concrete

## Verdicts

```
Verdict                                     Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Unsolvable                                          16 (9.5%)         45 (26.8%)
Unknown                                            36 (21.4%)           0 (0.0%)
Timeouts                                             3 (1.8%)           0 (0.0%)
Out of memory                                     113 (67.3%)        123 (73.2%)
Others                                               0 (0.0%)           0 (0.0%)
Total problems                                            168                168
```

## Head to head: abstract vs Concrete pipeline

```
Metric                                      Abstract pipeline  Concrete pipeline
--------------------------------------------------------------------------------
Proved unsolvable by both                                  13                 13
Faster when both proved it                          5 (38.5%)          8 (61.5%)
Proved it when the other did not                            3                 32
Median runtime when both proved it                     9.88 s             4.71 s
Total runtime across shared proofs                 1,094.01 s         1,763.27 s
```

## Where the timeouts died

```
Where the abstract pipeline was killed               Timeouts
-------------------------------------------------------------
abstract_pddl_writing                                3 (100%)
Total                                                       3
```
