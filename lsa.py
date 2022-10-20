#https://towardsdatascience.com/how-to-use-latent-semantic-analysis-to-classify-documents-1af717e7ee52
#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html
# import the method to load dataset
from sklearn.datasets import fetch_20newsgroups

# Load the train and test data
X_train, y_train = fetch_20newsgroups(subset='train',
                                      return_X_y=True)

X_test, y_test = fetch_20newsgroups(subset='test',
                                    return_X_y=True)

print("got here")

# import tfidf function
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the vectorizer
word_vectorizer = TfidfVectorizer(max_df=0.4, min_df=2,
                                  stop_words='english',
                                  lowercase=True, use_idf=True)

# Fit and transform vectorizer
X_train_transform = word_vectorizer.fit_transform(X_train)

# import python SVD implementation
from sklearn.decomposition import TruncatedSVD

# initialize and fit the algorithm
svd = TruncatedSVD(n_components=20, random_state=42)
X_train_svd = svd.fit_transform(X_train_transform)

# import svc
from sklearn.svm import SVC

# initialize and train the model
svm_algorithm = SVC()
svm_algorithm.fit(X_train_svd, y_train)

# Transform using tfidf
X_test_transform = word_vectorizer.transform(X_test)

# Get the LSA test dataset
X_test_svd = svd.transform(X_test_transform)

# get the accuracy
from sklearn.metrics import accuracy_score

svm_pred = svm_algorithm.predict(X_test_svd)
test_score = accuracy_score(y_test, svm_pred) * 100

print(f"Test accuracy score: {test_score:.2f}%")
