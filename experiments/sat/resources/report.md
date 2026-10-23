# Benchmark report

2026-10-23 09:53 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      72 (21.8%)   83 (25.2%)  124 (37.6%)  305 (92.4%)
Timeouts                        258 (78.2%)  247 (74.8%)  179 (54.2%)    22 (6.7%)
Out of memory                      0 (0.0%)     0 (0.0%)    27 (8.2%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      72           72          124          124
Faster                           40 (55.6%)   32 (44.4%)     9 (7.3%)  115 (92.7%)
Found when the other did not              0           11            0          181
Median runtime                       7.39 s       8.28 s      10.80 s       3.10 s
Total runtime                    6,180.44 s   3,732.65 s   9,492.32 s     725.85 s
Shorter plan                     60 (83.3%)     0 (0.0%)     5 (4.0%)  107 (86.3%)
Same plan length                 12 (16.7%)   12 (16.7%)    12 (9.7%)    12 (9.7%)
Median plan length                        8           12           22           18
Total plan length                       648        1,003        6,407        5,084
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       3 (2%)
Writing the abstract task            1 (0%)       2 (1%)
Abstract search                   158 (64%)       3 (2%)
Unguided concrete search           85 (34%)    137 (77%)
Guided concrete search               0 (0%)     34 (19%)
Total                                   247          179
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   62 (75%)     95 (77%)
Refined, some actions off          14 (17%)     22 (18%)
Solved above the abstract plan       7 (8%)       7 (6%)
Total                                    83          124
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             60 (79%)     65 (56%)
5 to 9                              8 (11%)     19 (16%)
10 to 19                            8 (11%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    76          117
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
nomystery-sat11-strips              19         2         8         7        12
openstacks-sat08-strips             27         3         3        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         0         1         5        15
tpp                                 24         5         5         5        24
transport-sat08-strips              30         5         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        72        83       124       305
```
