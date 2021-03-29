# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:56:50 2019

@author: hp
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib

data = pd.read_csv('updatedJowar.csv')
X = data.iloc[:,:-1].values
y = data.iloc[:,6].values

labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

regression = LinearRegression()
regression.fit(X_train, y_train)

y_pred =regression.predict(X_test)

r2_score(y_test, y_pred)

joblib.dump(regression, "multiple_regression_jowar_model.pkl")
