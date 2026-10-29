# Benchmark report

2026-10-29 09:35 — experiments/sat/resources/results.csv

330 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      89 (27.0%)   94 (28.5%)  127 (38.5%)  305 (92.4%)
Timeouts                        240 (72.7%)  236 (71.5%)  176 (53.3%)    22 (6.7%)
Out of memory                      1 (0.3%)     0 (0.0%)    27 (8.2%)     1 (0.3%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)     2 (0.6%)
Total problems                          330          330          330          330
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      85           85          127          127
Faster                           65 (76.5%)   20 (23.5%)     5 (3.9%)  122 (96.1%)
Found when the other did not              4            9            0          178
Median runtime                       7.11 s      11.15 s      13.26 s       3.15 s
Total runtime                    4,884.80 s   6,405.06 s   9,030.15 s     779.28 s
Shorter plan                     71 (83.5%)     5 (5.9%)     4 (3.1%)  112 (88.2%)
Same plan length                  9 (10.6%)    9 (10.6%)    11 (8.7%)    11 (8.7%)
Median plan length                        8           16           27           18
Total plan length                     1,238        1,865        6,518        5,158
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          3 (1%)       4 (2%)
Writing the abstract task            2 (1%)       1 (1%)
Abstract search                   129 (55%)       3 (2%)
Guided concrete search             32 (14%)     67 (38%)
Unguided concrete search           70 (30%)    101 (57%)
Total                                   236          176
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   55 (59%)     97 (76%)
Refined, some actions off          32 (34%)     22 (17%)
Solved above the abstract plan       7 (7%)       8 (6%)
Total                                    94          127
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             56 (64%)     69 (58%)
5 to 9                             16 (18%)     17 (14%)
10 to 19                           15 (17%)     14 (12%)
20 or more                           0 (0%)     19 (16%)
Total                                    87          119
```

## Plans found by domain

```
Domain                        Problems       ASP      ASPᵅ     LAMAᵅ      LAMA
------------------------------------------------------------------------------
data-network-sat18-strips           15         0         2         1        12
elevators-sat08-strips              30         2         8         9        30
elevators-sat11-strips              14         0         0         0        14
freecell                            73        16        13        10        72
mprime                              29        28        28        28        29
mystery                             26        17        17        17        17
nomystery-sat11-strips              19         4         3        10        12
openstacks-sat08-strips             27         5         6        24        27
openstacks-sat11-strips              7         0         0         4         7
thoughtful-sat14-strips             20         5         5         5        15
tpp                                 24         6         6         6        24
transport-sat08-strips              30         6         6        13        30
transport-sat11-strips              13         0         0         0        13
transport-sat14-strips               3         0         0         0         3
Total                              330        89        94       127       305
```
