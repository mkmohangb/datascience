import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

corpus = ["dog bites man", "man bites dog", "dog eats meat", "man eats food"]
#['bites', 'dog', 'eats', 'food', 'man', 'meat']
tfidf = TfidfVectorizer()
output = tfidf.fit_transform(corpus)
#print(sorted(tfidf.vocabulary_, key=tfidf.vocabulary_.get), tfidf.idf_)
print(tfidf.get_feature_names(), tfidf.idf_)
print(output.toarray())
pred = tfidf.transform(["dog man dog"]) #with word frequency 2
print(pred.toarray())

## manual calculation
dog_idf = 1 + np.log((1+4)/(1+3)) # add 1 to num & denom
bites_idf = 1 + np.log((1+4)/(1+2))
man_idf = 1 + np.log((1+4)/(1+3))
print(normalize([[bites_idf, dog_idf, 0, 0, man_idf, 0]])) #default is l2 norm