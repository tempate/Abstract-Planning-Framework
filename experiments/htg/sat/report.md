# Benchmark report

2026-11-05 14:21 — experiments/htg/sat/results.csv

288 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                      88 (30.6%)  209 (72.6%)
Timeouts                          27 (9.4%)   38 (13.2%)
Out of memory                   173 (60.1%)   41 (14.2%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                      88           88
Faster                             1 (1.1%)   87 (98.9%)
Found when the other did not              0          121
Median runtime                      14.17 s       4.28 s
Total runtime                    4,518.45 s     778.55 s
Shorter plan                     12 (13.6%)   62 (70.5%)
Same plan length                 14 (15.9%)   14 (15.9%)
Median plan length                     24.5           18
Total plan length                     2,556        2,041
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    18 (67%)
Guided concrete search              9 (33%)
Total                                    27
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                   57 (65%)
Refined, some actions off          31 (35%)
Solved above the abstract plan       0 (0%)
Total                                    88
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                               17 (19%)
1 to 4                             57 (65%)
5 to 9                               0 (0%)
10 to 19                           12 (14%)
20 or more                           2 (2%)
Total                                    88
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
rovers-large-simple (6)         goal-4         1         3
                                goal-6         1         2
                                goal-8         0         1
Total (288)                                   88       209
```
