# RANDOM FOREST REGRESSION

# IMPORTAR datasets
dataset = read.csv('Position_SalariesR.csv')
dataset = dataset[, 2:3] # Filtrar el dataset

# AJUSTAR modelo de REGRESIÓN
# Instalar: install.packages("randomForest")
library(randomForest)
set.seed(1234)
regression = randomForest(x = dataset[1],
                          y = dataset$Salary,
                          ntree = 1000)

# PREDICCIÓN de nuevos resultados con MODELO de REGRESIÓN
y_pred = predict(regression, newdata = data.frame(Level = 6.5))

# VISUALIZACIÓN del modelo de REGRESIÓN
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression,
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Predicción del modelo de Regresión de Bosques Aleatorios") +
  xlab("Posición del empleado") +
  ylab("Sueldo del empleado en dólares")