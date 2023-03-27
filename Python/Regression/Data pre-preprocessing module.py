"""
Data Preprocessinf Module
Created on Fri Jan 6 12:07:01 2023
@author: QV-137
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

# Importing dataset from ML Datasets folder
dataset = pd.read_csv('dataset.csv')
# iloc = index + localization (It searches for the rows and columns)
# We write [:, :] to make sure we include all rows and columns
# We write [:-1].values to exclude just a final part of the table from the dataset
# We write just [1,4] if we want specific rows & columns from the dataset
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Unknown data (nan or NaN)
"""
The NaN data is replaced by the average or mean data of the column
"""
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Categorical Data Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Encoding x_categorical_data
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)
x = np.array(ct.fit_transform(x), dtype=np.float64)

# Encoding y_categorical_data
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Divide data into training and testing data sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Variable scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
