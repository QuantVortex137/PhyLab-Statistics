# -*- coding: utf-8 -*-
"""
Generador de Campanas Gaussianas con Dada una Columna de Datos
Created on Sun Feb 26 12:44:09 2023
@author: QV-137
"""
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Lee los datos del archivo de Excel guardado como csv
dataset = pd.read_csv('C:/Users/1107473901/Documents/Universidad de Guanajuato/Laboratorios/LabMC/Reporte 02 - Movimiento Unidimensional/Datasets/S-V.csv')
vel = dataset.iloc[:, 3:4].values

# Reemplazar los datos nan por la media de la columna
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(vel)
vel = imputer.transform(vel)

# Calcular la media y desviación estándar de la columna de datos a normalizar
mu = round(np.mean(vel),4) # Media
sigma = round(np.std(vel),4) # Desviación estándar
stat_summ = '\u03BC = {}, \u03C3 = {}'.format(mu,sigma)

# Crea un rango de valores para graficar la distribución, elige el número de sigmas
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

# Calcula la densidad de probabilidad de la distribución normal
from scipy.stats import norm
y = norm.pdf(x, mu, sigma)

# Grafica la curva de la distribución normal
plt.plot(x, y)

# Agrega un título y etiquetas de los ejes
plt.text(0.79, 0.95, stat_summ, ha='center', va='center', transform=plt.gca().transAxes, fontsize = 11)
plt.title('Velocidad Normalizada')
plt.xlabel('v (m/s)')
plt.ylabel('Densidad de Probabilidad')

# Muestra el gráfico
plt.show()