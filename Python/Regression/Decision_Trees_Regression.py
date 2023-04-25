import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

""" If needed
# Values Scalating
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""

# Adjust decision tree regression model
from sklearn.tree import DecisionTreeRegressor
regression = DecisionTreeRegressor(random_state = 0)
regression.fit(x, y)

# Predictions (137)
y_pred = regression.predict([[137]])

# Plotting model

# Graph of the continuous ladder function
x_grid = np.arange(min(x), max(x), 0.1)  # For smoother curves
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regression.predict(x_grid), color = 'blue')
plt.title("Decision tree model")
plt.xlabel("Independent_var")
plt.ylabel("Dependent_var")
plt.show()

# Graph of dashed function
plt.scatter(x, y, color = 'red')
plt.plot(x, regression.predict(x), color = 'blue')
plt.title("Decision tree model")
plt.xlabel("Independent_var")
plt.ylabel("Dependent_var")
plt.show()
