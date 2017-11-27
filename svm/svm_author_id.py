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
reduce_choose = raw_input("Reduce 0.99 dataset(Y or N?): ")
if reduce_choose in ["Y", "y"]:
	features_train = features_train[:len(features_train)/100]
	labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
# Choose the kernel function and the C value
kernel = raw_input("Enter the kernel function: ")
C_value = float(raw_input("Enter the C value: "))

clf = SVC(kernel=kernel, C=C_value)
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

class_1 = 0
for i in range(0, len(prediction)):
	if prediction[i] == 1:
		class_1 += 1

print "The class in Chris is %d ." % class_1



#########################################################


