# -*- coding: utf-8 -*-
"""
# Regresión Lineal Múltiple
Created on Sun Jan  8 11:44:22 2023
@author: QV-137
"""
import numpy as np # For mathematical operations
import matplotlib.pyplot as plt # For plotting information
import pandas as pd # For managing large data collections

dataset = pd.read_csv('C:/Users/1107473901/Documents/Proyectos Software/Python/Data Science and Statistics/Py Part 2 - Regression/50_StartupsP.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Absence of unknown data (nan or NaN)

# Codificar DATOS CATEGÓRICOS
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
# x = np.array(ct.fit_transform(x), dtype=np.float64)

# No neccesity to encode y
# Evitar la trampa de las variables ficticias
# x=x[:,n:n] sirve para quitar variables dummy en otras versiones de Python
"""
En el caso de este código, no es necesario eliminar vectores de
variables dummy puesto que en Python 3.10.8 no se generan tantos
vectores como distintos datos categóricos hay en una columna,
sino que genera un sólo vector en el que se codifican del 0 a n datos
todos los datos categóricos, evitando así la multicolinealidad.
"""

# DIVIDIR el dataset en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# No fue necesario el escalado de variables

# Ajustar el modelo de regresión lineal múltiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)
"""
Con la función LinearRegression no es necesario especificar
si es simple o múltiple, esta solo la usaremos para entrenar
al modelo con el training set
"""

# Predicción de los resultados con el conjunto de testing
y_pred = regression.predict(x_test)

# Construir el modelo de RLM utilizando la Eliminación hacia atrás
import statsmodels.api as sm # En el curso se usó import statsmodels.formula.api
# axis = 1 como columna, axis = 0 como fila
x = np.append(arr = x, values = np.ones((50,1)).astype(int), axis = 1)
SL = 0.05
# Variable que guarda el número óptimo de variables para el modelo
x_opt = x[:,[0, 1, 2, 3, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()

# Aquí, el programador debe analizar el summary y eliminar las variables con un P-Valor mayor a SL
# Se elimina la primer variable con P-Valor alto, la variable dummy de "Estado"
x_opt = x[:,[0, 1, 2, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()

# Se elimina la segunda variable con P-Valor alto, la que corresponde al gasto en "Administración"
x_opt = x[:,[0, 2, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()

# Se elimina la tercera variable con P-Valor superior a SL, gastos en "Marketing"
x_opt = x[:,[0, 4]].tolist()
regression_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regression_OLS.summary()
# Concluyendo que la única varible estadísticamente significativa es el gasto en "R&D"
# Se obtiene un modelo de regresión lineal simple