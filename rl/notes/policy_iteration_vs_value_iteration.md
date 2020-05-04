Value Iteration and Policy Iteration are two algorithms for solving MDP. 

Both are cases of [Generalized Policy Iteration](http://incompleteideas.net/sutton/book/ebook/node46.html), which refers to the idea of alternating between updating the estimate of the value function by making it consistent with the current policy (Policy Evaluation) and improving the policy based on the current value function, by acting greedily with respect to it (Policy Improvement).

Both require a one-step lookahead, so from state s we evaluate all possible rewards in the next state s', add the discounted value of state s', and weight each path by its probability. In other words, VI and PI both require knowing the transition probabilities of each state s' from state s, in order to calculate the expected value of the reward + discounted V(s') combination. 

The value of state s, $V(s)$, is defined as the expected value over $P(s'|s,a)$ of $R(s') + \gamma V(s')$: this is the Bellman equation/update, defining the value of a state as the expected value of the immediate reward in the next state plus the discounted value of the next state.
$$
V_{t+1}(s) = \sum_{s'} P(s'| a, s)[R(s,a, s') + \gamma V_{t}(s')]
$$

Remembering that the value of a state $V(s)$ is defined as the expected sum of future rewards from state s.

**Value Iteration** is an iterative algorithm for finding values of V(s) (that is, the Value Function). The only difference versus the Bellman equation above is that instead of using all the values of s' in the expectation we only use the one that has the highest value $V(s')$, by taking the max over the actions available in $s$. That is, instead of the weighted sum of $n$ values (where $n$ is the number of actions available in state $s$), we use only a single value to update our estimate of the value of state $s$:

$$
V_{t+1}(s) := max_{a} ( \sum_{s'} P(s' | a, s)[R(s,a, s') + \gamma V_{t}(s')] )
$$

The value function is updated at each iteration, but the policy is extracted only once at the end, when the optimal value function has been learned. However at each iteration we need to evaluate $\sum_{s'} P(s' | a, s)[R(s,a, s') + \gamma V_{t}(s')]$ for all actions in order to take the $max()$, which is inefficient.

**Policy Iteration** instead is composed of two parts: policy evaluation and policy improvement. In policy evaluation, the value function $V(s)$ is computed, using the Bellman update above. Once $V_{t}(s)$ is updated into $V_{t+1}(s)$, the policy is updated with respect to the new value function: the new policy $\pi(s)$ is the greedy policy over $V_{t+1}$, so the iterative update for the value and policy functions are:

Policy evaluation:
$$
V_{t+1}(s) := \sum_{s'} P(s'| \pi(s), s)[R(s,a, s') + \gamma V_{t}(s')]
$$
Policy improvement:
$$
\pi(s) := argmax_{a} \sum_{s'} P(s'| a, s)[R(s,a, s') + \gamma V(s')]
$$

So the only difference between the two algorithms is in the formula for updating our estimate of the value function $V(s)$: VI uses a max over actions available in state $s$, thus using a single value, while PI takes the full expectation over states s', thus using an expectation over possible value . 