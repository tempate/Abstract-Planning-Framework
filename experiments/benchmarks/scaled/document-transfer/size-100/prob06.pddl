(define (problem unsolv-problem-6)
(:domain document)
(:objects
	fuel1 - document
	fuel2 - document
	document1 document1-copy1 document1-copy2 document1-copy3 document1-copy4 document1-copy5 document1-copy6 document1-copy7 document1-copy8 document1-copy9 document1-copy10 document1-copy11 document1-copy12 document1-copy13 document1-copy14 document1-copy15 document1-copy16 document1-copy17 document1-copy18 document1-copy19 document1-copy20 document1-copy21 document1-copy22 document1-copy23 document1-copy24 document1-copy25 document1-copy26 document1-copy27 document1-copy28 document1-copy29 document1-copy30 document1-copy31 document1-copy32 document1-copy33 document1-copy34 document1-copy35 document1-copy36 document1-copy37 document1-copy38 document1-copy39 document1-copy40 document1-copy41 document1-copy42 document1-copy43 document1-copy44 document1-copy45 document1-copy46 document1-copy47 document1-copy48 document1-copy49 document1-copy50 document1-copy51 document1-copy52 document1-copy53 document1-copy54 document1-copy55 document1-copy56 document1-copy57 document1-copy58 document1-copy59 document1-copy60 document1-copy61 document1-copy62 document1-copy63 document1-copy64 document1-copy65 document1-copy66 document1-copy67 document1-copy68 document1-copy69 document1-copy70 document1-copy71 document1-copy72 document1-copy73 document1-copy74 document1-copy75 document1-copy76 document1-copy77 document1-copy78 document1-copy79 document1-copy80 document1-copy81 document1-copy82 document1-copy83 document1-copy84 document1-copy85 document1-copy86 document1-copy87 document1-copy88 document1-copy89 document1-copy90 document1-copy91 document1-copy92 document1-copy93 document1-copy94 document1-copy95 document1-copy96 document1-copy97 - document
	document2 - document
	document3 - document
	document4 - document
	document5 - document
	document6 - document
	document7 - document
	document8 - document
	document9 - document
	document10 - document
	office1 - location
	office2 - location
	office3 - location
	office4 - location
	office5 - location
	office6 - location
	office7 - location
	depot - location
)
(:init
	(train-at office1)
	(in-train fuel1)
	(in-train fuel2)
	(at document1 office4) (at document1-copy1 office4) (at document1-copy2 office4) (at document1-copy3 office4) (at document1-copy4 office4) (at document1-copy5 office4) (at document1-copy6 office4) (at document1-copy7 office4) (at document1-copy8 office4) (at document1-copy9 office4) (at document1-copy10 office4) (at document1-copy11 office4) (at document1-copy12 office4) (at document1-copy13 office4) (at document1-copy14 office4) (at document1-copy15 office4) (at document1-copy16 office4) (at document1-copy17 office4) (at document1-copy18 office4) (at document1-copy19 office4) (at document1-copy20 office4) (at document1-copy21 office4) (at document1-copy22 office4) (at document1-copy23 office4) (at document1-copy24 office4) (at document1-copy25 office4) (at document1-copy26 office4) (at document1-copy27 office4) (at document1-copy28 office4) (at document1-copy29 office4) (at document1-copy30 office4) (at document1-copy31 office4) (at document1-copy32 office4) (at document1-copy33 office4) (at document1-copy34 office4) (at document1-copy35 office4) (at document1-copy36 office4) (at document1-copy37 office4) (at document1-copy38 office4) (at document1-copy39 office4) (at document1-copy40 office4) (at document1-copy41 office4) (at document1-copy42 office4) (at document1-copy43 office4) (at document1-copy44 office4) (at document1-copy45 office4) (at document1-copy46 office4) (at document1-copy47 office4) (at document1-copy48 office4) (at document1-copy49 office4) (at document1-copy50 office4) (at document1-copy51 office4) (at document1-copy52 office4) (at document1-copy53 office4) (at document1-copy54 office4) (at document1-copy55 office4) (at document1-copy56 office4) (at document1-copy57 office4) (at document1-copy58 office4) (at document1-copy59 office4) (at document1-copy60 office4) (at document1-copy61 office4) (at document1-copy62 office4) (at document1-copy63 office4) (at document1-copy64 office4) (at document1-copy65 office4) (at document1-copy66 office4) (at document1-copy67 office4) (at document1-copy68 office4) (at document1-copy69 office4) (at document1-copy70 office4) (at document1-copy71 office4) (at document1-copy72 office4) (at document1-copy73 office4) (at document1-copy74 office4) (at document1-copy75 office4) (at document1-copy76 office4) (at document1-copy77 office4) (at document1-copy78 office4) (at document1-copy79 office4) (at document1-copy80 office4) (at document1-copy81 office4) (at document1-copy82 office4) (at document1-copy83 office4) (at document1-copy84 office4) (at document1-copy85 office4) (at document1-copy86 office4) (at document1-copy87 office4) (at document1-copy88 office4) (at document1-copy89 office4) (at document1-copy90 office4) (at document1-copy91 office4) (at document1-copy92 office4) (at document1-copy93 office4) (at document1-copy94 office4) (at document1-copy95 office4) (at document1-copy96 office4) (at document1-copy97 office4)
	(at document2 office4)
	(at document3 office4)
	(at document4 office4)
	(at document5 office4)
	(at document6 office5)
	(at document7 office5)
	(at document8 office5)
	(at document9 office6)
	(at document10 office2)
	(track office1 depot)
	(track office1 office2)
	(track office2 office3)
	(track office4 office1)
	(track office4 office5)
	(track office5 office1)
	(track office5 office6)
	(track office6 office4)
	(track office6 office7)
	(track office7 office1)
	(track office7 office2)
	(track office7 depot)
	(track depot office4)
)
(:goal (and
	(at document4 depot)
	(at document5 depot)
	(at document6 depot)
	(at document10 depot)
)))
