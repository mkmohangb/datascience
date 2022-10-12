[Movement science needs different pose tracking algorithms](https://arxiv.org/abs/1907.10226) 2019

1. Current pose tracking algorithms fall short of the needs of movement science
    - metrics currently used for evaluating pose tracking algorithms use noisy hand-labeled ground truth data
    - do not prioritize precision of relevant variables like three-dimensional position, velocity, acceleration, and forces



<img width="513" alt="Screenshot 2022-10-12 at 12 30 46 PM" src="https://user-images.githubusercontent.com/2610866/195272416-65a419e7-a9a7-476e-b8d4-9a486333f33f.png">


2. Pose tracking provides the opportunity to conduct studies on people of all sexes, shapes, sizes, and ages
3. Pose tracking algorithms need to estimate different movement quantities
    - consecutive time frames are treated as statistically independent
    - ground truth data benchmarks currently used do not include quantities important to movement science like velocity, acceleration, and forces
    - benchmark datasets do not consist of the types of movements encountered in movement science
    
      * _Three-dimensional position, velocity and acceleration_ => To diagnose progress in a patient with a movement disorder, measures of the three-dimensional kinematics are analyzed. While more and more pose tracking algorithms are recently aiming for three-dimensional estimates, still fewer incorporate tracking in time to improve pose estimates i.e. using the past and future movements to improve localization of pose in a given frame. Frame-to-frame tracking errors of the kind shown in Figure 2b ii will lead to even larger errors in velocity and acceleration upon numerical differentiation. Skeletal motion naturally creates a hierarchical dependency structure that results in spatial (joint location) and temporal (laws of motion) constraints. Thus, if you know the position, velocity, acceleration, and skeletal shape from the past few frames, then you can build a strong prior for the next frame.
      
      * _External contact forces_ =>  For many applications, quantifying the external forces involved in a movement is important. After all, the external forces determine the stress on bones and joints which relate to injury. Given the importance of external force measurements for movement science, their estimation should be prioritized by the pose tracking algorithms and competitions.
      * _Absolute mass, length and inertia_ => Estimates of true whole-body as well as body segment mass and size are necessary for movement science. Estimation of mass and size of individuals is important for understanding how movements differ in people of different body types. The mass and inertia measures of body segments are needed to estimate internal forces and torques and to identify the joints that contribute to a given movement. The best one could do with existing pose tracking algorithms is to obtain the relative size of one segment with respect to other ones. One way to rectify this is by using computer vision to estimate the true size and scale of a known object in the background and use this information to estimate the size of the person or animal in the image. The estimates of absolute mass and inertia can then be made using standard cadaveric length-mass and length-inertia regressions.
      
      * _Pose tracking with task and subject generality_ => Infants have a comparatively larger torso and head while elderly individuals often have a hunched posture and use walkers or crutches; these body configurations are less typically seen in the image datasets used to train pose tracking models. we show an example of this where the pose estimation algorithms completely fails to detect an upside-down gymnast while still detecting a sitting human with similar amounts of blur, likely due to not being exposed to training data that contains a gymnast mid-task.
      
      * _Body contact and partial occlusion_ => These issues with not detecting contact and partial occlusions can be dealt with, for instance, by creating training examples by augmenting ground truth data such that individuals from distinct images are artificially brought in contact or occluded, to train the algorithms to better detect such scenarios.
      
      * _Fixed frame of reference_ => the estimates of body motion need to be in a fixed frame of reference. For example, what matters for understanding the progress of an individual undergoing physiotherapy is the knee angle in the body’s frame of reference not in the camera frame of reference.
     


 
 <img width="818" alt="Screenshot 2022-10-12 at 12 32 36 PM" src="https://user-images.githubusercontent.com/2610866/195272722-59f81496-000b-4da6-94cf-2aff8641f761.png">
