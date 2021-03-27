[Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004.pdf)
2018 - Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros

---

👁️

**Problem:**
Classic Image-to-image translation methods use loss functions that must be designed for each specific task and that lead to poor results.  

**Solution:**
Use a conditional GAN (conditioned on an input image $x$) 

**Architecture:**
UNet-based architecture for the Generator, PatchGAN inspired architecture for the Discriminator.
Generator is trained with classic adversarial loss, plus L1 norm between output image and ground truth output (this term requires paired training images)

**Results:**

**Notes:**
Interestingly they talk of GANs as learning a loss function that adapts to the data: this comes from thinking of the Discriminator itself as a loss function
[as explained here](https://medium.com/vitalify-asia/gans-as-a-loss-function-72d994dde4fb)

---

[BACK](../index.md)

[HOME](../../../index.md)