# Benchmark report

2026-11-12 10:42 — experiments/htg/opt/results.csv

329 problems compared over abs-lmcut, lmcut; 114 dropped as unfinished

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                     116 (35.3%)   58 (17.6%)
Timeouts                        193 (58.7%)  199 (60.5%)
Out of memory                     20 (6.1%)   72 (21.9%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          329          329
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      55           55
Faster                           39 (70.9%)   16 (29.1%)
Found when the other did not             61            3
Median runtime                      10.52 s      43.88 s
Total runtime                    3,530.87 s  17,320.39 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                55 (100.0%)  55 (100.0%)
Median plan length                        8            8
Total plan length                       397          397
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   136 (70%)
Guided concrete search             38 (20%)
Unguided concrete search           19 (10%)
Total                                   193
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                  106 (91%)
Refined, some actions off            0 (0%)
Solved above the abstract plan      10 (9%)
Total                                   116
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 1 (1%)
1 to 4                             42 (40%)
5 to 9                               0 (0%)
10 to 19                           47 (44%)
20 or more                         16 (15%)
Total                                   106
```

## Plans found by domain

```
Domain (problems)                 Size    LMcutᵅ     LMcut
----------------------------------------------------------
blocksworld-large-simple (40)    goal-2        10         3
                                goal-3        10         3
                                goal-4        10         3
                                goal-5        10         3
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
                            parsize4-cham7         0         0
gnad-et-al-aaai19-large-instances (86)agricola-large         0         0
                            depots-large         0         0
                            satellite-large         0         0
                             tpp-large         0         0
logistics-large-simple (24)     goal-1         6         5
                                goal-2         6         3
                                goal-3         6         2
                                goal-4         6         1
organic-synthesis-MIT (2)                      0         2
organic-synthesis-alkene (18)                  16        15
organic-synthesis-original (3)                   0         1
pipesworld-tankage-nosplit (17)                   7         6
rovers-large-simple (10)        goal-2         1         1
                                goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (329)                                  116        58
```
