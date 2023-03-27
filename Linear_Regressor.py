"""
Simple Linear Regression
Created on Wed Jan 11 12:59:51 2023
@author: QV-137
"""

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

# Import dataset
dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, 0:1].values # You must change the numbers inside .iloc
y = dataset.iloc[:, 3:4].values

# If NaN data is present, use this subroutine
# WARNING: If used, make sure to eliminate round function from slope and intersection objects
"""
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(y)
y = imputer.transform(y)
"""

# Divide data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

# If scaling data is needed, add this subroutine
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train) # Sets may have the same size

y_pred = regression.predict(x_test)

# Statistical summary
slope = round(regression.coef_[0], 5)
intercept = round(regression.intercept_, 5)
equation = 'y = {}x + {}'.format(slope,intercept)

# Training set plotting
plt.scatter(x_train, y_train, s=3, color = 'red')
plt.plot(x_train, regression.predict(x_train), linewidth=1, color = 'blue')
plt.title("Distancia-Tiempo (Training Set Only)")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.show()

# Testing set plotting
plt.scatter(x_test, y_test, s=3, color = 'red')
plt.plot(x_train, regression.predict(x_train), color = 'blue')
plt.title("Distancia-Tiempo (Testing Set Only)")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.show()

# Whole dataset plotting
plt.scatter(x, y, s=5, color = 'red')
plt.plot(x, regression.predict(x), linewidth=1, color = 'blue')
plt.text(0.75, 0.95, equation, ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)
plt.title("Distancia-Tiempo")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.show()
