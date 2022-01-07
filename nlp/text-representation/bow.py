corpus = ["dog bites man", "man bites dog", "dog eats meat", "man eats food"]

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer().fit(corpus)
print("Our vocabulary: ", count_vect.vocabulary_)
print(count_vect.transform([corpus[0]]).toarray())
print(count_vect.transform(["dog bites man likes man"]).toarray())

count_vect = CountVectorizer(binary=True).fit(corpus) #binary events rather than integer counts
print(count_vect.transform(["dog bites man likes man"]).toarray())

###n-gram - uni, bi and tri-gram
count_vect = CountVectorizer(ngram_range=(1,3))
nbow_rep = count_vect.fit_transform(corpus)
print(f"BoN representation for '{corpus[0]}' is ", nbow_rep[0].toarray())
