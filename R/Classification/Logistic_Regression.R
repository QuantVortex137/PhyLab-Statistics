# Logistic Regression

# Importar dataset
dataset = read.csv('dataset.csv')
dataset = dataset[,3:5] # Resizing dataset if needed

library(caTools)
set.seed(123)
split = sample.split(dataset$Predictable_var, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Values Scalating
training_set[,1:2] = scale(training_set[,1:2])
testing_set[,1:2] = scale(testing_set[,1:2])

# Adjust logistic regression model to training set
classifier = glm(formula = Predictable_var ~ .,
                 data = training_set,
                 family = binomial) # Needs to be binomial for yes & no data predictions

# Prediction of the results from the testing set
prob_pred = predict(classifier, type = "response", 
                    newdata = testing_set[,-3])

y_pred = ifelse(prob_pred > 0.5, 1, 0) # 1 & 0 for yes & no

# Create confusion matrix
cm = table(testing_set[,3], y_pred)

# Plotting traning_set. Change the value of var 'set' if needed
library(ElemStatLearn)
set = training_set
x1 = seq(min(set[,1]) - 1, max(set[,1]) + 1, by = 0.01)
x2 = seq(min(set[,2]) - 1, max(set[,2]) + 1, by = 0.01)
grid_set = expand.grid(x1,x2)
colnames(grid_set) = c('Independant_var', 'Dependant_var')
prob_set = predict(classifier, type = 'response', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[,-3],
     main = 'Clasificación (Testing Set)',
     xlab = 'Independant_var', ylab = 'Dependant_var',
     xlim = range(x1), ylim = range(x2))
contour(x1, x2, matrix(as.numeric(y_grid), length(x1), length(x2)))
points(grid_set, pch = '.', col = ifelse(y_grid == 1,'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[,3] == 1, 'green4', 'red3'))

