:- dynamic fact_taller/2.

taller(X, Y) :- fact_taller(X, Y).
taller(X, Z) :- fact_taller(X, Y), taller(Y, Z).

% Get all people from fact_taller/2
person(X) :- fact_taller(X, _).
person(Y) :- fact_taller(_, Y).


% Define shorter as the inverse of taller
shorter(X, Y) :- taller(Y, X).

% Someone is shortest if no one is shorter than them
shortest(X) :- person(X), \+ shorter(_, X).

tallest(X) :- person(X), \+ taller(_, X).



