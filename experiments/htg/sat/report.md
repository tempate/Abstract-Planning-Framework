# Benchmark report

2026-11-10 17:24 — experiments/htg/sat/results.csv

12 problems compared over abs-asp, abs-lama, lama; 456 dropped as unfinished

## Coverage

```
Metric                                 ASPᵅ        LAMAᵅ         LAMA
---------------------------------------------------------------------
Plans found                        0 (0.0%)    2 (16.7%)    4 (33.3%)
Timeouts                          8 (66.7%)     1 (8.3%)     0 (0.0%)
Out of memory                     4 (33.3%)    9 (75.0%)    8 (66.7%)
Others                             0 (0.0%)     0 (0.0%)     0 (0.0%)
Total problems                           12           12           12
```

## Head to head, over the problems both solved

```
Metric                                LAMAᵅ         LAMA
--------------------------------------------------------
Plans found by both                       2            2
Faster                             0 (0.0%)   2 (100.0%)
Found when the other did not              0            2
Median runtime                     448.37 s     214.74 s
Total runtime                      896.74 s     429.48 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                 2 (100.0%)   2 (100.0%)
Median plan length                     30.5         30.5
Total plan length                        61           61
```

## Where the timeouts died

```
Killed during                          ASPᵅ        LAMAᵅ
--------------------------------------------------------
Abstract search                    8 (100%)     1 (100%)
Total                                     8            1
```

## How the successes were solved

```
Solved by                              ASPᵅ        LAMAᵅ
--------------------------------------------------------
Refined directly                          0     2 (100%)
Refined, some actions off                 0       0 (0%)
Solved above the abstract plan            0       0 (0%)
Total                                     0            2
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                        ASPᵅ        LAMAᵅ
--------------------------------------------------------
None                                      0      1 (50%)
1 to 4                                    0       0 (0%)
5 to 9                                    0       0 (0%)
10 to 19                                  0      1 (50%)
20 or more                                0       0 (0%)
Total                                     0            2
```

## Plans found by domain

```
Domain (problems)                 Size      ASPᵅ     LAMAᵅ      LAMA
--------------------------------------------------------------------
gnad-et-al-aaai19-large-instances (7)caldera-large         0         0         1
organic-synthesis-original (3)                   0         0         1
pipesworld-tankage-nosplit (2)                   0         2         2
Total (12)                                     0         2         4
```
