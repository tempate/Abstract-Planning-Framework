# Benchmark report

2026-11-09 09:01 — experiments/htg/sat/results.csv

288 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                     190 (66.0%)  209 (72.6%)
Timeouts                         33 (11.5%)   38 (13.2%)
Out of memory                    65 (22.6%)   41 (14.2%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                     182          182
Faster                             5 (2.7%)  177 (97.3%)
Found when the other did not              8           27
Median runtime                      36.23 s      17.69 s
Total runtime                   37,206.17 s  18,057.95 s
Shorter plan                      11 (6.0%)   34 (18.7%)
Same plan length                137 (75.3%)  137 (75.3%)
Median plan length                     18.5           19
Total plan length                     7,610        7,531
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    21 (64%)
Translating the task                 1 (3%)
Guided concrete search             11 (33%)
Total                                    33
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                 190 (100%)
Refined, some actions off            0 (0%)
Solved above the abstract plan       0 (0%)
Total                                   190
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                                 6 (3%)
1 to 4                            119 (63%)
5 to 9                               1 (1%)
10 to 19                           42 (22%)
20 or more                         22 (12%)
Total                                   190
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
gnad-et-al-aaai19-large-instances (93)agricola-large        12        18
                            caldera-large         0         1
                            depots-large         0         1
                            satellite-large         3         5
                             tpp-large         0         9
logistics-large-simple (16)     goal-1         4         4
                                goal-2         4         4
                                goal-3         4         4
                                goal-4         4         4
organic-synthesis-alkene (17)                  15        15
pipesworld-tankage-nosplit (17)                  12        15
rovers-large-simple (6)         goal-4         3         3
                                goal-6         2         2
                                goal-8         1         1
Total (288)                                  190       209
```
