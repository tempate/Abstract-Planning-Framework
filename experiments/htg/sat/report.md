# Benchmark report

2026-11-06 07:53 — experiments/htg/sat/results.csv

288 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                     112 (38.9%)  209 (72.6%)
Timeouts                         42 (14.6%)   38 (13.2%)
Out of memory                   134 (46.5%)   41 (14.2%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          288          288
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                     112          112
Faster                             1 (0.9%)  111 (99.1%)
Found when the other did not              0           97
Median runtime                      17.96 s       4.38 s
Total runtime                    7,589.73 s   1,964.48 s
Shorter plan                      11 (9.8%)   71 (63.4%)
Same plan length                 30 (26.8%)   30 (26.8%)
Median plan length                     18.5           17
Total plan length                     2,901        2,305
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    30 (71%)
Translating the task                 1 (2%)
Guided concrete search             11 (26%)
Total                                    42
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                   81 (72%)
Refined, some actions off          31 (28%)
Solved above the abstract plan       0 (0%)
Total                                   112
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                               21 (19%)
1 to 4                             57 (51%)
5 to 9                               0 (0%)
10 to 19                           12 (11%)
20 or more                         22 (20%)
Total                                   112
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
                            parsize4-cham3         5        11
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
organic-synthesis-alkene (17)                  15        15
pipesworld-tankage-nosplit (17)                   8        15
rovers-large-simple (6)         goal-4         3         3
                                goal-6         2         2
                                goal-8         1         1
Total (288)                                  112       209
```
