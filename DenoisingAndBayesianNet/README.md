Author: ***Nishank Raisinghani***

Date: ***12/30/2022***

Project: ***Using UNet autoencoder to denoise Brain Tumor MRIs and measure efficacy of these results by using Bayesian Neural Network.***

Brain Tumor MRIs of 4 classifications: glioma, meningioma, pituitary, and no tumor. Data sourced from kaggle dataset. Applied red noise to these images (to see more about red noise read https://nickraisgit.github.io/paper.pdf). Used UNet autoencoder to clean the noisy images. Built and trained a Bayesian Neural Network to display probability distributions of tumor predictions of noisy images, denoised images, and original images. All of this data that was predicted by the Bayesian Network were part of a holdout set that neither of the models saw during training, in an attempt to simulate real world situations. Comparing results, the denoised images had much less uncertainty in the classification than the noisy images, and were very close to the original images as well. This goes to show how well the UNet denoised these images. 