# Multiple Linear Regression

## Import datasets, the .csv file
dataset = read.csv('50_StartupsR.csv')

## Categorical data encoding
dataset$State = factor(dataset$State,
                         levels = c("New York", "California", "Florida"),
                         labels = c(1, 2, 3))

## Divide data in training and test sets
# Run this to install a package from the script: install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# No se necesita escalar variables

# Ajustar el modelo de Regresión Lineal Múltiple con el training set
# formula = Profit ~ . significa que la variabl dependiente Profit está en función de todas las otras variabels
regression = lm(formula = Profit ~ .,# R.D.Spend + Administration + Marketing.Spend + ... + n.VariblesIndependientes
                data = training_set)

# Para obtener un resumen estadístico de la RLM se puede escribir el comando
# summary(regression) en consola o en el script

# Predecir los resultados con el testing set
y_pred = predict(regression, newdata = testing_set)

# Construir un modelo óptimo con la eliminación hacia atrás manualmente usando TODO el conjunto de datos
SL = 0.05
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend,
                data = dataset)
summary(regression)

# Modelo --> Profit(R.D.Spend) = (8.543e-01)(R.D.Spend) + (4.903e+04) con un R Cuadrada de 0.9454

# Para instalar ElemStatLearn: install.packages("https://cran.r-project.org/src/contrib/Archive/ElemStatLearn/ElemStatLearn_2015.6.26.2.tar.gz",repos=NULL, type="source")
library(ElemStatLearn)