# Benchmark report

2026-11-11 11:42 — experiments/htg/opt/results.csv

294 problems compared over abs-lmcut, lmcut; 149 dropped as unfinished

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      91 (31.0%)   58 (19.7%)
Timeouts                        181 (61.6%)  199 (67.7%)
Out of memory                     22 (7.5%)   37 (12.6%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          294          294
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      55           55
Faster                           30 (54.5%)   25 (45.5%)
Found when the other did not             36            3
Median runtime                      32.36 s      43.88 s
Total runtime                    7,875.56 s  17,320.39 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                55 (100.0%)  55 (100.0%)
Median plan length                        8            8
Total plan length                       397          397
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   123 (68%)
Guided concrete search             39 (22%)
Unguided concrete search           19 (10%)
Total                                   181
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   81 (89%)
Refined, some actions off            0 (0%)
Solved above the abstract plan     10 (11%)
Total                                    91
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 1 (1%)
1 to 4                             38 (47%)
5 to 9                               0 (0%)
10 to 19                           27 (33%)
20 or more                         15 (19%)
Total                                    81
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
gnad-et-al-aaai19-large-instances (86)agricola-large         0         0
                            depots-large         0         0
                            satellite-large         0         0
                             tpp-large         0         0
logistics-large-simple (20)     goal-1         5         5
                                goal-2         5         3
                                goal-3         5         2
                                goal-4         5         1
organic-synthesis-MIT (2)                      0         2
organic-synthesis-alkene (17)                  15        15
organic-synthesis-original (3)                   0         1
pipesworld-tankage-nosplit (17)                   7         6
rovers-large-simple (10)        goal-2         1         1
                                goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (294)                                   91        58
```
