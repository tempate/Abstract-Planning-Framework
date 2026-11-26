# Benchmark report

2026-11-26 05:41 — experiments/htg/sat/results.csv

443 problems compared over asp, abs-asp, abs-lama, lama, lama-symmetry-pruning, abs-powerlifted, powerlifted

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA        LAMA+ Powerliftedᵅ  Powerlifted
-------------------------------------------------------------------------------------------------------------------------
Plans found                      79 (17.8%)   99 (22.3%)  242 (54.6%)  219 (49.4%)  180 (40.6%)  288 (65.0%)  325 (73.4%)
Timeouts                         89 (20.1%)  106 (23.9%)    28 (6.3%)    38 (8.6%)   77 (17.4%)    13 (2.9%)    41 (9.3%)
Out of memory                   275 (62.1%)  238 (53.7%)  173 (39.1%)  186 (42.0%)  186 (42.0%)  142 (32.1%)   77 (17.4%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                          443          443          443          443          443          443          443
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA Powerliftedᵅ  Powerlifted
------------------------------------------------------------------------------------------------------------
Plans found by both                      74           74          196          196          254          254
Faster                           38 (51.4%)   36 (48.6%)  141 (71.9%)   55 (28.1%)   95 (37.4%)  159 (62.6%)
Found when the other did not              5           25           46           23           34           71
Median runtime                      19.52 s      14.54 s       8.34 s      26.08 s      10.49 s       6.40 s
Total runtime                   10,776.49 s   6,379.93 s  15,193.16 s  21,577.15 s   8,398.39 s  14,105.43 s
Shorter plan                     15 (20.3%)   15 (20.3%)    13 (6.6%)   35 (17.9%)   39 (15.4%)   32 (12.6%)
Same plan length                 44 (59.5%)   44 (59.5%)  148 (75.5%)  148 (75.5%)  183 (72.0%)  183 (72.0%)
Median plan length                       15           14           21         20.5           21           21
Total plan length                       968          991        8,583        8,482        9,406        9,432
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ Powerliftedᵅ
---------------------------------------------------------------------
Abstract search                  106 (100%)     20 (71%)     10 (77%)
Guided concrete search               0 (0%)      5 (18%)      2 (15%)
Translating the task                 0 (0%)       2 (7%)       1 (8%)
Translating the task to ASP          0 (0%)       1 (4%)       0 (0%)
Total                                   106           28           13
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ Powerliftedᵅ
---------------------------------------------------------------------
Refined directly                  99 (100%)   242 (100%)   287 (100%)
Refined, some actions off            0 (0%)       0 (0%)       1 (0%)
Solved above the abstract plan       0 (0%)       0 (0%)       0 (0%)
Total                                    99          242          288
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ Powerliftedᵅ
---------------------------------------------------------------------
None                                 6 (6%)      11 (5%)      19 (7%)
1 to 4                             40 (40%)    136 (56%)    128 (44%)
5 to 9                               0 (0%)       5 (2%)       6 (2%)
10 to 19                           32 (32%)     65 (27%)    103 (36%)
20 or more                         21 (21%)     25 (10%)     32 (11%)
Total                                    99          242          288
```

## Plans found by domain

```
Domain (problems)                 Size       ASP      ASPᵅ     LAMAᵅ      LAMA     LAMA+PowerliftedᵅPowerlifted
---------------------------------------------------------------------------------------------------------------
blocksworld-large-simple (40)    goal-2         3         5        10         3         3        10        10
                                goal-3         3         5        10         3         3        10         4
                                goal-4         3         5        10         3         3        10         3
                                goal-5         2         4        10         3         3        10         3
childsnack-contents (44)    parsize1-cham3        12        12        12        12        12        12        12
                            parsize1-cham5         0         0        12        12        12        12        12
                            parsize1-cham7         0         0        12        12        12        12        12
                            parsize2-cham3        12        12        12        12        12        12        12
                            parsize2-cham5         0         0        12        12        12        12        12
                            parsize2-cham7         0         0        12        12        12        12         7
                            parsize3-cham3         7         8        12        12        12        12        12
                            parsize3-cham5         0         0        11         9         9        11         8
                            parsize3-cham7         0         0         6         5         5         5         2
                            parsize4-cham3         3         7        11        11        10        12        12
                            parsize4-cham5         0         0         2         2         1         2         3
                            parsize4-cham7         0         0         0         0         0         0         0
gnad-et-al-aaai19-large-instances (97)agricola-large         0         0        21        18         0        25        25
                            depots-large         0         0         0         1         0         0         7
                            satellite-large         0         0         3         5         2         2         4
                             tpp-large         0         0         0         9         9         0         9
logistics-large-simple (24)     goal-1         2         5         6         5         1         6         6
                                goal-2         0         4         6         5         1         6         6
                                goal-3         0         1         6         5         1         6         6
                                goal-4         0         4         6         5         1         6         6
organic-synthesis-MIT (18)                     2         0         0         2         2         4        18
organic-synthesis-alkene (18)                  15        15        16        15        15        15        18
organic-synthesis-original (20)                   1         0         0         1         1         0        16
pipesworld-tankage-nosplit (47)                   6         6        14        15        16        46        45
rovers-large-simple (35)        goal-2         1         1         1         1         1         5         7
                                goal-4         3         2         3         3         3         7         9
                                goal-6         3         2         3         3         3         3         9
                                goal-8         1         1         3         3         3         3        10
Total (443)                                   79        99       242       219       180       288       325
```
