# Benchmark report

2026-10-23 09:53 — experiments/opt/resources/results.csv

373 problems compared over asp, abs-asp, abs-fd, fd-lmcut

## Coverage

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found                     129 (34.6%)  136 (36.5%)  199 (53.4%)  209 (56.0%)
Timeouts                        244 (65.4%)  227 (60.9%)  164 (44.0%)  162 (43.4%)
Out of memory                      0 (0.0%)    10 (2.7%)    10 (2.7%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.5%)
Total problems                          373          373          373          373
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ       LMcutᵅ        LMcut
----------------------------------------------------------------------------------
Plans found by both                     121          121          170          170
Faster                           81 (66.9%)   40 (33.1%)   63 (37.1%)  107 (62.9%)
Found when the other did not              8           15           29           39
Median runtime                       6.99 s      10.55 s       6.54 s       3.59 s
Total runtime                   14,458.70 s  13,296.75 s   9,999.65 s  16,122.27 s
Shorter plan                     26 (21.5%)     0 (0.0%)     0 (0.0%)   56 (32.9%)
Same plan length                 95 (78.5%)   95 (78.5%)  114 (67.1%)  114 (67.1%)
Median plan length                       10           11         16.5         15.5
Total plan length                     1,347        1,418        3,161        2,769
```

## Where the timeouts died

```
Killed during                          ASPᵅ       LMcutᵅ
--------------------------------------------------------
Abstract search                   125 (55%)     30 (18%)
Guided concrete search               7 (3%)     33 (20%)
Unguided concrete search           95 (42%)    101 (62%)
Total                                   227          164
```

## How the successes were solved

```
Solved by                              ASPᵅ       LMcutᵅ
--------------------------------------------------------
Refined directly                  102 (75%)    161 (81%)
Refined, some actions off          26 (19%)     30 (15%)
Solved above the abstract plan       8 (6%)       8 (4%)
Total                                   136          199
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ       LMcutᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             93 (73%)    111 (58%)
5 to 9                             29 (23%)     45 (24%)
10 to 19                             6 (5%)     22 (12%)
20 or more                           0 (0%)      13 (7%)
Total                                   128          191
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ    LMcutᵅ     LMcut
------------------------------------------------------------------------------
data-network-opt18-strips           20        16        14        17        20
elevators-opt08-strips              30        10        14        23        26
elevators-opt11-strips              20         9        12        19        20
freecell                            80        10         8         8        28
mprime                              31        31        29        25        24
mystery                             27        18        16        16        17
nomystery-opt11-strips              20        10        12        17        18
openstacks-opt08-strips             30         2         3        19        10
openstacks-opt11-strips             20         0         0        13         5
tpp                                 24         5         5         5         7
transport-opt08-strips              30         9        11        16        14
transport-opt11-strips              20         5         6        11        10
transport-opt14-strips              20         3         5         9         9
visitall-opt11-strips                1         1         1         1         1
Total                              373       129       136       199       209
```
