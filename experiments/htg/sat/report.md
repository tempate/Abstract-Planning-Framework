# Benchmark report

2026-11-06 07:53 — experiments/htg/sat/results.csv

288 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                      92 (31.9%)  209 (72.6%)
Timeouts                         34 (11.8%)   38 (13.2%)
Out of memory                   162 (56.2%)   41 (14.2%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                      92           92
Faster                             1 (1.1%)   91 (98.9%)
Found when the other did not              0          117
Median runtime                      11.94 s       4.36 s
Total runtime                    5,869.51 s   1,598.89 s
Shorter plan                     11 (12.0%)   66 (71.7%)
Same plan length                 15 (16.3%)   15 (16.3%)
Median plan length                       25         20.5
Total plan length                     2,735        2,211
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    23 (68%)
Translating the task to ASP          1 (3%)
Guided concrete search             10 (29%)
Total                                    34
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                   61 (66%)
Refined, some actions off          31 (34%)
Solved above the abstract plan       0 (0%)
Total                                    92
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                               21 (23%)
1 to 4                             57 (62%)
5 to 9                               0 (0%)
10 to 19                           12 (13%)
20 or more                           2 (2%)
Total                                    92
```

## Plans found by domain

```
Domain (problems)                 Size     LAMAᵅ      LAMA
----------------------------------------------------------
blocksworld-large-simple (24)    goal-2         2         3
                                goal-3         2         3
                                goal-4         1         3
                                goal-5         1         3
childsnack-contents (44)    parsize1-cham3        12        12
                            parsize1-cham5        12        12
                            parsize1-cham7        12        12
                            parsize2-cham3        12        12
                            parsize2-cham5         7        12
                            parsize2-cham7         4        12
                            parsize3-cham3        11        12
                            parsize3-cham5         2         9
                            parsize3-cham7         0         5
                            parsize4-cham3         0        11
                            parsize4-cham5         0         2
gnad-et-al-aaai19-large-instances (93)agricola-large         0        18
                            caldera-large         0         1
                            depots-large         0         1
                            satellite-large         0         5
                             tpp-large         0         9
logistics-large-simple (16)     goal-1         0         4
                                goal-2         0         4
                                goal-3         0         4
                                goal-4         0         4
organic-synthesis-alkene (17)                   0        15
pipesworld-tankage-nosplit (17)                   8        15
rovers-large-simple (6)         goal-4         3         3
                                goal-6         2         2
                                goal-8         1         1
Total (288)                                   92       209
```
