# Polynomial Regression

# Import datasets
dataset = read.csv('Position_SalariesR.csv')
dataset = dataset[, 2:3] # Filtrar el dataset

# AJUSTAR modelo de regresión LINEAL con el dataset
lin_reg = lm(formula = Salary ~ .,
             data = dataset)

# AJUSTAR modelo de regresión POLINOMIAL con el dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)

# VISUALIZACIÓN del modelo LINEAL
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Predicción lineal del sueldo en función del nivel del empleado") +
  xlab("Nivel del empleado") +
  ylab("Sueldo en $ usd")


# VISUALIZACIÓN del modelo POLINÓMICO
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(poly_reg,
                                        newdata = data.frame(Level = x_grid,
                                                             Level2 = x_grid^2,
                                                             Level3 = x_grid^3,
                                                             Level4 = x_grid^4))),
            color = "blue") +
  ggtitle("Predicción polinómica del sueldo en función del nivel del empleado") +
  xlab("Nivel del empleado") +
  ylab("Sueldo en $ usd")

# PREDICCIÓN de nuevos resultados con regresión LINEAL
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))

# PREDICCIÓN de nuevos resultados con regresión POLINÓMICA
y_PolyPred = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                    Level2 = 6.5^2,
                                                    Level3 = 6.5^3,
                                                    Level4 = 6.5^4))