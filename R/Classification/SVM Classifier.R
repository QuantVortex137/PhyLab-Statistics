# SVM Classifier

# Importar el dataset
dataset = read.csv('Social_Network_Ads.csv')
dataset = dataset[,3:5] # Resizing dataset

library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
training_set[,1:2] = scale(training_set[,1:2])
testing_set[,1:2] = scale(testing_set[,1:2])

# Ajustar el modelo de svm con el conjunto de entrenamiento
library(e1071)
classifier = svm(formula = Purchased ~ .,
                 data = training_set,
                 type = "C-classification",
                 kernel = "linear")

# Predicción de los resultados con el conjunto de entrenamiento
y_pred = predict(classifier, type = "response",
                    newdata = testing_set[,-3])

# Crear la matriz de confusión
cm = table(testing_set[,3], y_pred)

# Visualización del conjunto de entrenamiento
library(ElemStatLearn)
set = training_set
x1 = seq(min(set[,1]) - 1, max(set[,1]) + 1, by = 0.01)
x2 = seq(min(set[,2]) - 1, max(set[,2]) + 1, by = 0.01)
grid_set = expand.grid(x1,x2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set)
plot(set[,-3],
     main = 'SVM (Training Set)',
     xlab = 'Edad', ylab = 'Suedo Estimado',
     xlim = range(x1), ylim = range(x2))
contour(x1, x2, matrix(as.numeric(y_grid), length(x1), length(x2)))
points(grid_set, pch = '.', col = ifelse(y_grid == 1,'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[,3] == 1, 'green4', 'red3'))