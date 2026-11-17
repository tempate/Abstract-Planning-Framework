(define (problem DLOG-2-2-2)
	(:domain driverlog)
	(:objects
	driver1
	driver2
	truck1
	truck2
	package1 package1-copy1 package1-copy2 package1-copy3 package1-copy4 package1-copy5 package1-copy6 package1-copy7 package1-copy8 package1-copy9 package1-copy10 package1-copy11 package1-copy12 package1-copy13 package1-copy14 package1-copy15 package1-copy16 package1-copy17 package1-copy18 package1-copy19 package1-copy20 package1-copy21 package1-copy22 package1-copy23 package1-copy24 package1-copy25 package1-copy26 package1-copy27 package1-copy28 package1-copy29 package1-copy30 package1-copy31 package1-copy32 package1-copy33 package1-copy34 package1-copy35 package1-copy36 package1-copy37 package1-copy38 package1-copy39 package1-copy40 package1-copy41 package1-copy42 package1-copy43 package1-copy44 package1-copy45 package1-copy46 package1-copy47 package1-copy48
	package2
	s0
	s1
	s2
	p1-0
	p1-2
	)
	(:init
	(at driver1 s2)
	(DRIVER driver1)
	(at driver2 s2)
	(DRIVER driver2)
	(at truck1 s0)
	(empty truck1)
	(TRUCK truck1)
	(at truck2 s0)
	(empty truck2)
	(TRUCK truck2)
	(at package1 s0) (at package1-copy1 s0) (at package1-copy2 s0) (at package1-copy3 s0) (at package1-copy4 s0) (at package1-copy5 s0) (at package1-copy6 s0) (at package1-copy7 s0) (at package1-copy8 s0) (at package1-copy9 s0) (at package1-copy10 s0) (at package1-copy11 s0) (at package1-copy12 s0) (at package1-copy13 s0) (at package1-copy14 s0) (at package1-copy15 s0) (at package1-copy16 s0) (at package1-copy17 s0) (at package1-copy18 s0) (at package1-copy19 s0) (at package1-copy20 s0) (at package1-copy21 s0) (at package1-copy22 s0) (at package1-copy23 s0) (at package1-copy24 s0) (at package1-copy25 s0) (at package1-copy26 s0) (at package1-copy27 s0) (at package1-copy28 s0) (at package1-copy29 s0) (at package1-copy30 s0) (at package1-copy31 s0) (at package1-copy32 s0) (at package1-copy33 s0) (at package1-copy34 s0) (at package1-copy35 s0) (at package1-copy36 s0) (at package1-copy37 s0) (at package1-copy38 s0) (at package1-copy39 s0) (at package1-copy40 s0) (at package1-copy41 s0) (at package1-copy42 s0) (at package1-copy43 s0) (at package1-copy44 s0) (at package1-copy45 s0) (at package1-copy46 s0) (at package1-copy47 s0) (at package1-copy48 s0)
	(OBJ package1) (OBJ package1-copy1) (OBJ package1-copy2) (OBJ package1-copy3) (OBJ package1-copy4) (OBJ package1-copy5) (OBJ package1-copy6) (OBJ package1-copy7) (OBJ package1-copy8) (OBJ package1-copy9) (OBJ package1-copy10) (OBJ package1-copy11) (OBJ package1-copy12) (OBJ package1-copy13) (OBJ package1-copy14) (OBJ package1-copy15) (OBJ package1-copy16) (OBJ package1-copy17) (OBJ package1-copy18) (OBJ package1-copy19) (OBJ package1-copy20) (OBJ package1-copy21) (OBJ package1-copy22) (OBJ package1-copy23) (OBJ package1-copy24) (OBJ package1-copy25) (OBJ package1-copy26) (OBJ package1-copy27) (OBJ package1-copy28) (OBJ package1-copy29) (OBJ package1-copy30) (OBJ package1-copy31) (OBJ package1-copy32) (OBJ package1-copy33) (OBJ package1-copy34) (OBJ package1-copy35) (OBJ package1-copy36) (OBJ package1-copy37) (OBJ package1-copy38) (OBJ package1-copy39) (OBJ package1-copy40) (OBJ package1-copy41) (OBJ package1-copy42) (OBJ package1-copy43) (OBJ package1-copy44) (OBJ package1-copy45) (OBJ package1-copy46) (OBJ package1-copy47) (OBJ package1-copy48)
	(at package2 s0)
	(OBJ package2)
	(LOCATION s0)
	(LOCATION s1)
	(LOCATION s2)
	(LOCATION p1-0)
	(LOCATION p1-2)
	(path s1 p1-0)
	(path p1-0 s1)
	(path s0 p1-0)
	(path p1-0 s0)
	(path s1 p1-2)
	(path p1-2 s1)
	(path s2 p1-2)
	(path p1-2 s2)
	(link s0 s1)
	(link s1 s0)
	(link s0 s2)
	(link s2 s0)
	(link s2 s1)
	(link s1 s2)
)
	(:goal (and
	(at driver1 s1)
	(at truck1 s1)
	(at package1 s0) (at package1-copy1 s0) (at package1-copy2 s0) (at package1-copy3 s0) (at package1-copy4 s0) (at package1-copy5 s0) (at package1-copy6 s0) (at package1-copy7 s0) (at package1-copy8 s0) (at package1-copy9 s0) (at package1-copy10 s0) (at package1-copy11 s0) (at package1-copy12 s0) (at package1-copy13 s0) (at package1-copy14 s0) (at package1-copy15 s0) (at package1-copy16 s0) (at package1-copy17 s0) (at package1-copy18 s0) (at package1-copy19 s0) (at package1-copy20 s0) (at package1-copy21 s0) (at package1-copy22 s0) (at package1-copy23 s0) (at package1-copy24 s0) (at package1-copy25 s0) (at package1-copy26 s0) (at package1-copy27 s0) (at package1-copy28 s0) (at package1-copy29 s0) (at package1-copy30 s0) (at package1-copy31 s0) (at package1-copy32 s0) (at package1-copy33 s0) (at package1-copy34 s0) (at package1-copy35 s0) (at package1-copy36 s0) (at package1-copy37 s0) (at package1-copy38 s0) (at package1-copy39 s0) (at package1-copy40 s0) (at package1-copy41 s0) (at package1-copy42 s0) (at package1-copy43 s0) (at package1-copy44 s0) (at package1-copy45 s0) (at package1-copy46 s0) (at package1-copy47 s0) (at package1-copy48 s0)
	(at package2 s0)
	))


)
