
(define (problem example-problem)
  (:domain htg-child-snack)
  (:objects
    child0 child1 child2 - child
    bread0 bread0-copy1 bread0-copy2 bread0-copy3 bread0-copy4 bread0-copy5 bread0-copy6 bread0-copy7 bread0-copy8 bread0-copy9 bread0-copy10 bread0-copy11 bread0-copy12 bread0-copy13 bread0-copy14 bread0-copy15 bread0-copy16 bread0-copy17 bread0-copy18 bread0-copy19 bread0-copy20 bread0-copy21 bread0-copy22 bread0-copy23 bread0-copy24 bread0-copy25 bread0-copy26 bread0-copy27 bread0-copy28 bread0-copy29 bread0-copy30 bread0-copy31 bread0-copy32 bread0-copy33 bread0-copy34 bread0-copy35 bread0-copy36 bread0-copy37 bread0-copy38 bread0-copy39 bread0-copy40 bread0-copy41 bread0-copy42 bread0-copy43 bread0-copy44 bread0-copy45 bread0-copy46 bread0-copy47 bread1 bread2 - bread-portion
    content-0 content-1 content-2 - content-description
    content-0-0 - content-portion
    content-1-0 - content-portion
    content-2-0 - content-portion
    tray0 tray1 tray2 - tray
    table0 table1 table2 table3 table4 - place
    sandw0 sandw1 sandw2 - sandwich
  )
  (:init
     ;; everythin starts in the kitchen
     (at tray0 kitchen)
     (at tray1 kitchen)
     (at tray2 kitchen)
			    (at_kitchen_bread bread0) (at_kitchen_bread bread0-copy1) (at_kitchen_bread bread0-copy2) (at_kitchen_bread bread0-copy3) (at_kitchen_bread bread0-copy4) (at_kitchen_bread bread0-copy5) (at_kitchen_bread bread0-copy6) (at_kitchen_bread bread0-copy7) (at_kitchen_bread bread0-copy8) (at_kitchen_bread bread0-copy9) (at_kitchen_bread bread0-copy10) (at_kitchen_bread bread0-copy11) (at_kitchen_bread bread0-copy12) (at_kitchen_bread bread0-copy13) (at_kitchen_bread bread0-copy14) (at_kitchen_bread bread0-copy15) (at_kitchen_bread bread0-copy16) (at_kitchen_bread bread0-copy17) (at_kitchen_bread bread0-copy18) (at_kitchen_bread bread0-copy19) (at_kitchen_bread bread0-copy20) (at_kitchen_bread bread0-copy21) (at_kitchen_bread bread0-copy22) (at_kitchen_bread bread0-copy23) (at_kitchen_bread bread0-copy24) (at_kitchen_bread bread0-copy25) (at_kitchen_bread bread0-copy26) (at_kitchen_bread bread0-copy27) (at_kitchen_bread bread0-copy28) (at_kitchen_bread bread0-copy29) (at_kitchen_bread bread0-copy30) (at_kitchen_bread bread0-copy31) (at_kitchen_bread bread0-copy32) (at_kitchen_bread bread0-copy33) (at_kitchen_bread bread0-copy34) (at_kitchen_bread bread0-copy35) (at_kitchen_bread bread0-copy36) (at_kitchen_bread bread0-copy37) (at_kitchen_bread bread0-copy38) (at_kitchen_bread bread0-copy39) (at_kitchen_bread bread0-copy40) (at_kitchen_bread bread0-copy41) (at_kitchen_bread bread0-copy42) (at_kitchen_bread bread0-copy43) (at_kitchen_bread bread0-copy44) (at_kitchen_bread bread0-copy45) (at_kitchen_bread bread0-copy46) (at_kitchen_bread bread0-copy47)
			    (at_kitchen_bread bread1)
			    (at_kitchen_bread bread2)
			    (at_kitchen_content content-0-0)
			    (at_kitchen_content content-1-0)
			    (at_kitchen_content content-2-0) 

     ;; content descriptions
                (descr content-0-0 content-0)
                (descr content-1-0 content-1)
                (descr content-2-0 content-2)
     
     ;; which sandwichs the kids accept
     (likes child1 content-1)
     (likes child2 content-2)
     (likes child0 content-0)

     ;; where children are
     (waiting child0 table0)
     (waiting child1 table1)
     (waiting child2 table2)

     ;;sandwich dummies
     (notexist sandw0)
     (notexist sandw1)
     (notexist sandw2)
  )
  (:goal
    (and
     (served child0)
     (served child1)
     (served child2)
    )
  )
)

