# SVM Classifier

# Import dataset
dataset = read.csv('dataset.csv')
dataset = dataset[,3:5] # Resizing dataset

library(caTools)
set.seed(123)
split = sample.split(dataset$dep_var, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Scaling values
training_set[,1:2] = scale(training_set[,1:2])
testing_set[,1:2] = scale(testing_set[,1:2])

# Adjust SVM model
library(e1071)
classifier = svm(formula = dep_var ~ .,
                 data = training_set,
                 type = "C-classification",
                 kernel = "linear") # kernel = "radial" got a better fit

# Predictions
y_pred = predict(classifier, type = "response",
                    newdata = testing_set[,-3])

# Create confusion matrix
cm = table(testing_set[,3], y_pred)

# SVM model graph
library(ElemStatLearn)
set = training_set
x1 = seq(min(set[,1]) - 1, max(set[,1]) + 1, by = 0.01)
x2 = seq(min(set[,2]) - 1, max(set[,2]) + 1, by = 0.01)
grid_set = expand.grid(x1,x2)
colnames(grid_set) = c('ind_var', 'dep_var')
y_grid = predict(classifier, newdata = grid_set)
plot(set[,-3],
     main = 'SVM (Training Set)',
     xlab = 'ind_var', ylab = 'dep_var',
     xlim = range(x1), ylim = range(x2))
contour(x1, x2, matrix(as.numeric(y_grid), length(x1), length(x2)))
points(grid_set, pch = '.', col = ifelse(y_grid == 1,'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[,3] == 1, 'green4', 'red3'))
