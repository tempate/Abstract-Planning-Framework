# Benchmark report

2026-10-23 14:03 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      72 (21.8%)   83 (25.2%)  126 (38.2%)  305 (92.4%)
Timeouts                        258 (78.2%)  247 (74.8%)  177 (53.6%)    22 (6.7%)
Out of memory                      0 (0.0%)     0 (0.0%)    27 (8.2%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      72           72          126          126
Faster                           42 (58.3%)   30 (41.7%)     7 (5.6%)  119 (94.4%)
Found when the other did not              0           11            0          179
Median runtime                       7.39 s      10.83 s      14.71 s       3.16 s
Total runtime                    6,180.44 s   3,282.90 s  10,547.91 s     779.68 s
Shorter plan                     60 (83.3%)     0 (0.0%)     5 (4.0%)  108 (85.7%)
Same plan length                 12 (16.7%)   12 (16.7%)   13 (10.3%)   13 (10.3%)
Median plan length                        8           12           23           18
Total plan length                       648          990        6,501        5,097
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       3 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   158 (64%)       3 (2%)
Guided concrete search               6 (2%)     67 (38%)
Unguided concrete search           79 (32%)    103 (58%)
Total                                   247          177
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   63 (76%)     95 (75%)
Refined, some actions off          13 (16%)     24 (19%)
Solved above the abstract plan       7 (8%)       7 (6%)
Total                                    83          126
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             31 (41%)     41 (34%)
5 to 9                             35 (46%)     41 (34%)
10 to 19                             2 (3%)       9 (8%)
20 or more                          8 (11%)     28 (24%)
Total                                    76          119
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         1         1        12
elevators-sat08-strips              30         1         3         8        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        10        10        10        72
mprime                              29        29        29        29        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         2         8        10        12
openstacks-sat08-strips             27         3         3        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         0         1         5        15
tpp                                 24         5         5         5        24
transport-sat08-strips              30         5         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        72        83       126       305
```
