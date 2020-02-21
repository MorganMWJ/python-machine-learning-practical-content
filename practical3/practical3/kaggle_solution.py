# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
import pandas as pd


# Does not have class attribute (test data)
test_data = pd.read_csv("test.csv").dropna()
print(test_data.head(10))
print(test_data.columns)

# Has class attribute (training data)
train_data = pd.read_csv("train.csv").dropna()
print(train_data.head(10))
print(train_data.columns)

# 10-fold CV
kf = KFold(n_splits=10, random_state=None, shuffle= False)

for train, test in kf.split(train_data):
    print(train)
    print(test)

# for train, test in kf.split(train_data):
#     # split training data frame into input(x) and labels(y)
#     train_X = train.values[:, 1:]
#     train_y = train["Class"].values
#
#     test_X = test.values[:, 1:]
#     test_y = test["Class"].values
#
#     # check equal samples in x and y - sanity check
#     if train_X.shape[0] != train_y.shape[0]:
#         raise Exception("Sample counts do not align! Try again!")
#
#     # Very simple example with DT
#     clf = DecisionTreeClassifier()
#     clf.fit(train_X, train_y)
#     predicted_labels = clf.predict(test_y)
#
#     print("Result of Validation: ")
#     print(classification_report(test_y, predicted_labels))




