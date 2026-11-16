(define (problem grid-2)
(:domain grid-visit-all)
(:objects 
	loc-x0-y0
	loc-x0-y1 loc-x0-y1-copy1 loc-x0-y1-copy2 loc-x0-y1-copy3 loc-x0-y1-copy4 loc-x0-y1-copy5 loc-x0-y1-copy6 loc-x0-y1-copy7 loc-x0-y1-copy8
	loc-x1-y0
	loc-x1-y1
- place 
        
)
(:init
	(at-robot loc-x1-y1)
	(visited loc-x1-y1)
	(connected loc-x0-y0 loc-x1-y0)
 	(connected loc-x0-y0 loc-x0-y1) (connected loc-x0-y0 loc-x0-y1-copy1) (connected loc-x0-y0 loc-x0-y1-copy2) (connected loc-x0-y0 loc-x0-y1-copy3) (connected loc-x0-y0 loc-x0-y1-copy4) (connected loc-x0-y0 loc-x0-y1-copy5) (connected loc-x0-y0 loc-x0-y1-copy6) (connected loc-x0-y0 loc-x0-y1-copy7) (connected loc-x0-y0 loc-x0-y1-copy8)
 	(connected loc-x0-y1 loc-x1-y1) (connected loc-x0-y1-copy1 loc-x1-y1) (connected loc-x0-y1-copy2 loc-x1-y1) (connected loc-x0-y1-copy3 loc-x1-y1) (connected loc-x0-y1-copy4 loc-x1-y1) (connected loc-x0-y1-copy5 loc-x1-y1) (connected loc-x0-y1-copy6 loc-x1-y1) (connected loc-x0-y1-copy7 loc-x1-y1) (connected loc-x0-y1-copy8 loc-x1-y1)
 	(connected loc-x0-y1 loc-x0-y0) (connected loc-x0-y1-copy1 loc-x0-y0) (connected loc-x0-y1-copy2 loc-x0-y0) (connected loc-x0-y1-copy3 loc-x0-y0) (connected loc-x0-y1-copy4 loc-x0-y0) (connected loc-x0-y1-copy5 loc-x0-y0) (connected loc-x0-y1-copy6 loc-x0-y0) (connected loc-x0-y1-copy7 loc-x0-y0) (connected loc-x0-y1-copy8 loc-x0-y0)
 	(connected loc-x1-y0 loc-x0-y0)
 	(connected loc-x1-y0 loc-x1-y1)
 	(connected loc-x1-y1 loc-x0-y1) (connected loc-x1-y1 loc-x0-y1-copy1) (connected loc-x1-y1 loc-x0-y1-copy2) (connected loc-x1-y1 loc-x0-y1-copy3) (connected loc-x1-y1 loc-x0-y1-copy4) (connected loc-x1-y1 loc-x0-y1-copy5) (connected loc-x1-y1 loc-x0-y1-copy6) (connected loc-x1-y1 loc-x0-y1-copy7) (connected loc-x1-y1 loc-x0-y1-copy8)
 	(connected loc-x1-y1 loc-x1-y0)
 
)
(:goal
(and 
	(visited loc-x0-y0)
	(visited loc-x0-y1) (visited loc-x0-y1-copy1) (visited loc-x0-y1-copy2) (visited loc-x0-y1-copy3) (visited loc-x0-y1-copy4) (visited loc-x0-y1-copy5) (visited loc-x0-y1-copy6) (visited loc-x0-y1-copy7) (visited loc-x0-y1-copy8)
	(visited loc-x1-y0)
	(visited loc-x1-y1)
)
)
)