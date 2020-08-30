### Improvements to Fixed-point GAN
- Cycle consistency loss seems to lead to forse image translations, since it leaves traces of the original image are left in the translated image, to help reconstruction (Nizan and Tal 2020)
- It is unable to remove large items from image (e.g. glasses) (Nizan and Tal 2020)
- It is unable to translate across domains that require large shape changes (e.g. turning photorealistic portraits into anime painting) (Nizan and Tal 2020)
- FPGan is generates a difference mask, instead of a whole new image, which might limit the ability to generate images with deformations (see Wolleb et al 2020)

CouncilGAN (Nizan and Tal 2020) replaces the Cycle Consistency loss with multiple Generators.

DeScarGAN (Wolleb et al 2020) keeps the same loss as FPGan but modifies the architecture of G and D, with skip connections for G and with a multihead network for D. Also, it generates a complete image instead of an additive map.