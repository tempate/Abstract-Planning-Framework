# Benchmark report

2026-11-17 13:43 — experiments/ipc/opt/scaled/results.csv

398 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                     227 (57.0%)  270 (67.8%)
Timeouts                        170 (42.7%)  128 (32.2%)
Out of memory                      1 (0.3%)     0 (0.0%)
Others                             0 (0.0%)     0 (0.0%)
Total problems                          398          398
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                     209          209
Faster                           38 (18.2%)  171 (81.8%)
Found when the other did not             18           61
Median runtime                       8.30 s       2.87 s
Total runtime                   11,725.82 s  11,725.16 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length               209 (100.0%) 209 (100.0%)
Median plan length                       13           13
Total plan length                     5,006        5,006
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstraction                          6 (4%)
Guided concrete search             30 (18%)
Unguided concrete search          134 (79%)
Total                                   170
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                  149 (66%)
Refined, some actions off            3 (1%)
Solved above the abstract plan     75 (33%)
Total                                   227
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                               70 (46%)
1 to 4                             61 (40%)
5 to 9                             21 (14%)
10 to 19                             0 (0%)
20 or more                           0 (0%)
Total                                   152
```

## Plans found by domain

```
Domain (problems)                 Size    LMcutᵅ     LMcut
----------------------------------------------------------
airport (3)                     size-2         3         3
                                size-3         3         3
                                size-5         3         3
                               size-10         3         3
                               size-20         3         3
                               size-50         3         3
                              size-100         3         3
                              size-200         3         3
                              size-500         3         3
                             size-1000         3         3
depot (2)                       size-2         2         2
                                size-3         1         2
                                size-5         1         1
                               size-10         1         1
                               size-20         1         1
                               size-50         1         0
                              size-100         0         0
                              size-200         0         0
                              size-500         0         0
                             size-1000         0         0
driverlog (3)                   size-2         3         3
                                size-3         2         3
                                size-5         2         3
                               size-10         1         2
                               size-20         1         2
                               size-50         1         1
                              size-100         1         1
                              size-200         1         1
                              size-500         1         1
                             size-1000         1         1
gripper (3)                     size-4         1         1
                                size-5         1         1
                                size-6         1         1
                                size-8         1         1
                               size-10         0         3
                               size-20         0         0
                               size-50         0         0
                              size-100         0         0
                              size-200         0         0
                              size-500         0         0
                             size-1000         0         0
hiking-opt14-strips (3)         size-2         3         3
                                size-3         3         3
                                size-5         2         3
                               size-10         2         2
                               size-20         2         1
                               size-50         1         1
                              size-100         1         0
                              size-200         1         0
                              size-500         1         0
                             size-1000         0         0
logistics00 (3)                 size-2         3         3
                                size-3         3         3
                                size-5         2         3
                               size-10         2         3
                               size-20         2         2
                               size-50         2         1
                              size-100         2         1
                              size-200         2         1
                              size-500         2         1
                             size-1000         2         1
logistics98 (1)                 size-2         1         1
                                size-3         0         1
                                size-5         0         1
                               size-10         1         1
                               size-20         0         1
                               size-50         0         1
                              size-100         0         1
                              size-200         0         1
                              size-500         0         1
                             size-1000         0         1
miconic (1)                     size-2         1         1
                                size-3         1         1
                                size-5         0         1
                               size-10         0         1
                               size-20         0         1
                               size-50         0         1
                              size-100         0         1
                              size-200         0         1
                              size-500         0         0
                             size-1000         0         0
mprime (3)                      size-2         1         1
                                size-3         2         2
                                size-5         3         3
                               size-10         3         3
                               size-20         3         3
                               size-50         3         2
                              size-100         3         2
                              size-200         3         2
                              size-500         0         0
                             size-1000         0         0
mystery (2)                     size-2         1         1
                                size-3         1         1
                                size-5         2         2
                               size-10         2         2
                               size-20         2         2
                               size-50         2         2
                              size-100         2         2
                              size-200         2         2
                              size-500         2         2
                             size-1000         2         2
nomystery-opt11-strips (2)      size-2         2         2
                                size-3         2         2
                                size-5         2         2
                               size-10         0         2
                               size-20         0         2
                               size-50         0         2
                              size-100         0         2
                              size-200         0         2
                              size-500         0         0
                             size-1000         0         0
sokoban-opt08-strips (2)        size-2         2         2
                                size-3         2         2
                                size-5         2         2
                               size-10         2         2
                               size-20         2         2
                               size-50         2         2
                              size-100         2         2
                              size-200         2         2
                              size-500         2         2
                             size-1000         2         2
sokoban-opt11-strips (2)        size-2         2         2
                                size-3         2         2
                                size-5         2         2
                               size-10         2         2
                               size-20         2         2
                               size-50         2         2
                              size-100         2         2
                              size-200         2         2
                              size-500         2         2
                             size-1000         2         2
tpp (3)                         size-2         1         1
                                size-3         2         2
                                size-4         1         1
                                size-5         3         3
                               size-10         0         3
                               size-20         0         3
                               size-50         0         3
                              size-100         0         3
                              size-200         0         3
                              size-500         0         0
                             size-1000         0         0
transport-opt08-strips (3)      size-2         3         3
                                size-3         3         3
                                size-5         3         3
                               size-10         2         2
                               size-20         2         2
                               size-50         2         1
                              size-100         2         0
                              size-200         2         0
                              size-500         0         0
                             size-1000         0         0
transport-opt14-strips (1)      size-2         1         1
                                size-3         1         1
                                size-5         0         1
                               size-10         0         0
                               size-20         0         0
                               size-50         0         0
                              size-100         0         0
                              size-200         0         0
                              size-500         0         0
                             size-1000         0         0
visitall-opt11-strips (1)       size-2         1         1
                                size-3         1         1
                                size-5         1         1
                               size-10         1         1
                               size-20         0         1
                               size-50         0         0
                              size-100         0         0
                              size-200         0         0
                              size-500         0         0
                             size-1000         0         0
zenotravel (3)                  size-2         3         3
                                size-3         2         3
                                size-5         1         3
                               size-10         1         3
                               size-20         1         2
                               size-50         1         2
                              size-100         1         2
                              size-200         1         2
                              size-500         1         1
                             size-1000         1         1
Total (398)                                  227       270
```
