(define (problem grid-2)
(:domain grid-visit-all)
(:objects 
	loc-x0-y0
	loc-x0-y1 loc-x0-y1-copy1 loc-x0-y1-copy2 loc-x0-y1-copy3 loc-x0-y1-copy4 loc-x0-y1-copy5 loc-x0-y1-copy6 loc-x0-y1-copy7 loc-x0-y1-copy8 loc-x0-y1-copy9 loc-x0-y1-copy10 loc-x0-y1-copy11 loc-x0-y1-copy12 loc-x0-y1-copy13 loc-x0-y1-copy14 loc-x0-y1-copy15 loc-x0-y1-copy16 loc-x0-y1-copy17 loc-x0-y1-copy18
	loc-x1-y0
	loc-x1-y1
- place 
        
)
(:init
	(at-robot loc-x1-y1)
	(visited loc-x1-y1)
	(connected loc-x0-y0 loc-x1-y0)
 	(connected loc-x0-y0 loc-x0-y1) (connected loc-x0-y0 loc-x0-y1-copy1) (connected loc-x0-y0 loc-x0-y1-copy2) (connected loc-x0-y0 loc-x0-y1-copy3) (connected loc-x0-y0 loc-x0-y1-copy4) (connected loc-x0-y0 loc-x0-y1-copy5) (connected loc-x0-y0 loc-x0-y1-copy6) (connected loc-x0-y0 loc-x0-y1-copy7) (connected loc-x0-y0 loc-x0-y1-copy8) (connected loc-x0-y0 loc-x0-y1-copy9) (connected loc-x0-y0 loc-x0-y1-copy10) (connected loc-x0-y0 loc-x0-y1-copy11) (connected loc-x0-y0 loc-x0-y1-copy12) (connected loc-x0-y0 loc-x0-y1-copy13) (connected loc-x0-y0 loc-x0-y1-copy14) (connected loc-x0-y0 loc-x0-y1-copy15) (connected loc-x0-y0 loc-x0-y1-copy16) (connected loc-x0-y0 loc-x0-y1-copy17) (connected loc-x0-y0 loc-x0-y1-copy18)
 	(connected loc-x0-y1 loc-x1-y1) (connected loc-x0-y1-copy1 loc-x1-y1) (connected loc-x0-y1-copy2 loc-x1-y1) (connected loc-x0-y1-copy3 loc-x1-y1) (connected loc-x0-y1-copy4 loc-x1-y1) (connected loc-x0-y1-copy5 loc-x1-y1) (connected loc-x0-y1-copy6 loc-x1-y1) (connected loc-x0-y1-copy7 loc-x1-y1) (connected loc-x0-y1-copy8 loc-x1-y1) (connected loc-x0-y1-copy9 loc-x1-y1) (connected loc-x0-y1-copy10 loc-x1-y1) (connected loc-x0-y1-copy11 loc-x1-y1) (connected loc-x0-y1-copy12 loc-x1-y1) (connected loc-x0-y1-copy13 loc-x1-y1) (connected loc-x0-y1-copy14 loc-x1-y1) (connected loc-x0-y1-copy15 loc-x1-y1) (connected loc-x0-y1-copy16 loc-x1-y1) (connected loc-x0-y1-copy17 loc-x1-y1) (connected loc-x0-y1-copy18 loc-x1-y1)
 	(connected loc-x0-y1 loc-x0-y0) (connected loc-x0-y1-copy1 loc-x0-y0) (connected loc-x0-y1-copy2 loc-x0-y0) (connected loc-x0-y1-copy3 loc-x0-y0) (connected loc-x0-y1-copy4 loc-x0-y0) (connected loc-x0-y1-copy5 loc-x0-y0) (connected loc-x0-y1-copy6 loc-x0-y0) (connected loc-x0-y1-copy7 loc-x0-y0) (connected loc-x0-y1-copy8 loc-x0-y0) (connected loc-x0-y1-copy9 loc-x0-y0) (connected loc-x0-y1-copy10 loc-x0-y0) (connected loc-x0-y1-copy11 loc-x0-y0) (connected loc-x0-y1-copy12 loc-x0-y0) (connected loc-x0-y1-copy13 loc-x0-y0) (connected loc-x0-y1-copy14 loc-x0-y0) (connected loc-x0-y1-copy15 loc-x0-y0) (connected loc-x0-y1-copy16 loc-x0-y0) (connected loc-x0-y1-copy17 loc-x0-y0) (connected loc-x0-y1-copy18 loc-x0-y0)
 	(connected loc-x1-y0 loc-x0-y0)
 	(connected loc-x1-y0 loc-x1-y1)
 	(connected loc-x1-y1 loc-x0-y1) (connected loc-x1-y1 loc-x0-y1-copy1) (connected loc-x1-y1 loc-x0-y1-copy2) (connected loc-x1-y1 loc-x0-y1-copy3) (connected loc-x1-y1 loc-x0-y1-copy4) (connected loc-x1-y1 loc-x0-y1-copy5) (connected loc-x1-y1 loc-x0-y1-copy6) (connected loc-x1-y1 loc-x0-y1-copy7) (connected loc-x1-y1 loc-x0-y1-copy8) (connected loc-x1-y1 loc-x0-y1-copy9) (connected loc-x1-y1 loc-x0-y1-copy10) (connected loc-x1-y1 loc-x0-y1-copy11) (connected loc-x1-y1 loc-x0-y1-copy12) (connected loc-x1-y1 loc-x0-y1-copy13) (connected loc-x1-y1 loc-x0-y1-copy14) (connected loc-x1-y1 loc-x0-y1-copy15) (connected loc-x1-y1 loc-x0-y1-copy16) (connected loc-x1-y1 loc-x0-y1-copy17) (connected loc-x1-y1 loc-x0-y1-copy18)
 	(connected loc-x1-y1 loc-x1-y0)
 
)
(:goal
(and 
	(visited loc-x0-y0)
	(visited loc-x0-y1) (visited loc-x0-y1-copy1) (visited loc-x0-y1-copy2) (visited loc-x0-y1-copy3) (visited loc-x0-y1-copy4) (visited loc-x0-y1-copy5) (visited loc-x0-y1-copy6) (visited loc-x0-y1-copy7) (visited loc-x0-y1-copy8) (visited loc-x0-y1-copy9) (visited loc-x0-y1-copy10) (visited loc-x0-y1-copy11) (visited loc-x0-y1-copy12) (visited loc-x0-y1-copy13) (visited loc-x0-y1-copy14) (visited loc-x0-y1-copy15) (visited loc-x0-y1-copy16) (visited loc-x0-y1-copy17) (visited loc-x0-y1-copy18)
	(visited loc-x1-y0)
	(visited loc-x1-y1)
)
)
)