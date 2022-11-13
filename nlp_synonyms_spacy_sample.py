#https://towardsdatascience.com/how-to-build-a-fast-most-similar-words-method-in-spacy-32ed104fe498
#https://www.sean-holt.com/single-post/2018/11/04/using-spacy-to-generate-synonyms-and-grammatical-variations
#https://stackoverflow.com/questions/49964028/spacy-oserror-cant-find-model-en
#https://medium.com/@nikhilbd/how-to-use-machine-learning-to-find-synonyms-6380c0c6106b

# import spacy
# import numpy as np
# nlp = spacy.load('en_core_web_lg')
#
# def most_similar(word, topn=5):
#     word = nlp.vocab[str(word)]
#     queries = [
#         w for w in word.vocab
#         if w.is_lower == word.is_lower and w.prob >= -15 and np.count_nonzero(w.vector)
#     ]
#
#     by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
#     return [(w.lower_,w.similarity(word)) for w in by_similarity[:topn+1] if w.lower_ != word.lower_]
#
# most_similar("dog", topn=3)

import numpy as np
import pandas as pd
import spacy
from tqdm import tqdm
import hdbscan

nlp = spacy.load('en_core_web_lg')

"""define all vectors and strings"""
strings = []
vectors = []
for key, vector in tqdm(nlp.vocab.vectors.items(), total = len(nlp.vocab.vectors.keys())):
    try:
        strings.append(nlp.vocab.strings[key])
        vectors.append(vector)
    except:
        pass

vectors = np.vstack(vectors)

"""Generate clusters, you will need to save the clusterer to use as 
clustering can take a while"""
clusterer = hdbscan.HDBSCAN(min_cluster_size = 1000)
clusterer.fit(vectors)
labels = clusterer.labels_

#main function
def closest(word, count = 10):

    word = nlp(word)
    main = word.vector

    cluster = clusterer.fit(main).labels_
    tmp_vectors = vectors[np.where(labels == cluster)[0]]
    tmp_strings = np.array(strings)[np.where(labels == cluster)[0]]

    diff = tmp_vectors - main
    diff = diff**2
    diff = np.sqrt(diff.sum(axis = 1), dtype = np.float64)

    df = pd.DataFrame(tmp_strings, columns = ['keyword'])
    df['diff'] = diff
    df = df.sort_values('diff', ascending = True).head(count)
    df['keyword'] = df['keyword'].str.lower()
    df = df.drop_duplicates(subset = 'keyword', keep = 'first')
    return df

closest("Dogs", count = 10)