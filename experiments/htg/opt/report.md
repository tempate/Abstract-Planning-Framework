# Benchmark report

2026-11-11 09:30 — experiments/htg/opt/results.csv

5 problems compared over abs-asp, abs-lmcut, lmcut; 438 dropped as unfinished

## Coverage

```
Metric                                 ASPᵅ       LMcutᵅ        LMcut
---------------------------------------------------------------------
Plans found                        0 (0.0%)     0 (0.0%)    1 (20.0%)
Timeouts                          2 (40.0%)    2 (40.0%)    2 (40.0%)
Out of memory                     3 (60.0%)    3 (60.0%)    2 (40.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                            5            5            5
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                       0            0
Faster                                    0            0
Found when the other did not              0            1
Median runtime                          n/a          n/a
Total runtime                        0.00 s       0.00 s
Shorter plan                              0            0
Same plan length                          0            0
Median plan length                      n/a          n/a
Total plan length                         0            0
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                    2 (100%)     2 (100%)
Total                                     2            2
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                          0            0
Refined, some actions off                 0            0
Solved above the abstract plan            0            0
Total                                     0            0
```

## Deletes relaxed by the refined plans

```
No success was solved with its abstract plan
```

## Plans found by domain

```
Domain (problems)                 ASPᵅ    LMcutᵅ     LMcut
----------------------------------------------------------
organic-synthesis-original (3)         0         0         1
pipesworld-tankage-nosplit (2)         0         0         0
Total (5)                            0         0         1
```
