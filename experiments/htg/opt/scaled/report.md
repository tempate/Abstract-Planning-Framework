# Benchmark report

2026-11-17 16:22 — experiments/htg/opt/scaled/results.csv

107 problems compared over abs-lmcut, lmcut

## Coverage

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found                      77 (72.0%)   54 (50.5%)
Timeouts                         25 (23.4%)   32 (29.9%)
Out of memory                      4 (3.7%)   21 (19.6%)
Others                             1 (0.9%)     0 (0.0%)
Total problems                          107          107
```

## Head to head, over the problems both solved

```
Metric                               LMcutᵅ        LMcut
--------------------------------------------------------
Plans found by both                      52           52
Faster                           34 (65.4%)   18 (34.6%)
Found when the other did not             25            2
Median runtime                      20.26 s      96.85 s
Total runtime                    4,413.95 s  13,663.72 s
Shorter plan                       0 (0.0%)     0 (0.0%)
Same plan length                52 (100.0%)  52 (100.0%)
Median plan length                       10           10
Total plan length                       440          440
```

## Where the timeouts died

```
Killed during                        LMcutᵅ
-------------------------------------------
Abstraction                         6 (24%)
Guided concrete search              5 (20%)
Unguided concrete search           14 (56%)
Total                                    25
```

## How the successes were solved

```
Solved by                            LMcutᵅ
-------------------------------------------
Refined directly                   72 (94%)
Refined, some actions off            0 (0%)
Solved above the abstract plan       5 (6%)
Total                                    77
```

## Deletes relaxed by the refined plans

```
Deletes relaxed                      LMcutᵅ
-------------------------------------------
None                                9 (12%)
1 to 4                             24 (33%)
5 to 9                               0 (0%)
10 to 19                           15 (21%)
20 or more                         24 (33%)
Total                                    72
```

## Plans found by domain

```
Domain (problems)                 Size    LMcutᵅ     LMcut
----------------------------------------------------------
blocksworld-large-simple/goal-3 (1)   size-96         1         1
                              size-100         1         1
                              size-200         1         1
                              size-500         1         1
                             size-1000         1         0
blocksworld-large-simple/goal-4 (1)   size-95         1         1
                              size-100         1         1
                              size-200         1         1
                              size-500         1         1
                             size-1000         1         0
blocksworld-large-simple/goal-5 (1)   size-94         1         1
                              size-100         1         1
                              size-200         1         1
                              size-500         1         1
                             size-1000         1         0
childsnack-contents/parsize1-cham3 (3)    size-3         3         3
                                size-5         3         2
                               size-10         3         2
                               size-20         2         2
                               size-50         2         0
                              size-100         2         0
                              size-200         2         0
                              size-500         2         0
                             size-1000         2         0
logistics-large-simple/goal-2 (1)  size-987         1         1
                             size-1000         1         1
logistics-large-simple/goal-3 (1)  size-986         1         1
                             size-1000         1         1
logistics-large-simple/goal-4 (1)  size-985         1         1
                             size-1000         1         1
organic-synthesis-alkene (3)    size-2         3         3
                                size-3         3         3
                                size-5         3         3
                               size-10         3         1
                               size-20         3         1
                               size-50         3         1
                              size-100         3         1
                              size-200         3         1
                              size-500         0         0
                             size-1000         0         0
rovers-large-simple/goal-2 (1)    size-2         1         1
                                size-3         1         1
                                size-5         1         1
                               size-10         1         1
                               size-20         1         1
                               size-50         1         1
                              size-100         1         1
                              size-200         1         1
                              size-500         1         1
                             size-1000         0         1
rovers-large-simple/goal-4 (2)    size-2         1         1
                                size-3         1         1
                                size-5         0         1
                               size-10         0         0
                               size-20         0         0
                               size-50         0         0
                              size-100         0         0
                              size-200         0         0
                              size-500         0         0
                             size-1000         0         0
Total (107)                                   77        54
```
