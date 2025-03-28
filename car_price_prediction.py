# -*- coding: utf-8 -*-
"""Car Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Izh7oNkhkxX9OCQH1PU7A3UaZssZ83xC
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics

#load the data from csv file to pandas dataframe
car_dataset = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')

#inspecting from first 5 rows of the dataframe
car_dataset.head()

#checking the number of rows and columns
car_dataset.shape

# Getting some information about the dataset
car_dataset.info()

#Checking the number of missing valuescar_dataset
car_dataset.isnull().sum()

#checking the distribution of categorial data
print(car_dataset.fuel.value_counts())
print(car_dataset.seller_type.value_counts())
print(car_dataset.transmission.value_counts())

"""Encoding Categorical Data"""

#Encoding "Fuel Type" Column
car_dataset.replace({"fuel" :{'Petrol':0, 'Diesel':1, 'CNG':2, 'LPG':3, 'Electric':4}}, inplace=True)

#Encoding "Seller Type" Column
car_dataset.replace({"seller_type" :{'Dealer':0, 'Individual':1, 'Trustmark Dealer':2}}, inplace=True)

#Encoding "Transmission" Column
car_dataset.replace({"transmission" :{'Manual':0, 'Automatic':1}}, inplace=True)

#Encoding "owner" Column
car_dataset.replace({"owner" :{'Test Drive Car': 0, 'First Owner':1, 'Second Owner':2, 'Third Owner':3, 'Fourth & Above Owner':4}}, inplace=True)

car_dataset.head()

"""Splitting the Data and Target"""

X = car_dataset.drop(['name' , 'selling_price'], axis=1)
Y = car_dataset['selling_price']

print(X)

print(Y)

"""Splitting Training And Testing Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y ,test_size=0.1, random_state=2)

"""Model Training

1. Linear Regression
"""

#loading the linear Regression model
lin_reg_model = LinearRegression()

lin_reg_model.fit(X_train, Y_train)

"""Model Evalution"""

training_data_prediction = lin_reg_model.predict(X_train)

error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

"""Visualize the actual prices and prediction prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

#prediction and Training Data
test_data_prediction = lin_reg_model.predict(X_test)

#R Squared  Error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""Lasso Regression"""

lass_reg_model = Lasso()

lass_reg_model.fit(X_train, Y_train)

"""Model Evalution"""

training_data_prediction = lass_reg_model.predict(X_train)

error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

"""Visualize the Actual Prices and Predictions"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

test_data_prediction = lass_reg_model.predict(X_test)

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

