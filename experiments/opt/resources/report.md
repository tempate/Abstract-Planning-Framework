# Benchmark report

2026-10-20 09:04 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)   96 (25.7%)   96 (25.7%)  209 (56.0%)
Timeouts                        244 (65.4%)  267 (71.6%)  267 (71.6%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                      96           96           95           95
Faster                           94 (97.9%)     2 (2.1%)     5 (5.3%)   90 (94.7%)
Found when the other did not             33            0            1          114
Median runtime                       4.41 s      15.33 s      13.57 s       2.41 s
Total runtime                    2,484.33 s  12,989.91 s  11,166.55 s     680.20 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length                96 (100.0%)  96 (100.0%)  95 (100.0%)  95 (100.0%)
Median plan length                        8            8            8            8
Total plan length                       906          906          914          914
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   125 (47%)     30 (11%)
Guided concrete search            137 (51%)    234 (88%)
Unguided concrete search             5 (2%)       3 (1%)
Total                                   267          267
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   88 (92%)     88 (92%)
Refined, some actions off            0 (0%)       0 (0%)
Solved above the abstract plan       8 (8%)       8 (8%)
Total                                    96           96
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             78 (89%)     78 (89%)
5 to 9                               4 (5%)       4 (5%)
10 to 19                             6 (7%)       6 (7%)
20 or more                           0 (0%)       0 (0%)
Total                                    88           88
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        14        14        20
elevators-opt08-strips              30        10         2         2        26
elevators-opt11-strips              20         9         1         1        20
freecell                            80        10         8         8        28
mprime                              31        31        26        24        24
mystery                             27        18        16        16        17
nomystery-opt11-strips              20        10         6         6        18
openstacks-opt08-strips             30         2         1         1        10
openstacks-opt11-strips             20         0         0         0         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9         9        10        14
transport-opt11-strips              20         5         4         5        10
transport-opt14-strips              20         3         3         3         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129        96        96       209
```
