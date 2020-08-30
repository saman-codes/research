[Blundell, C., Cornebise, J., Kavukcuoglu, K. and Wierstra, D., 2015. Weight uncertainty in neural networks. arXiv preprint arXiv:1505.05424](https://arxiv.org/pdf/1505.05424.pdf)

---

👁️

Introduces Bayesian Neural Networks, where each weight is a distribution instead of a fixed value. 

**Problem:**

Standard deterministic neural networks can overfit and cannot express uncertainty over regions with scarce data. 

**Solution:**

Define a NN where each weight is represented by a probability distribution, thus learning an ensemble of networks. The distribution is learned, so it models the uncertainty in the training data. It proposes an algorithm for training BNN, Bayes by Backprop.

**Architecture:**

**Results:**

**Notes:**

---

[BACK](../index.md)

[HOME](../../../index.md)