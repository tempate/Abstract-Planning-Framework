# Benchmark report

2026-11-10 17:24 — experiments/htg/opt/results.csv

12 problems compared over abs-asp, abs-lmcut, lmcut; 456 dropped as unfinished

## Coverage

```
Metric                                 ASPᵅ       LMcutᵅ        LMcut
---------------------------------------------------------------------
Plans found                        0 (0.0%)     0 (0.0%)     1 (8.3%)
Timeouts                          9 (75.0%)    2 (16.7%)    2 (16.7%)
Out of memory                     3 (25.0%)    3 (25.0%)    8 (66.7%)
Others                             0 (0.0%)    7 (58.3%)     1 (8.3%)
Total problems                           12           12           12
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
Abstract search                    9 (100%)     2 (100%)
Total                                     9            2
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
Domain (problems)                 Size      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
gnad-et-al-aaai19-large-instances (7)caldera-large         0         0         0
organic-synthesis-original (3)                   0         0         1
pipesworld-tankage-nosplit (2)                   0         0         0
Total (12)                                     0         0         1
```
