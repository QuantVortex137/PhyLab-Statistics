# TREE DECISION REGRESSION

# IMPORTAR datasets
dataset = read.csv('Position_SalariesR.csv')
dataset = dataset[, 2:3] # Filtrar el dataset

# AJUSTAR modelo de REGRESIÓN con ÁRBOLES DE DECISIÓN
# Instalar: install.packages("rpart")
library(rpart)
regression = rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))

# PREDICCIÓN de nuevos resultados con MODELO de REGRESIÓN
y_pred = predict(regression, newdata = data.frame(Level = 6.5))

# VISUALIZACIÓN del modelo de REGRESIÓN
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1) # Para lograr una mayor resolución
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression,
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Predicción del modelo de Regresión con Árbol de Decisión") +
  xlab("Posición del empleado") +
  ylab("Sueldo del empleado en dólares")

# VISUALIZACIÓN con x = dataset$Level
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(regression,
                                        newdata = data.frame(Level = dataset$Level))),
            color = "blue") +
  ggtitle("Predicción del modelo de Regresión con Árbol de Decisión") +
  xlab("Posición del empleado") +
  ylab("Sueldo del empleado en dólares")
