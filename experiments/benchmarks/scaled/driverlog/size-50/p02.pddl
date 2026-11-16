(define (problem DLOG-2-2-3)
	(:domain driverlog)
	(:objects
	driver1 driver1-copy1 driver1-copy2 driver1-copy3 driver1-copy4 driver1-copy5 driver1-copy6 driver1-copy7 driver1-copy8 driver1-copy9 driver1-copy10 driver1-copy11 driver1-copy12 driver1-copy13 driver1-copy14 driver1-copy15 driver1-copy16 driver1-copy17 driver1-copy18 driver1-copy19 driver1-copy20 driver1-copy21 driver1-copy22 driver1-copy23 driver1-copy24 driver1-copy25 driver1-copy26 driver1-copy27 driver1-copy28 driver1-copy29 driver1-copy30 driver1-copy31 driver1-copy32 driver1-copy33 driver1-copy34 driver1-copy35 driver1-copy36 driver1-copy37 driver1-copy38 driver1-copy39 driver1-copy40 driver1-copy41 driver1-copy42 driver1-copy43 driver1-copy44 driver1-copy45 driver1-copy46 driver1-copy47 driver1-copy48
	driver2
	truck1
	truck2
	package1
	package2
	package3
	s0
	s1
	s2
	p0-1
	p0-2
	p1-0
	p2-1
	)
	(:init
	(at driver1 s0) (at driver1-copy1 s0) (at driver1-copy2 s0) (at driver1-copy3 s0) (at driver1-copy4 s0) (at driver1-copy5 s0) (at driver1-copy6 s0) (at driver1-copy7 s0) (at driver1-copy8 s0) (at driver1-copy9 s0) (at driver1-copy10 s0) (at driver1-copy11 s0) (at driver1-copy12 s0) (at driver1-copy13 s0) (at driver1-copy14 s0) (at driver1-copy15 s0) (at driver1-copy16 s0) (at driver1-copy17 s0) (at driver1-copy18 s0) (at driver1-copy19 s0) (at driver1-copy20 s0) (at driver1-copy21 s0) (at driver1-copy22 s0) (at driver1-copy23 s0) (at driver1-copy24 s0) (at driver1-copy25 s0) (at driver1-copy26 s0) (at driver1-copy27 s0) (at driver1-copy28 s0) (at driver1-copy29 s0) (at driver1-copy30 s0) (at driver1-copy31 s0) (at driver1-copy32 s0) (at driver1-copy33 s0) (at driver1-copy34 s0) (at driver1-copy35 s0) (at driver1-copy36 s0) (at driver1-copy37 s0) (at driver1-copy38 s0) (at driver1-copy39 s0) (at driver1-copy40 s0) (at driver1-copy41 s0) (at driver1-copy42 s0) (at driver1-copy43 s0) (at driver1-copy44 s0) (at driver1-copy45 s0) (at driver1-copy46 s0) (at driver1-copy47 s0) (at driver1-copy48 s0)
	(DRIVER driver1) (DRIVER driver1-copy1) (DRIVER driver1-copy2) (DRIVER driver1-copy3) (DRIVER driver1-copy4) (DRIVER driver1-copy5) (DRIVER driver1-copy6) (DRIVER driver1-copy7) (DRIVER driver1-copy8) (DRIVER driver1-copy9) (DRIVER driver1-copy10) (DRIVER driver1-copy11) (DRIVER driver1-copy12) (DRIVER driver1-copy13) (DRIVER driver1-copy14) (DRIVER driver1-copy15) (DRIVER driver1-copy16) (DRIVER driver1-copy17) (DRIVER driver1-copy18) (DRIVER driver1-copy19) (DRIVER driver1-copy20) (DRIVER driver1-copy21) (DRIVER driver1-copy22) (DRIVER driver1-copy23) (DRIVER driver1-copy24) (DRIVER driver1-copy25) (DRIVER driver1-copy26) (DRIVER driver1-copy27) (DRIVER driver1-copy28) (DRIVER driver1-copy29) (DRIVER driver1-copy30) (DRIVER driver1-copy31) (DRIVER driver1-copy32) (DRIVER driver1-copy33) (DRIVER driver1-copy34) (DRIVER driver1-copy35) (DRIVER driver1-copy36) (DRIVER driver1-copy37) (DRIVER driver1-copy38) (DRIVER driver1-copy39) (DRIVER driver1-copy40) (DRIVER driver1-copy41) (DRIVER driver1-copy42) (DRIVER driver1-copy43) (DRIVER driver1-copy44) (DRIVER driver1-copy45) (DRIVER driver1-copy46) (DRIVER driver1-copy47) (DRIVER driver1-copy48)
	(at driver2 s0)
	(DRIVER driver2)
	(at truck1 s0)
	(empty truck1)
	(TRUCK truck1)
	(at truck2 s1)
	(empty truck2)
	(TRUCK truck2)
	(at package1 s2)
	(OBJ package1)
	(at package2 s1)
	(OBJ package2)
	(at package3 s1)
	(OBJ package3)
	(LOCATION s0)
	(LOCATION s1)
	(LOCATION s2)
	(LOCATION p0-1)
	(LOCATION p0-2)
	(LOCATION p1-0)
	(LOCATION p2-1)
	(path s0 p0-1)
	(path p0-1 s0)
	(path s1 p0-1)
	(path p0-1 s1)
	(path s0 p0-2)
	(path p0-2 s0)
	(path s2 p0-2)
	(path p0-2 s2)
	(path s2 p2-1)
	(path p2-1 s2)
	(path s1 p2-1)
	(path p2-1 s1)
	(link s0 s2)
	(link s2 s0)
	(link s1 s0)
	(link s0 s1)
	(link s1 s2)
	(link s2 s1)
)
	(:goal (and
	(at driver1 s1) (at driver1-copy1 s1) (at driver1-copy2 s1) (at driver1-copy3 s1) (at driver1-copy4 s1) (at driver1-copy5 s1) (at driver1-copy6 s1) (at driver1-copy7 s1) (at driver1-copy8 s1) (at driver1-copy9 s1) (at driver1-copy10 s1) (at driver1-copy11 s1) (at driver1-copy12 s1) (at driver1-copy13 s1) (at driver1-copy14 s1) (at driver1-copy15 s1) (at driver1-copy16 s1) (at driver1-copy17 s1) (at driver1-copy18 s1) (at driver1-copy19 s1) (at driver1-copy20 s1) (at driver1-copy21 s1) (at driver1-copy22 s1) (at driver1-copy23 s1) (at driver1-copy24 s1) (at driver1-copy25 s1) (at driver1-copy26 s1) (at driver1-copy27 s1) (at driver1-copy28 s1) (at driver1-copy29 s1) (at driver1-copy30 s1) (at driver1-copy31 s1) (at driver1-copy32 s1) (at driver1-copy33 s1) (at driver1-copy34 s1) (at driver1-copy35 s1) (at driver1-copy36 s1) (at driver1-copy37 s1) (at driver1-copy38 s1) (at driver1-copy39 s1) (at driver1-copy40 s1) (at driver1-copy41 s1) (at driver1-copy42 s1) (at driver1-copy43 s1) (at driver1-copy44 s1) (at driver1-copy45 s1) (at driver1-copy46 s1) (at driver1-copy47 s1) (at driver1-copy48 s1)
	(at driver2 s1)
	(at truck1 s2)
	(at truck2 s0)
	(at package1 s0)
	(at package2 s2)
	(at package3 s0)
	))


)
