##
- [Mathews Correlation Coefficient](https://towardsdatascience.com/the-best-classification-metric-youve-never-heard-of-the-matthews-correlation-coefficient-3bf50a2f3e9a)
    - MCC takes into account all four values in the confusion matrix, and a high value (close to 1) means that both classes are predicted well, even if one class is disproportionately under- (or over-) represented.
    
##
- [Probability Calibration Imbalanced dataset](https://machinelearningmastery.com/probability-calibration-for-imbalanced-classification/)
    - Calibrated Probabilities. Probabilities match the true likelihood of events.
    - Uncalibrated Probabilities. Probabilities are over-confident and/or under-confident.
  - There are two main causes for uncalibrated probabilities; they are:
      - Algorithms not trained using a probabilistic framework.
          - algorithms that provide calibrated probabilities include: Logistic Regression, LDA, Naive Bayes, Artificial Neural Networks.
          - algorithms that require their “probabilities” to be calibrated prior to use: SVM, Decision Trees & Ensembles like RF, GBM, k-NN.
      - Biases in the training data - A bias in the training dataset, such as a skew in the class distribution, means that the model will naturally predict a higher probability for the majority class than the minority class on average.

##
- [Skip connections](https://theaisummer.com/skip-connections/)
    - vanishing gradient problem in the early layers because of the way backpropagation is done
    - Skip connection 
        - provides an alternative path for the gradient.
        - also allow the later layers to learn from the information that was captured in the initial layers(lower semantic information extracted from the input). 
    - Two ways to use it:
        - **addition** as in residual architectures
        - **concatenation** as in densely connected architectures - maximum information flow between layers in the network
        - short skip connections - used along with consecutive conv. layers like in Resnet
        - long skip connections - used in encoder-decoder architecture 
    - loss landscape changes significantly when introducing skip connections

##
- [Receptive field](https://theaisummer.com/receptive-field/)
    - key parameter to map output feature to input region, defined as size of the region in the input that produces the feature.
