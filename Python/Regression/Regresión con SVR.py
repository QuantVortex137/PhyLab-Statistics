"""
Regresión con SVR
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
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y.reshape(-1,1))

## Ajustar el modelo de REGRESIÓN que sea necesario con el dataset
from sklearn.svm import SVR
regression = SVR(kernel = "rbf") # rbf es el núcleo gaussiano
regression.fit(x, y)

## PREDICCIÃN de nuestro modelo SVR
pred = np.array([[6.5]]) # Crear un array pred desde numpy
y_pred = regression.predict(sc_x.transform(pred))
# y_pred = regression.predict(sc_x.transform(np.array([[6.5]])))
y_pred = sc_y.inverse_transform(y_pred.reshape(-1,1))

## VISUALIZACIÃN del modelo

# VISUALIZACIÃN de los resultados del modelo SVR
x_grid = np.arange(min(x), max(x), 0.1)  # Se usa para crear una grÃ¡fica con curvas mÃ¡s suavizadas
x_grid = x_grid.reshape(len(x_grid), 1) # Se hace la transpuesta del vector que se crea anteriormente
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regression.predict(x_grid), color = 'blue') # Se usa x_grid para obtener la mejor grÃ¡fica
# Es lo mismo escribir: plt.plot(x, lin_reg_2.predict(x_pol), color = 'blue')
plt.title("Modelo de Regresión (SVR)")
plt.xlabel("Posición del Empleado")
plt.ylabel("Sueldo en dólares")
plt.show()

# VISUALIZACIÓN de los resultados del SVR sin escalado de variables
X_grid = np.arange(min(x), max(x), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y.reshape(-1,1)), color = "red")
plt.plot(sc_x.inverse_transform(X_grid), sc_y.inverse_transform(regression.predict(X_grid).reshape(-1,1)), color = "blue")
plt.title("Modelo de Regresión (SVR)")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()
