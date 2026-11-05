# Benchmark report

2026-11-05 10:16 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  119 (31.9%)  131 (35.1%)  209 (56.0%)
Timeouts                        244 (65.4%)  244 (65.4%)  232 (62.2%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     118          118          124          124
Faster                           99 (83.9%)   19 (16.1%)   17 (13.7%)  107 (86.3%)
Found when the other did not             11            1            7           85
Median runtime                       6.59 s      17.35 s      11.89 s       2.66 s
Total runtime                    9,184.03 s  10,686.60 s  10,145.13 s   6,774.03 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               118 (100.0%) 118 (100.0%) 124 (100.0%) 124 (100.0%)
Median plan length                      9.5          9.5           11           11
Total plan length                     1,259        1,259        1,551        1,551
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   130 (53%)     31 (13%)
Guided concrete search               9 (4%)     35 (15%)
Unguided concrete search          105 (43%)    166 (72%)
Total                                   244          232
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   63 (53%)     72 (55%)
Refined, some actions off          15 (13%)     20 (15%)
Solved above the abstract plan     41 (34%)     39 (30%)
Total                                   119          131
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             46 (59%)     60 (65%)
5 to 9                             32 (41%)     30 (33%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       2 (2%)
Total                                    78           92
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        14        20
elevators-opt08-strips (30)         10         8         9        26
elevators-opt11-strips (20)          9         6         7        20
freecell (80)                       10        10         9        28
mprime (31)                         31        29        24        24
mystery (27)                        18        17        17        17
nomystery-opt11-strips (20)         10         8        12        18
openstacks-opt08-strips (30)         2         2         2        10
openstacks-opt11-strips (20)         0         0         0         5
tpp (24)                             5         5         5         7
transport-opt08-strips (30)          9        10        15        14
transport-opt11-strips (20)          5         5         9        10
transport-opt14-strips (20)          3         3         7         9
visitall-opt11-strips (1)            1         1         1         1
Total (373)                        129       119       131       209
```
