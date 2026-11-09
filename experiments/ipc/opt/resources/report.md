# Benchmark report

2026-11-09 09:01 — experiments/ipc/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     125 (33.5%)  120 (32.2%)  132 (35.4%)  209 (56.0%)
Timeouts                        248 (66.5%)  243 (65.1%)  231 (61.9%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     117          117          125          125
Faster                           91 (77.8%)   26 (22.2%)   20 (16.0%)  105 (84.0%)
Found when the other did not              8            3            7           84
Median runtime                       8.09 s      12.71 s       7.79 s       2.67 s
Total runtime                    9,836.43 s   9,810.49 s  11,626.07 s   6,787.84 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               117 (100.0%) 117 (100.0%) 125 (100.0%) 125 (100.0%)
Median plan length                        9            9           11           11
Total plan length                     1,240        1,240        1,569        1,569
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   130 (53%)     31 (13%)
Guided concrete search               8 (3%)     35 (15%)
Unguided concrete search          105 (43%)    165 (71%)
Total                                   243          231
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   64 (53%)     72 (55%)
Refined, some actions off          15 (12%)     20 (15%)
Solved above the abstract plan     41 (34%)     40 (30%)
Total                                   120          132
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             47 (59%)     60 (65%)
5 to 9                             32 (41%)     30 (33%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       2 (2%)
Total                                    79           92
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ    LMcutᵅ     LMcut
--------------------------------------------------------------------
data-network-opt18-strips (20)        16        15        15        20
elevators-opt08-strips (30)          9         8         9        26
elevators-opt11-strips (20)          7         6         7        20
freecell (80)                       10        10         9        28
mprime (31)                         31        29        24        24
mystery (27)                        18        17        17        17
nomystery-opt11-strips (20)         10         8        12        18
openstacks-opt08-strips (30)         2         2         2        10
openstacks-opt11-strips (20)         0         0         0         5
tpp (24)                             5         5         5         7
transport-opt08-strips (30)          9        10        15        14
transport-opt11-strips (20)          4         5         9        10
transport-opt14-strips (20)          3         4         7         9
visitall-opt11-strips (1)            1         1         1         1
Total (373)                        125       120       132       209
```
