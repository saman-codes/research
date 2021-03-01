[CollaGAN : Collaborative GAN for Missing Image Data Imputation](https://arxiv.org/pdf/1901.09764.pdf)
2019 - Dongwook Lee, Junyoung Kim, Won-Jin Moon, Jong Chul Ye

---

👁️

**Problem:**
Missing data imputation in image datasets: when we have images for a given subject for N-1 domains, and we want to generate the remaining domain using image to image translation. Methods like CycleGAN require training N(N-1) generators to learn mapping across N domains, while StarGAN is trained by sampling a translation between only two domains at a time instead of using the images from all other domains (in this imputation problem, we use data from N-1 domains to impute the remaining domain for a given subject)

**Solution:**
The Generator takes as input images from N-1 domains and outputs an image from the remaining domain. Adapts the cycle-consistency loss to use multiple combinations of inputs in the cycle 

**Architecture:**
Uses a multiple cycle-consistency loss, using different combinations of the input domains. Generator and discriminator use Least Squares adversarial loss.
Discriminator also uses has a domain classification head trained with Cross Entropy loss: interestingly they mention that they train the classifier head of D on real data only in order to learn a proper classifier, then they freeze the classification head to get the loss used to train the generator.
Finally, it uses the Structural Similarity Index Loss as an additional multiple cycle consistency loss

**Results:**

**Notes:**

---

[BACK](../index.md)

[HOME](../../../index.md)