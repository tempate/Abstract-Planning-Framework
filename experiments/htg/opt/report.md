# Benchmark report

2026-11-06 11:27 — experiments/htg/opt/results.csv

288 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      85 (29.5%)   53 (18.4%)
Timeouts                        176 (61.1%)  193 (67.0%)
Out of memory                     21 (7.3%)   41 (14.2%)
Others                             6 (2.1%)     1 (0.3%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      53           53
Faster                           23 (43.4%)   30 (56.6%)
Found when the other did not             32            0
Median runtime                      46.65 s      43.46 s
Total runtime                   11,859.03 s  16,299.39 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                53 (100.0%)  53 (100.0%)
Median plan length                        8            8
Total plan length                       382          382
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstract search                   175 (99%)
Translating the task to ASP          1 (1%)
Total                                   176
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   75 (88%)
Refined, some actions off            0 (0%)
Solved above the abstract plan     10 (12%)
Total                                    85
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                 0 (0%)
1 to 4                             34 (45%)
5 to 9                               0 (0%)
10 to 19                           26 (35%)
20 or more                         15 (20%)
Total                                    75
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
pipesworld-tankage-nosplit (17)                   6         6
rovers-large-simple (6)         goal-4         2         2
                                goal-6         0         0
                                goal-8         0         0
Total (288)                                   85        53
```
