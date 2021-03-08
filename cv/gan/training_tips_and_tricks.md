# Training tips and tricks for GANs

- Adding capacity in the form of more convolutional filters might not help reducing G loss, even when D loss is near zero [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- Early stopping might lead to a suboptimal solution, as losses are quite volatile [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- There doesn't seem to be a great difference across loss functions, when it comes to convergence, so it's best to first try using the simplest one [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- G and D updates should be balanced: having multiple updates of one per update of the other is unlikely to increase training stability [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- Lowering the learning rate can help with mode collapse [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- Adding noise to both real and fake images can increase training stability by complicating D training [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- Use Label Smoothing: replace 0-1 labels with real values in an interval (e.g. give true images a label $0.7<y<1.2$ and fake images a label $<y< 0.3$),  [[source]](https://arxiv.org/pdf/1606.03498.pdf)

- Multiscale Gradient GAN architecture can be used to generate high-resolution images, by adding skip connections concatenating images at progressively increasing resolutions to both G and D [[source]](https://arxiv.org/pdf/1903.06048.pdf)

- Choose a higher learning rate for D than for G (see Two Time-Scale Update Rule) [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)

- Use spectral normalisation [[source]](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)


- [GANHacks repo](https://github.com/soumith/ganhacks)
- [Salimans et al. 2016, Improved techniques for training GANS](https://arxiv.org/pdf/1606.03498.pdf)