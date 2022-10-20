# import the method to load dataset
from sklearn.datasets import fetch_20newsgroups

# Load the train and test data
X_train, y_train = fetch_20newsgroups(subset='train',
                                      return_X_y=True)

X_test, y_test = fetch_20newsgroups(subset='test',
return_X_y=True)

