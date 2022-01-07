corpus = ["Dog bites man", "Man bites dog", "Dog eats meat", "Man eats food"]
import numpy as np
#One hot encoding from scratch
def create_vocab(documents):
    vocab_words = {word.lower() for doc in documents for word in doc.split()}
    vocab = {}
    count = 0
    for word in sorted(vocab_words):
        count += 1
        vocab[word] = count
    return vocab

def get_onehot_encoding(vocab, doc):
    onehot_enc = []
    for word in doc.split():
        word = word.lower()
        enc = [0] * len(vocab)
        if word in vocab:
            enc[vocab[word] - 1] = 1
        onehot_enc.append(enc)
    return np.array(onehot_enc)

vocab = create_vocab(corpus)
print("from scratch")
print("vocabulary: ", vocab)
print(f"one-hot encoding for '{corpus[1]}' is \n", get_onehot_encoding(vocab, corpus[1]))
print("")

#One hot encoding using scikit-learn
print("using scikit-learn")
from scipy import sparse
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
corpus_lower = [doc.lower() for doc in corpus]
onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoder.fit([[v] for v in vocab.keys()])
print("categories:", onehot_encoder.categories_)
print(f"one-hot encoding for '{corpus[1]}' is \n", onehot_encoder.transform([[word.lower()] for word in corpus[1].split()]))
