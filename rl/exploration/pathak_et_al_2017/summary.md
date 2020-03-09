[Pathak, D., Agrawal, P., Efros, A.A. and Darrell, T., 2017. Curiosity-driven exploration by self-supervised prediction. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops (pp. 16-17).](https://arxiv.org/pdf/1705.05363.pdf)

---

**Problem:** Extrinsic rewards sparsity, e.g. when reward is received only at goal state, but reaching goal state by pure exploration is unlikely. Existing methods that add an intrinsic reward that rewards novel states:
1) require a model of the statistical distribution of the environment, which can be hard to obtain in a high-dimensional continuous state space (such as pixel space)
2) are subject to the noisy TV problem, where an agent rewarded for prediction errors in its model of the environment will be attracted by states that are difficult to predict but not related to the agent's goals and cannot be influenced by its actions, such such as sources of noise in the environment (*distractors*)
3) don't generalize well across physically or even visually distinct states that are however functionally similar
[Schmidhuber (1991)](../schmidhuber_1991/summary.md) suggested to derive novelty-based intrinsic reward only from states that are hard to predict but learnable, but estimating learnability is difficult

**Solution:** Only reward the agent for predicting changes in the environment that are due to its actions or that relate to the agent and ignore the rest. Instead of predicting in pixel space, map to a latent space where only information that is relevant to the agent's action is represented using a proxy task of predicting action $a_{t}$ given $s_{t}$ and $s_{t+1}$. The latent features $\phi(s_{t})$ are used to train a forward dynamics model predicting $\phi(s_{t+1})$ given $\phi(s_{t})$ and $a_{t}$. The prediction error of the forward dynamics model is used as intrinsic reward.

**Results:** 

**Architecture:**


---

[HOME](../../../README.md)