# SVR Regression

# Import dataset
dataset = read.csv('dataset.csv')
dataset = dataset[, 2:3]

# Divide dataset
library(caTools)
set.seed(123)
split = sample.split(dataset$dependent_var, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Values Scalating
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# install.packages("e1071")
library(e1071)

# Adjust SVR Regression model
regression = svm(formula = dependent_var ~ .,
                 data = dataset,
                 type = "eps-regression",
                 kernel = "radial")

# Predictions
y_pred= predict(regression, newdata = data.frame(ind_var = 137))

# Model graph
# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$ind_var), max(dataset$ind_var), 0.1) # Grid for smoother curves
ggplot() +
  geom_point(aes(x = dataset$ind_var, y = dataset$dependent_var),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression,
                                        newdata = data.frame(ind_var = x_grid))),
            color = "blue") +
  ggtitle("SVR Model") +
  xlab("ind_var") +
  ylab("dependent_var")
