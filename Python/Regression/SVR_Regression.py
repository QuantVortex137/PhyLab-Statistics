import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

""" If needed
# Variables Scalating 
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y.reshape(-1,1))
"""

# Adjust SVR regression model to dataset
from sklearn.svm import SVR
regression = SVR(kernel = "rbf") # rbf is the gaussian kernel
regression.fit(x, y)

# Predictions (example value = 137)
pred = np.array([[137]])
y_pred = regression.predict(sc_x.transform(pred))
y_pred = sc_y.inverse_transform(y_pred.reshape(-1,1))

# Plotting SVR model 
x_grid = np.arange(min(x), max(x), 0.1)  # For smoother curves
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regression.predict(x_grid), color = 'blue') 
plt.title("SVR regression model")
plt.xlabel("Independent_var")
plt.ylabel("Dependent_var")
plt.show()
