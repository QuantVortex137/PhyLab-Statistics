# K-NN Classifier

# Importar el dataset
dataset = read.csv('dataset.csv')
dataset = dataset[,3:5] # Resizing dataset, if needed

library(caTools)
set.seed(123)
split = sample.split(dataset$Predictable_var, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Values scalating, if needed
# training_set[,1:2] = scale(training_set[,1:2])
# testing_set[,1:2] = scale(testing_set[,1:2])

# Adjust K-NN classifier to data
library(class)
y_pred = knn(train = training_set[,-3],
             test = testing_set[,-3],
             cl = training_set[,3],
             k = 5)

# Confusion Matrix
cm = table(testing_set[,3], y_pred)

# Plot with ElemStatLearn
library(ElemStatLearn)
set = training_set
x1 = seq(min(set[,1]) - 1, max(set[,1]) + 1, by = 0.01)
x2 = seq(min(set[,2]) - 1, max(set[,2]) + 1, by = 0.01)
grid_set = expand.grid(x1,x2)
colnames(grid_set) = c('var1', 'var2')
y_grid = knn(train = training_set[,-3],
             test = grid_set,
             cl = training_set[,3],
             k = 5)
plot(set[,-3],
     main = 'K-NN (Training Set)',
     xlab = 'var1', ylab = 'var2',
     xlim = range(x1), ylim = range(x2))
contour(x1, x2, matrix(as.numeric(y_grid), length(x1), length(x2)))
points(grid_set, pch = '.', col = ifelse(y_grid == 1,'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[,3] == 1, 'green4', 'red3'))
