# Benchmark report

2026-11-12 17:30 — experiments/htg/opt/results.csv

329 problems compared over asp, abs-asp, abs-lmcut, lmcut; 114 dropped as unfinished

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                      62 (18.8%)   80 (24.3%)  116 (35.3%)   58 (17.6%)
Timeouts                        121 (36.8%)  139 (42.2%)  193 (58.7%)  199 (60.5%)
Out of memory                   146 (44.4%)  110 (33.4%)    20 (6.1%)   72 (21.9%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                          329          329          329          329
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                      57           57           55           55
Faster                           31 (54.4%)   26 (45.6%)   39 (70.9%)   16 (29.1%)
Found when the other did not              5           23           61            3
Median runtime                      47.70 s      34.62 s      10.52 s      43.88 s
Total runtime                    7,160.03 s   6,962.41 s   3,530.87 s  17,320.39 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length                57 (100.0%)  57 (100.0%)  55 (100.0%)  55 (100.0%)
Median plan length                        8            8            8            8
Total plan length                       451          451          397          397
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                    83 (60%)    136 (70%)
Guided concrete search               0 (0%)     38 (20%)
Unguided concrete search             0 (0%)     19 (10%)
Extended concrete search           56 (40%)       0 (0%)
Total                                   139          193
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   70 (88%)    106 (91%)
Refined, some actions off            0 (0%)       0 (0%)
Solved above the abstract plan     10 (12%)      10 (9%)
Total                                    80          116
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 1 (1%)       1 (1%)
1 to 4                             28 (40%)     42 (40%)
5 to 9                               0 (0%)       0 (0%)
10 to 19                           26 (37%)     47 (44%)
20 or more                         15 (21%)     16 (15%)
Total                                    70          106
```

## Plans found by domain

```
Domain (problems)                 Size       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
blocksworld-large-simple (40)    goal-2         3         5        10         3
                                goal-3         3         5        10         3
                                goal-4         3         5        10         3
                                goal-5         2         5        10         3
childsnack-contents (44)    parsize1-cham3        12        12        12         5
                            parsize1-cham5         0         0         7         0
                            parsize1-cham7         0         0         0         0
                            parsize2-cham3         6         5         5         2
                            parsize2-cham5         0         0         0         0
                            parsize2-cham7         0         0         0         0
                            parsize3-cham3         3         2         2         1
                            parsize3-cham5         0         0         0         0
                            parsize3-cham7         0         0         0         0
                            parsize4-cham3         0         0         0         0
                            parsize4-cham5         0         0         0         0
                            parsize4-cham7         0         0         0         0
gnad-et-al-aaai19-large-instances (86)agricola-large         0         0         0         0
                            depots-large         0         0         0         0
                            satellite-large         0         0         0         0
                             tpp-large         0         0         0         0
logistics-large-simple (24)     goal-1         2         5         6         5
                                goal-2         1         4         6         3
                                goal-3         0         4         6         2
                                goal-4         0         4         6         1
organic-synthesis-MIT (2)                      2         0         0         2
organic-synthesis-alkene (18)                  15        15        16        15
organic-synthesis-original (3)                   0         0         0         1
pipesworld-tankage-nosplit (17)                   6         6         7         6
rovers-large-simple (10)        goal-2         1         1         1         1
                                goal-4         3         2         2         2
                                goal-6         0         0         0         0
                                goal-8         0         0         0         0
Total (329)                                   62        80       116        58
```
