# -*- coding: utf-8 -*-
"""
Técnicas de Pre-procesamiento de Datos___________________________________
Para Machine Learning, antes de escribir cualquier modelo
de aprendizaje se tienen que procesar todos los datos que se
usarán a lo largo del proceso, se debe hacer el pre-procesado
de datos.

Created on Fri Jan 6 12:07:01 2023

@author: QV-137
"""

# Dataset.csv from Part 1: Data preprocessing

import numpy as np # For mathematical operations
import matplotlib.pyplot as plt # For plotting information
import pandas as pd # For managing large data collections

# Importing dataset from ML Datasets folder
dataset = pd.read_csv('C:/Users/1107473901/Documents/Proyectos Software/Python/Data Science and Statistics/Py Part 1 - Data pre-processing/Data1P.csv')
# iloc = index + localization (It searches for the columns and rows)
# rows in: fin, columns in:fin
# We write [:, :] to make sure we include all rows and columns
# We write [:-1].values to exclude just a final part of the table from the dataset
# We write just [1,4] if we want specific rows & columns from the dataset
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Unknown data (nan or NaN)
"""
The NaN data is replaced by the average or mean data of the column
"""
"""
CHECK LATER FOR SCIKITLEARN INSTALLATION ISSUE
"""
# from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# DATOS CATEGÓRICOS
# Codificar datos categóricos (en el dataset se tienen 3 países diferentes)
# Pasar datos tipo string como Francia a números como 0

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Encoding x
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)
x = np.array(ct.fit_transform(x), dtype=np.float64)

# Encoding y
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# DIVIDIR el dataset en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)




