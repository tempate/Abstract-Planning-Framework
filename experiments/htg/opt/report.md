# Benchmark report

2026-11-10 10:07 — experiments/htg/opt/results.csv

288 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      86 (29.9%)   53 (18.4%)
Timeouts                        178 (61.8%)  193 (67.0%)
Out of memory                     20 (6.9%)   41 (14.2%)
Others                             4 (1.4%)     1 (0.3%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      53           53
Faster                           29 (54.7%)   24 (45.3%)
Found when the other did not             33            0
Median runtime                      27.21 s      43.46 s
Total runtime                    7,123.92 s  16,299.39 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                53 (100.0%)  53 (100.0%)
Median plan length                        8            8
Total plan length                       382          382
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   120 (67%)
Guided concrete search             39 (22%)
Unguided concrete search           19 (11%)
Total                                   178
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   76 (88%)
Refined, some actions off            0 (0%)
Solved above the abstract plan     10 (12%)
Total                                    86
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 0 (0%)
1 to 4                             34 (45%)
5 to 9                               0 (0%)
10 to 19                           27 (36%)
20 or more                         15 (20%)
Total                                    76
```

## Plans found by domain

```
Domain (problems)                 Size    LMcutᵅ     LMcut
----------------------------------------------------------
blocksworld-large-simple (24)    goal-2         5         3
                                goal-3         5         3
                                goal-4         5         3
                                goal-5         5         3
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
logistics-large-simple (16)     goal-1         4         4
                                goal-2         4         3
                                goal-3         4         2
                                goal-4         4         1
organic-synthesis-alkene (17)                  15        15
pipesworld-tankage-nosplit (17)                   7         6
rovers-large-simple (6)         goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (288)                                   86        53
```
