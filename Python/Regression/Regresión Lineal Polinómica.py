"""
Regresión Lineal Polinómica
Created on Wed Jan 11 11:47:45 2023
@author: QV-137
"""
import numpy as np # For mathematical operations
import matplotlib.pyplot as plt # For plotting information
import pandas as pd # For managing large data collections

# LEER el dataset y establecer X y Y
dataset = pd.read_csv('Position_SalariesP.csv')
x = dataset.iloc[:, 1:2].values # [:, 1] indica que X es un VECTOR, [:, 1:2] indica que X es una MATRIZ
y = dataset.iloc[:, 2].values # Y siempre debe ser un vector

"""
# DIVIDIR el dataset en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

Cuando se tienen tan pocos datos, no es necesario dividirlos en subconjuntos para entrenar 
y testear, pues incluso la regresión podría verse afectada
"""
# Ajustar la regresión lineal simple con el dataset
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(x, y)

# Ajustar la regresión polinómica con el dataset
from sklearn.preprocessing import PolynomialFeatures
pol_reg = PolynomialFeatures(degree = 4) # degree = 2, degree = 3, n grado = n
# A mayr grado, mayor precisión
x_pol = pol_reg.fit_transform(x) # fit hace la regresión, transform aplica los cambios al objeto
# Se genera una columna de 1's, que corresponde al término independiente del modelo
lin_reg_2 = LinearRegression() # Se crea la variable del modelo polinómico
lin_reg_2.fit(x_pol, y) # Se realiza el modelo con la función LinearRegression usando x_pol

# Visualización de los resultados del modelo lineal
plt.scatter(x, y, color = 'red')
plt.plot(x, linear_reg.predict(x), color = 'blue')
plt.title("Modelo de Regresión Lineal Simple")
plt.xlabel("Posición del Empleado")
plt.ylabel("Sueldo en $ usd")
plt.show()

# Visualización de los resultados del modelo polinómico
x_grid = np.arange(min(x), max(x), 0.1)  # Se usa para crear una gráfica con curvas más suavizadas
x_grid = x_grid.reshape(len(x_grid), 1) # Se hace la transpuesta del vector que se crea anteriormente
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, lin_reg_2.predict(pol_reg.fit_transform(x_grid)), color = 'blue') # Se usa x_grid para obtener la mejor gráfica
# Es lo mismo escribir: plt.plot(x, lin_reg_2.predict(x_pol), color = 'blue')
plt.title("Modelo de Regresión Lineal Polinómica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en $ usd")
plt.show()

# Predicción de nuestros modelos
linear_reg.predict([[6.5]]) # Usando el modelo lineal simple (grado = 1)
lin_reg_2.predict(pol_reg.fit_transform([[6.5]])) # Usando el modelo polinómico (grado = 4)