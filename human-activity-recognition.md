## Graph NNs
  - https://distill.pub/2021/gnn-intro/
  - https://theaisummer.com/graph-convolutional-networks/
  - [Pytorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)
  - [GNN Playlist](https://www.youtube.com/watch?v=OI0Jo-5d190&list=PLSgGvve8UweGx4_6hhrF3n4wpHf_RV76_)
  - [GCN example](https://blog.zakjost.com/post/gcn_citeseer/)

## Existing approaches for Human Activity Recognition

[Spatial Temporal Graph Convolutional Networks (ST-GCN) for Skeleton-Based Action Recognition](https://github.com/yysijie/st-gcn)
<img width="717" alt="st-gcn" src="https://user-images.githubusercontent.com/2610866/169747079-201a86e3-9e50-4e4b-91ef-bb0e703b89e7.png">

[Two-Stream Adaptive Graph Convolutional Networks for Skeleton-Based Action Recognition](https://github.com/open-mmlab/mmaction2/blob/master/configs/skeleton/2s-agcn/README.md)

<img width="669" alt="2s-agcn" src="https://user-images.githubusercontent.com/2610866/169750248-1bc1634a-3340-4bb9-a805-a22c0aa18924.png">

[Revisiting skeleton-based action recognition](https://arxiv.org/pdf/2104.13586.pdf)

<img width="688" alt="poseconv3d" src="https://user-images.githubusercontent.com/2610866/169755849-79d1cd1e-a8be-42b9-a75e-630d0738d16d.png">


[MoViNets: Mobile Video Networks for Efficient Video Recognition](https://arxiv.org/abs/2103.11511)
  - Run TuNAS on Kinetics 600 and results reported on the datasets Kinetics 400, Kinetics 700, Moments in Time, Charades and Something Somthing V2.
  - Stream buffer with Causal operations
  - Cumulative Global Average Pooling (CGAP)
  - **CausalSE** with Positional Encoding
  - **ReZero** by applying zero-initialized learnable scalar weights that are multiplied with features before the final sum in a residual block.
  - similar to ResNet-D where we apply 1x3x3 spatial average pooling before the convolution to improve feature representations.
  - (2+1)D architectures, splitting up any 3D depthwise convolutions into a 2D spatial convolution followed by a 1D temporal convolution. We show that trivially changing a 3D architecture to (2+1)D decreases FLOPs while also keeping similar accuracy



## Datasets

  - [FineGym](https://sdolivia.github.io/FineGym/)
  - [ActivityNet](http://activity-net.org/)
  - [HVU](https://competitions.codalab.org/competitions/29546)
