# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


# Does not have class attribute
data = pd.read_csv("test.csv").dropna()
print(data.head(10))
print(data.columns)

# Has class attribute
data = pd.read_csv("train.csv").dropna()
print(data.head(10))
print(data.columns)


# split data frame into input(x) and labels(y)
X = data.values[:,1:]
y = data["Class"].values

#check equal samples in x and y - sanity check
if X.shape[0] != y.shape[0]:
    raise Exception("Sample counts do not align! Try again!")