# Benchmark report

2026-10-23 14:03 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  142 (38.1%)  197 (52.8%)  209 (56.0%)
Timeouts                        244 (65.4%)  221 (59.2%)  166 (44.5%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     123          123          168          168
Faster                           85 (69.1%)   38 (30.9%)   59 (35.1%)  109 (64.9%)
Found when the other did not              6           19           29           41
Median runtime                       7.54 s      13.01 s       7.59 s       3.41 s
Total runtime                   15,713.98 s  12,646.04 s  12,327.24 s  16,504.29 s
Shorter plan                     24 (19.5%)     0 (0.0%)     0 (0.0%)   57 (33.9%)
Same plan length                 99 (80.5%)   99 (80.5%)  111 (66.1%)  111 (66.1%)
Median plan length                       10           11         16.5         15.5
Total plan length                     1,380        1,455        3,042        2,751
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   125 (57%)     31 (19%)
Guided concrete search              15 (7%)     48 (29%)
Unguided concrete search           81 (37%)     87 (52%)
Total                                   221          166
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                  103 (73%)    156 (79%)
Refined, some actions off          30 (21%)     32 (16%)
Solved above the abstract plan       9 (6%)       9 (5%)
Total                                   142          197
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             62 (47%)     83 (44%)
5 to 9                             45 (34%)     50 (27%)
10 to 19                           14 (11%)     32 (17%)
20 or more                          12 (9%)     23 (12%)
Total                                   133          188
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        16        17        20
elevators-opt08-strips              30        10        15        21        26
elevators-opt11-strips              20         9        14        17        20
freecell                            80        10         8         8        28
mprime                              31        31        29        24        24
mystery                             27        18        17        16        17
nomystery-opt11-strips              20        10        12        18        18
openstacks-opt08-strips             30         2         3        20        10
openstacks-opt11-strips             20         0         0        13         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9        10        16        14
transport-opt11-strips              20         5         6        11        10
transport-opt14-strips              20         3         6        10         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       142       197       209
```
