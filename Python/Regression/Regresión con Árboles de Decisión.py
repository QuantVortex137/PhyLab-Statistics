"""
Regresión con Árboles de Decisión
Created on Wed Jan 11 12:59:51 2023
@author: QV-137
"""
## IMPORTAR librerÃ­as
import numpy as np # For mathematical operations
import matplotlib.pyplot as plt # For plotting information
import pandas as pd # For managing large data collections

## LEER el dataset y establecer X y Y
dataset = pd.read_csv('Position_SalariesP.csv')
x = dataset.iloc[:, 1:2].values # [:, 1] indica que X es un VECTOR, [:, 1:2] indica que X es una MATRIZ
y = dataset.iloc[:, 2].values # Y siempre debe ser un vector

## DIVIDIR el dataset en conjunto de entrenamiento y conjunto de testing
"""
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
# Cuando no se tengan muchos datos no es necesario dividirlos en subconjuntos
"""

# ESCALADO de variables
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""

## Ajustar el modelo de REGRESIÓN con ÁRBOLES DE DECISIÓN
from sklearn.tree import DecisionTreeRegressor
regression = DecisionTreeRegressor(random_state = 0)
regression.fit(x, y)

## PREDICCIÓN del modelo con árbol de decisión
y_pred = regression.predict([[6.5]])

## VISUALIZACIÓN del modelo

# VISUALIZACIÓN de los resultados del modelo con árbol de decisión "CONTINUA"
# FUNCIÓN ESCALERA
x_grid = np.arange(min(x), max(x), 0.1)  # Se usa para crear una grÃ¡fica con curvas mÃ¡s suavizadas
x_grid = x_grid.reshape(len(x_grid), 1) # Se hace la transpuesta del vector que se crea anteriormente
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regression.predict(x_grid), color = 'blue') # Se usa x_grid para obtener la mejor grÃ¡fica
plt.title("Modelo por Árboles de Decisión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo del empleado en dólares")
plt.show()

# VISUALIZACIÓN de los resultados del modelo con árbol de decisión "DISCONTINUA"
plt.scatter(x, y, color = 'red')
plt.plot(x, regression.predict(x), color = 'blue') # Se usa x_grid para obtener la mejor grÃ¡fica
plt.title("Modelo por Árboles de Decisión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo del empleado en dólares")
plt.show()

# Este modelo no puede predecir valores más allá de los que se contienen en las divisiones creadas en el árbol