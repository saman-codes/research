# Minimax games

Minimax games are zero-sum games where each opponent is trying to minimize the other's score, e.g. Chess, Checkers, Backgammon and Go. This gives us an implicit action function, since for each state player A will choose the action that moves her to the state with the highest value, and can assume that the opponent will choose the action that moves Player A to the state with the lowest value.

These are games of perfect information, and can be represented as a tree, where each node correspond to a state. The tree would have $b^{d}$ nodes, where $b$ is the number of legal moves per state (*breadth of the game*) and $d$ is the game length (*depth of the game*)
Trees with small branching factor can be solved by direct methods, by evaluating each state based on the implicit action function defined above, and computing the optimal value function. However in trees with high branching factor (e.g. Go, where $b=250$, and $d=150$), we can't perform exhaustive search.

We can then simplify the search by: 
- reducing the depth of the search tree at state $s$, and replacing the sub-tree with an approximate value function
- reducing the breadth of the search tree, by defining a pdf over actions $P(a|s)$ and sampling from this distribution, instead of evaluating every action $a$ (and thus each resulting state $s'$)a