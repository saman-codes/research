[Unsupervised Anomaly Detection with Generative Adversarial Networks to Guide Marker Discovery](https://arxiv.org/pdf/1703.05921.pdf)
2017 - Thomas Schlegl, Philipp Seeböck, Sebastian M. Waldstein, Ursula Schmidt-Erfurth, Georg Langs

---

👁️

**Problem:**

Unsupervised discovery of anomalies in OCT scans

**Solution:**

Train a GAN $G(z)$ to learn the manifold of healthy image patches. randomly extracted from training images. Given a test image $x$, which could either be healthy or unhealthy, use an iterative method to find the latent vector $z'$ such that $G(z') = x'$, where $x'$ is the projection of $x$ on the manifold of healthy images (i.e. $x'$ corresponds to how $x$ would look like if it was coming from a healthy patient).

**Architecture:**

The generator $G(z)$ is first trained on healthy image patches. The latent vector $z'$ such that $G(z')$ is the healthyfied version of input image $x$ is found by backpropagating a loss directly to $z_{i}'$, to obtain $z_{i+1}$.

The loss used for backpropagation to the latent vector is composed of two terms:

- Residual loss: $L_{r}(z_{i}) = \sum |x-G(z_{i})|$
  - Forces the latent vector $z_{i}$ to generate an image similar to the input image
- Discrimination loss: $L_{d}(z_{i}) = \sum |f(x) - f(G(z_{i}))|$ where $f(\cdot)$ is the output of an intermediate layer of the Discriminator
  - This is an adapted Discrimination loss, the usual one uses the output of the Discriminator instead

It also defines an anomaly score to assess how anomalous a patch is.

**Results:**

**Notes:**

First approach I know of using GANs for unsupervised anomaly detection on OCT data. The iterative approach to find the latent vector is very slow though, so f-AnoGAN improves on this by getting that vector through a network, so in a single feedforward pass.

---

[BACK](../index.md)

[HOME](../../../index.md)
