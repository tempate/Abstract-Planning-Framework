# Benchmark report

2026-10-27 09:04 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  138 (37.0%)  160 (42.9%)  209 (56.0%)
Timeouts                        244 (65.4%)  225 (60.3%)  203 (54.4%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     126          126          151          151
Faster                           93 (73.8%)   33 (26.2%)   46 (30.5%)  105 (69.5%)
Found when the other did not              3           12            9           58
Median runtime                       7.94 s      11.25 s       7.10 s       3.05 s
Total runtime                   17,437.87 s  15,058.24 s   7,909.02 s   9,355.04 s
Shorter plan                       9 (7.1%)     0 (0.0%)     0 (0.0%)   33 (21.9%)
Same plan length                117 (92.9%)  117 (92.9%)  118 (78.1%)  118 (78.1%)
Median plan length                       11           11           14           14
Total plan length                     1,425        1,457        2,472        2,159
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   125 (56%)     30 (15%)
Guided concrete search               5 (2%)     35 (17%)
Unguided concrete search           95 (42%)    138 (68%)
Total                                   225          203
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   80 (58%)     95 (59%)
Refined, some actions off          22 (16%)     36 (22%)
Solved above the abstract plan     36 (26%)     29 (18%)
Total                                   138          160
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             87 (85%)     97 (74%)
5 to 9                             15 (15%)     34 (26%)
10 to 19                             0 (0%)       0 (0%)
20 or more                           0 (0%)       0 (0%)
Total                                   102          131
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        16        15        20
elevators-opt08-strips              30        10        13        20        26
elevators-opt11-strips              20         9        11        17        20
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
Total                              373       129       138       160       209
```
