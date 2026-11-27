# Benchmark report

2026-11-27 09:06 — experiments/htg/sat/results.csv

443 problems compared over asp, abs-asp, abs-lama, lama, lama-symmetry-pruning, abs-powerlifted, powerlifted, rnd-g

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA        LAMA+ Powerliftedᵅ  Powerlifted        rnd-g
--------------------------------------------------------------------------------------------------------------------------------------
Plans found                      79 (17.8%)  165 (37.2%)  250 (56.4%)  219 (49.4%)  180 (40.6%)  288 (65.0%)  325 (73.4%)  111 (25.1%)
Timeouts                         89 (20.1%)   50 (11.3%)    29 (6.5%)    38 (8.6%)   77 (17.4%)    13 (2.9%)    41 (9.3%)  202 (45.6%)
Out of memory                   275 (62.1%)  228 (51.5%)  164 (37.0%)  186 (42.0%)  186 (42.0%)  142 (32.1%)   77 (17.4%)  130 (29.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                          443          443          443          443          443          443          443          443
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA Powerliftedᵅ  Powerlifted
------------------------------------------------------------------------------------------------------------
Plans found by both                      74           74          204          204          254          254
Faster                           26 (35.1%)   48 (64.9%)  132 (64.7%)   72 (35.3%)   95 (37.4%)  159 (62.6%)
Found when the other did not              5           91           46           15           34           71
Median runtime                      26.65 s       6.89 s       7.76 s      35.69 s      10.49 s       6.40 s
Total runtime                   11,564.06 s   3,902.78 s  17,638.81 s  25,979.31 s   8,398.39 s  14,105.43 s
Shorter plan                     27 (36.5%)     5 (6.8%)     7 (3.4%)   34 (16.7%)   39 (15.4%)   32 (12.6%)
Same plan length                 42 (56.8%)   42 (56.8%)  163 (79.9%)  163 (79.9%)  183 (72.0%)  183 (72.0%)
Median plan length                       15           15           21           21           21           21
Total plan length                       968        1,067        9,733        9,640        9,406        9,432
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ Powerliftedᵅ
---------------------------------------------------------------------
Abstract search                    44 (88%)     23 (79%)     10 (77%)
Translating the task                 0 (0%)       1 (3%)       1 (8%)
Translating the task to ASP          0 (0%)       2 (7%)       0 (0%)
Guided concrete search              6 (12%)      3 (10%)      2 (15%)
Total                                    50           29           13
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ Powerliftedᵅ
---------------------------------------------------------------------
Refined directly                  114 (69%)   250 (100%)   287 (100%)
Refined, some actions off          51 (31%)       0 (0%)       1 (0%)
Solved above the abstract plan       0 (0%)       0 (0%)       0 (0%)
Total                                   165          250          288
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ Powerliftedᵅ
---------------------------------------------------------------------
None                                 6 (4%)      11 (4%)      19 (7%)
1 to 4                             90 (55%)    149 (60%)    128 (44%)
5 to 9                               0 (0%)       0 (0%)       6 (2%)
10 to 19                           51 (31%)     68 (27%)    103 (36%)
20 or more                         18 (11%)      22 (9%)     32 (11%)
Total                                   165          250          288
```

## Plans found by domain

```
Domain (problems)                 Size       ASP      ASPᵅ     LAMAᵅ      LAMA     LAMA+PowerliftedᵅPowerlifted     rnd-g
-------------------------------------------------------------------------------------------------------------------------
blocksworld-large-simple (40)    goal-2         3        10        10         3         3        10        10         2
                                goal-3         3        10        10         3         3        10         4         0
                                goal-4         3        10        10         3         3        10         3         0
                                goal-5         2         9        10         3         3        10         3         0
childsnack-contents (44)    parsize1-cham3        12        12        12        12        12        12        12        12
                            parsize1-cham5         0        12        12        12        12        12        12        11
                            parsize1-cham7         0        11        12        12        12        12        12         3
                            parsize2-cham3        12        12        12        12        12        12        12        10
                            parsize2-cham5         0        10        12        12        12        12        12         3
                            parsize2-cham7         0         2        12        12        12        12         7         1
                            parsize3-cham3         7        11        12        12        12        12        12         8
                            parsize3-cham5         0         3        12         9         9        11         8         1
                            parsize3-cham7         0         0         8         5         5         5         2         0
                            parsize4-cham3         3         6        12        11        10        12        12         6
                            parsize4-cham5         0         0         3         2         1         2         3         0
                            parsize4-cham7         0         0         0         0         0         0         0         0
gnad-et-al-aaai19-large-instances (97)agricola-large         0         0        23        18         0        25        25         0
                            depots-large         0         0         0         1         0         0         7         0
                            satellite-large         0         0         4         5         2         2         4         0
                             tpp-large         0         0         0         9         9         0         9         0
logistics-large-simple (24)     goal-1         2         6         6         5         1         6         6         4
                                goal-2         0         5         6         5         1         6         6         2
                                goal-3         0         2         6         5         1         6         6         1
                                goal-4         0         5         6         5         1         6         6         0
organic-synthesis-MIT (18)                     2         0         0         2         2         4        18        10
organic-synthesis-alkene (18)                  15        16        16        15        15        15        18        18
organic-synthesis-original (20)                   1         0         0         1         1         0        16         2
pipesworld-tankage-nosplit (47)                   6         7        14        15        16        46        45        11
rovers-large-simple (35)        goal-2         1         1         1         1         1         5         7         3
                                goal-4         3         2         3         3         3         7         9         2
                                goal-6         3         2         3         3         3         3         9         1
                                goal-8         1         1         3         3         3         3        10         0
Total (443)                                   79       165       250       219       180       288       325       111
```
