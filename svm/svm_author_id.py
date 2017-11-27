#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
# import svc
from sklearn.svm import SVC
# import accuracy score
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# takes long time to run the svm
# reduce the number of dataset to run more quickly
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
kernel = raw_input("Enter the kernel function: ")

# linear kernel
if kernel == "linear":
	clf = SVC(kernel="linear")
	# train the dataset and running time
	t0 = time()
	clf.fit(features_train, labels_train)
	print "Training time %f s\n" % round(time() - t0, 3)
	# predict the test dataset and running time
	t1 = time()
	prediction = clf.predict(features_test)
	print "Prediction time %f s\n" % round(time() - t1, 3)
	# get the prediction accuracy
	print("Prediciton accuracy score:\n")
	print accuracy_score(prediction, labels_test)

# rbf kernel
elif kernel == "rbf":
	C_value = [10.0, 100.0, 1000.0, 10000.0]
	for i in C_value:
		print "The kernel is rbf. The C value is %f." % i
		clf = SVC(kernel="rbf", C=i)
		# train the dataset and running time
		t0 = time()
		clf.fit(features_train, labels_train)
		print "Training time %f s\n" % round(time() - t0, 3)
		# predict the test dataset and running time
		t1 = time()
		prediction = clf.predict(features_test)
		print "Prediction time %f s\n" % round(time() - t1, 3)
		# get the prediction accuracy
		print("Prediciton accuracy score:\n")
		print accuracy_score(prediction, labels_test)


#########################################################


