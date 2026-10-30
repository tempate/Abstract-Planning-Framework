# Benchmark report

2026-10-30 16:36 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  126 (33.8%)  137 (36.7%)  209 (56.0%)
Timeouts                        244 (65.4%)  237 (63.5%)  226 (60.6%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     119          119          130          130
Faster                           97 (81.5%)   22 (18.5%)   20 (15.4%)  110 (84.6%)
Found when the other did not             10            7            7           79
Median runtime                       6.69 s      15.44 s      10.87 s       2.70 s
Total runtime                    9,985.83 s  11,876.85 s  10,199.97 s   6,983.81 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               119 (100.0%) 119 (100.0%) 130 (100.0%) 130 (100.0%)
Median plan length                       10           10         11.5         11.5
Total plan length                     1,299        1,299        1,694        1,694
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   129 (54%)     32 (14%)
Guided concrete search               8 (3%)     35 (15%)
Unguided concrete search          100 (42%)    159 (70%)
Total                                   237          226
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   77 (61%)     82 (60%)
Refined, some actions off          12 (10%)     15 (11%)
Solved above the abstract plan     37 (29%)     40 (29%)
Total                                   126          137
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             54 (61%)     64 (66%)
5 to 9                             33 (37%)     31 (32%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           2 (2%)       2 (2%)
Total                                    89           97
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        15        20
elevators-opt08-strips (30)         10         8         9        26
elevators-opt11-strips (20)          9         6         7        20
freecell (80)                       10         9        10        28
mprime (31)                         31        29        24        24
mystery (27)                        18        17        16        17
nomystery-opt11-strips (20)         10        12        17        18
openstacks-opt08-strips (30)         2         2         2        10
openstacks-opt11-strips (20)         0         0         0         5
tpp (24)                             5         5         5         7
transport-opt08-strips (30)          9        11        15        14
transport-opt11-strips (20)          5         6         9        10
transport-opt14-strips (20)          3         5         7         9
visitall-opt11-strips (1)            1         1         1         1
Total (373)                        129       126       137       209
```
