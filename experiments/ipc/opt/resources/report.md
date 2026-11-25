# Benchmark report

2026-11-25 15:42 — experiments/ipc/opt/resources/results.csv

383 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     122 (31.9%)  119 (31.1%)  129 (33.7%)  206 (53.8%)
Timeouts                        261 (68.1%)  264 (68.9%)  251 (65.5%)  175 (45.7%)
Out of memory                      0 (0.0%)     0 (0.0%)     3 (0.8%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          383          383          383          383
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     117          117          122          122
Faster                           84 (71.8%)   33 (28.2%)   26 (21.3%)   96 (78.7%)
Found when the other did not              5            2            7           84
Median runtime                       7.15 s      11.89 s       6.80 s       2.92 s
Total runtime                    9,460.61 s  10,342.25 s   9,732.37 s   5,583.09 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               117 (100.0%) 117 (100.0%) 122 (100.0%) 122 (100.0%)
Median plan length                        9            9           11           11
Total plan length                     1,240        1,240        1,471        1,471
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   149 (56%)     31 (12%)
Guided concrete search              18 (7%)     44 (18%)
Unguided concrete search           97 (37%)    176 (70%)
Total                                   264          251
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   61 (51%)     69 (53%)
Refined, some actions off          18 (15%)     21 (16%)
Solved above the abstract plan     40 (34%)     39 (30%)
Total                                   119          129
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             42 (53%)     56 (62%)
5 to 9                             37 (47%)     32 (36%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       2 (2%)
Total                                    79           90
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        15        20
elevators-opt08-strips (30)          9         8         9        26
elevators-opt11-strips (20)          7         6         7        20
freecell (73)                       10        10         9        27
mprime (29)                         29        29        24        23
mystery (26)                        17        17        17        16
nomystery-opt11-strips (20)         10         8         9        18
openstacks-opt08-strips (30)         2         2         2        10
openstacks-opt11-strips (20)         0         0         0         5
openstacks-opt14-strips (20)         0         0         0         0
tpp (24)                             5         5         5         7
transport-opt08-strips (30)          9        10        15        14
transport-opt11-strips (20)          4         5         9        10
transport-opt14-strips (20)          3         3         7         9
visitall-opt11-strips (1)            1         1         1         1
Total (383)                        122       119       129       206
```
