% feature requirements
requires(feature(actionCosts)).

% variables
variable(variable(0)).
contains(variable(0), value("size(jig0002, n09)", true)).
contains(variable(0), value("size(jig0002, n18)", true)).

variable(variable(1)).
contains(variable(1), value("size(jig0001, n18)", true)).
contains(variable(1), value("size(jig0001, n25)", true)).

variable(variable(2)).
contains(variable(2), value("to_deliver(dummy_jig, pl0)", true)).
contains(variable(2), value("to_deliver(jig0002, pl0)", true)).

variable(variable(3)).
contains(variable(3), value("empty(hangar1)", true)).
contains(variable(3), value("empty(hangar1)", false)).

variable(variable(4)).
contains(variable(4), value("empty(hangar2)", true)).
contains(variable(4), value("empty(hangar2)", false)).

variable(variable(5)).
contains(variable(5), value("to_deliver(dummy_jig, pl1)", true)).
contains(variable(5), value("to_deliver(jig0001, pl1)", true)).

variable(variable(6)).
contains(variable(6), value("empty(hangar3)", true)).
contains(variable(6), value("empty(hangar3)", false)).

variable(variable(7)).
contains(variable(7), value("empty(rack00)", true)).
contains(variable(7), value("empty(rack00)", false)).

variable(variable(8)).
contains(variable(8), value("free_space(rack00, n04)", true)).
contains(variable(8), value("free_space(rack00, n13)", true)).
contains(variable(8), value("free_space(rack00, n22)", true)).

variable(variable(9)).
contains(variable(9), value("empty(beluga_trailer_1)", true)).
contains(variable(9), value("empty(beluga_trailer_1)", false)).

variable(variable(10)).
contains(variable(10), value("empty(beluga_trailer_2)", true)).
contains(variable(10), value("empty(beluga_trailer_2)", false)).

variable(variable(11)).
contains(variable(11), value("empty(beluga_trailer_3)", true)).
contains(variable(11), value("empty(beluga_trailer_3)", false)).

variable(variable(12)).
contains(variable(12), value("empty(factory_trailer_1)", true)).
contains(variable(12), value("empty(factory_trailer_1)", false)).

variable(variable(13)).
contains(variable(13), value("empty(factory_trailer_2)", true)).
contains(variable(13), value("empty(factory_trailer_2)", false)).

variable(variable(14)).
contains(variable(14), value("next_to(jig0001, jig0002, bside)", true)).
contains(variable(14), value("next_to(jig0001, jig0002, bside)", false)).

variable(variable(15)).
contains(variable(15), value("next_to(jig0002, jig0001, fside)", true)).
contains(variable(15), value("next_to(jig0002, jig0001, fside)", false)).

variable(variable(16)).
contains(variable(16), value("in(jig0001, beluga_trailer_1)", true)).
contains(variable(16), value("in(jig0001, beluga_trailer_2)", true)).
contains(variable(16), value("in(jig0001, beluga_trailer_3)", true)).
contains(variable(16), value("in(jig0001, factory_trailer_1)", true)).
contains(variable(16), value("in(jig0001, factory_trailer_2)", true)).
contains(variable(16), value("in(jig0001, hangar1)", true)).
contains(variable(16), value("in(jig0001, hangar2)", true)).
contains(variable(16), value("in(jig0001, hangar3)", true)).
contains(variable(16), value("in(jig0001, rack00)", true)).
contains(variable(16), value("in(jig0001, rack01)", true)).

variable(variable(17)).
contains(variable(17), value("clear(jig0001, fside)", true)).
contains(variable(17), value("clear(jig0001, fside)", false)).

variable(variable(18)).
contains(variable(18), value("next_to(jig0001, jig0002, fside)", true)).
contains(variable(18), value("next_to(jig0001, jig0002, fside)", false)).

variable(variable(19)).
contains(variable(19), value("next_to(jig0002, jig0001, bside)", true)).
contains(variable(19), value("next_to(jig0002, jig0001, bside)", false)).

variable(variable(20)).
contains(variable(20), value("clear(jig0001, bside)", true)).
contains(variable(20), value("clear(jig0001, bside)", false)).

variable(variable(21)).
contains(variable(21), value("empty(rack01)", true)).
contains(variable(21), value("empty(rack01)", false)).

variable(variable(22)).
contains(variable(22), value("clear(jig0002, fside)", true)).
contains(variable(22), value("clear(jig0002, fside)", false)).

variable(variable(23)).
contains(variable(23), value("in(jig0002, beluga1)", true)).
contains(variable(23), value("in(jig0002, beluga_trailer_1)", true)).
contains(variable(23), value("in(jig0002, beluga_trailer_2)", true)).
contains(variable(23), value("in(jig0002, beluga_trailer_3)", true)).
contains(variable(23), value("in(jig0002, factory_trailer_1)", true)).
contains(variable(23), value("in(jig0002, factory_trailer_2)", true)).
contains(variable(23), value("in(jig0002, hangar1)", true)).
contains(variable(23), value("in(jig0002, hangar2)", true)).
contains(variable(23), value("in(jig0002, hangar3)", true)).
contains(variable(23), value("in(jig0002, rack00)", true)).
contains(variable(23), value("in(jig0002, rack01)", true)).

variable(variable(24)).
contains(variable(24), value("free_space(rack01, n04)", true)).
contains(variable(24), value("free_space(rack01, n06)", true)).
contains(variable(24), value("free_space(rack01, n13)", true)).
contains(variable(24), value("free_space(rack01, n15)", true)).
contains(variable(24), value("free_space(rack01, n22)", true)).
contains(variable(24), value("free_space(rack01, n31)", true)).
contains(variable(24), value("free_space(rack01, n40)", true)).

variable(variable(25)).
contains(variable(25), value("clear(jig0002, bside)", true)).
contains(variable(25), value("clear(jig0002, bside)", false)).

variable(variable(26)).
contains(variable(26), value("to_unload(dummy_jig, beluga1)", true)).
contains(variable(26), value("to_unload(jig0002, beluga1)", true)).

variable(variable(27)).
contains(variable(27), value("empty(jig0002)", true)).
contains(variable(27), value("empty(jig0002)", false)).

variable(variable(28)).
contains(variable(28), value("empty(jig0001)", true)).
contains(variable(28), value("empty(jig0001)", false)).

% actions
action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n18", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(1), value("size(jig0001, n18)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar1", "pl1", "n25", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n18", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(1), value("size(jig0001, n18)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar2", "pl1", "n25", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n18", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(1), value("size(jig0001, n18)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_1", "hangar3", "pl1", "n25", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n18", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(1), value("size(jig0001, n18)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar1", "pl1", "n25", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n18", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(1), value("size(jig0001, n18)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar2", "pl1", "n25", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n18", "n18")), 1).

action(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18"))).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), variable(5), value("to_deliver(jig0001, pl1)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(28), value("empty(jig0001)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(16), value("in(jig0001, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(1), value("size(jig0001, n18)", true)).
postcondition(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), effect(unconditional), variable(5), value("to_deliver(dummy_jig, pl1)", true)).
costs(action(("deliver_to_hangar", "jig0001", "dummy_jig", "factory_trailer_2", "hangar3", "pl1", "n25", "n18")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n09", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(0), value("size(jig0002, n09)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar1", "pl0", "n18", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n09", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(0), value("size(jig0002, n09)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar2", "pl0", "n18", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n09", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(0), value("size(jig0002, n09)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_1", "hangar3", "pl0", "n18", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n09", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), variable(3), value("empty(hangar1)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(3), value("empty(hangar1)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar1)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(0), value("size(jig0002, n09)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar1", "pl0", "n18", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n09", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), variable(4), value("empty(hangar2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(4), value("empty(hangar2)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(0), value("size(jig0002, n09)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar2", "pl0", "n18", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n09", "n09")), 1).

action(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09"))).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), variable(6), value("empty(hangar3)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), variable(2), value("to_deliver(jig0002, pl0)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(6), value("empty(hangar3)", false)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(27), value("empty(jig0002)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(23), value("in(jig0002, hangar3)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(0), value("size(jig0002, n09)", true)).
postcondition(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), effect(unconditional), variable(2), value("to_deliver(dummy_jig, pl0)", true)).
costs(action(("deliver_to_hangar", "jig0002", "dummy_jig", "factory_trailer_2", "hangar3", "pl0", "n18", "n09")), 1).

action(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1"))).
precondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1")), variable(16), value("in(jig0001, hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1")), effect(unconditional), variable(3), value("empty(hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_1")), 1).

action(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2"))).
precondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2")), variable(16), value("in(jig0001, hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2")), effect(unconditional), variable(3), value("empty(hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("get_from_hangar", "jig0001", "hangar1", "factory_trailer_2")), 1).

action(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1"))).
precondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1")), variable(16), value("in(jig0001, hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1")), effect(unconditional), variable(4), value("empty(hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_1")), 1).

action(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2"))).
precondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2")), variable(16), value("in(jig0001, hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2")), effect(unconditional), variable(4), value("empty(hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("get_from_hangar", "jig0001", "hangar2", "factory_trailer_2")), 1).

action(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1"))).
precondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1")), variable(16), value("in(jig0001, hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1")), effect(unconditional), variable(6), value("empty(hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_1")), 1).

action(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2"))).
precondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2")), variable(16), value("in(jig0001, hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2")), effect(unconditional), variable(6), value("empty(hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("get_from_hangar", "jig0001", "hangar3", "factory_trailer_2")), 1).

action(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1"))).
precondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1")), variable(23), value("in(jig0002, hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1")), effect(unconditional), variable(3), value("empty(hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_1")), 1).

action(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2"))).
precondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2")), variable(23), value("in(jig0002, hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2")), effect(unconditional), variable(3), value("empty(hangar1)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("get_from_hangar", "jig0002", "hangar1", "factory_trailer_2")), 1).

action(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1"))).
precondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1")), variable(23), value("in(jig0002, hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1")), effect(unconditional), variable(4), value("empty(hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_1")), 1).

action(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2"))).
precondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2")), variable(23), value("in(jig0002, hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2")), effect(unconditional), variable(4), value("empty(hangar2)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("get_from_hangar", "jig0002", "hangar2", "factory_trailer_2")), 1).

action(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1"))).
precondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1")), variable(23), value("in(jig0002, hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1")), effect(unconditional), variable(6), value("empty(hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_1")), 1).

action(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2"))).
precondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2")), variable(23), value("in(jig0002, hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2")), effect(unconditional), variable(6), value("empty(hangar3)", true)).
postcondition(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("get_from_hangar", "jig0002", "hangar3", "factory_trailer_2")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), 1).

action(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40"))).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
costs(action(("pick_up_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(7), value("empty(rack00)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(21), value("empty(rack01)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
costs(action(("pick_up_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n31", "n06")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_1", "rack01", "bside", "n25", "n40", "n15")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n31", "n06")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_2", "rack01", "bside", "n25", "n40", "n15")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n31", "n06")), 1).

action(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15"))).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "beluga_trailer_3", "rack01", "bside", "n25", "n40", "n15")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n31", "n06")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_1", "rack01", "fside", "n25", "n40", "n15")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n31", "n06")), 1).

action(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15"))).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
costs(action(("put_down_rack", "jig0001", "factory_trailer_2", "rack01", "fside", "n25", "n40", "n15")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack00", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n15", "n06")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n31", "n22")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n09", "n40", "n31")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_1", "rack01", "bside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack00", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n15", "n06")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n31", "n22")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n09", "n40", "n31")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_2", "rack01", "bside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack00", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n15", "n06")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n31", "n22")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n09", "n40", "n31")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "beluga_trailer_3", "rack01", "bside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack00", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n15", "n06")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n31", "n22")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n09", "n40", "n31")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_1", "rack01", "fside", "n18", "n40", "n22")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(7), value("empty(rack00)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(7), value("empty(rack00)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack00", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n13", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n15", "n06")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n22", "n13")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n31", "n22")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n09", "n40", "n31")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n22", "n04")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n31", "n13")), 1).

action(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22"))).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(21), value("empty(rack01)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(21), value("empty(rack01)", false)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
costs(action(("put_down_rack", "jig0002", "factory_trailer_2", "rack01", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n31", "n06")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n40", "n15")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n31", "n06")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n40", "n15")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n31", "n06")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(25), value("clear(jig0002, bside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n40", "n15")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n31", "n06")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n40", "n15")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack00)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n31", "n06")), 1).

action(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15"))).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(22), value("clear(jig0002, fside)", false)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(16), value("in(jig0001, rack01)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n40", "n15")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n15", "n06")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n40", "n31")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n15", "n06")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n40", "n31")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n15", "n06")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n40", "n31")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n15", "n06")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n40", "n31")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n40", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(8), value("free_space(rack00, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(8), value("free_space(rack00, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack00)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(24), value("free_space(rack01, n06)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n15", "n06")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n22")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n40", "n31")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(24), value("free_space(rack01, n04)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n04")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n31", "n13")), 1).

action(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22"))).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(24), value("free_space(rack01, n40)", true)).
precondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", false)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(23), value("in(jig0002, rack01)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
postcondition(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
costs(action(("stack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n40", "n22")), 1).

action(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1"))).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), variable(23), value("in(jig0002, beluga1)", true)).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), variable(26), value("to_unload(jig0002, beluga1)", true)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), effect(unconditional), variable(26), value("to_unload(dummy_jig, beluga1)", true)).
costs(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_1", "beluga1")), 1).

action(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1"))).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), variable(23), value("in(jig0002, beluga1)", true)).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), variable(26), value("to_unload(jig0002, beluga1)", true)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), effect(unconditional), variable(26), value("to_unload(dummy_jig, beluga1)", true)).
costs(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_2", "beluga1")), 1).

action(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1"))).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), variable(23), value("in(jig0002, beluga1)", true)).
precondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), variable(26), value("to_unload(jig0002, beluga1)", true)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), effect(unconditional), variable(26), value("to_unload(dummy_jig, beluga1)", true)).
costs(action(("unload_beluga", "jig0002", "dummy_jig", "beluga_trailer_3", "beluga1")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n06", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_1", "rack01", "bside", "fside", "n25", "n15", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n06", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_2", "rack01", "bside", "fside", "n25", "n15", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n06", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(20), value("clear(jig0001, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(25), value("clear(jig0002, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "beluga_trailer_3", "rack01", "bside", "fside", "n25", "n15", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n06", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_1", "rack01", "fside", "bside", "n25", "n15", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(1), value("size(jig0001, n18)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n06", "n31")), 1).

action(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40"))).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(17), value("clear(jig0001, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(1), value("size(jig0001, n25)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(24), value("free_space(rack01, n15)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(22), value("clear(jig0002, fside)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(16), value("in(jig0001, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0001", "jig0002", "factory_trailer_2", "rack01", "fside", "bside", "n25", "n15", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n06", "n15")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n22", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n09", "n31", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(9), value("empty(beluga_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(9), value("empty(beluga_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_1", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n06", "n15")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n22", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n09", "n31", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(10), value("empty(beluga_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(10), value("empty(beluga_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_2", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack00", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n06", "n15")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n22", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n09", "n31", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(25), value("clear(jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(11), value("empty(beluga_trailer_3)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(18), value("next_to(jig0001, jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), variable(19), value("next_to(jig0002, jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(20), value("clear(jig0001, bside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(11), value("empty(beluga_trailer_3)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, beluga_trailer_3)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(18), value("next_to(jig0001, jig0002, fside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), effect(unconditional), variable(19), value("next_to(jig0002, jig0001, bside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "beluga_trailer_3", "rack01", "bside", "fside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n06", "n15")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n22", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n09", "n31", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(12), value("empty(factory_trailer_1)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(12), value("empty(factory_trailer_1)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_1)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_1", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(8), value("free_space(rack00, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(8), value("free_space(rack00, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(8), value("free_space(rack00, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack00)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(8), value("free_space(rack00, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack00", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(24), value("free_space(rack01, n13)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n04", "n13")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(24), value("free_space(rack01, n06)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(24), value("free_space(rack01, n15)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n06", "n15")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n13", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n22", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(0), value("size(jig0002, n09)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(24), value("free_space(rack01, n31)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n09", "n31", "n40")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(24), value("free_space(rack01, n04)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(24), value("free_space(rack01, n22)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n04", "n22")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(24), value("free_space(rack01, n13)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(24), value("free_space(rack01, n31)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n13", "n31")), 1).

action(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40"))).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(22), value("clear(jig0002, fside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(16), value("in(jig0001, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(0), value("size(jig0002, n18)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(13), value("empty(factory_trailer_2)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(24), value("free_space(rack01, n22)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(23), value("in(jig0002, rack01)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(14), value("next_to(jig0001, jig0002, bside)", true)).
precondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), variable(15), value("next_to(jig0002, jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(17), value("clear(jig0001, fside)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(13), value("empty(factory_trailer_2)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(24), value("free_space(rack01, n40)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(23), value("in(jig0002, factory_trailer_2)", true)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(14), value("next_to(jig0001, jig0002, bside)", false)).
postcondition(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), effect(unconditional), variable(15), value("next_to(jig0002, jig0001, fside)", false)).
costs(action(("unstack_rack", "jig0002", "jig0001", "factory_trailer_2", "rack01", "fside", "bside", "n18", "n22", "n40")), 1).

% initial state
initialState(variable(0), value("size(jig0002, n18)", true)).
initialState(variable(1), value("size(jig0001, n25)", true)).
initialState(variable(2), value("to_deliver(jig0002, pl0)", true)).
initialState(variable(3), value("empty(hangar1)", true)).
initialState(variable(4), value("empty(hangar2)", true)).
initialState(variable(5), value("to_deliver(jig0001, pl1)", true)).
initialState(variable(6), value("empty(hangar3)", true)).
initialState(variable(7), value("empty(rack00)", true)).
initialState(variable(8), value("free_space(rack00, n22)", true)).
initialState(variable(9), value("empty(beluga_trailer_1)", true)).
initialState(variable(10), value("empty(beluga_trailer_2)", true)).
initialState(variable(11), value("empty(beluga_trailer_3)", true)).
initialState(variable(12), value("empty(factory_trailer_1)", true)).
initialState(variable(13), value("empty(factory_trailer_2)", true)).
initialState(variable(14), value("next_to(jig0001, jig0002, bside)", false)).
initialState(variable(15), value("next_to(jig0002, jig0001, fside)", false)).
initialState(variable(16), value("in(jig0001, rack01)", true)).
initialState(variable(17), value("clear(jig0001, fside)", true)).
initialState(variable(18), value("next_to(jig0001, jig0002, fside)", false)).
initialState(variable(19), value("next_to(jig0002, jig0001, bside)", false)).
initialState(variable(20), value("clear(jig0001, bside)", true)).
initialState(variable(21), value("empty(rack01)", false)).
initialState(variable(22), value("clear(jig0002, fside)", false)).
initialState(variable(23), value("in(jig0002, beluga1)", true)).
initialState(variable(24), value("free_space(rack01, n15)", true)).
initialState(variable(25), value("clear(jig0002, bside)", false)).
initialState(variable(26), value("to_unload(jig0002, beluga1)", true)).
initialState(variable(27), value("empty(jig0002)", false)).
initialState(variable(28), value("empty(jig0001)", false)).

% goal
goal(variable(26), value("to_unload(dummy_jig, beluga1)", true)).
goal(variable(27), value("empty(jig0002)", true)).
goal(variable(28), value("empty(jig0001)", true)).
#const horizon=1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Horizon, must be defined externally
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

time(0..horizon).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Establish initial state
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

holds(Variable, Value, 0) :- initialState(Variable, Value).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Compute derived predicates
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% conjunctive preconditions
satisfied(DerivedPredicate, type(and), T) :- derivedPredicate(DerivedPredicate, type(and)), holds(Variable, Value, T) : precondition(DerivedPredicate, type(and), Variable, Value); time(T).

% disjunctive preconditions
satisfied(DerivedPredicate, type(or), T) :- precondition(DerivedPredicate, type(or), Variable, Value), holds(Variable, Value, T), time(T).

holds(DerivedVariable, Value, T) :- satisfied(DerivedPredicate, Type, T), postcondition(DerivedPredicate, Type, effect(unconditional), DerivedVariable, Value).

holds(derivedVariable(DerivedVariable), value(DerivedVariable, false), T) :- derivedVariable(DerivedVariable), not holds(derivedVariable(DerivedVariable), value(DerivedVariable, true), T), time(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Perform actions
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

1 {occurs(Action, T) : action(Action)} 1 :- time(T), T > 0.

% Check preconditions
:- occurs(Action, T), precondition(Action, Variable, Value), not holds(Variable, Value, T - 1).

% Apply effects
caused(Variable, Value, T) :-
	occurs(Action, T),
	postcondition(Action, Effect, Variable, Value),
	holds(VariablePre, ValuePre, T - 1) : precondition(Effect, VariablePre, ValuePre).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Inertia rules
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

modified(Variable, T) :- caused(Variable, Value, T).

holds(Variable, Value, T) :- caused(Variable, Value, T).
holds(variable(V), Value, T) :- holds(variable(V), Value, T - 1), not modified(variable(V), T), time(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Variables and mutex groups
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Check that variables have unique values
:- variable(Variable), not 1 {holds(Variable, Value, T) : contains(Variable, Value)} 1, time(T).

% Check mutexes
:- mutexGroup(MutexGroup), not {holds(Variable, Value, T) : contains(MutexGroup, Variable, Value)} 1, time(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Verify that goal is met
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- goal(Variable, Value), not holds(Variable, Value, horizon).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Shows all 'occurs' atoms.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#show occurs/2.