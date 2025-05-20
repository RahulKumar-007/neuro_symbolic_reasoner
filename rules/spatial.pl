:- dynamic fact_left_of/2.

% Base rule
left_of(X, Y) :- fact_left_of(X, Y).

% Transitive rule
left_of(X, Z) :- fact_left_of(X, Y), left_of(Y, Z).

% Right-of is the inverse of left-of
right_of(X, Y) :- left_of(Y, X).

% Define all objects
object(X) :- fact_left_of(X, _).
object(Y) :- fact_left_of(_, Y).

% X is the leftmost if no object is to its left
leftmost(X) :- object(X), \+ left_of(_, X).

