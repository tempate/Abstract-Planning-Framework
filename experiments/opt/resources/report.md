# Benchmark report

2026-10-29 09:35 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  119 (31.9%)  138 (37.0%)  209 (56.0%)
Timeouts                        244 (65.4%)  244 (65.4%)  225 (60.3%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     118          118          130          130
Faster                           98 (83.1%)   20 (16.9%)   21 (16.2%)  109 (83.8%)
Found when the other did not             11            1            8           79
Median runtime                       6.59 s      13.21 s       9.39 s       2.70 s
Total runtime                    8,928.65 s  10,049.74 s  10,153.38 s   6,987.01 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               118 (100.0%) 118 (100.0%) 130 (100.0%) 130 (100.0%)
Median plan length                      9.5          9.5         11.5         11.5
Total plan length                     1,262        1,262        1,700        1,700
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   129 (53%)     32 (14%)
Guided concrete search               4 (2%)     39 (17%)
Unguided concrete search          111 (45%)    154 (68%)
Total                                   244          225
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   60 (50%)     80 (58%)
Refined, some actions off          19 (16%)     16 (12%)
Solved above the abstract plan     40 (34%)     42 (30%)
Total                                   119          138
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                            79 (100%)    96 (100%)
5 to 9                               0 (0%)       0 (0%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       0 (0%)
Total                                    79           96
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        16        15        20
elevators-opt08-strips              30        10         8         9        26
elevators-opt11-strips              20         9         6         8        20
freecell                            80        10         9         9        28
mprime                              31        31        29        25        24
mystery                             27        18        17        16        17
nomystery-opt11-strips              20        10         8        17        18
openstacks-opt08-strips             30         2         2         2        10
openstacks-opt11-strips             20         0         0         0         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9        10        15        14
transport-opt11-strips              20         5         5         9        10
transport-opt14-strips              20         3         3         7         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       119       138       209
```
