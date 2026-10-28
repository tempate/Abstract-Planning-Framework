# Benchmark report

2026-10-28 05:22 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  128 (34.3%)  141 (37.8%)  209 (56.0%)
Timeouts                        244 (65.4%)  235 (63.0%)  222 (59.5%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          132          132
Faster                           95 (78.5%)   26 (21.5%)   26 (19.7%)  106 (80.3%)
Found when the other did not              8            7            9           77
Median runtime                       6.99 s      11.70 s       7.77 s       2.72 s
Total runtime                   11,450.69 s   9,903.94 s  11,737.91 s   7,001.71 s
Shorter plan                       0 (0.0%)     0 (0.0%)     0 (0.0%)     0 (0.0%)
Same plan length               121 (100.0%) 121 (100.0%) 132 (100.0%) 132 (100.0%)
Median plan length                       10           10           12           12
Total plan length                     1,326        1,326        1,730        1,730
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   125 (53%)     30 (14%)
Guided concrete search               4 (2%)     39 (18%)
Unguided concrete search          106 (45%)    153 (69%)
Total                                   235          222
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   73 (57%)     80 (57%)
Refined, some actions off          13 (10%)     16 (11%)
Solved above the abstract plan     42 (33%)     45 (32%)
Total                                   128          141
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                            86 (100%)    96 (100%)
5 to 9                               0 (0%)       0 (0%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       0 (0%)
Total                                    86           96
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        16        15        20
elevators-opt08-strips              30        10         8        10        26
elevators-opt11-strips              20         9         6         8        20
freecell                            80        10        10        10        28
mprime                              31        31        29        25        24
mystery                             27        18        17        17        17
nomystery-opt11-strips              20        10        12        17        18
openstacks-opt08-strips             30         2         2         2        10
openstacks-opt11-strips             20         0         0         0         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9        11        15        14
transport-opt11-strips              20         5         6         9        10
transport-opt14-strips              20         3         5         7         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       128       141       209
```
