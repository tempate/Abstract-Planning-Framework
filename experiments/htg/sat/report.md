# Benchmark report

2026-11-05 16:34 — experiments/htg/sat/results.csv

288 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                      57 (19.8%)  209 (72.6%)
Timeouts                         70 (24.3%)   38 (13.2%)
Out of memory                   161 (55.9%)   41 (14.2%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                      57           57
Faster                             2 (3.5%)   55 (96.5%)
Found when the other did not              0          152
Median runtime                      20.59 s       3.30 s
Total runtime                    8,394.75 s     524.98 s
Shorter plan                     30 (52.6%)     0 (0.0%)
Same plan length                 27 (47.4%)   27 (47.4%)
Median plan length                       14           17
Total plan length                     1,047        1,160
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    23 (33%)
Translating the task to ASP          2 (3%)
Guided concrete search             33 (47%)
Unguided concrete search           12 (17%)
Total                                    70
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                   34 (60%)
Refined, some actions off            3 (5%)
Solved above the abstract plan     20 (35%)
Total                                    57
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                                 1 (3%)
1 to 4                             22 (59%)
5 to 9                               0 (0%)
10 to 19                           14 (38%)
20 or more                           0 (0%)
Total                                    37
```

## Plans found by domain

```
Domain (problems)                 Size     LAMAᵅ      LAMA
----------------------------------------------------------
blocksworld-large-simple (24)    goal-2         2         3
                                goal-3         2         3
                                goal-4         2         3
                                goal-5         2         3
childsnack-contents (44)    parsize1-cham3        12        12
                            parsize1-cham5        10        12
                            parsize1-cham7         1        12
                            parsize2-cham3         6        12
                            parsize2-cham5         7        12
                            parsize2-cham7         0        12
                            parsize3-cham3         3        12
                            parsize3-cham5         1         9
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
pipesworld-tankage-nosplit (17)                   7        15
rovers-large-simple (6)         goal-4         1         3
                                goal-6         1         2
                                goal-8         0         1
Total (288)                                   57       209
```
