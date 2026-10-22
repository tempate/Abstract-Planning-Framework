# Benchmark report

2026-10-22 14:27 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-lmcut, lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  139 (37.3%)  206 (55.2%)  209 (56.0%)
Timeouts                        244 (65.4%)  224 (60.1%)  157 (42.1%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          176          176
Faster                           79 (65.3%)   42 (34.7%)   69 (39.2%)  107 (60.8%)
Found when the other did not              8           18           30           33
Median runtime                       6.99 s       9.68 s       6.61 s       4.00 s
Total runtime                   15,664.30 s  11,374.03 s   9,309.64 s  18,340.38 s
Shorter plan                     32 (26.4%)     0 (0.0%)     0 (0.0%)   73 (41.5%)
Same plan length                 89 (73.6%)   89 (73.6%)  103 (58.5%)  103 (58.5%)
Median plan length                       10           11         18.5           16
Total plan length                     1,346        1,431        3,405        2,954
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   125 (56%)     30 (19%)
Guided concrete search              16 (7%)     41 (26%)
Unguided concrete search           83 (37%)     86 (55%)
Total                                   224          157
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                  101 (73%)    159 (77%)
Refined, some actions off          30 (22%)     39 (19%)
Solved above the abstract plan       8 (6%)       8 (4%)
Total                                   139          206
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             97 (74%)    113 (57%)
5 to 9                             28 (21%)     49 (25%)
10 to 19                             6 (5%)     23 (12%)
20 or more                           0 (0%)      13 (7%)
Total                                   131          198
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        17        17        20
elevators-opt08-strips              30        10        13        26        26
elevators-opt11-strips              20         9        11        20        20
freecell                            80        10         8         8        28
mprime                              31        31        29        25        24
mystery                             27        18        17        16        17
nomystery-opt11-strips              20        10        12        18        18
openstacks-opt08-strips             30         2         3        20        10
openstacks-opt11-strips             20         0         0        13         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9        11        16        14
transport-opt11-strips              20         5         6        11        10
transport-opt14-strips              20         3         6        10         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       139       206       209
```
