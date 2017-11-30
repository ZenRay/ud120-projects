#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)
# import lasso regresssion decisiontree and accuracy score
from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# The words (features) and authors (labels), already largely processed.
# These files should have been created from the previous (Lesson 10)
# mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load(open(words_file, "r"))
authors = pickle.load(open(authors_file, "r"))


# test_size is the percentage of events assigned to the test set (the
# remainder go into training)
# feature matrices changed to dense representations for compatibility with
# classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test = vectorizer.transform(features_test).toarray()


# a classic way to overfit is to use a small number
# of data points and a large number of features;
# train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train = labels_train[:150]


# your code goes here
regresssion = DecisionTreeClassifier()
regresssion.fit(features_train, labels_train)

prediction = regresssion.predict(features_test)

print "The number of training points is %d ." % len(prediction)
print "The accuracy score is %f ." % accuracy_score(labels_test, prediction)


# use feature_importances_ to display the features' importance
feature_index = 0
for i in regresssion.feature_importances_:

    if i >= 0.2:
        print i
        print feature_index
        break
    feature_index += 1

# print the most importance feature by using get_feature_naems
print "The importance feature is %s .It's index is %d ." % \
	(vectorizer.get_feature_names()[feature_index], feature_index)