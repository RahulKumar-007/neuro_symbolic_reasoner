:- dynamic fact_mother/2, fact_father/2, fact_male/1, fact_female/1, fact_spouse/2.

% Base facts
mother(X, Y) :- fact_mother(X, Y).
father(X, Y) :- fact_father(X, Y).
male(X) :- fact_male(X).
female(X) :- fact_female(X).
spouse(X, Y) :- fact_spouse(X, Y); fact_spouse(Y, X).  % Spouse relation is symmetric

% Basic relations
parent(X, Y) :- mother(X, Y).
parent(X, Y) :- father(X, Y).

% Child relations
child(X, Y) :- parent(Y, X).
son(X, Y) :- child(X, Y), male(X).
daughter(X, Y) :- child(X, Y), female(X).

% Sibling relations
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).

% Half-siblings: share one parent but not both
half_sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y,
                       parent(P1, X), parent(P2, Y),
                       P1 \= Z, P2 \= Z, P1 \= P2.

% Step-siblings: parents are married but not biologically related
step_sibling(X, Y) :- parent(P1, X), parent(P2, Y),
                       spouse(P1, P3), spouse(P2, P4),
                       P3 \= P1, P4 \= P2,
                       \+ parent(P1, Y), \+ parent(P2, X).

% Grandparent relations
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- grandparent(X, Y), male(X).
grandmother(X, Y) :- grandparent(X, Y), female(X).

% Grandchild relations
grandchild(X, Y) :- grandparent(Y, X).
grandson(X, Y) :- grandchild(X, Y), male(X).
granddaughter(X, Y) :- grandchild(X, Y), female(X).

% Aunt/Uncle relations
aunt(X, Y) :- parent(Z, Y), sister(X, Z).
aunt(X, Y) :- parent(Z, Y), brother(W, Z), spouse(X, W), female(X).
uncle(X, Y) :- parent(Z, Y), brother(X, Z).
uncle(X, Y) :- parent(Z, Y), sister(W, Z), spouse(X, W), male(X).

% Niece/Nephew relations
niece(X, Y) :- aunt(Y, X), female(X).
niece(X, Y) :- uncle(Y, X), female(X).
nephew(X, Y) :- aunt(Y, X), male(X).
nephew(X, Y) :- uncle(Y, X), male(X).

% Cousin relations
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).
first_cousin(X, Y) :- cousin(X, Y).

% In-law relations
parent_in_law(X, Y) :- parent(X, Z), spouse(Z, Y).
mother_in_law(X, Y) :- mother(X, Z), spouse(Z, Y).
father_in_law(X, Y) :- father(X, Z), spouse(Z, Y).
child_in_law(X, Y) :- spouse(X, Z), parent(Y, Z).
son_in_law(X, Y) :- child_in_law(X, Y), male(X).
daughter_in_law(X, Y) :- child_in_law(X, Y), female(X).
sibling_in_law(X, Y) :- sibling(X, Z), spouse(Z, Y).
sibling_in_law(X, Y) :- spouse(X, Z), sibling(Z, Y).
brother_in_law(X, Y) :- sibling_in_law(X, Y), male(X).
sister_in_law(X, Y) :- sibling_in_law(X, Y), female(X).

% Ancestor and descendant relations
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
descendant(X, Y) :- ancestor(Y, X).
