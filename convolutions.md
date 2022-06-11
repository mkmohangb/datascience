### Depthwise Separable Convolutions

  - https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1
  - https://towardsdatascience.com/a-basic-introduction-to-separable-convolutions-b99ec3102728
      - the main difference is this: in the normal convolution, we are transforming the image 256 times. And every transformation uses up 5x5x3x8x8=4800 multiplications. In the separable convolution, we only really transform the image once — in the depthwise convolution. Then, we take the transformed image and simply elongate it to 256 channels. Without having to transform the image over and over again, we can save up on computational power.
        - 12x12x3 — (5x5x3x256) →12x12x256 (normal) - 256x3x5x5x8x8=1,228,800 multiplications
        - 12x12x3 — (5x5x1x1) — > (1x1x3x256) — >12x12x256 (depthwise) - 3x5x5x8x8 = 4,800 + 256x1x1x3x8x8 = 49,152 => 53,952 multiplications
      - Are the disadvantages to a depthwise separable convolution? Definitely! Because it reduces the number of parameters in a convolution, if your network is already small, you might end up with too few parameters and your network might fail to properly learn during training. If used properly, however, it manages to enhance efficiency without significantly reducing effectiveness, which makes it a quite popular choice.
      

