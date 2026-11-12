# Benchmark report

2026-11-12 10:38 — experiments/htg/sat/results.csv

294 problems compared over abs-lama, lama; 149 dropped as unfinished

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                     198 (67.3%)  219 (74.5%)
Timeouts                         31 (10.5%)   38 (12.9%)
Out of memory                    65 (22.1%)   37 (12.6%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          294          294
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                     190          190
Faster                             8 (4.2%)  182 (95.8%)
Found when the other did not              8           29
Median runtime                      49.21 s      23.99 s
Total runtime                   35,199.55 s  18,888.60 s
Shorter plan                      11 (5.8%)   33 (17.4%)
Same plan length                146 (76.8%)  146 (76.8%)
Median plan length                     18.5           19
Total plan length                     7,735        7,661
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    21 (68%)
Translating the task                 1 (3%)
Guided concrete search              9 (29%)
Total                                    31
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                 198 (100%)
Refined, some actions off            0 (0%)
Solved above the abstract plan       0 (0%)
Total                                   198
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                                11 (6%)
1 to 4                            123 (62%)
5 to 9                               0 (0%)
10 to 19                           42 (21%)
20 or more                         22 (11%)
Total                                   198
```

## Plans found by domain

```
Domain (problems)                 Size     LAMAᵅ      LAMA
----------------------------------------------------------
blocksworld-large-simple (24)    goal-2         5         3
                                goal-3         5         3
                                goal-4         5         3
                                goal-5         5         3
childsnack-contents (44)    parsize1-cham3        12        12
                            parsize1-cham5        12        12
                            parsize1-cham7        12        12
                            parsize2-cham3        12        12
                            parsize2-cham5        12        12
                            parsize2-cham7        12        12
                            parsize3-cham3        12        12
                            parsize3-cham5         8         9
                            parsize3-cham7         3         5
                            parsize4-cham3        10        11
                            parsize4-cham5         1         2
gnad-et-al-aaai19-large-instances (86)agricola-large        11        18
                            depots-large         0         1
                            satellite-large         3         5
                             tpp-large         0         9
logistics-large-simple (20)     goal-1         5         5
                                goal-2         5         5
                                goal-3         5         5
                                goal-4         5         5
organic-synthesis-MIT (2)                      0         2
organic-synthesis-alkene (17)                  15        15
organic-synthesis-original (3)                   0         1
pipesworld-tankage-nosplit (17)                  13        15
rovers-large-simple (10)        goal-2         1         1
                                goal-4         3         3
                                goal-6         3         3
                                goal-8         3         3
Total (294)                                  198       219
```
