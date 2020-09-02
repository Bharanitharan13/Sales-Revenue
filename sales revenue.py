# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:16:27 2020

@author: Bharanitharan
"""

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

#setting path
os.chdir('E:\Assignment 2')



#importing data

data = pd.read_csv('Sales Revenue data-dataset.csv',delimiter = ',')
data.describe()

#audit the data
data.head()
print(data.shape)

data.dtypes

#univeriyate analysis
data.isnull().sum()

for i in data:
    print (i,':',data[i].skew())

plt.plot(data['AdSpend'])
plt.plot(data['SalesRevenue'])
plt.boxplot(data['AdSpend'],vert=True,patch_artist=True)
plt.boxplot(data['SalesRevenue'],vert=True,patch_artist=True)
#univeriate analysis

corelation = data.corr()
sns.heatmap(corelation,annot = True)

plt.scatter(data['AdSpend'],data['SalesRevenue']) # 'r' is the color red
plt.xlabel('Adspend')
plt.ylabel('Sales revernue')
plt.title('Salesrevenue with adspend')
plt.show()


# feature selecition
from sklearn.model_selection import train_test_split 

data['log_Ad'] = np.log(data['AdSpend'])


x_train,x_test,y_train,y_test = train_test_split(data['log_Ad'],data['SalesRevenue'],test_size=0.3,random_state=123)

x_train = pd.DataFrame(x_train)
y_train = pd.DataFrame(y_train)
x_test = pd.DataFrame(x_test)
y_test = pd.DataFrame(y_test)


# Create linear regression object
from sklearn import datasets, linear_model
import math

regr = linear_model.LinearRegression()

regr.fit(x_train,y_train)

y_preds = regr.predict(x_train)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_train, y_preds)
train_rmse = math.sqrt(mse)
print('Coefficients: \n', regr.coef_)
y_preds_test = regr.predict(x_test)
mse = mean_squared_error(y_test, y_preds_test)
test_rmse = math.sqrt(mse)


z = [50]
loged_Z = np.log(z)
z = pd.DataFrame(z)
loged_Z = pd.DataFrame(loged_Z)
z_preds_test = regr.predict(loged_Z)




reg_2 = linear_model.BayesianRidge()
reg_2.fit(x_train,y_train)

y_preds = reg_2.predict(x_train)
mse = mean_squared_error(y_train, y_preds)
train_rmse = math.sqrt(mse)
print('Coefficients: \n', regr.coef_)


y_preds_test = reg_2.predict(x_test)
mse = mean_squared_error(y_test, y_preds_test)
test_rmse = math.sqrt(mse)


