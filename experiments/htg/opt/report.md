# Benchmark report

2026-11-05 23:00 — experiments/htg/opt/results.csv

288 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      42 (14.6%)   53 (18.4%)
Timeouts                        149 (51.7%)  193 (67.0%)
Out of memory                    92 (31.9%)   41 (14.2%)
Others                             5 (1.7%)     1 (0.3%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      24           24
Faster                           12 (50.0%)   12 (50.0%)
Found when the other did not             18           29
Median runtime                      18.59 s      29.66 s
Total runtime                    2,670.88 s   5,662.57 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                24 (100.0%)  24 (100.0%)
Median plan length                     10.5         10.5
Total plan length                       253          253
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   147 (99%)
Translating the task                 1 (1%)
Guided concrete search               1 (1%)
Total                                   149
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   32 (76%)
Refined, some actions off            0 (0%)
Solved above the abstract plan     10 (24%)
Total                                    42
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 0 (0%)
1 to 4                             18 (56%)
5 to 9                               0 (0%)
10 to 19                           14 (44%)
20 or more                           0 (0%)
Total                                    32
```

## Plans found by domain

```
Domain (problems)                 Size    LMcutᵅ     LMcut
----------------------------------------------------------
blocksworld-large-simple (24)    goal-2         2         3
                                goal-3         2         3
                                goal-4         2         3
                                goal-5         2         3
childsnack-contents (44)    parsize1-cham3        12         5
                            parsize1-cham5         7         0
                            parsize1-cham7         0         0
                            parsize2-cham3         5         2
                            parsize2-cham5         0         0
                            parsize2-cham7         0         0
                            parsize3-cham3         2         1
                            parsize3-cham5         0         0
                            parsize3-cham7         0         0
                            parsize4-cham3         0         0
                            parsize4-cham5         0         0
gnad-et-al-aaai19-large-instances (93)agricola-large         0         0
                            caldera-large         0         0
                            depots-large         0         0
                            satellite-large         0         0
                             tpp-large         0         0
logistics-large-simple (16)     goal-1         0         4
                                goal-2         0         3
                                goal-3         0         2
                                goal-4         0         1
organic-synthesis-alkene (17)                   0        15
pipesworld-tankage-nosplit (17)                   6         6
rovers-large-simple (6)         goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (288)                                   42        53
```
