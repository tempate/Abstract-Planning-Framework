(define (domain beluga_prob1-domain)
 (:requirements :strips :typing :negative-preconditions :equality :action-costs)
 (:types
    location num production_line side slot type - object
    beluga hangar jig rack trailer - location
 )
 (:constants
   fside bside - side
   dummy_jig - jig
   dummy_type - type
   dummy_slot - slot
 )
 (:predicates (at-side ?l - location ?s - side) (clear ?j - jig ?s - side) (empty ?l - location) (empty_size ?j - jig ?es - num) (fit ?nspace - num ?jsize - num ?fspace - num ?r - rack) (free_space ?r - rack ?n - num) (in ?j - jig ?l - location) (is_type ?j - jig ?jt - type) (next_flight_to_process ?b - beluga ?nb - beluga) (next_to ?j - jig ?nj - jig ?s - side) (next_deliver ?j - jig ?jn - jig) (next_load ?jt - type ?s_0 - slot ?ns - slot ?b - beluga) (next_unload ?j - jig ?nj - jig) (processed_flight ?b - beluga) (size ?j - jig ?s_1 - num) (to_deliver ?j - jig ?pl - production_line) (to_load ?jt - type ?s_0 - slot ?b - beluga) (to_unload ?j - jig ?b - beluga) (started))
 (:functions (total-cost))
 (:action load_beluga
  :parameters ( ?j - jig ?jt - type ?njt - type ?b - beluga ?t - trailer ?s_0 - slot ?ns - slot)
  :precondition (and (in ?j ?t) (empty ?j) (is_type ?j ?jt) (processed_flight ?b) (to_load ?jt ?s_0 ?b) (next_load ?njt ?s_0 ?ns ?b) (at-side ?t bside) (started))
  :effect (and (in ?j ?b) (not (in ?j ?t)) (empty ?t) (not (to_load ?jt ?s_0 ?b)) (to_load ?njt ?ns ?b) (increase (total-cost) 1)))
 (:action unload_beluga
  :parameters ( ?j - jig ?nj - jig ?t - trailer ?b - beluga)
  :precondition (and (in ?j ?b) (empty ?t) (at-side ?t bside) (processed_flight ?b) (to_unload ?j ?b) (next_unload ?j ?nj) (started))
  :effect (and (not (in ?j ?b)) (in ?j ?t) (not (empty ?t)) (not (to_unload ?j ?b)) (to_unload ?nj ?b) (increase (total-cost) 1)))
 (:action get_from_hangar
  :parameters ( ?j - jig ?h - hangar ?t - trailer)
  :precondition (and (in ?j ?h) (empty ?t) (at-side ?t fside) (started))
  :effect (and (not (in ?j ?h)) (in ?j ?t) (not (empty ?t)) (empty ?h) (increase (total-cost) 1)))
 (:action deliver_to_hangar
  :parameters ( ?j - jig ?jn - jig ?t - trailer ?h - hangar ?pl - production_line ?s_1 - num ?es - num)
  :precondition (and (in ?j ?t) (empty ?h) (at-side ?t fside) (to_deliver ?j ?pl) (next_deliver ?j ?jn) (size ?j ?s_1) (empty_size ?j ?es) (started))
  :effect (and (empty ?t) (empty ?j) (in ?j ?h) (not (in ?j ?t)) (not (empty ?h)) (not (to_deliver ?j ?pl)) (to_deliver ?jn ?pl) (not (size ?j ?s_1)) (size ?j ?es) (increase (total-cost) 1)))
 (:action put_down_rack
  :parameters ( ?j - jig ?t - trailer ?r - rack ?s - side ?jsize - num ?fspace - num ?nspace - num)
  :precondition (and (in ?j ?t) (empty ?r) (at-side ?t ?s) (at-side ?r ?s) (size ?j ?jsize) (free_space ?r ?fspace) (fit ?nspace ?jsize ?fspace ?r) (started))
  :effect (and (in ?j ?r) (not (in ?j ?t)) (empty ?t) (not (empty ?r)) (clear ?j bside) (clear ?j fside) (not (free_space ?r ?fspace)) (free_space ?r ?nspace) (increase (total-cost) 1)))
 (:action stack_rack
  :parameters ( ?j - jig ?nj - jig ?t - trailer ?r - rack ?s - side ?os - side ?jsize - num ?fspace - num ?nspace - num)
  :precondition (and (not (= ?s ?os)) (in ?j ?t) (in ?nj ?r) (at-side ?t ?s) (at-side ?r ?s) (clear ?nj ?s) (size ?j ?jsize) (free_space ?r ?fspace) (fit ?nspace ?jsize ?fspace ?r) (started))
  :effect (and (in ?j ?r) (not (in ?j ?t)) (empty ?t) (not (clear ?nj ?s)) (clear ?j ?s) (next_to ?j ?nj ?s) (next_to ?nj ?j ?os) (not (free_space ?r ?fspace)) (free_space ?r ?nspace) (increase (total-cost) 1)))
 (:action pick_up_rack
  :parameters ( ?j - jig ?t - trailer ?r - rack ?s - side ?os - side ?jsize - num ?fspace - num ?nspace - num)
  :precondition (and (not (= ?s ?os)) (empty ?t) (in ?j ?r) (at-side ?t ?s) (at-side ?r ?s) (clear ?j bside) (clear ?j fside) (size ?j ?jsize) (free_space ?r ?fspace) (fit ?fspace ?jsize ?nspace ?r) (started))
  :effect (and (in ?j ?t) (not (in ?j ?r)) (empty ?r) (not (empty ?t)) (not (clear ?j bside)) (not (clear ?j fside)) (free_space ?r ?nspace) (not (free_space ?r ?fspace)) (increase (total-cost) 1)))
 (:action unstack_rack
  :parameters ( ?j - jig ?nj - jig ?t - trailer ?r - rack ?s - side ?os - side ?jsize - num ?fspace - num ?nspace - num)
  :precondition (and (not (= ?s ?os)) (empty ?t) (in ?j ?r) (in ?nj ?r) (at-side ?t ?s) (at-side ?r ?s) (clear ?j ?s) (next_to ?j ?nj ?s) (next_to ?nj ?j ?os) (size ?j ?jsize) (free_space ?r ?fspace) (fit ?fspace ?jsize ?nspace ?r) (started))
  :effect (and (in ?j ?t) (not (in ?j ?r)) (not (empty ?t)) (not (next_to ?j ?nj ?s)) (not (next_to ?nj ?j ?os)) (clear ?nj ?s) (free_space ?r ?nspace) (not (free_space ?r ?fspace)) (increase (total-cost) 1)))
 (:action beluga_complete
  :parameters ( ?b - beluga ?nb - beluga)
  :precondition (and (processed_flight ?b) (next_flight_to_process ?b ?nb) (to_unload dummy_jig ?b) (to_load dummy_type dummy_slot ?b) (started))
  :effect (and (not (processed_flight ?b)) (processed_flight ?nb) (increase (total-cost) 1)))
 (:action start_
  :parameters ()
  :precondition (and (not (started)))
  :effect (and (started) (increase (total-cost) 0)))
)
