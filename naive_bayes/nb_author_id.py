#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
# import sklearn naive_bayes
from sklearn.naive_bayes import GaussianNB
# import bayes score
from sklearn.metrics import accuracy_score



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = GaussianNB() # GaussianNB classifier
t0 = time()
clf.fit(features_train, labels_train)
print "Training time: %f s\n" % round(time() - t0, 3)

# test the running time
t1 = time()
prediction = clf.predict(features_test) # get the predition label
print "Prediction time: %f s" % round(time() - t1, 3)
print "The prediction accuracy score:\n"
print accuracy_score(prediction, labels_test)

#########################################################


