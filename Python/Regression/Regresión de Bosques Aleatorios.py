"""
Regresión de Bosques Aleatorios
Created on Wed Jan 11 12:59:51 2023
@author: QV-137
"""
## IMPORTAR librerías
import numpy as np # For mathematical operations
import matplotlib.pyplot as plt # For plotting information
import pandas as pd # For managing large data collections

## LEER el dataset y establecer X y Y
dataset = pd.read_csv('Position_SalariesP.csv')
x = dataset.iloc[:, 1:2].values # [:, 1] indica que X es un VECTOR, [:, 1:2] indica que X es una MATRIZ
y = dataset.iloc[:, 2].values # Y siempre debe ser un vector

## Ajustar el modelo de REGRESIÃN que sea necesario con el dataset
from sklearn.ensemble import RandomForestRegressor
regression = RandomForestRegressor(n_estimators = 1000, random_state = 0)
regression.fit(x, y)

## PREDICCIÓN de nuestros modelos
y_pred = regression.predict([[6.5]])

## VISUALIZACIÓN del modelo

# VISUALIZACIÓN de los resultados del modelo de regresión con BOSQUES ALEATORIOS
x_grid = np.arange(min(x), max(x), 0.01)  # Se usa para crear una grÃ¡fica con curvas mÃ¡s suavizadas
x_grid = x_grid.reshape(len(x_grid), 1) # Se hace la transpuesta del vector que se crea anteriormente
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regression.predict(x_grid), color = 'blue') # Se usa x_grid para obtener la mejor grÃ¡fica
plt.title("Modelo de Regresión con Bosques Aleatorios")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo del empleado en dólares")
plt.show()