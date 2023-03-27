# Simple Linear Regression

# Import datasets
dataset = read.csv('Salary_DataR.csv')

# Divide data in training and test sets
# Run this to install a package from the script: install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# No fue necesario codificar datos ni escalar valores

# Ajustar el modelo de regresión lineal simple con el conjunto de entrenamiento
# "~" Define el salario en función de los años de experiencia
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

# Predecir resultados con testing set
y_pred = predict(regressor, newdata = testing_set)

# Visualización de los resultados del training set usando ggplot2
# install.packages("ggplot2")
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience,
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo v.s. Años de experiencia (Training Set Only)") +
  xlab("Años de experiencia (años)") +
  ylab("Sueldo ($ usd)")

# Visualización de los resulatdos en el testing set
ggplot() + 
  geom_point(aes(x = testing_set$YearsExperience, y = testing_set$Salary),
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience,
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo v.s. Años de experiencia (Testing Set Only)") +
  xlab("Años de experiencia (años)") +
  ylab("Sueldo ($ usd)")