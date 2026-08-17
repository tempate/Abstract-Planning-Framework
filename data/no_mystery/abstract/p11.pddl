(define (problem transport-l4-t1-p3---int100n150-m25---int100c110---s1---e0)
(:domain transport-strips)

(:objects
l0 l1 l2 l3 - location
t0 - truck
p0 p1 p2 - package
abslevel1 abslevel2 - fuellevel
)

(:init
(sum abslevel1 abslevel2 abslevel1)

(connected l0 l1)
(fuelcost abslevel2 l0 l1)
(connected l0 l2)
(fuelcost abslevel2 l0 l2)
(connected l0 l3)
(fuelcost abslevel2 l0 l3)
(connected l1 l0)
(fuelcost abslevel2 l1 l0)
(connected l1 l2)
(fuelcost abslevel2 l1 l2)
(connected l1 l3)
(fuelcost abslevel2 l1 l3)
(connected l2 l0)
(fuelcost abslevel2 l2 l0)
(connected l2 l1)
(fuelcost abslevel2 l2 l1)
(connected l2 l3)
(fuelcost abslevel2 l2 l3)
(connected l3 l0)
(fuelcost abslevel2 l3 l0)
(connected l3 l1)
(fuelcost abslevel2 l3 l1)
(connected l3 l2)
(fuelcost abslevel2 l3 l2)

(at t0 l2)
(fuel t0 abslevel1)
(= (total-cost) 0)

(at p0 l0)
(at p1 l1)
(at p2 l3)
)

(:goal
(and
(at p0 l1)
(at p1 l0)
(at p2 l0)
)
)
(:metric minimize (total-cost)))
