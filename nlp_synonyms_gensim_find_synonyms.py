#https://stackoverflow.com/questions/68004710/python-nlp-get-synonyms-for-a-word-based-on-my-own-corpus
#https://radimrehurek.com/gensim/models/word2vec.html
#https://rare-technologies.com/word2vec-tutorial/

from gensim.test.utils import common_texts
from gensim.models import Word2Vec
model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")

from gensim.models import Word2Vec
sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
model = Word2Vec(sentences, min_count=1)

