(define (problem beluga)
 (:domain beluga)
 (:objects
   beluga1 - beluga
   hangar1 hangar2 hangar3 - hangar
   jig0001 jig0002 - jig
   n00 n04 n06 n09 n13 n15 n18 n22 n25 n31 n40 - num
   pl0 pl1 - production-line
   rack00 rack01 - rack
   beluga_trailer_1 beluga_trailer_2 beluga_trailer_3 factory_trailer_1 factory_trailer_2 - trailer
   typec typed - type
 )
 (:init (fit n04 n18 n22 rack00) (fit n13 n09 n22 rack00) (fit n04 n09 n13 rack00) (fit n15 n25 n40 rack01) (fit n22 n18 n40 rack01) (fit n31 n09 n40 rack01) (fit n04 n09 n13 rack01) (fit n06 n09 n15 rack01) (fit n04 n18 n22 rack01) (fit n13 n09 n22 rack01) (fit n06 n25 n31 rack01) (fit n13 n18 n31 rack01) (fit n22 n09 n31 rack01) (empty beluga_trailer_1) (at-side beluga_trailer_1 bside) (empty beluga_trailer_2) (at-side beluga_trailer_2 bside) (empty beluga_trailer_3) (at-side beluga_trailer_3 bside) (empty factory_trailer_1) (at-side factory_trailer_1 fside) (empty factory_trailer_2) (at-side factory_trailer_2 fside) (empty rack00) (at-side rack00 bside) (at-side rack00 fside) (free-space rack00 n22) (at-side rack01 bside) (at-side rack01 fside) (free-space rack01 n15) (in jig0001 rack01) (clear jig0001 bside) (clear jig0001 fside) (is_type jig0001 typed) (size jig0001 n25) (empty-size jig0001 n18) (is_type jig0002 typec) (size jig0002 n18) (empty-size jig0002 n09) (empty hangar1) (empty hangar2) (empty hangar3) (processed-flight beluga1) (to_unload jig0002 beluga1) (in jig0002 beluga1) (next_unload jig0002 dummy-jig) (to_load dummy-type dummy-slot beluga1) (to_deliver jig0002 pl0) (next_deliver jig0002 dummy-jig) (to_deliver jig0001 pl1) (next_deliver jig0001 dummy-jig) (= (total-cost) 0))
 (:goal (and (empty jig0002) (empty jig0001) (to_unload dummy-jig beluga1) (to_load dummy-type dummy-slot beluga1)))
 (:metric minimize (total-cost))
)
