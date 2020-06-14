[Choi, Y., Choi, M., Kim, M., Ha, J.W., Kim, S. and Choo, J., 2018. Stargan: Unified generative adversarial networks for multi-domain image-to-image translation. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 8789-8797).](https://arxiv.org/pdf/1912.01865.pdf)

---

👁️👁️

**Problem:**

Translating images between *k* domains requires training *k(k-1)* generators:
- this is computationally inefficient
- each generator has access to data between only two domains, so global features (e.g. face shapes) cannot be used efficiently, which lowers image quality


**Solution:**

Translate between *k* domains using a single generator and discriminator. Instead of learning the mapping from one domain to the next, add domain information as input to the generator, together with the input image. Also introduces a method to use a mask vector as input that allows them to train with data from datasets with different labels.

**Architecture:**

Single generator G; discriminator D outputs one probability distribution over Real/Fake and one over domain, so D has one 0-1 regression head and one classifier head. Loss is a combination of:

- Adversarial loss $L_{adv}$: standard GAN loss 
- Domain classification loss $L_{cls}$: error of domain classification, a simple negative log loss. This loss is different for D and G: D gets the error signal from classifying real images to real domain c' (from the dataset), while G gets the error signal from D classifying fake images into target domain c.
- Reconstruction loss $L_{rec}$: enforces the constraint that the generated image is similar to the input image. It only applies to G. Uses Cycle-consistency loss, which is the L1 norm of the difference between the input image x from domain c' and the generated image y of domain c after it's passed back into the generator and translated back into domain c': 

$$
L_{rec} = \mathbb{E}[f(x)]_{x, c, c'}[||x- G(G(x,c),c') ||_{1}]
$$

The combined losses are: 
$$
L_{D} = -L_{adv} + \lambda_{cls} L_{cls}^{r} 
$$
$$
L_{G} = L_{adv} + \lambda_{cls} L_{cls}^{f} + \lambda_{rec}L _{rec}  
$$

For the input class labels, it concatenates label vectors from different datasets and adds a one-hot vector entry to indicate which dataset the input image belongs to. This allows it to use input images from different datasets, that have different classes and couldn't be used together otherwise. They only use 2 datasets, so each class label is binary and the dataset indicator is also binary. Indicators for classes not present in a dataset are set to 0.  
  
It uses Wasserstein loss with Gradient penalty for training.
G has two con layers and 2 transposed conv layers for upsampling, and instance normalisation. 
D uses PatchGAN and has no normalisation

**Results:**

Compares with DIAT, IcGAN and CycleGAN on an attribute transfer task (using CelebA dataset) and on a facial expression synthesis task (using RaFD dataset). First task: performs better following an evaluation on Mechanical Turk. Second task: it says that it performs better in qualitative evaluation (but don't specify methodology for assessing that), while for quantitative evaluation it uses a pretrained ResNet to classify facial expressions in generated images, and StarGAN obtains lowest classification error or all models.

Also important, StarGAN has 14 times fewer parameter than CycleGAN, since it uses a single generator.

Finally, it jointly trains the model on both datasets at the same time using the mask vector input. it compares this with the model trained on a single dataset on facial expression syntesis on CelebA, which doesn't have facial expression labels, finds that the training with joint datasets performs much better, as it allows G to learn low-level features from both sets. 

It shows also that the model properly learns to ignore certain classes depending on which dataset indicator is switched on in the mask vector: if I understand correctly, they switch the indicator for the facial expression dataset off and try to translate the input image to different facial expressions, failing to do so (the input image is instead turned from young to old). When the proper dataset indicator is switched on, G transfers facial expressions successfully.


**Notes**

- Really cool approach, using a single generator and discriminator to perform multi-domain translation, getting really good quality images with way fewer parameters than CycleGAN
- This paper is the starting point for the improvement in [Fixed-point GAN](../siddiquee_et_al_2019/summary.md)
- There's an updated version of this model, StarGAN 2


---

[BACK](../index.md)

[HOME](../../../index.md)