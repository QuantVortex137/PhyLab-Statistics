import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1:5].values

# Encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Encoding x
labelencoder_x = LabelEncoder()
x[:, 3] = labelencoder_x.fit_transform(x[:, 3])
# Column Transformer
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)

# Divide dataset into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Adjust multiple linear regression with the training set
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)

# Prediction using testing set
y_pred = regression.predict(x_test)

# Use backwards elimination to eliminate variables with a p-value>SL, usually SL=0.05
# This is an exmaple of manual backwards elimination with 5 variables
import statsmodels.api as sm
x = np.append(arr = x, values = np.ones((50,1)).astype(int), axis = 1)
SL = 0.05
x_opt = x[:,[0, 1, 2, 3, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()

# It is necessary to check the statistical summary
x_opt = x[:,[0, 1, 2, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()

x_opt = x[:,[0, 2, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()

x_opt = x[:,[0, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()
