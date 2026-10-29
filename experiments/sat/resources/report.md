# Benchmark report

2026-10-29 09:35 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      72 (21.8%)   83 (25.2%)  125 (37.9%)  305 (92.4%)
Timeouts                        258 (78.2%)  247 (74.8%)  175 (53.0%)    22 (6.7%)
Out of memory                      0 (0.0%)     0 (0.0%)    30 (9.1%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      72           72          125          125
Faster                           45 (62.5%)   27 (37.5%)     7 (5.6%)  118 (94.4%)
Found when the other did not              0           11            0          180
Median runtime                       7.39 s       9.22 s      12.77 s       3.15 s
Total runtime                    6,180.44 s   2,633.98 s   6,403.35 s     773.04 s
Shorter plan                     62 (86.1%)     0 (0.0%)     5 (4.0%)  107 (85.6%)
Same plan length                 10 (13.9%)   10 (13.9%)   13 (10.4%)   13 (10.4%)
Median plan length                        8           12           23           18
Total plan length                       648          994        6,278        5,054
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       4 (2%)
Writing the abstract task            2 (1%)       1 (1%)
Abstract search                   157 (64%)       3 (2%)
Guided concrete search               4 (2%)     67 (38%)
Unguided concrete search           81 (33%)    100 (57%)
Total                                   247          175
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   62 (75%)     95 (76%)
Refined, some actions off          14 (17%)     23 (18%)
Solved above the abstract plan       7 (8%)       7 (6%)
Total                                    83          125
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             60 (79%)     67 (57%)
5 to 9                              8 (11%)     18 (15%)
10 to 19                            8 (11%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    76          118
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         1         1        12
elevators-sat08-strips              30         1         3         9        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        10        10        10        72
mprime                              29        29        29        28        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         2         8        10        12
openstacks-sat08-strips             27         3         3        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         0         1         5        15
tpp                                 24         5         5         5        24
transport-sat08-strips              30         5         6        12        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        72        83       125       305
```
