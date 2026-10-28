# Benchmark report

2026-10-28 11:22 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   91 (27.6%)  127 (38.5%)  305 (92.4%)
Timeouts                        240 (72.7%)  239 (72.4%)  174 (52.7%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    29 (8.8%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      81           81          127          127
Faster                           60 (74.1%)   21 (25.9%)     5 (3.9%)  122 (96.1%)
Found when the other did not              8           10            0          178
Median runtime                       6.17 s       8.60 s      14.21 s       3.15 s
Total runtime                    3,341.79 s   4,767.16 s  10,384.97 s     778.64 s
Shorter plan                     65 (80.2%)    9 (11.1%)    11 (8.7%)  100 (78.7%)
Same plan length                   7 (8.6%)     7 (8.6%)   16 (12.6%)   16 (12.6%)
Median plan length                        8           16           23           18
Total plan length                     1,124        1,619        6,346        5,170
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       3 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   130 (54%)       3 (2%)
Guided concrete search             36 (15%)     65 (37%)
Unguided concrete search           69 (29%)    102 (59%)
Total                                   239          174
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   56 (62%)     96 (76%)
Refined, some actions off          29 (32%)     24 (19%)
Solved above the abstract plan       6 (7%)       7 (6%)
Total                                    91          127
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             54 (64%)     68 (57%)
5 to 9                             16 (19%)     19 (16%)
10 to 19                           15 (18%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    85          120
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         2         1        12
elevators-sat08-strips              30         2         7        10        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        16        13        10        72
mprime                              29        28        28        28        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         4         2        10        12
openstacks-sat08-strips             27         5         6        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         5         5         5        15
tpp                                 24         6         5         5        24
transport-sat08-strips              30         6         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        89        91       127       305
```
