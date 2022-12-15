




![image](https://user-images.githubusercontent.com/2610866/207792897-3b791f6f-cdd4-4a6a-8092-a61db8f5f0f3.png)


Diffusion models are inspired by non-equilibrium thermodynamics (how perfume molecules in high concentration diffuse to other areas in sapce to reach equilibrium state). They define a Markov chain of diffusion steps to slowly add random noise to data and then learn to reverse the diffusion process  to construct desired data samples from the noise. Diffuse more & more noise... Diffusion model reverses the Diffusion process.

Unlike VAE or flow models, diffusion models
  - are learned with a fixed procedure (??)
  - latent variable has high dimensionality

Stable Diffusion introduced in the paper "High-Resolution Image Synthesis with Latent Diffusion Models".
Diffusion process happens in the Latent space instead of image space.


![image](https://user-images.githubusercontent.com/2610866/207803720-8b938185-1697-4623-aea3-ae7cec694597.png)


## References
 
  - https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
  - https://github.com/CompVis/latent-diffusion
  - [Fast AI Lesson 9](https://www.youtube.com/watch?v=_7rMfsA24Ls)
  - [Fast AI Lesson 10](https://www.youtube.com/watch?v=6StU6UtZEbU)
