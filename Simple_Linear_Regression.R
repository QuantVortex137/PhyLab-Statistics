# Simple Linear Regression

# Import dataset
dataset = read.csv('dataset.csv')

# Divide data in training and testing sets
# If needed, run this to install a package from the script: install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Future Update: Data encoding and scaling

regressor = lm(formula = Y ~ X,
               data = training_set)

y_pred = predict(regressor, newdata = testing_set)

# If needed, run this to install a package from the script: install.packages("ggplot2")
library(ggplot2)

# Training data set plotting with ggplot2
ggplot() + 
  geom_point(aes(x = training_set$X_column, y = training_set$Y_column),
             colour = "red") + 
  geom_line(aes(x = training_set$X_column,
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("X-Y (Training Set Only)") +
  xlab("X_data") +
  ylab("Y_data")

# Testinf data set plotting with ggplot2
ggplot() + 
  geom_point(aes(x = testing_set$X_column, y = testing_set$Y_column),
             colour = "red") + 
  geom_line(aes(x = training_set$X_column,
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("X-Y (Testing Set Only)") +
  xlab("X_data") +
  ylab("Y_data")
