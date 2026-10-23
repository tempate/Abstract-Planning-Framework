# Benchmark report

2026-10-23 10:42 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-fd, fd

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   95 (28.8%)  125 (37.9%)  305 (92.4%)
Timeouts                        240 (72.7%)  235 (71.2%)  176 (53.3%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    29 (8.8%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      85           85          125          125
Faster                           60 (70.6%)   25 (29.4%)     7 (5.6%)  118 (94.4%)
Found when the other did not              4           10            0          180
Median runtime                       7.11 s       8.60 s      10.31 s       3.07 s
Total runtime                    4,884.80 s   5,970.55 s   7,512.80 s     728.91 s
Shorter plan                     70 (82.4%)     6 (7.1%)    10 (8.0%)  101 (80.8%)
Same plan length                  9 (10.6%)    9 (10.6%)   14 (11.2%)   14 (11.2%)
Median plan length                        8           16           23           18
Total plan length                     1,238        1,858        6,295        5,113
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       3 (2%)
Writing the abstract task            1 (0%)       1 (1%)
Abstract search                   129 (55%)       3 (2%)
Guided concrete search               1 (0%)     31 (18%)
Unguided concrete search          101 (43%)    138 (78%)
Total                                   235          176
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   56 (59%)     96 (77%)
Refined, some actions off          32 (34%)     21 (17%)
Solved above the abstract plan       7 (7%)       8 (6%)
Total                                    95          125
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             56 (64%)     65 (56%)
5 to 9                             17 (19%)     19 (16%)
10 to 19                           15 (17%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    88          117
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         1         1        12
elevators-sat08-strips              30         2         8        10        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        16        13        10        72
mprime                              29        28        28        28        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         4         5         7        12
openstacks-sat08-strips             27         5         6        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         5         5         5        15
tpp                                 24         6         6         6        24
transport-sat08-strips              30         6         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        89        95       125       305
```
