import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2].values

# Divide dataset into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Adjust regression model to data
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(x, y)

# Adjust polynomial regression to dataset
from sklearn.preprocessing import PolynomialFeatures
pol_reg = PolynomialFeatures(degree = 4) # You must check for the best fitting degree
x_pol = pol_reg.fit_transform(x)
lin_reg_2 = LinearRegression() 
lin_reg_2.fit(x_pol, y)

# Plotting linear model
plt.scatter(x, y, color = 'red')
plt.plot(x, linear_reg.predict(x), color = 'blue')
plt.title("Simple linear regression model")
plt.xlabel("independent_var")
plt.ylabel("dependent_var")
plt.show()

# Plotting polynomial model
x_grid = np.arange(min(x), max(x), 0.1)  # For smoother curves
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, lin_reg_2.predict(pol_reg.fit_transform(x_grid)), color = 'blue') # plt.plot(x, lin_reg_2.predict(x_pol), color = 'blue') could also work for this
plt.title("Simple polynomial regression model")
plt.xlabel("independent_var")
plt.ylabel("dependent_var")
plt.show()

# Predictions from models (example value = 137)
linear_reg.predict([[137]]) # Linear model
lin_reg_2.predict(pol_reg.fit_transform([[137]])) # Polynomial model
