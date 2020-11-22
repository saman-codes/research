[Arjovsky, M., Chintala, S. and Bottou, L., 2017. Wasserstein gan. arXiv preprint arXiv:1701.07875.](https://arxiv.org/pdf/1701.07875.pdf)

---

👁️ (skimmed paper, skimmed [summary article](https://lilianweng.github.io/lil-log/2017/08/20/from-GAN-to-WGAN.html), [implementation article](https://developers.google.com/machine-learning/gan/loss))

The introduction has a good discussion of generative models in general. 
There's an interesting observation on why we need to add noise to these models, which I don't fully understand.
Also, a discussion  of the advantages of VAE and GANs over other types of generative models: instead of learning a density directly, they learn a parameterised function mapping from a noise vector to the target distribution.

- Learning a high-dimensional density directly fails to represent distributions that are constrained to a lower-dimensional manifold: using a low-dimensional input noise vector constrains the learned distribution to lie on a lower-dimensional manifold (the constrain is given by the lower dimensionality of the noise vector)
- Generating samples from an arbitary high-dimensional density is computationally difficult. Mapping a noise vector to a datapoint through a learned function will not give the correct numerical value of the density, but this is generally less important than generating samples, which can be done efficiently with the noise vector approach. 

**Problem:**

GAN training is very unstable and difficult. There are several references to a theoretical investigation by the same authors of why it is so [(Arjovsky and Bottou 2017)](../arjovsky_and_bottou_2017/summary.md)

**Solution:**

Propose a new distance measure between the generative distribution and the target (real data) distribution, the Wassertein's distance, an approximation of the Earth Mover distance.

Earth Mover distance: 
![](../arjovsky_et_al_2017/arjovsky_et_al_2017_distance_1.png)

Intuitively, it represents the amount of work required to move mass from one distribution to the other.
It's proportional to the amount of mass to be moved and to the distance between the two distributions.

**Results:**

A theoretical analysis of the Earth Mover (EM) distance

Empirical results on training GANs with Wassertein's distance:

- doesn't require balance in training between generator and discriminator
- doesn't require careful design of network architecture
- reduces mode collapse
- gives the ability to estimate EM distance by training the discriminator; EM distance correlates with observed sample quality

According to [implementation article](https://developers.google.com/machine-learning/gan/loss), they also avoid problems with vanishing gradients, and that EM distance, unlike Cross Entropy, is a true measure of distance in space of probability distributions 

**Architecture:**

From the [implementation article](https://developers.google.com/machine-learning/gan/loss) (the actual paper is a bit technical, I'm not understanding everything):

- The discriminator outputs an arbitrary scalar instead of a probability: D(x) and D(G(z)) can be < 0 and > 1
- The discriminator is trained to make the difference between the value for real and fake instances large
- The discriminator is called *critic* instead of *discriminator*, since it cannot actually discriminate between real and fake instances, it just assigns an arbitrary value to each
- Critic and Generator maximize the following functions:
  - Critic: **D(x) - D(G(z))**
  - Generator: **D(G(z)) **
- Apparently, theoretical justification requires that the weights are clipped in the GAN to constrain them to a constrained range 

---

[BACK](../index.md)

[HOME](../../../index.md)