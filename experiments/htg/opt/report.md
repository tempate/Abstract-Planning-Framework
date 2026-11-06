# Benchmark report

2026-11-06 07:53 — experiments/htg/opt/results.csv

288 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      61 (21.2%)   53 (18.4%)
Timeouts                        177 (61.5%)  193 (67.0%)
Out of memory                    45 (15.6%)   41 (14.2%)
Others                             5 (1.7%)     1 (0.3%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      43           43
Faster                           13 (30.2%)   30 (69.8%)
Found when the other did not             18           10
Median runtime                      21.37 s      10.23 s
Total runtime                    5,685.52 s   7,166.72 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                43 (100.0%)  43 (100.0%)
Median plan length                        6            6
Total plan length                       292          292
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   175 (99%)
Guided concrete search               2 (1%)
Total                                   177
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   51 (84%)
Refined, some actions off            0 (0%)
Solved above the abstract plan     10 (16%)
Total                                    61
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 0 (0%)
1 to 4                             20 (39%)
5 to 9                               0 (0%)
10 to 19                           16 (31%)
20 or more                         15 (29%)
Total                                    51
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
organic-synthesis-alkene (17)                  15        15
pipesworld-tankage-nosplit (17)                   6         6
rovers-large-simple (6)         goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (288)                                   61        53
```
