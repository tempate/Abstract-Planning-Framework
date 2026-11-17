(define (problem DLOG-2-2-2)
	(:domain driverlog)
	(:objects
	driver1
	driver2
	truck1
	truck2
	package1 package1-copy1 package1-copy2 package1-copy3 package1-copy4 package1-copy5 package1-copy6 package1-copy7 package1-copy8 package1-copy9 package1-copy10 package1-copy11 package1-copy12 package1-copy13 package1-copy14 package1-copy15 package1-copy16 package1-copy17 package1-copy18 package1-copy19 package1-copy20 package1-copy21 package1-copy22 package1-copy23 package1-copy24 package1-copy25 package1-copy26 package1-copy27 package1-copy28 package1-copy29 package1-copy30 package1-copy31 package1-copy32 package1-copy33 package1-copy34 package1-copy35 package1-copy36 package1-copy37 package1-copy38 package1-copy39 package1-copy40 package1-copy41 package1-copy42 package1-copy43 package1-copy44 package1-copy45 package1-copy46 package1-copy47 package1-copy48 package1-copy49 package1-copy50 package1-copy51 package1-copy52 package1-copy53 package1-copy54 package1-copy55 package1-copy56 package1-copy57 package1-copy58 package1-copy59 package1-copy60 package1-copy61 package1-copy62 package1-copy63 package1-copy64 package1-copy65 package1-copy66 package1-copy67 package1-copy68 package1-copy69 package1-copy70 package1-copy71 package1-copy72 package1-copy73 package1-copy74 package1-copy75 package1-copy76 package1-copy77 package1-copy78 package1-copy79 package1-copy80 package1-copy81 package1-copy82 package1-copy83 package1-copy84 package1-copy85 package1-copy86 package1-copy87 package1-copy88 package1-copy89 package1-copy90 package1-copy91 package1-copy92 package1-copy93 package1-copy94 package1-copy95 package1-copy96 package1-copy97 package1-copy98
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
	(at package1 s0) (at package1-copy1 s0) (at package1-copy2 s0) (at package1-copy3 s0) (at package1-copy4 s0) (at package1-copy5 s0) (at package1-copy6 s0) (at package1-copy7 s0) (at package1-copy8 s0) (at package1-copy9 s0) (at package1-copy10 s0) (at package1-copy11 s0) (at package1-copy12 s0) (at package1-copy13 s0) (at package1-copy14 s0) (at package1-copy15 s0) (at package1-copy16 s0) (at package1-copy17 s0) (at package1-copy18 s0) (at package1-copy19 s0) (at package1-copy20 s0) (at package1-copy21 s0) (at package1-copy22 s0) (at package1-copy23 s0) (at package1-copy24 s0) (at package1-copy25 s0) (at package1-copy26 s0) (at package1-copy27 s0) (at package1-copy28 s0) (at package1-copy29 s0) (at package1-copy30 s0) (at package1-copy31 s0) (at package1-copy32 s0) (at package1-copy33 s0) (at package1-copy34 s0) (at package1-copy35 s0) (at package1-copy36 s0) (at package1-copy37 s0) (at package1-copy38 s0) (at package1-copy39 s0) (at package1-copy40 s0) (at package1-copy41 s0) (at package1-copy42 s0) (at package1-copy43 s0) (at package1-copy44 s0) (at package1-copy45 s0) (at package1-copy46 s0) (at package1-copy47 s0) (at package1-copy48 s0) (at package1-copy49 s0) (at package1-copy50 s0) (at package1-copy51 s0) (at package1-copy52 s0) (at package1-copy53 s0) (at package1-copy54 s0) (at package1-copy55 s0) (at package1-copy56 s0) (at package1-copy57 s0) (at package1-copy58 s0) (at package1-copy59 s0) (at package1-copy60 s0) (at package1-copy61 s0) (at package1-copy62 s0) (at package1-copy63 s0) (at package1-copy64 s0) (at package1-copy65 s0) (at package1-copy66 s0) (at package1-copy67 s0) (at package1-copy68 s0) (at package1-copy69 s0) (at package1-copy70 s0) (at package1-copy71 s0) (at package1-copy72 s0) (at package1-copy73 s0) (at package1-copy74 s0) (at package1-copy75 s0) (at package1-copy76 s0) (at package1-copy77 s0) (at package1-copy78 s0) (at package1-copy79 s0) (at package1-copy80 s0) (at package1-copy81 s0) (at package1-copy82 s0) (at package1-copy83 s0) (at package1-copy84 s0) (at package1-copy85 s0) (at package1-copy86 s0) (at package1-copy87 s0) (at package1-copy88 s0) (at package1-copy89 s0) (at package1-copy90 s0) (at package1-copy91 s0) (at package1-copy92 s0) (at package1-copy93 s0) (at package1-copy94 s0) (at package1-copy95 s0) (at package1-copy96 s0) (at package1-copy97 s0) (at package1-copy98 s0)
	(OBJ package1) (OBJ package1-copy1) (OBJ package1-copy2) (OBJ package1-copy3) (OBJ package1-copy4) (OBJ package1-copy5) (OBJ package1-copy6) (OBJ package1-copy7) (OBJ package1-copy8) (OBJ package1-copy9) (OBJ package1-copy10) (OBJ package1-copy11) (OBJ package1-copy12) (OBJ package1-copy13) (OBJ package1-copy14) (OBJ package1-copy15) (OBJ package1-copy16) (OBJ package1-copy17) (OBJ package1-copy18) (OBJ package1-copy19) (OBJ package1-copy20) (OBJ package1-copy21) (OBJ package1-copy22) (OBJ package1-copy23) (OBJ package1-copy24) (OBJ package1-copy25) (OBJ package1-copy26) (OBJ package1-copy27) (OBJ package1-copy28) (OBJ package1-copy29) (OBJ package1-copy30) (OBJ package1-copy31) (OBJ package1-copy32) (OBJ package1-copy33) (OBJ package1-copy34) (OBJ package1-copy35) (OBJ package1-copy36) (OBJ package1-copy37) (OBJ package1-copy38) (OBJ package1-copy39) (OBJ package1-copy40) (OBJ package1-copy41) (OBJ package1-copy42) (OBJ package1-copy43) (OBJ package1-copy44) (OBJ package1-copy45) (OBJ package1-copy46) (OBJ package1-copy47) (OBJ package1-copy48) (OBJ package1-copy49) (OBJ package1-copy50) (OBJ package1-copy51) (OBJ package1-copy52) (OBJ package1-copy53) (OBJ package1-copy54) (OBJ package1-copy55) (OBJ package1-copy56) (OBJ package1-copy57) (OBJ package1-copy58) (OBJ package1-copy59) (OBJ package1-copy60) (OBJ package1-copy61) (OBJ package1-copy62) (OBJ package1-copy63) (OBJ package1-copy64) (OBJ package1-copy65) (OBJ package1-copy66) (OBJ package1-copy67) (OBJ package1-copy68) (OBJ package1-copy69) (OBJ package1-copy70) (OBJ package1-copy71) (OBJ package1-copy72) (OBJ package1-copy73) (OBJ package1-copy74) (OBJ package1-copy75) (OBJ package1-copy76) (OBJ package1-copy77) (OBJ package1-copy78) (OBJ package1-copy79) (OBJ package1-copy80) (OBJ package1-copy81) (OBJ package1-copy82) (OBJ package1-copy83) (OBJ package1-copy84) (OBJ package1-copy85) (OBJ package1-copy86) (OBJ package1-copy87) (OBJ package1-copy88) (OBJ package1-copy89) (OBJ package1-copy90) (OBJ package1-copy91) (OBJ package1-copy92) (OBJ package1-copy93) (OBJ package1-copy94) (OBJ package1-copy95) (OBJ package1-copy96) (OBJ package1-copy97) (OBJ package1-copy98)
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
	(at package1 s0) (at package1-copy1 s0) (at package1-copy2 s0) (at package1-copy3 s0) (at package1-copy4 s0) (at package1-copy5 s0) (at package1-copy6 s0) (at package1-copy7 s0) (at package1-copy8 s0) (at package1-copy9 s0) (at package1-copy10 s0) (at package1-copy11 s0) (at package1-copy12 s0) (at package1-copy13 s0) (at package1-copy14 s0) (at package1-copy15 s0) (at package1-copy16 s0) (at package1-copy17 s0) (at package1-copy18 s0) (at package1-copy19 s0) (at package1-copy20 s0) (at package1-copy21 s0) (at package1-copy22 s0) (at package1-copy23 s0) (at package1-copy24 s0) (at package1-copy25 s0) (at package1-copy26 s0) (at package1-copy27 s0) (at package1-copy28 s0) (at package1-copy29 s0) (at package1-copy30 s0) (at package1-copy31 s0) (at package1-copy32 s0) (at package1-copy33 s0) (at package1-copy34 s0) (at package1-copy35 s0) (at package1-copy36 s0) (at package1-copy37 s0) (at package1-copy38 s0) (at package1-copy39 s0) (at package1-copy40 s0) (at package1-copy41 s0) (at package1-copy42 s0) (at package1-copy43 s0) (at package1-copy44 s0) (at package1-copy45 s0) (at package1-copy46 s0) (at package1-copy47 s0) (at package1-copy48 s0) (at package1-copy49 s0) (at package1-copy50 s0) (at package1-copy51 s0) (at package1-copy52 s0) (at package1-copy53 s0) (at package1-copy54 s0) (at package1-copy55 s0) (at package1-copy56 s0) (at package1-copy57 s0) (at package1-copy58 s0) (at package1-copy59 s0) (at package1-copy60 s0) (at package1-copy61 s0) (at package1-copy62 s0) (at package1-copy63 s0) (at package1-copy64 s0) (at package1-copy65 s0) (at package1-copy66 s0) (at package1-copy67 s0) (at package1-copy68 s0) (at package1-copy69 s0) (at package1-copy70 s0) (at package1-copy71 s0) (at package1-copy72 s0) (at package1-copy73 s0) (at package1-copy74 s0) (at package1-copy75 s0) (at package1-copy76 s0) (at package1-copy77 s0) (at package1-copy78 s0) (at package1-copy79 s0) (at package1-copy80 s0) (at package1-copy81 s0) (at package1-copy82 s0) (at package1-copy83 s0) (at package1-copy84 s0) (at package1-copy85 s0) (at package1-copy86 s0) (at package1-copy87 s0) (at package1-copy88 s0) (at package1-copy89 s0) (at package1-copy90 s0) (at package1-copy91 s0) (at package1-copy92 s0) (at package1-copy93 s0) (at package1-copy94 s0) (at package1-copy95 s0) (at package1-copy96 s0) (at package1-copy97 s0) (at package1-copy98 s0)
	(at package2 s0)
	))


)
