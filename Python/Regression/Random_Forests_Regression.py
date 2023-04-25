import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2].values

from sklearn.ensemble import RandomForestRegressor
regression = RandomForestRegressor(n_estimators = 1000, random_state = 0) # Increase the number of n_estimators to taste
regression.fit(x, y)

y_pred = regression.predict([[137]])

# Plotting random forests model
x_grid = np.arange(min(x), max(x), 0.01) 
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regression.predict(x_grid), color = 'blue')
plt.title("Random forests model")
plt.xlabel("Independent_var")
plt.ylabel("Dependent_var")
plt.show()
