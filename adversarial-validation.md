## [Adversarial Validation](https://blog.zakjost.com/post/adversarial_validation/)

Build a classifer to predict which data rows come from training set and which are from the test set.  If the two datasets came from the same distribution, this should be impossible. But if there are systematic differences in the feature values of your training and test datasets, then a classifier will be able to successfully learn to distinguish between them. The better a model you can learn to distinguish them, the bigger the problem you have.

But the good news is that you can analyze the learned model to help you diagnose the problem. And once you understand the problem, you can go about fixing it.
