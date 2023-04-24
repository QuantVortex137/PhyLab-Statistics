# REGRESSION SVR

# IMPORTAR datasets
dataset = read.csv('Position_SalariesR.csv')
dataset = dataset[, 2:3] # Filtrar el dataset

# # DIVIDIR el dataset en subconjuntos
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Salary, SplitRatio = 2/3)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)

# ESCALADO de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Instalar: install.packages("e1071")
library(e1071)

# AJUSTAR modelo de REGRESIÓN SVR
regression = svm(formula = Salary ~ .,
                 data = dataset,
                 type = "eps-regression",
                 kernel = "radial")


# PREDICCIÓN de nuevos resultados con MODELO de REGRESIÓN
y_pred= predict(regression, newdata = data.frame(Level = 6.5,..., n_Level = 6.5^n))

# VISUALIZACIÓN del modelo de REGRESIÓN
# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1) # Para lograr una mayor resolución
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression,
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Predicción del modelo de Regresión SVR") +
  xlab("Posición del empleado") +
  ylab("Sueldo del empleado en dólares")
