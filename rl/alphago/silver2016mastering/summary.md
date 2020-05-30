[Silver, D., Huang, A., Maddison, C.J., Guez, A., Sifre, L., Van Den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M. and Dieleman, S., 2016. Mastering the game of Go with deep neural networks and tree search. nature, 529(7587), p.484.](http://deepmind-media.storage.googleapis.com/alphago/AlphaGoNaturePaper.pdf)

---

👁️

The first iteration of the AlphaGo model, the first program to defeat a human professional Go player on the full-sized board, defeating the european champion 5-0. 

**Problem:**

Even though Go is a game of perfect information, it cannot be solved by recursively computing the optimal value function in a search tree: such tree would contain $b^{d}$ states, where breadth of the game $b$ is the number of legal moves per state, and depth of the game $d$ is the game's length. Go has $b=250$ and $d=150$ so exhaustive search is not possible. Search space can be reduced by:

- reducing the depth by truncating the search tree at state $s$, and replacing the subtree by an approximate value function that estimates the outcome of the game from state $s$. This worked well for chess, checkers and othello, bu was believed to still be intractable for Go. 
- reducing the breadth by defining a pdf over actions $$P(a|s)$ and sampling from this distribution, instead of evaluating every state. Montecarlo Rollouts

**Solution:**

**Architecture:**

**Results:**

**Notes:**

---

[BACK](../index.md)

[HOME](../../../index.md)