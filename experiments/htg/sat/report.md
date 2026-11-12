# Benchmark report

2026-11-12 10:04 — experiments/htg/sat/results.csv

443 problems compared over abs-lama, lama

## Coverage

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found                     242 (54.6%)  219 (49.4%)
Timeouts                          28 (6.3%)    38 (8.6%)
Out of memory                   173 (39.1%)  186 (42.0%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          443          443
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                     196          196
Faster                          141 (71.9%)   55 (28.1%)
Found when the other did not             46           23
Median runtime                       8.34 s      26.08 s
Total runtime                   15,193.16 s  21,577.15 s
Shorter plan                      13 (6.6%)   35 (17.9%)
Same plan length                148 (75.5%)  148 (75.5%)
Median plan length                       21         20.5
Total plan length                     8,583        8,482
```

## Where the timeouts died

```
Killed during                         LAMAᵅ
-------------------------------------------
Abstract search                    20 (71%)
Guided concrete search              5 (18%)
Translating the task                 2 (7%)
Translating the task to ASP          1 (4%)
Total                                    28
```

## How the successes were solved

```
Solved by                             LAMAᵅ
-------------------------------------------
Refined directly                 242 (100%)
Refined, some actions off            0 (0%)
Solved above the abstract plan       0 (0%)
Total                                   242
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                       LAMAᵅ
-------------------------------------------
None                                11 (5%)
1 to 4                            136 (56%)
5 to 9                               5 (2%)
10 to 19                           65 (27%)
20 or more                         25 (10%)
Total                                   242
```

## Plans found by domain

```
Domain (problems)                 Size     LAMAᵅ      LAMA
----------------------------------------------------------
blocksworld-large-simple (40)    goal-2        10         3
                                goal-3        10         3
                                goal-4        10         3
                                goal-5        10         3
childsnack-contents (44)    parsize1-cham3        12        12
                            parsize1-cham5        12        12
                            parsize1-cham7        12        12
                            parsize2-cham3        12        12
                            parsize2-cham5        12        12
                            parsize2-cham7        12        12
                            parsize3-cham3        12        12
                            parsize3-cham5        11         9
                            parsize3-cham7         6         5
                            parsize4-cham3        11        11
                            parsize4-cham5         2         2
                            parsize4-cham7         0         0
gnad-et-al-aaai19-large-instances (97)agricola-large        21        18
                            depots-large         0         1
                            satellite-large         3         5
                             tpp-large         0         9
logistics-large-simple (24)     goal-1         6         5
                                goal-2         6         5
                                goal-3         6         5
                                goal-4         6         5
organic-synthesis-MIT (18)                     0         2
organic-synthesis-alkene (18)                  16        15
organic-synthesis-original (20)                   0         1
pipesworld-tankage-nosplit (47)                  14        15
rovers-large-simple (35)        goal-2         1         1
                                goal-4         3         3
                                goal-6         3         3
                                goal-8         3         3
Total (443)                                  242       219
```
