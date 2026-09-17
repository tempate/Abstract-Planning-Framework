%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Static problem and initial state
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#program base.

time(0).

holds(Variable, Value, 0) :- initialState(Variable, Value).

% Compute derived predicates in the initial state.
satisfied(DerivedPredicate, type(and), 0) :-
	derivedPredicate(DerivedPredicate, type(and)),
	holds(Variable, Value, 0) : precondition(DerivedPredicate, type(and), Variable, Value).

satisfied(DerivedPredicate, type(or), 0) :-
	precondition(DerivedPredicate, type(or), Variable, Value),
	holds(Variable, Value, 0).

holds(DerivedVariable, Value, 0) :-
	satisfied(DerivedPredicate, Type, 0),
	postcondition(DerivedPredicate, Type, effect(unconditional), DerivedVariable, Value).

holds(derivedVariable(DerivedVariable), value(DerivedVariable, false), 0) :-
	derivedVariable(DerivedVariable),
	not holds(derivedVariable(DerivedVariable), value(DerivedVariable, true), 0).

% Check the initial state.
:- variable(Variable), not 1 {holds(Variable, Value, 0) : contains(Variable, Value)} 1.
:- mutexGroup(MutexGroup), not {holds(Variable, Value, 0) : contains(MutexGroup, Variable, Value)} 1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Add one transition when the horizon grows
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#program step(t).

time(t).

% Compute derived predicates.
satisfied(DerivedPredicate, type(and), t) :-
	derivedPredicate(DerivedPredicate, type(and)),
	holds(Variable, Value, t) : precondition(DerivedPredicate, type(and), Variable, Value).

satisfied(DerivedPredicate, type(or), t) :-
	precondition(DerivedPredicate, type(or), Variable, Value),
	holds(Variable, Value, t).

holds(DerivedVariable, Value, t) :-
	satisfied(DerivedPredicate, Type, t),
	postcondition(DerivedPredicate, Type, effect(unconditional), DerivedVariable, Value).

holds(derivedVariable(DerivedVariable), value(DerivedVariable, false), t) :-
	derivedVariable(DerivedVariable),
	not holds(derivedVariable(DerivedVariable), value(DerivedVariable, true), t).

% Perform exactly one action.
1 {occurs(Action, t) : action(Action)} 1.

:- occurs(Action, t), precondition(Action, Variable, Value), not holds(Variable, Value, t - 1).

caused(Variable, Value, t) :-
	occurs(Action, t),
	postcondition(Action, Effect, Variable, Value),
	holds(VariablePre, ValuePre, t - 1) : precondition(Effect, VariablePre, ValuePre).

% Apply effects and inertia.
modified(Variable, t) :- caused(Variable, Value, t).
holds(Variable, Value, t) :- caused(Variable, Value, t).
holds(variable(V), Value, t) :-
	holds(variable(V), Value, t - 1),
	not modified(variable(V), t).

% Check the resulting state.
:- variable(Variable), not 1 {holds(Variable, Value, t) : contains(Variable, Value)} 1.
:- mutexGroup(MutexGroup), not {holds(Variable, Value, t) : contains(MutexGroup, Variable, Value)} 1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Activate the goal test for only the current horizon
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#program check(t).

#external query(t).
:- query(t), goal(Variable, Value), not holds(Variable, Value, t).

% Keep subsequently appended translator facts and mapping rules static.
#program base.
