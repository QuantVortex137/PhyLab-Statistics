"""
Gaussian Distribution
Created on Sun Feb 26 12:44:09 2023
@author: QV-137
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import a data column from a .csv
dataset = pd.read_csv('dataset.csv')
norm_data = dataset.iloc[:, 3:4].values # You must change the numbers inside .iloc

# Replace the NaN data with the mean of the column
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(norm_data)
norm_data = imputer.transform(norm_data)

# Calculate mean and standard deviation of the normalized data
mu = round(np.mean(vel),4)
sigma = round(np.std(vel),4)
stat_summ = '\u03BC = {}, \u03C3 = {}'.format(mu,sigma)

# Range and number of sigmas
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

from scipy.stats import norm
y = norm.pdf(x, mu, sigma)

plt.plot(x, y)
plt.text(0.79, 0.95, stat_summ, ha = 'center', va = 'center', transform = plt.gca().transAxes, fontsize = 11)
plt.title('Normalized data "X"')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.show()
