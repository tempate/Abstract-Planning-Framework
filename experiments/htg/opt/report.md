# Benchmark report

2026-11-27 09:06 — experiments/htg/opt/results.csv

443 problems compared over asp, abs-asp, abs-lmcut, lmcut, abs-powerlifted, powerlifted, lmcut-symmetry-pruning, rnd-g

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut Powerliftedᵅ  Powerlifted       LMcut+        rnd-g
--------------------------------------------------------------------------------------------------------------------------------------
Plans found                      62 (14.0%)  117 (26.4%)  116 (26.2%)   55 (12.4%)   92 (20.8%)   61 (13.8%)  121 (27.3%)   78 (17.6%)
Timeouts                        121 (27.3%)  155 (35.0%)  195 (44.0%)  202 (45.6%)  322 (72.7%)  370 (83.5%)  136 (30.7%)  164 (37.0%)
Out of memory                   260 (58.7%)  171 (38.6%)  132 (29.8%)  186 (42.0%)    29 (6.5%)    12 (2.7%)  186 (42.0%)  201 (45.4%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                          443          443          443          443          443          443          443          443
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut Powerliftedᵅ  Powerlifted
------------------------------------------------------------------------------------------------------------
Plans found by both                      59           59           52           52           36           36
Faster                           16 (27.1%)   43 (72.9%)   31 (59.6%)   21 (40.4%)   10 (27.8%)   26 (72.2%)
Found when the other did not              3           58           64            3           56           25
Median runtime                      50.47 s      23.51 s       6.37 s      40.31 s      24.27 s       2.16 s
Total runtime                    8,090.89 s   4,423.08 s   2,890.88 s  16,757.72 s   4,157.38 s   4,220.74 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length                59 (100.0%)  59 (100.0%)  52 (100.0%)  52 (100.0%)  36 (100.0%)  36 (100.0%)
Median plan length                        8            8            7            7            2            2
Total plan length                       475          475          361          361          154          154
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ Powerliftedᵅ
---------------------------------------------------------------------
Abstract search                    92 (59%)    134 (69%)   321 (100%)
Translating the task                 2 (1%)       1 (1%)       0 (0%)
Translating the task to ASP          0 (0%)       1 (1%)       0 (0%)
Guided concrete search             49 (32%)     40 (21%)       0 (0%)
Unguided concrete search            12 (8%)     19 (10%)       1 (0%)
Total                                   155          195          322
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ Powerliftedᵅ
---------------------------------------------------------------------
Refined directly                  114 (97%)    106 (91%)     86 (93%)
Refined, some actions off            1 (1%)       0 (0%)       2 (2%)
Solved above the abstract plan       2 (2%)      10 (9%)       4 (4%)
Total                                   117          116           92
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ Powerliftedᵅ
---------------------------------------------------------------------
None                                 1 (1%)       1 (1%)       2 (2%)
1 to 4                             47 (41%)     42 (40%)     18 (20%)
5 to 9                               0 (0%)       0 (0%)       0 (0%)
10 to 19                           50 (43%)     47 (44%)     47 (53%)
20 or more                         17 (15%)     16 (15%)     21 (24%)
Total                                   115          106           88
```

## Plans found by domain

```
Domain (problems)                 Size       ASP      ASPᵅ    LMcutᵅ     LMcutPowerliftedᵅPowerlifted    LMcut+     rnd-g
-------------------------------------------------------------------------------------------------------------------------
blocksworld-large-simple (40)    goal-2         3        10        10         3        10         0         3         9
                                goal-3         3        10        10         3        10         0         3         1
                                goal-4         3        10        10         3        10         0         3         1
                                goal-5         2        10        10         3        10         0         3         0
childsnack-contents (44)    parsize1-cham3        12        12        12         4         8         2        12         2
                            parsize1-cham5         0         0         7         0         0         0        12         0
                            parsize1-cham7         0         0         0         0         0         0         7         0
                            parsize2-cham3         6        11         5         2         2         0        12         2
                            parsize2-cham5         0         0         0         0         0         0         7         0
                            parsize2-cham7         0         0         0         0         0         0         2         0
                            parsize3-cham3         3         7         2         0         0         0        10         0
                            parsize3-cham5         0         0         0         0         0         0         5         0
                            parsize3-cham7         0         0         0         0         0         0         0         0
                            parsize4-cham3         0         1         0         0         0         0         7         0
                            parsize4-cham5         0         0         0         0         0         0         0         0
                            parsize4-cham7         0         0         0         0         0         0         0         0
gnad-et-al-aaai19-large-instances (97)agricola-large         0         0         0         0         0         0         0         0
                            depots-large         0         0         0         0         0         0         0         0
                            satellite-large         0         0         0         0         0         0         0         0
                             tpp-large         0         0         0         0         0         0         0         0
logistics-large-simple (24)     goal-1         2         6         6         5         6         5         1         6
                                goal-2         1         5         6         3         5         0         1         6
                                goal-3         0         5         6         1         0         0         1         3
                                goal-4         0         5         6         1         0         0         1         3
organic-synthesis-MIT (18)                     2         0         0         2         6        18         2        10
organic-synthesis-alkene (18)                  15        16        16        15        15        18        15        18
organic-synthesis-original (20)                   0         0         0         1         0         8         1         1
pipesworld-tankage-nosplit (47)                   6         6         7         6         9         7        10        12
rovers-large-simple (35)        goal-2         1         1         1         1         1         3         1         3
                                goal-4         3         2         2         2         0         0         2         1
                                goal-6         0         0         0         0         0         0         0         0
                                goal-8         0         0         0         0         0         0         0         0
Total (443)                                   62       117       116        55        92        61       121        78
```
