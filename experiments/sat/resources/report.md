# Benchmark report

2026-10-22 14:27 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      72 (21.8%)   83 (25.2%)  127 (38.5%)  305 (92.4%)
Timeouts                        258 (78.2%)  247 (74.8%)  174 (52.7%)    22 (6.7%)
Out of memory                      0 (0.0%)     0 (0.0%)    29 (8.8%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      72           72          127          127
Faster                           45 (62.5%)   27 (37.5%)     5 (3.9%)  122 (96.1%)
Found when the other did not              0           11            0          178
Median runtime                       7.39 s       9.45 s      14.21 s       3.15 s
Total runtime                    6,180.44 s   3,583.28 s  10,384.97 s     778.64 s
Shorter plan                     62 (86.1%)     0 (0.0%)    11 (8.7%)  100 (78.7%)
Same plan length                 10 (13.9%)   10 (13.9%)   16 (12.6%)   16 (12.6%)
Median plan length                        8           12           23           18
Total plan length                       648        1,001        6,346        5,170
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       3 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   158 (64%)       3 (2%)
Guided concrete search               5 (2%)     65 (37%)
Unguided concrete search           80 (32%)    102 (59%)
Total                                   247          174
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   62 (75%)     96 (76%)
Refined, some actions off          14 (17%)     24 (19%)
Solved above the abstract plan       7 (8%)       7 (6%)
Total                                    83          127
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             60 (79%)     68 (57%)
5 to 9                              8 (11%)     19 (16%)
10 to 19                            8 (11%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    76          120
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         1         1        12
elevators-sat08-strips              30         1         3        10        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        10        10        10        72
mprime                              29        29        29        28        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         2         8        10        12
openstacks-sat08-strips             27         3         3        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         0         1         5        15
tpp                                 24         5         5         5        24
transport-sat08-strips              30         5         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        72        83       127       305
```
