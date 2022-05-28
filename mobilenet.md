## MobileNet

[V1 2017](https://arxiv.org/abs/1704.04861)
  - Depthwise separable convolutions
  
[V2 2018](https://arxiv.org/abs/1801.04381)
  - introduces two new features to the architecture: 
    1) linear bottlenecks between the layers, and 
    2) shortcut connections between the bottlenecks
    
[V3 2019](https://openaccess.thecvf.com/content_ICCV_2019/papers/Howard_Searching_for_MobileNetV3_ICCV_2019_paper.pdf)
  - harness multiple network architecture search algorithms as well as advances in network design and adapt nonlinearities like **swish** and apply **squeeze and excite** in a quantization friendly and efficient manner
    1) introducing lightweight attention modules based on squeeze and excitation into the bottleneck structure (from MnasNet)
    2) Layers are also upgraded with modified swish nonlinearities (hard sigmoid)
    3) platform-aware NAS to search for the global network structures by optimizing each network block. NetAdapt algorithm to search per layer for the number of filters.

### References
  - [MobileNet v2 Google ai blog](https://ai.googleblog.com/2018/04/mobilenetv2-next-generation-of-on.html)
  - [MnasNet](https://openaccess.thecvf.com/content_CVPR_2019/papers/Tan_MnasNet_Platform-Aware_Neural_Architecture_Search_for_Mobile_CVPR_2019_paper.pdf)
  - [NetAdapt](https://openaccess.thecvf.com/content_ECCV_2018/papers/Tien-Ju_Yang_NetAdapt_Platform-Aware_Neural_ECCV_2018_paper.pdf)
