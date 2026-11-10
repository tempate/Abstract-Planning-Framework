# Benchmark report

2026-11-10 11:32 — experiments/htg/sat/results.csv

299 problems compared over abs-lama, lama; 169 dropped as unfinished

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                     198 (66.2%)  220 (73.6%)
Timeouts                         32 (10.7%)   38 (12.7%)
Out of memory                    69 (23.1%)   41 (13.7%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          299          299
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                     190          190
Faster                             8 (4.2%)  182 (95.8%)
Found when the other did not              8           30
Median runtime                      48.46 s      23.99 s
Total runtime                   35,590.05 s  18,888.60 s
Shorter plan                      11 (5.8%)   33 (17.4%)
Same plan length                146 (76.8%)  146 (76.8%)
Median plan length                     18.5           19
Total plan length                     7,735        7,661
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    20 (62%)
Translating the task                 1 (3%)
Guided concrete search             11 (34%)
Total                                    32
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
gnad-et-al-aaai19-large-instances (93)agricola-large        11        18
                            caldera-large         0         1
                            depots-large         0         1
                            satellite-large         3         5
                             tpp-large         0         9
logistics-large-simple (20)     goal-1         5         5
                                goal-2         5         5
                                goal-3         5         5
                                goal-4         5         5
organic-synthesis-MIT (2)                      0         2
organic-synthesis-alkene (17)                  15        15
organic-synthesis-original (1)                   0         1
pipesworld-tankage-nosplit (17)                  13        15
rovers-large-simple (10)        goal-2         1         1
                                goal-4         3         3
                                goal-6         3         3
                                goal-8         3         3
Total (299)                                  198       220
```
