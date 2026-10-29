# Benchmark report

2026-10-29 09:45 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  123 (33.0%)  140 (37.5%)  209 (56.0%)
Timeouts                        244 (65.4%)  240 (64.3%)  223 (59.8%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     120          120          131          131
Faster                           98 (81.7%)   22 (18.3%)   15 (11.5%)  116 (88.5%)
Found when the other did not              9            3            9           78
Median runtime                       6.84 s      12.66 s      10.96 s       2.71 s
Total runtime                   10,557.89 s  10,821.05 s  12,576.56 s   6,990.76 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               120 (100.0%) 120 (100.0%) 131 (100.0%) 131 (100.0%)
Median plan length                       10           10           12           12
Total plan length                     1,313        1,313        1,716        1,716
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   130 (54%)     30 (13%)
Unguided concrete search          110 (46%)    193 (87%)
Total                                   240          223
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   69 (56%)     80 (57%)
Refined, some actions off           11 (9%)     17 (12%)
Solved above the abstract plan     43 (35%)     43 (31%)
Total                                   123          140
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                            80 (100%)    97 (100%)
5 to 9                               0 (0%)       0 (0%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       0 (0%)
Total                                    80           97
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        17        16        20
elevators-opt08-strips              30        10         8         9        26
elevators-opt11-strips              20         9         7         7        20
freecell                            80        10         9         9        28
mprime                              31        31        29        25        24
mystery                             27        18        17        17        17
nomystery-opt11-strips              20        10        12        18        18
openstacks-opt08-strips             30         2         2         2        10
openstacks-opt11-strips             20         0         0         0         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9         9        15        14
transport-opt11-strips              20         5         4         9        10
transport-opt14-strips              20         3         3         7         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       123       140       209
```
