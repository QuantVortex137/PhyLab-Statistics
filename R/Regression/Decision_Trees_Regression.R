# Decision Trees Regression

# Import dataset
dataset = read.csv('dataset.csv')
dataset = dataset[, 2:3]

# Adjust decision trees model
# install.packages("rpart")
library(rpart)
regression = rpart(formula = dep_var ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))

# Predictions
y_pred = predict(regression, newdata = data.frame(ind_var = 137))

# Model graph
library(ggplot2)
x_grid = seq(min(dataset$ind_var), max(dataset$ind_var), 0.1) # Smoother curves
ggplot() +
  geom_point(aes(x = dataset$ind_var, y = dataset$dep_var),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression,
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Decision trees model") +
  xlab("ind_var") +
  ylab("dep_var")
