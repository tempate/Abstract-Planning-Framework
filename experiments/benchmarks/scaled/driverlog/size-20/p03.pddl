(define (problem DLOG-2-2-4)
	(:domain driverlog)
	(:objects
	driver1
	driver2
	truck1
	truck2
	package1 package1-copy1 package1-copy2 package1-copy3 package1-copy4 package1-copy5 package1-copy6 package1-copy7 package1-copy8 package1-copy9 package1-copy10 package1-copy11 package1-copy12 package1-copy13 package1-copy14 package1-copy15 package1-copy16 package1-copy17 package1-copy18
	package2
	package3
	package4
	s0
	s1
	s2
	p0-1
	p2-0
	p2-1
	)
	(:init
	(at driver1 s1)
	(DRIVER driver1)
	(at driver2 s0)
	(DRIVER driver2)
	(at truck1 s1)
	(empty truck1)
	(TRUCK truck1)
	(at truck2 s2)
	(empty truck2)
	(TRUCK truck2)
	(at package1 s0) (at package1-copy1 s0) (at package1-copy2 s0) (at package1-copy3 s0) (at package1-copy4 s0) (at package1-copy5 s0) (at package1-copy6 s0) (at package1-copy7 s0) (at package1-copy8 s0) (at package1-copy9 s0) (at package1-copy10 s0) (at package1-copy11 s0) (at package1-copy12 s0) (at package1-copy13 s0) (at package1-copy14 s0) (at package1-copy15 s0) (at package1-copy16 s0) (at package1-copy17 s0) (at package1-copy18 s0)
	(OBJ package1) (OBJ package1-copy1) (OBJ package1-copy2) (OBJ package1-copy3) (OBJ package1-copy4) (OBJ package1-copy5) (OBJ package1-copy6) (OBJ package1-copy7) (OBJ package1-copy8) (OBJ package1-copy9) (OBJ package1-copy10) (OBJ package1-copy11) (OBJ package1-copy12) (OBJ package1-copy13) (OBJ package1-copy14) (OBJ package1-copy15) (OBJ package1-copy16) (OBJ package1-copy17) (OBJ package1-copy18)
	(at package2 s0)
	(OBJ package2)
	(at package3 s1)
	(OBJ package3)
	(at package4 s1)
	(OBJ package4)
	(LOCATION s0)
	(LOCATION s1)
	(LOCATION s2)
	(LOCATION p0-1)
	(LOCATION p2-0)
	(LOCATION p2-1)
	(path s0 p0-1)
	(path p0-1 s0)
	(path s1 p0-1)
	(path p0-1 s1)
	(path s2 p2-0)
	(path p2-0 s2)
	(path s0 p2-0)
	(path p2-0 s0)
	(path s2 p2-1)
	(path p2-1 s2)
	(path s1 p2-1)
	(path p2-1 s1)
	(link s1 s0)
	(link s0 s1)
	(link s1 s2)
	(link s2 s1)
	(link s2 s0)
	(link s0 s2)
)
	(:goal (and
	(at driver2 s2)
	(at truck1 s1)
	(at truck2 s2)
	(at package1 s1) (at package1-copy1 s1) (at package1-copy2 s1) (at package1-copy3 s1) (at package1-copy4 s1) (at package1-copy5 s1) (at package1-copy6 s1) (at package1-copy7 s1) (at package1-copy8 s1) (at package1-copy9 s1) (at package1-copy10 s1) (at package1-copy11 s1) (at package1-copy12 s1) (at package1-copy13 s1) (at package1-copy14 s1) (at package1-copy15 s1) (at package1-copy16 s1) (at package1-copy17 s1) (at package1-copy18 s1)
	(at package2 s1)
	(at package3 s2)
	))


)
