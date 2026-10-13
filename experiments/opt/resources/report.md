# Benchmark report

2026-10-13 12:57 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  134 (35.9%)  196 (52.5%)  212 (56.8%)
Timeouts                        244 (65.4%)  229 (61.4%)  166 (44.5%)  159 (42.6%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     1 (0.3%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     117          117          168          168
Faster                           79 (67.5%)   38 (32.5%)   69 (41.1%)   99 (58.9%)
Found when the other did not             12           17           28           44
Median runtime                       6.48 s       9.49 s       6.02 s       4.14 s
Total runtime                   15,283.35 s  10,887.54 s  10,431.25 s  14,122.70 s
Shorter plan                     29 (24.8%)     0 (0.0%)    12 (7.1%)   56 (33.3%)
Same plan length                 88 (75.2%)   88 (75.2%)  100 (59.5%)  100 (59.5%)
Median plan length                        9           11           17           17
Total plan length                     1,286        1,365        3,643        3,450
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   126 (55%)     30 (18%)
Guided concrete search              20 (9%)     49 (30%)
Unguided concrete search           83 (36%)     87 (52%)
Total                                   229          166
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                   99 (74%)    152 (78%)
Refined, some actions off          26 (19%)     35 (18%)
Solved above the abstract plan       9 (7%)       9 (5%)
Total                                   134          196
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             95 (76%)    111 (59%)
5 to 9                             24 (19%)     40 (21%)
10 to 19                             6 (5%)     23 (12%)
20 or more                           0 (0%)      13 (7%)
Total                                   125          187
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        16        16        13
elevators-opt08-strips              30        10        12        21        22
elevators-opt11-strips              20         9        10        17        18
freecell                            80        10         8         8        28
mprime                              31        31        29        25        24
mystery                             27        18        15        15        17
nomystery-opt11-strips              20        10        12        18        18
openstacks-opt08-strips             30         2         3        20        23
openstacks-opt11-strips             20         0         0        13        18
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9        11        16        11
transport-opt11-strips              20         5         6        11         6
transport-opt14-strips              20         3         6        10         6
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       134       196       212
```
