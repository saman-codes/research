[Choi, Y., Choi, M., Kim, M., Ha, J.W., Kim, S. and Choo, J., 2018. Stargan: Unified generative adversarial networks for multi-domain image-to-image translation. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 8789-8797).](https://arxiv.org/pdf/1912.01865.pdf)

---

👁️

**Problem:**

Translating images between *k* domains requires training *k(k-1)* generators:
- this is inefficient
- each generator has access to data between only two domains, so global features (e.g. face shapes) cannot be used efficiently

**Solution:**

Translate between *k* domains using a single generator and discriminator. 

**Results:**

**Architecture:**

---

[BACK](../index.md)

[HOME](../../../index.md)