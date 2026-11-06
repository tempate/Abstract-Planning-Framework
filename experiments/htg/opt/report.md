# Benchmark report

2026-11-06 07:53 — experiments/htg/opt/results.csv

288 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      46 (16.0%)   53 (18.4%)
Timeouts                        149 (51.7%)  193 (67.0%)
Out of memory                    88 (30.6%)   41 (14.2%)
Others                             5 (1.7%)     1 (0.3%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      28           28
Faster                           13 (46.4%)   15 (53.6%)
Found when the other did not             18           25
Median runtime                      17.73 s      63.20 s
Total runtime                    4,725.06 s   7,004.80 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                28 (100.0%)  28 (100.0%)
Median plan length                       10           10
Total plan length                       271          271
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   148 (99%)
Guided concrete search               1 (1%)
Total                                   149
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   36 (78%)
Refined, some actions off            0 (0%)
Solved above the abstract plan     10 (22%)
Total                                    46
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 0 (0%)
1 to 4                             20 (56%)
5 to 9                               0 (0%)
10 to 19                           16 (44%)
20 or more                           0 (0%)
Total                                    36
```

## Plans found by domain

```
Domain (problems)                 Size    LMcutᵅ     LMcut
----------------------------------------------------------
blocksworld-large-simple (24)    goal-2         3         3
                                goal-3         3         3
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
logistics-large-simple (16)     goal-1         2         4
                                goal-2         0         3
                                goal-3         0         2
                                goal-4         0         1
organic-synthesis-alkene (17)                   0        15
pipesworld-tankage-nosplit (17)                   6         6
rovers-large-simple (6)         goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (288)                                   46        53
```
