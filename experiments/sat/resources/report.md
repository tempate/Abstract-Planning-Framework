# Benchmark report

2026-10-28 11:24 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   93 (28.2%)  129 (39.1%)  305 (92.4%)
Timeouts                        240 (72.7%)  237 (71.8%)  172 (52.1%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    29 (8.8%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      82           82          129          129
Faster                           60 (73.2%)   22 (26.8%)     6 (4.7%)  123 (95.3%)
Found when the other did not              7           11            0          176
Median runtime                       6.27 s       8.57 s      13.97 s       3.14 s
Total runtime                    3,374.27 s   4,409.59 s  11,521.60 s     784.44 s
Shorter plan                     67 (81.7%)     7 (8.5%)    11 (8.5%)  104 (80.6%)
Same plan length                   8 (9.8%)     8 (9.8%)   14 (10.9%)   14 (10.9%)
Median plan length                        8           16           27           19
Total plan length                     1,156        1,669        6,427        5,233
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       3 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   129 (54%)       3 (2%)
Guided concrete search             39 (16%)     65 (38%)
Unguided concrete search           65 (27%)    100 (58%)
Total                                   237          172
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   56 (60%)     96 (74%)
Refined, some actions off          30 (32%)     24 (19%)
Solved above the abstract plan       7 (8%)       9 (7%)
Total                                    93          129
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             54 (63%)     68 (57%)
5 to 9                             17 (20%)     19 (16%)
10 to 19                           15 (17%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    86          120
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         2         1        12
elevators-sat08-strips              30         2         8        10        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        16        13        11        72
mprime                              29        28        28        28        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         4         2        10        12
openstacks-sat08-strips             27         5         6        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         5         5         5        15
tpp                                 24         6         6         6        24
transport-sat08-strips              30         6         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        89        93       129       305
```
