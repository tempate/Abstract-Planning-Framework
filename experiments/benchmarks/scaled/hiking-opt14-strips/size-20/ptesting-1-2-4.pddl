(define (problem Hiking-1-2)
(:domain hiking)
(:objects 
 car0 car0-copy1 car0-copy2 car0-copy3 car0-copy4 car0-copy5 car0-copy6 car0-copy7 car0-copy8 car0-copy9 car0-copy10 car0-copy11 car0-copy12 car0-copy13 car0-copy14 car0-copy15 car0-copy16 car0-copy17 car0-copy18 car1 - car
 tent0 - tent
 couple0 - couple
 place0 place1 place2 place3 - place
 guy0 girl0 - person
)
(:init
(partners couple0 guy0 girl0)
(at_person guy0 place0)
(at_person girl0 place0)
(walked couple0 place0)
(at_tent tent0 place0)
(down tent0)
(at_car car0 place0) (at_car car0-copy1 place0) (at_car car0-copy2 place0) (at_car car0-copy3 place0) (at_car car0-copy4 place0) (at_car car0-copy5 place0) (at_car car0-copy6 place0) (at_car car0-copy7 place0) (at_car car0-copy8 place0) (at_car car0-copy9 place0) (at_car car0-copy10 place0) (at_car car0-copy11 place0) (at_car car0-copy12 place0) (at_car car0-copy13 place0) (at_car car0-copy14 place0) (at_car car0-copy15 place0) (at_car car0-copy16 place0) (at_car car0-copy17 place0) (at_car car0-copy18 place0)
(at_car car1 place0)
(next place0 place1)
(next place1 place2)
(next place2 place3)
)
(:goal
(and
(walked couple0 place3)
)
)
)
