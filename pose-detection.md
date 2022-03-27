## Pose Estimation
| Paper | Year | Training data | Keypoints | Training | Inference |
| ----- |------|---------------|-----------|----------|-----------|
| Joint Training of a Convolutional Network and a Graphical Model for Human Pose Estimation | 2014 | LSP/FLIC | 14 |
| Convolutional Pose Machines | 2016 | MPII/LSP/FLIC | 16 |
| Stacked Hourglass Networks for Human Pose Estimation | 2016 | MPII/FLIC | 16 | MSE loss is applied comparing the predicted heatmap (16 x 64 x 64) to a ground-truth heatmap consisting of a 2D-gaussian (with S.D of 1 px) centered on the joint location.| For generating final test predictions we run both the original input and a flipped version of the image through the network and average the heatmaps together (accounting for a 1% average improvement on validation). The final prediction of the network is the max activating location of the heatmap for a given joint.
| Human pose estimation via Convolutional Part Heatmap Regression | 2016 | MPII/LSP | 16 |
|  Mask R-CNN | 2017 | COCO | 17 |
| Towards Accurate Multi-person Pose estimation in the Wild | 2017 | COCO/Private | 17 |
| Exploiting Offset-guided Network for Pose Estimation and Tracking | 2019 | COCO/PoseTrack | 17 |
| BlazePose | 2020 | Private | 33 |
