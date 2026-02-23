begin_version
3
end_version
begin_metric
1
end_metric
30
begin_variable
var0
-1
2
Atom started()
NegatedAtom started()
end_variable
begin_variable
var1
-1
2
Atom size(jig0002, n09)
Atom size(jig0002, n18)
end_variable
begin_variable
var2
-1
2
Atom size(jig0001, n18)
Atom size(jig0001, n25)
end_variable
begin_variable
var3
-1
2
Atom to_deliver(dummy-jig, pl0)
Atom to_deliver(jig0002, pl0)
end_variable
begin_variable
var4
-1
2
Atom empty(hangar1)
NegatedAtom empty(hangar1)
end_variable
begin_variable
var5
-1
2
Atom empty(hangar2)
NegatedAtom empty(hangar2)
end_variable
begin_variable
var6
-1
2
Atom to_deliver(dummy-jig, pl1)
Atom to_deliver(jig0001, pl1)
end_variable
begin_variable
var7
-1
2
Atom empty(hangar3)
NegatedAtom empty(hangar3)
end_variable
begin_variable
var8
-1
2
Atom empty(rack00)
NegatedAtom empty(rack00)
end_variable
begin_variable
var9
-1
3
Atom free-space(rack00, n04)
Atom free-space(rack00, n13)
Atom free-space(rack00, n22)
end_variable
begin_variable
var10
-1
2
Atom empty(beluga_trailer_1)
NegatedAtom empty(beluga_trailer_1)
end_variable
begin_variable
var11
-1
2
Atom empty(beluga_trailer_2)
NegatedAtom empty(beluga_trailer_2)
end_variable
begin_variable
var12
-1
2
Atom empty(beluga_trailer_3)
NegatedAtom empty(beluga_trailer_3)
end_variable
begin_variable
var13
-1
2
Atom empty(factory_trailer_1)
NegatedAtom empty(factory_trailer_1)
end_variable
begin_variable
var14
-1
2
Atom empty(factory_trailer_2)
NegatedAtom empty(factory_trailer_2)
end_variable
begin_variable
var15
-1
2
Atom next_to(jig0001, jig0002, bside)
NegatedAtom next_to(jig0001, jig0002, bside)
end_variable
begin_variable
var16
-1
2
Atom next_to(jig0002, jig0001, fside)
NegatedAtom next_to(jig0002, jig0001, fside)
end_variable
begin_variable
var17
-1
10
Atom in(jig0001, beluga_trailer_1)
Atom in(jig0001, beluga_trailer_2)
Atom in(jig0001, beluga_trailer_3)
Atom in(jig0001, factory_trailer_1)
Atom in(jig0001, factory_trailer_2)
Atom in(jig0001, hangar1)
Atom in(jig0001, hangar2)
Atom in(jig0001, hangar3)
Atom in(jig0001, rack00)
Atom in(jig0001, rack01)
end_variable
begin_variable
var18
-1
2
Atom clear(jig0001, fside)
NegatedAtom clear(jig0001, fside)
end_variable
begin_variable
var19
-1
2
Atom next_to(jig0001, jig0002, fside)
NegatedAtom next_to(jig0001, jig0002, fside)
end_variable
begin_variable
var20
-1
2
Atom next_to(jig0002, jig0001, bside)
NegatedAtom next_to(jig0002, jig0001, bside)
end_variable
begin_variable
var21
-1
2
Atom clear(jig0001, bside)
NegatedAtom clear(jig0001, bside)
end_variable
begin_variable
var22
-1
2
Atom empty(rack01)
NegatedAtom empty(rack01)
end_variable
begin_variable
var23
-1
2
Atom clear(jig0002, fside)
NegatedAtom clear(jig0002, fside)
end_variable
begin_variable
var24
-1
11
Atom in(jig0002, beluga1)
Atom in(jig0002, beluga_trailer_1)
Atom in(jig0002, beluga_trailer_2)
Atom in(jig0002, beluga_trailer_3)
Atom in(jig0002, factory_trailer_1)
Atom in(jig0002, factory_trailer_2)
Atom in(jig0002, hangar1)
Atom in(jig0002, hangar2)
Atom in(jig0002, hangar3)
Atom in(jig0002, rack00)
Atom in(jig0002, rack01)
end_variable
begin_variable
var25
-1
7
Atom free-space(rack01, n04)
Atom free-space(rack01, n06)
Atom free-space(rack01, n13)
Atom free-space(rack01, n15)
Atom free-space(rack01, n22)
Atom free-space(rack01, n31)
Atom free-space(rack01, n40)
end_variable
begin_variable
var26
-1
2
Atom clear(jig0002, bside)
NegatedAtom clear(jig0002, bside)
end_variable
begin_variable
var27
-1
2
Atom to_unload(dummy-jig, beluga1)
Atom to_unload(jig0002, beluga1)
end_variable
begin_variable
var28
-1
2
Atom empty(jig0002)
NegatedAtom empty(jig0002)
end_variable
begin_variable
var29
-1
2
Atom empty(jig0001)
NegatedAtom empty(jig0001)
end_variable
0
begin_state
1
1
1
1
0
0
1
0
0
2
0
0
0
0
0
1
1
9
0
1
1
0
1
1
0
3
1
1
1
1
end_state
begin_goal
3
27 0
28 0
29 0
end_goal
380
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_1 hangar1 pl1 n18 n18
2
2 0
0 0
5
0 13 -1 0
0 4 0 1
0 29 -1 0
0 17 3 5
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_1 hangar1 pl1 n25 n18
1
0 0
6
0 13 -1 0
0 4 0 1
0 29 -1 0
0 17 3 5
0 2 1 0
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_1 hangar2 pl1 n18 n18
2
2 0
0 0
5
0 13 -1 0
0 5 0 1
0 29 -1 0
0 17 3 6
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_1 hangar2 pl1 n25 n18
1
0 0
6
0 13 -1 0
0 5 0 1
0 29 -1 0
0 17 3 6
0 2 1 0
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_1 hangar3 pl1 n18 n18
2
2 0
0 0
5
0 13 -1 0
0 7 0 1
0 29 -1 0
0 17 3 7
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_1 hangar3 pl1 n25 n18
1
0 0
6
0 13 -1 0
0 7 0 1
0 29 -1 0
0 17 3 7
0 2 1 0
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_2 hangar1 pl1 n18 n18
2
2 0
0 0
5
0 14 -1 0
0 4 0 1
0 29 -1 0
0 17 4 5
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_2 hangar1 pl1 n25 n18
1
0 0
6
0 14 -1 0
0 4 0 1
0 29 -1 0
0 17 4 5
0 2 1 0
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_2 hangar2 pl1 n18 n18
2
2 0
0 0
5
0 14 -1 0
0 5 0 1
0 29 -1 0
0 17 4 6
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_2 hangar2 pl1 n25 n18
1
0 0
6
0 14 -1 0
0 5 0 1
0 29 -1 0
0 17 4 6
0 2 1 0
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_2 hangar3 pl1 n18 n18
2
2 0
0 0
5
0 14 -1 0
0 7 0 1
0 29 -1 0
0 17 4 7
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0001 dummy-jig factory_trailer_2 hangar3 pl1 n25 n18
1
0 0
6
0 14 -1 0
0 7 0 1
0 29 -1 0
0 17 4 7
0 2 1 0
0 6 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_1 hangar1 pl0 n09 n09
2
1 0
0 0
5
0 13 -1 0
0 4 0 1
0 28 -1 0
0 24 4 6
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_1 hangar1 pl0 n18 n09
1
0 0
6
0 13 -1 0
0 4 0 1
0 28 -1 0
0 24 4 6
0 1 1 0
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_1 hangar2 pl0 n09 n09
2
1 0
0 0
5
0 13 -1 0
0 5 0 1
0 28 -1 0
0 24 4 7
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_1 hangar2 pl0 n18 n09
1
0 0
6
0 13 -1 0
0 5 0 1
0 28 -1 0
0 24 4 7
0 1 1 0
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_1 hangar3 pl0 n09 n09
2
1 0
0 0
5
0 13 -1 0
0 7 0 1
0 28 -1 0
0 24 4 8
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_1 hangar3 pl0 n18 n09
1
0 0
6
0 13 -1 0
0 7 0 1
0 28 -1 0
0 24 4 8
0 1 1 0
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_2 hangar1 pl0 n09 n09
2
1 0
0 0
5
0 14 -1 0
0 4 0 1
0 28 -1 0
0 24 5 6
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_2 hangar1 pl0 n18 n09
1
0 0
6
0 14 -1 0
0 4 0 1
0 28 -1 0
0 24 5 6
0 1 1 0
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_2 hangar2 pl0 n09 n09
2
1 0
0 0
5
0 14 -1 0
0 5 0 1
0 28 -1 0
0 24 5 7
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_2 hangar2 pl0 n18 n09
1
0 0
6
0 14 -1 0
0 5 0 1
0 28 -1 0
0 24 5 7
0 1 1 0
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_2 hangar3 pl0 n09 n09
2
1 0
0 0
5
0 14 -1 0
0 7 0 1
0 28 -1 0
0 24 5 8
0 3 1 0
1
end_operator
begin_operator
deliver_to_hangar jig0002 dummy-jig factory_trailer_2 hangar3 pl0 n18 n09
1
0 0
6
0 14 -1 0
0 7 0 1
0 28 -1 0
0 24 5 8
0 1 1 0
0 3 1 0
1
end_operator
begin_operator
get_from_hangar jig0001 hangar1 factory_trailer_1
1
0 0
3
0 13 0 1
0 4 -1 0
0 17 5 3
1
end_operator
begin_operator
get_from_hangar jig0001 hangar1 factory_trailer_2
1
0 0
3
0 14 0 1
0 4 -1 0
0 17 5 4
1
end_operator
begin_operator
get_from_hangar jig0001 hangar2 factory_trailer_1
1
0 0
3
0 13 0 1
0 5 -1 0
0 17 6 3
1
end_operator
begin_operator
get_from_hangar jig0001 hangar2 factory_trailer_2
1
0 0
3
0 14 0 1
0 5 -1 0
0 17 6 4
1
end_operator
begin_operator
get_from_hangar jig0001 hangar3 factory_trailer_1
1
0 0
3
0 13 0 1
0 7 -1 0
0 17 7 3
1
end_operator
begin_operator
get_from_hangar jig0001 hangar3 factory_trailer_2
1
0 0
3
0 14 0 1
0 7 -1 0
0 17 7 4
1
end_operator
begin_operator
get_from_hangar jig0002 hangar1 factory_trailer_1
1
0 0
3
0 13 0 1
0 4 -1 0
0 24 6 4
1
end_operator
begin_operator
get_from_hangar jig0002 hangar1 factory_trailer_2
1
0 0
3
0 14 0 1
0 4 -1 0
0 24 6 5
1
end_operator
begin_operator
get_from_hangar jig0002 hangar2 factory_trailer_1
1
0 0
3
0 13 0 1
0 5 -1 0
0 24 7 4
1
end_operator
begin_operator
get_from_hangar jig0002 hangar2 factory_trailer_2
1
0 0
3
0 14 0 1
0 5 -1 0
0 24 7 5
1
end_operator
begin_operator
get_from_hangar jig0002 hangar3 factory_trailer_1
1
0 0
3
0 13 0 1
0 7 -1 0
0 24 8 4
1
end_operator
begin_operator
get_from_hangar jig0002 hangar3 factory_trailer_2
1
0 0
3
0 14 0 1
0 7 -1 0
0 24 8 5
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_1 rack00 bside fside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 10 0 1
0 8 -1 0
0 9 0 2
0 17 8 0
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_1 rack01 bside fside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 10 0 1
0 22 -1 0
0 25 0 4
0 17 9 0
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_1 rack01 bside fside n18 n13 n31
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 10 0 1
0 22 -1 0
0 25 2 5
0 17 9 0
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_1 rack01 bside fside n18 n22 n40
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 10 0 1
0 22 -1 0
0 25 4 6
0 17 9 0
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_1 rack01 bside fside n25 n06 n31
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 10 0 1
0 22 -1 0
0 25 1 5
0 17 9 0
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_1 rack01 bside fside n25 n15 n40
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 10 0 1
0 22 -1 0
0 25 3 6
0 17 9 0
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_2 rack00 bside fside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 11 0 1
0 8 -1 0
0 9 0 2
0 17 8 1
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_2 rack01 bside fside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 11 0 1
0 22 -1 0
0 25 0 4
0 17 9 1
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_2 rack01 bside fside n18 n13 n31
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 11 0 1
0 22 -1 0
0 25 2 5
0 17 9 1
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_2 rack01 bside fside n18 n22 n40
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 11 0 1
0 22 -1 0
0 25 4 6
0 17 9 1
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_2 rack01 bside fside n25 n06 n31
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 11 0 1
0 22 -1 0
0 25 1 5
0 17 9 1
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_2 rack01 bside fside n25 n15 n40
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 11 0 1
0 22 -1 0
0 25 3 6
0 17 9 1
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_3 rack00 bside fside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 12 0 1
0 8 -1 0
0 9 0 2
0 17 8 2
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_3 rack01 bside fside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 12 0 1
0 22 -1 0
0 25 0 4
0 17 9 2
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_3 rack01 bside fside n18 n13 n31
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 12 0 1
0 22 -1 0
0 25 2 5
0 17 9 2
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_3 rack01 bside fside n18 n22 n40
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 12 0 1
0 22 -1 0
0 25 4 6
0 17 9 2
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_3 rack01 bside fside n25 n06 n31
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 12 0 1
0 22 -1 0
0 25 1 5
0 17 9 2
1
end_operator
begin_operator
pick_up_rack jig0001 beluga_trailer_3 rack01 bside fside n25 n15 n40
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 12 0 1
0 22 -1 0
0 25 3 6
0 17 9 2
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_1 rack00 fside bside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 13 0 1
0 8 -1 0
0 9 0 2
0 17 8 3
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_1 rack01 fside bside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 13 0 1
0 22 -1 0
0 25 0 4
0 17 9 3
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_1 rack01 fside bside n18 n13 n31
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 13 0 1
0 22 -1 0
0 25 2 5
0 17 9 3
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_1 rack01 fside bside n18 n22 n40
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 13 0 1
0 22 -1 0
0 25 4 6
0 17 9 3
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_1 rack01 fside bside n25 n06 n31
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 13 0 1
0 22 -1 0
0 25 1 5
0 17 9 3
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_1 rack01 fside bside n25 n15 n40
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 13 0 1
0 22 -1 0
0 25 3 6
0 17 9 3
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_2 rack00 fside bside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 14 0 1
0 8 -1 0
0 9 0 2
0 17 8 4
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_2 rack01 fside bside n18 n04 n22
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 14 0 1
0 22 -1 0
0 25 0 4
0 17 9 4
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_2 rack01 fside bside n18 n13 n31
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 14 0 1
0 22 -1 0
0 25 2 5
0 17 9 4
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_2 rack01 fside bside n18 n22 n40
2
2 0
0 0
6
0 21 0 1
0 18 0 1
0 14 0 1
0 22 -1 0
0 25 4 6
0 17 9 4
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_2 rack01 fside bside n25 n06 n31
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 14 0 1
0 22 -1 0
0 25 1 5
0 17 9 4
1
end_operator
begin_operator
pick_up_rack jig0001 factory_trailer_2 rack01 fside bside n25 n15 n40
2
2 1
0 0
6
0 21 0 1
0 18 0 1
0 14 0 1
0 22 -1 0
0 25 3 6
0 17 9 4
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack00 bside fside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 8 -1 0
0 9 0 1
0 24 9 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack00 bside fside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 8 -1 0
0 9 1 2
0 24 9 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack00 bside fside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 8 -1 0
0 9 0 2
0 24 9 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 0 2
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n09 n06 n15
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 1 3
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 2 4
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n09 n22 n31
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 4 5
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n09 n31 n40
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 5 6
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 0 4
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n18 n13 n31
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 2 5
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_1 rack01 bside fside n18 n22 n40
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 10 0 1
0 22 -1 0
0 25 4 6
0 24 10 1
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack00 bside fside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 8 -1 0
0 9 0 1
0 24 9 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack00 bside fside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 8 -1 0
0 9 1 2
0 24 9 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack00 bside fside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 8 -1 0
0 9 0 2
0 24 9 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 0 2
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n09 n06 n15
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 1 3
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 2 4
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n09 n22 n31
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 4 5
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n09 n31 n40
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 5 6
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 0 4
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n18 n13 n31
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 2 5
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_2 rack01 bside fside n18 n22 n40
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 11 0 1
0 22 -1 0
0 25 4 6
0 24 10 2
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack00 bside fside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 8 -1 0
0 9 0 1
0 24 9 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack00 bside fside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 8 -1 0
0 9 1 2
0 24 9 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack00 bside fside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 8 -1 0
0 9 0 2
0 24 9 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 0 2
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n09 n06 n15
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 1 3
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 2 4
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n09 n22 n31
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 4 5
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n09 n31 n40
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 5 6
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 0 4
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n18 n13 n31
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 2 5
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 beluga_trailer_3 rack01 bside fside n18 n22 n40
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 12 0 1
0 22 -1 0
0 25 4 6
0 24 10 3
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack00 fside bside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 8 -1 0
0 9 0 1
0 24 9 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack00 fside bside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 8 -1 0
0 9 1 2
0 24 9 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack00 fside bside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 8 -1 0
0 9 0 2
0 24 9 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 0 2
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n09 n06 n15
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 1 3
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 2 4
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n09 n22 n31
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 4 5
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n09 n31 n40
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 5 6
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 0 4
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n18 n13 n31
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 2 5
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_1 rack01 fside bside n18 n22 n40
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 13 0 1
0 22 -1 0
0 25 4 6
0 24 10 4
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack00 fside bside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 8 -1 0
0 9 0 1
0 24 9 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack00 fside bside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 8 -1 0
0 9 1 2
0 24 9 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack00 fside bside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 8 -1 0
0 9 0 2
0 24 9 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n09 n04 n13
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 0 2
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n09 n06 n15
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 1 3
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n09 n13 n22
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 2 4
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n09 n22 n31
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 4 5
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n09 n31 n40
2
1 0
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 5 6
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n18 n04 n22
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 0 4
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n18 n13 n31
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 2 5
0 24 10 5
1
end_operator
begin_operator
pick_up_rack jig0002 factory_trailer_2 rack01 fside bside n18 n22 n40
2
1 1
0 0
6
0 26 0 1
0 23 0 1
0 14 0 1
0 22 -1 0
0 25 4 6
0 24 10 5
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_1 rack00 bside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 10 -1 0
0 8 0 1
0 9 2 0
0 17 0 8
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_1 rack01 bside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 10 -1 0
0 22 0 1
0 25 4 0
0 17 0 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_1 rack01 bside n18 n31 n13
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 10 -1 0
0 22 0 1
0 25 5 2
0 17 0 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_1 rack01 bside n18 n40 n22
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 10 -1 0
0 22 0 1
0 25 6 4
0 17 0 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_1 rack01 bside n25 n31 n06
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 10 -1 0
0 22 0 1
0 25 5 1
0 17 0 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_1 rack01 bside n25 n40 n15
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 10 -1 0
0 22 0 1
0 25 6 3
0 17 0 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_2 rack00 bside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 11 -1 0
0 8 0 1
0 9 2 0
0 17 1 8
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_2 rack01 bside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 11 -1 0
0 22 0 1
0 25 4 0
0 17 1 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_2 rack01 bside n18 n31 n13
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 11 -1 0
0 22 0 1
0 25 5 2
0 17 1 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_2 rack01 bside n18 n40 n22
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 11 -1 0
0 22 0 1
0 25 6 4
0 17 1 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_2 rack01 bside n25 n31 n06
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 11 -1 0
0 22 0 1
0 25 5 1
0 17 1 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_2 rack01 bside n25 n40 n15
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 11 -1 0
0 22 0 1
0 25 6 3
0 17 1 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_3 rack00 bside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 12 -1 0
0 8 0 1
0 9 2 0
0 17 2 8
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_3 rack01 bside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 12 -1 0
0 22 0 1
0 25 4 0
0 17 2 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_3 rack01 bside n18 n31 n13
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 12 -1 0
0 22 0 1
0 25 5 2
0 17 2 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_3 rack01 bside n18 n40 n22
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 12 -1 0
0 22 0 1
0 25 6 4
0 17 2 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_3 rack01 bside n25 n31 n06
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 12 -1 0
0 22 0 1
0 25 5 1
0 17 2 9
1
end_operator
begin_operator
put_down_rack jig0001 beluga_trailer_3 rack01 bside n25 n40 n15
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 12 -1 0
0 22 0 1
0 25 6 3
0 17 2 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_1 rack00 fside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 13 -1 0
0 8 0 1
0 9 2 0
0 17 3 8
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_1 rack01 fside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 13 -1 0
0 22 0 1
0 25 4 0
0 17 3 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_1 rack01 fside n18 n31 n13
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 13 -1 0
0 22 0 1
0 25 5 2
0 17 3 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_1 rack01 fside n18 n40 n22
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 13 -1 0
0 22 0 1
0 25 6 4
0 17 3 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_1 rack01 fside n25 n31 n06
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 13 -1 0
0 22 0 1
0 25 5 1
0 17 3 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_1 rack01 fside n25 n40 n15
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 13 -1 0
0 22 0 1
0 25 6 3
0 17 3 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_2 rack00 fside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 14 -1 0
0 8 0 1
0 9 2 0
0 17 4 8
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_2 rack01 fside n18 n22 n04
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 14 -1 0
0 22 0 1
0 25 4 0
0 17 4 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_2 rack01 fside n18 n31 n13
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 14 -1 0
0 22 0 1
0 25 5 2
0 17 4 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_2 rack01 fside n18 n40 n22
2
2 0
0 0
6
0 21 -1 0
0 18 -1 0
0 14 -1 0
0 22 0 1
0 25 6 4
0 17 4 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_2 rack01 fside n25 n31 n06
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 14 -1 0
0 22 0 1
0 25 5 1
0 17 4 9
1
end_operator
begin_operator
put_down_rack jig0001 factory_trailer_2 rack01 fside n25 n40 n15
2
2 1
0 0
6
0 21 -1 0
0 18 -1 0
0 14 -1 0
0 22 0 1
0 25 6 3
0 17 4 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack00 bside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 8 0 1
0 9 1 0
0 24 1 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack00 bside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 8 0 1
0 9 2 1
0 24 1 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack00 bside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 8 0 1
0 9 2 0
0 24 1 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 2 0
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n09 n15 n06
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 3 1
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 4 2
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n09 n31 n22
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 5 4
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n09 n40 n31
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 6 5
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 4 0
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n18 n31 n13
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 5 2
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_1 rack01 bside n18 n40 n22
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 10 -1 0
0 22 0 1
0 25 6 4
0 24 1 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack00 bside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 8 0 1
0 9 1 0
0 24 2 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack00 bside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 8 0 1
0 9 2 1
0 24 2 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack00 bside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 8 0 1
0 9 2 0
0 24 2 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 2 0
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n09 n15 n06
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 3 1
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 4 2
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n09 n31 n22
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 5 4
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n09 n40 n31
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 6 5
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 4 0
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n18 n31 n13
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 5 2
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_2 rack01 bside n18 n40 n22
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 11 -1 0
0 22 0 1
0 25 6 4
0 24 2 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack00 bside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 8 0 1
0 9 1 0
0 24 3 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack00 bside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 8 0 1
0 9 2 1
0 24 3 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack00 bside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 8 0 1
0 9 2 0
0 24 3 9
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 2 0
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n09 n15 n06
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 3 1
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 4 2
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n09 n31 n22
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 5 4
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n09 n40 n31
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 6 5
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 4 0
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n18 n31 n13
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 5 2
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 beluga_trailer_3 rack01 bside n18 n40 n22
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 12 -1 0
0 22 0 1
0 25 6 4
0 24 3 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack00 fside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 8 0 1
0 9 1 0
0 24 4 9
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack00 fside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 8 0 1
0 9 2 1
0 24 4 9
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack00 fside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 8 0 1
0 9 2 0
0 24 4 9
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 2 0
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n09 n15 n06
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 3 1
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 4 2
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n09 n31 n22
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 5 4
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n09 n40 n31
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 6 5
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 4 0
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n18 n31 n13
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 5 2
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_1 rack01 fside n18 n40 n22
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 13 -1 0
0 22 0 1
0 25 6 4
0 24 4 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack00 fside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 8 0 1
0 9 1 0
0 24 5 9
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack00 fside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 8 0 1
0 9 2 1
0 24 5 9
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack00 fside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 8 0 1
0 9 2 0
0 24 5 9
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n09 n13 n04
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 2 0
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n09 n15 n06
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 3 1
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n09 n22 n13
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 4 2
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n09 n31 n22
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 5 4
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n09 n40 n31
2
1 0
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 6 5
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n18 n22 n04
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 4 0
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n18 n31 n13
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 5 2
0 24 5 10
1
end_operator
begin_operator
put_down_rack jig0002 factory_trailer_2 rack01 fside n18 n40 n22
2
1 1
0 0
6
0 26 -1 0
0 23 -1 0
0 14 -1 0
0 22 0 1
0 25 6 4
0 24 5 10
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_1 rack00 bside fside n18 n22 n04
3
24 9
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 10 -1 0
0 9 2 0
0 17 0 8
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n18 n22 n04
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 10 -1 0
0 25 4 0
0 17 0 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n18 n31 n13
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 10 -1 0
0 25 5 2
0 17 0 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n18 n40 n22
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 10 -1 0
0 25 6 4
0 17 0 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n25 n31 n06
3
24 10
2 1
0 0
7
0 21 -1 0
0 26 0 1
0 10 -1 0
0 25 5 1
0 17 0 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n25 n40 n15
3
24 10
2 1
0 0
7
0 21 -1 0
0 26 0 1
0 10 -1 0
0 25 6 3
0 17 0 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_2 rack00 bside fside n18 n22 n04
3
24 9
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 11 -1 0
0 9 2 0
0 17 1 8
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n18 n22 n04
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 11 -1 0
0 25 4 0
0 17 1 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n18 n31 n13
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 11 -1 0
0 25 5 2
0 17 1 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n18 n40 n22
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 11 -1 0
0 25 6 4
0 17 1 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n25 n31 n06
3
24 10
2 1
0 0
7
0 21 -1 0
0 26 0 1
0 11 -1 0
0 25 5 1
0 17 1 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n25 n40 n15
3
24 10
2 1
0 0
7
0 21 -1 0
0 26 0 1
0 11 -1 0
0 25 6 3
0 17 1 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_3 rack00 bside fside n18 n22 n04
3
24 9
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 12 -1 0
0 9 2 0
0 17 2 8
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n18 n22 n04
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 12 -1 0
0 25 4 0
0 17 2 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n18 n31 n13
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 12 -1 0
0 25 5 2
0 17 2 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n18 n40 n22
3
24 10
2 0
0 0
7
0 21 -1 0
0 26 0 1
0 12 -1 0
0 25 6 4
0 17 2 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n25 n31 n06
3
24 10
2 1
0 0
7
0 21 -1 0
0 26 0 1
0 12 -1 0
0 25 5 1
0 17 2 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n25 n40 n15
3
24 10
2 1
0 0
7
0 21 -1 0
0 26 0 1
0 12 -1 0
0 25 6 3
0 17 2 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_1 rack00 fside bside n18 n22 n04
3
24 9
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 13 -1 0
0 9 2 0
0 17 3 8
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n22 n04
3
24 10
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 13 -1 0
0 25 4 0
0 17 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n31 n13
3
24 10
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 13 -1 0
0 25 5 2
0 17 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n40 n22
3
24 10
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 13 -1 0
0 25 6 4
0 17 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n31 n06
3
24 10
2 1
0 0
7
0 18 -1 0
0 23 0 1
0 13 -1 0
0 25 5 1
0 17 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n40 n15
3
24 10
2 1
0 0
7
0 18 -1 0
0 23 0 1
0 13 -1 0
0 25 6 3
0 17 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_2 rack00 fside bside n18 n22 n04
3
24 9
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 14 -1 0
0 9 2 0
0 17 4 8
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n22 n04
3
24 10
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 14 -1 0
0 25 4 0
0 17 4 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n31 n13
3
24 10
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 14 -1 0
0 25 5 2
0 17 4 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n40 n22
3
24 10
2 0
0 0
7
0 18 -1 0
0 23 0 1
0 14 -1 0
0 25 6 4
0 17 4 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n31 n06
3
24 10
2 1
0 0
7
0 18 -1 0
0 23 0 1
0 14 -1 0
0 25 5 1
0 17 4 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n40 n15
3
24 10
2 1
0 0
7
0 18 -1 0
0 23 0 1
0 14 -1 0
0 25 6 3
0 17 4 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack00 bside fside n09 n13 n04
3
17 8
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 9 1 0
0 24 1 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack00 bside fside n09 n22 n13
3
17 8
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 9 2 1
0 24 1 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack00 bside fside n18 n22 n04
3
17 8
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 9 2 0
0 24 1 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n13 n04
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 2 0
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n15 n06
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 3 1
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n22 n13
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 4 2
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n31 n22
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 5 4
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n40 n31
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 6 5
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n18 n22 n04
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 4 0
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n18 n31 n13
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 5 2
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n18 n40 n22
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 10 -1 0
0 25 6 4
0 24 1 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack00 bside fside n09 n13 n04
3
17 8
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 9 1 0
0 24 2 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack00 bside fside n09 n22 n13
3
17 8
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 9 2 1
0 24 2 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack00 bside fside n18 n22 n04
3
17 8
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 9 2 0
0 24 2 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n13 n04
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 2 0
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n15 n06
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 3 1
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n22 n13
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 4 2
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n31 n22
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 5 4
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n40 n31
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 6 5
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n18 n22 n04
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 4 0
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n18 n31 n13
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 5 2
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n18 n40 n22
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 11 -1 0
0 25 6 4
0 24 2 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack00 bside fside n09 n13 n04
3
17 8
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 9 1 0
0 24 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack00 bside fside n09 n22 n13
3
17 8
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 9 2 1
0 24 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack00 bside fside n18 n22 n04
3
17 8
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 9 2 0
0 24 3 9
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n13 n04
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 2 0
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n15 n06
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 3 1
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n22 n13
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 4 2
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n31 n22
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 5 4
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n40 n31
3
17 9
1 0
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 6 5
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n18 n22 n04
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 4 0
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n18 n31 n13
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 5 2
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n18 n40 n22
3
17 9
1 1
0 0
7
0 21 0 1
0 26 -1 0
0 12 -1 0
0 25 6 4
0 24 3 10
0 19 -1 0
0 20 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n13 n04
3
17 8
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 9 1 0
0 24 4 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n22 n13
3
17 8
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 9 2 1
0 24 4 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n18 n22 n04
3
17 8
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 9 2 0
0 24 4 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n13 n04
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 2 0
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n15 n06
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 3 1
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n22 n13
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 4 2
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n31 n22
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 5 4
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n40 n31
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 6 5
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n22 n04
3
17 9
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 4 0
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n31 n13
3
17 9
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 5 2
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n40 n22
3
17 9
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 13 -1 0
0 25 6 4
0 24 4 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n13 n04
3
17 8
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 9 1 0
0 24 5 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n22 n13
3
17 8
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 9 2 1
0 24 5 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n18 n22 n04
3
17 8
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 9 2 0
0 24 5 9
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n13 n04
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 2 0
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n15 n06
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 3 1
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n22 n13
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 4 2
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n31 n22
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 5 4
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n40 n31
3
17 9
1 0
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 6 5
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n22 n04
3
17 9
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 4 0
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n31 n13
3
17 9
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 5 2
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
stack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n40 n22
3
17 9
1 1
0 0
7
0 18 0 1
0 23 -1 0
0 14 -1 0
0 25 6 4
0 24 5 10
0 15 -1 0
0 16 -1 0
1
end_operator
begin_operator
start_ 
0
1
0 0 1 0
0
end_operator
begin_operator
unload_beluga jig0002 dummy-jig beluga_trailer_1 beluga1
1
0 0
3
0 10 0 1
0 24 0 1
0 27 1 0
1
end_operator
begin_operator
unload_beluga jig0002 dummy-jig beluga_trailer_2 beluga1
1
0 0
3
0 11 0 1
0 24 0 2
0 27 1 0
1
end_operator
begin_operator
unload_beluga jig0002 dummy-jig beluga_trailer_3 beluga1
1
0 0
3
0 12 0 1
0 24 0 3
0 27 1 0
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_1 rack00 bside fside n18 n04 n22
4
21 0
24 9
2 0
0 0
6
0 26 -1 0
0 10 0 1
0 9 0 2
0 17 8 0
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n18 n04 n22
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 10 0 1
0 25 0 4
0 17 9 0
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n18 n13 n31
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 10 0 1
0 25 2 5
0 17 9 0
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n18 n22 n40
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 10 0 1
0 25 4 6
0 17 9 0
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n25 n06 n31
4
21 0
24 10
2 1
0 0
6
0 26 -1 0
0 10 0 1
0 25 1 5
0 17 9 0
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_1 rack01 bside fside n25 n15 n40
4
21 0
24 10
2 1
0 0
6
0 26 -1 0
0 10 0 1
0 25 3 6
0 17 9 0
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_2 rack00 bside fside n18 n04 n22
4
21 0
24 9
2 0
0 0
6
0 26 -1 0
0 11 0 1
0 9 0 2
0 17 8 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n18 n04 n22
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 11 0 1
0 25 0 4
0 17 9 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n18 n13 n31
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 11 0 1
0 25 2 5
0 17 9 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n18 n22 n40
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 11 0 1
0 25 4 6
0 17 9 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n25 n06 n31
4
21 0
24 10
2 1
0 0
6
0 26 -1 0
0 11 0 1
0 25 1 5
0 17 9 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_2 rack01 bside fside n25 n15 n40
4
21 0
24 10
2 1
0 0
6
0 26 -1 0
0 11 0 1
0 25 3 6
0 17 9 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_3 rack00 bside fside n18 n04 n22
4
21 0
24 9
2 0
0 0
6
0 26 -1 0
0 12 0 1
0 9 0 2
0 17 8 2
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n18 n04 n22
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 12 0 1
0 25 0 4
0 17 9 2
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n18 n13 n31
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 12 0 1
0 25 2 5
0 17 9 2
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n18 n22 n40
4
21 0
24 10
2 0
0 0
6
0 26 -1 0
0 12 0 1
0 25 4 6
0 17 9 2
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n25 n06 n31
4
21 0
24 10
2 1
0 0
6
0 26 -1 0
0 12 0 1
0 25 1 5
0 17 9 2
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 beluga_trailer_3 rack01 bside fside n25 n15 n40
4
21 0
24 10
2 1
0 0
6
0 26 -1 0
0 12 0 1
0 25 3 6
0 17 9 2
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_1 rack00 fside bside n18 n04 n22
4
18 0
24 9
2 0
0 0
6
0 23 -1 0
0 13 0 1
0 9 0 2
0 17 8 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n04 n22
4
18 0
24 10
2 0
0 0
6
0 23 -1 0
0 13 0 1
0 25 0 4
0 17 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n13 n31
4
18 0
24 10
2 0
0 0
6
0 23 -1 0
0 13 0 1
0 25 2 5
0 17 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n18 n22 n40
4
18 0
24 10
2 0
0 0
6
0 23 -1 0
0 13 0 1
0 25 4 6
0 17 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n06 n31
4
18 0
24 10
2 1
0 0
6
0 23 -1 0
0 13 0 1
0 25 1 5
0 17 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_1 rack01 fside bside n25 n15 n40
4
18 0
24 10
2 1
0 0
6
0 23 -1 0
0 13 0 1
0 25 3 6
0 17 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_2 rack00 fside bside n18 n04 n22
4
18 0
24 9
2 0
0 0
6
0 23 -1 0
0 14 0 1
0 9 0 2
0 17 8 4
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n04 n22
4
18 0
24 10
2 0
0 0
6
0 23 -1 0
0 14 0 1
0 25 0 4
0 17 9 4
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n13 n31
4
18 0
24 10
2 0
0 0
6
0 23 -1 0
0 14 0 1
0 25 2 5
0 17 9 4
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n18 n22 n40
4
18 0
24 10
2 0
0 0
6
0 23 -1 0
0 14 0 1
0 25 4 6
0 17 9 4
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n06 n31
4
18 0
24 10
2 1
0 0
6
0 23 -1 0
0 14 0 1
0 25 1 5
0 17 9 4
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0001 jig0002 factory_trailer_2 rack01 fside bside n25 n15 n40
4
18 0
24 10
2 1
0 0
6
0 23 -1 0
0 14 0 1
0 25 3 6
0 17 9 4
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack00 bside fside n09 n04 n13
4
26 0
17 8
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 9 0 1
0 24 9 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack00 bside fside n09 n13 n22
4
26 0
17 8
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 9 1 2
0 24 9 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack00 bside fside n18 n04 n22
4
26 0
17 8
1 1
0 0
6
0 21 -1 0
0 10 0 1
0 9 0 2
0 24 9 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n04 n13
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 25 0 2
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n06 n15
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 25 1 3
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n13 n22
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 25 2 4
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n22 n31
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 25 4 5
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n09 n31 n40
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 10 0 1
0 25 5 6
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n18 n04 n22
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 10 0 1
0 25 0 4
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n18 n13 n31
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 10 0 1
0 25 2 5
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_1 rack01 bside fside n18 n22 n40
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 10 0 1
0 25 4 6
0 24 10 1
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack00 bside fside n09 n04 n13
4
26 0
17 8
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 9 0 1
0 24 9 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack00 bside fside n09 n13 n22
4
26 0
17 8
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 9 1 2
0 24 9 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack00 bside fside n18 n04 n22
4
26 0
17 8
1 1
0 0
6
0 21 -1 0
0 11 0 1
0 9 0 2
0 24 9 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n04 n13
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 25 0 2
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n06 n15
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 25 1 3
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n13 n22
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 25 2 4
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n22 n31
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 25 4 5
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n09 n31 n40
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 11 0 1
0 25 5 6
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n18 n04 n22
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 11 0 1
0 25 0 4
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n18 n13 n31
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 11 0 1
0 25 2 5
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_2 rack01 bside fside n18 n22 n40
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 11 0 1
0 25 4 6
0 24 10 2
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack00 bside fside n09 n04 n13
4
26 0
17 8
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 9 0 1
0 24 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack00 bside fside n09 n13 n22
4
26 0
17 8
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 9 1 2
0 24 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack00 bside fside n18 n04 n22
4
26 0
17 8
1 1
0 0
6
0 21 -1 0
0 12 0 1
0 9 0 2
0 24 9 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n04 n13
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 25 0 2
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n06 n15
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 25 1 3
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n13 n22
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 25 2 4
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n22 n31
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 25 4 5
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n09 n31 n40
4
26 0
17 9
1 0
0 0
6
0 21 -1 0
0 12 0 1
0 25 5 6
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n18 n04 n22
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 12 0 1
0 25 0 4
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n18 n13 n31
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 12 0 1
0 25 2 5
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 beluga_trailer_3 rack01 bside fside n18 n22 n40
4
26 0
17 9
1 1
0 0
6
0 21 -1 0
0 12 0 1
0 25 4 6
0 24 10 3
0 19 0 1
0 20 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n04 n13
4
23 0
17 8
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 9 0 1
0 24 9 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n09 n13 n22
4
23 0
17 8
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 9 1 2
0 24 9 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack00 fside bside n18 n04 n22
4
23 0
17 8
1 1
0 0
6
0 18 -1 0
0 13 0 1
0 9 0 2
0 24 9 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n04 n13
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 25 0 2
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n06 n15
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 25 1 3
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n13 n22
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 25 2 4
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n22 n31
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 25 4 5
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n09 n31 n40
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 13 0 1
0 25 5 6
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n04 n22
4
23 0
17 9
1 1
0 0
6
0 18 -1 0
0 13 0 1
0 25 0 4
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n13 n31
4
23 0
17 9
1 1
0 0
6
0 18 -1 0
0 13 0 1
0 25 2 5
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_1 rack01 fside bside n18 n22 n40
4
23 0
17 9
1 1
0 0
6
0 18 -1 0
0 13 0 1
0 25 4 6
0 24 10 4
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n04 n13
4
23 0
17 8
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 9 0 1
0 24 9 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n09 n13 n22
4
23 0
17 8
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 9 1 2
0 24 9 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack00 fside bside n18 n04 n22
4
23 0
17 8
1 1
0 0
6
0 18 -1 0
0 14 0 1
0 9 0 2
0 24 9 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n04 n13
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 25 0 2
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n06 n15
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 25 1 3
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n13 n22
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 25 2 4
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n22 n31
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 25 4 5
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n09 n31 n40
4
23 0
17 9
1 0
0 0
6
0 18 -1 0
0 14 0 1
0 25 5 6
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n04 n22
4
23 0
17 9
1 1
0 0
6
0 18 -1 0
0 14 0 1
0 25 0 4
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n13 n31
4
23 0
17 9
1 1
0 0
6
0 18 -1 0
0 14 0 1
0 25 2 5
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
unstack_rack jig0002 jig0001 factory_trailer_2 rack01 fside bside n18 n22 n40
4
23 0
17 9
1 1
0 0
6
0 18 -1 0
0 14 0 1
0 25 4 6
0 24 10 5
0 15 0 1
0 16 0 1
1
end_operator
0
