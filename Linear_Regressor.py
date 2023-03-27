"""
Analisis de Datos para Movimiento Unidimensional
Created on Wed Jan 11 12:59:51 2023
@author: QV-137
"""
## IMPORTAR librerÃ­as
# Importación de librerías
import numpy as np # For mathematical operations
import matplotlib.pyplot as plt # For plotting information
import pandas as pd # For managing large data collections

# Importar el dataset
dataset = pd.read_csv('C:/Users/1107473901/Documents/Universidad de Guanajuato/Laboratorios/LabMC/Reporte 02 - Movimiento Unidimensional/Datasets/S-I-1.csv')
x = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 3:4].values

# En caso de tener una columna con espacios vacíos y se asignen datos nan, incluir esta subrutina
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(y)
y = imputer.transform(y)

# Si se usa, no se podrá usar la fnución round para la pendiente y la ordenada al origen

# Dividir el dataset en training y testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

# Escalado de variables
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""

# Crear modelo de regresión lineal simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train) # Los conjuntos deben ser del mismo tamaño

# Predecir el conjunto de test
y_pred = regression.predict(x_test) # Con las variables independientes se predicen las dependientes

# Resumen estadístico de la regresión
slope = round(regression.coef_[0], 5)
intercept = round(regression.intercept_, 5)
equation = 'y = {}x + {}'.format(slope,intercept)

# Visualizar los resultados de entrenamiento con matplotlib
plt.scatter(x_train, y_train, s=3, color = 'red')
plt.plot(x_train, regression.predict(x_train), linewidth=1, color = 'blue')
plt.title("Distancia-Tiempo (Training Set Only)")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.show()
# La recta que se dibuja con el training set y el testing set es la misma
# Por lo que es más eficiente dibujar la recta con el conjunto más grande (training set)

# Visualizar los resultados de testing con matplotlib
plt.scatter(x_test, y_test, s=3, color = 'red')
plt.plot(x_train, regression.predict(x_train), color = 'blue')
plt.title("Distancia-Tiempo (Testing Set Only)")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.show()

# Visualizar el conjunto de datos completo
plt.scatter(x, y, s=5, color = 'red')
plt.plot(x, regression.predict(x), linewidth=1, color = 'blue')
plt.text(0.75, 0.95, equation, ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)
plt.title("Distancia-Tiempo")
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.show()
