[Scaling and evaluating sparse autoencoders](https://arxiv.org/pdf/2406.04093)
2024 - Leo Gao, Tom Dupré la Tour, Henk Tillman, Gabriel Goh, Rajan Troll, Alec Radford, Ilya Sutskever, Jan Leike, Jeffrey Wu

---

👁️

**Abstract**

  Sparse autoencoders provide a promising unsupervised approach for extracting
interpretable features from a language model by reconstructing activations from
a sparse bottleneck layer. Since language models learn many concepts,
autoencoders need to be very large to recover all relevant features. However,
studying the properties of autoencoder scaling is difficult due to the need to
balance reconstruction and sparsity objectives and the presence of dead
latents. We propose using k-sparse autoencoders [Makhzani and Frey, 2013] to
directly control sparsity, simplifying tuning and improving the
reconstruction-sparsity frontier. Additionally, we find modifications that
result in few dead latents, even at the largest scales we tried. Using these
techniques, we find clean scaling laws with respect to autoencoder size and
sparsity. We also introduce several new metrics for evaluating feature quality
based on the recovery of hypothesized features, the explainability of
activation patterns, and the sparsity of downstream effects. These metrics all
generally improve with autoencoder size. To demonstrate the scalability of our
approach, we train a 16 million latent autoencoder on GPT-4 activations for 40
billion tokens. We release training code and autoencoders for open-source
models, as well as a visualizer.


**Problem:**
Increase sparsity of the latent representation of SAEs trained on NN activations. 
Previous approaches add the L1 norm of the latent activations as penalty to the loss, but this adds a difficult to select hyperparameter to the training, the relative weight of the L1 penalty vs the MSE term of the loss.

**Solution:**
Select the top-K activations of the sparse latent vector, and zero out the rest

**Architecture:**


**Results:**
Better sparsity, better training stability


**Notes:**
Neurons are generally polysemantic. SAEs attempt to induce neuron monosemanticity by passing the activations of a nn layer through an autoencoder where the latent dimension is much larger than the input dimension. Having a latent dimension larger than the input dimension induces representational sparsity, which I also interpret as reducing polysemanticity/increasing monosemanticity by increasing the capacity of the nn. This works because, as the [Anthropic series](https://transformer-circuits.pub/2022/toy_model/index.html) shows, polisemanticity is a function of network capacity, where more frequent concepts are assigned monosemantic neurons, and less frequent/important concepts are assigned polysemantic neurons.

---

[BACK](../index.md)

[HOME](../../../index.md)
