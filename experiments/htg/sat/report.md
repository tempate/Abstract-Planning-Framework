# Benchmark report

2026-11-06 11:27 — experiments/htg/sat/results.csv

288 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                     162 (56.2%)  209 (72.6%)
Timeouts                         46 (16.0%)   38 (13.2%)
Out of memory                    80 (27.8%)   41 (14.2%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                     154          154
Faster                             3 (1.9%)  151 (98.1%)
Found when the other did not              8           55
Median runtime                      29.88 s       7.81 s
Total runtime                   28,108.99 s  10,563.91 s
Shorter plan                     21 (13.6%)   47 (30.5%)
Same plan length                 86 (55.8%)   86 (55.8%)
Median plan length                       17           17
Total plan length                     4,754        4,475
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    30 (65%)
Translating the task                 1 (2%)
Translating the task to ASP          1 (2%)
Guided concrete search             14 (30%)
Total                                    46
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                  131 (81%)
Refined, some actions off          31 (19%)
Solved above the abstract plan       0 (0%)
Total                                   162
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                               21 (13%)
1 to 4                             74 (46%)
5 to 9                              10 (6%)
10 to 19                           29 (18%)
20 or more                         28 (17%)
Total                                   162
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
                            parsize2-cham5         7        12
                            parsize2-cham7         4        12
                            parsize3-cham3        11        12
                            parsize3-cham5         3         9
                            parsize3-cham7         0         5
                            parsize4-cham3        10        11
                            parsize4-cham5         1         2
gnad-et-al-aaai19-large-instances (93)agricola-large        11        18
                            caldera-large         0         1
                            depots-large         0         1
                            satellite-large         0         5
                             tpp-large         0         9
logistics-large-simple (16)     goal-1         4         4
                                goal-2         4         4
                                goal-3         4         4
                                goal-4         4         4
organic-synthesis-alkene (17)                  15        15
pipesworld-tankage-nosplit (17)                  10        15
rovers-large-simple (6)         goal-4         3         3
                                goal-6         2         2
                                goal-8         1         1
Total (288)                                  162       209
```
