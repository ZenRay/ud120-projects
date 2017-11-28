#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
# import the regression package
from sklearn.linear_model import LinearRegression

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
# avoid the dict keys sequence after py3.3
sort_keys = "../tools/python2_lesson06_keys.pkl"
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
reg = LinearRegression()
reg.fit(feature_train, target_train)

# get the slope and intercepte
print "The regression slope is: %f ." % reg.coef_[0]

print "The regression intercepte is:  %f." % reg.intercept_

# get the regression score
print "The regression score in the train dataset is: %f." % \
    reg.score(feature_train, target_train)
print "The regression score in the test dataset is: %f." % \
    reg.score(feature_test, target_test)


### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test), color="r" )
except NameError:
    pass
# add a line about train dataset
reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b")

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()

# print slope about the train feature and its predict 
train_prediction = reg.predict(feature_train)
reg.fit(feature_train, train_prediction)
print "The slope about the train and its predition is %f ." % reg.coef_[0]