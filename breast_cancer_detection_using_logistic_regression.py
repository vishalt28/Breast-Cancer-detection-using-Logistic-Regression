# -*- coding: utf-8 -*-
"""Breast Cancer detection using Logistic Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CDAy48KyIRuLC5jRwUzqihdF34sJSNyn

# Logistic Regression

## Importing the libraries
"""

import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('breast_cancer.csv')
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

X,y

"""## Training the Logistic Regression model on the Training set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""## Predicting the Test set results"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

y_pred

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
cm

"""## Computing the accuracy with k-Fold Cross Validation"""

accuracy = accuracy_score(y_test, y_pred)
accuracy

from sklearn.model_selection import cross_val_score
#cv represents number of folds for the 10 diff accuracies
accuracies = cross_val_score(classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))

"""# Predicting the Test set results"""

import numpy as np
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

