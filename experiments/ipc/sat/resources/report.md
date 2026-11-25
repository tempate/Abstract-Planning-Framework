# Benchmark report

2026-11-25 15:42 — experiments/ipc/sat/resources/results.csv

331 problems compared over asp, abs-asp, abs-lama, lama

## Coverage

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found                      88 (26.6%)   92 (27.8%)  120 (36.3%)  305 (92.1%)
Timeouts                        243 (73.4%)  231 (69.8%)  177 (53.5%)    23 (6.9%)
Out of memory                      0 (0.0%)     7 (2.1%)   33 (10.0%)     1 (0.3%)
Others                             0 (0.0%)     1 (0.3%)     1 (0.3%)     2 (0.6%)
Total problems                          331          331          331          331
```

## Head to head, over the problems both solved

```
Metric                                  ASP         ASPᵅ        LAMAᵅ         LAMA
----------------------------------------------------------------------------------
Plans found by both                      85           85          120          120
Faster                           51 (60.0%)   34 (40.0%)     3 (2.5%)  117 (97.5%)
Found when the other did not              3            7            0          185
Median runtime                       8.47 s       9.73 s       9.29 s       2.67 s
Total runtime                    6,559.83 s   3,458.56 s   6,233.27 s     523.64 s
Shorter plan                     34 (40.0%)   10 (11.8%)   14 (11.7%)   71 (59.2%)
Same plan length                 41 (48.2%)   41 (48.2%)   35 (29.2%)   35 (29.2%)
Median plan length                        8           13           20         17.5
Total plan length                     1,238        1,546        5,712        4,824
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstraction                          4 (2%)       4 (2%)
Abstract search                   136 (59%)       3 (2%)
Guided concrete search              20 (9%)     59 (33%)
Unguided concrete search           71 (31%)    111 (63%)
Total                                   231          177
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                   61 (66%)     92 (77%)
Refined, some actions off          24 (26%)     20 (17%)
Solved above the abstract plan       7 (8%)       8 (7%)
Total                                    92          120
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                 0 (0%)       0 (0%)
1 to 4                             28 (33%)     35 (31%)
5 to 9                             36 (42%)     37 (33%)
10 to 19                             7 (8%)     11 (10%)
20 or more                         14 (16%)     29 (26%)
Total                                    85          112
```

## Plans found by domain

```
Domain (problems)                  ASP      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
data-network-sat18-strips (15)         0         1         1        12
elevators-sat08-strips (30)          2         6         7        30
elevators-sat11-strips (14)          0         0         0        14
freecell (73)                       15        13        10        72
mprime (29)                         28        28        29        29
mystery (26)                        17        17        17        17
nomystery-sat11-strips (20)          4         4         4        12
openstacks-sat08-strips (27)         5         6        24        27
openstacks-sat11-strips (7)          0         0         4         7
thoughtful-sat14-strips (20)         5         5         5        15
tpp (24)                             6         6         6        24
transport-sat08-strips (30)          6         6        13        30
transport-sat11-strips (13)          0         0         0        13
transport-sat14-strips (3)           0         0         0         3
Total (331)                         88        92       120       305
```
