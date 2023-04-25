# Random Forest Regression

# Import dataset
dataset = read.csv('dataset.csv')
dataset = dataset[, 2:3]

# Adjust model
# install.packages("randomForest")
library(randomForest)
set.seed(31415)
regression = randomForest(x = dataset[1],
                          y = dataset$dep_var,
                          ntree = 1000) # Increase or decrease the number of trees used

# Predictions
y_pred = predict(regression, newdata = data.frame(dep_var = 137))

# Model graph
library(ggplot2)
x_grid = seq(min(dataset$ind_var), max(dataset$ind_var), 0.01)
ggplot() +
  geom_point(aes(x = dataset$ind_var, y = dataset$dep_var),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression,
                                        newdata = data.frame(ind_var = x_grid))),
            color = "blue") +
  ggtitle("Random forest model") +
  xlab("ind_var") +
  ylab("dep_var")
