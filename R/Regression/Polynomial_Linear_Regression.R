# Polynomial Regression

# Import datasets
dataset = read.csv('Position_SalariesR.csv')
dataset = dataset[, 2:3] # Filtrar el dataset

# Adjust linear regression model
lin_reg = lm(formula = Dependent_var ~ .,
             data = dataset)

# Adjust polynomial regression model
dataset$ind_var2 = dataset$ind_var^2
dataset$ind_var3 = dataset$ind_var^3
dataset$ind_var4 = dataset$ind_var^4
poly_reg = lm(formula = Dependent_var ~ .,
              data = dataset)

# Linear model graph
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$ind_var, y = dataset$Dependent_var),
             color = "red") +
  geom_line(aes(x = dataset$ind_var, y = predict(lin_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Linear model") +
  xlab("ind_var") +
  ylab("Dependent_var")


# Polynomial model graph
library(ggplot2)
x_grid = seq(min(dataset$ind_var), max(dataset$ind_var), 0.1)
ggplot() +
  geom_point(aes(x = dataset$ind_var, y = dataset$Dependent_var),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(poly_reg,
                                        newdata = data.frame(ind_var = x_grid,
                                                             ind_var2 = x_grid^2,
                                                             ind_var3 = x_grid^3,
                                                             ind_var4 = x_grid^4))),
            color = "blue") +
  ggtitle("Polynomial model") +
  xlab("ind_var") +
  ylab("Dependent_var")

# Linear model predictions
y_pred = predict(lin_reg, newdata = data.frame(ind_var = 137))

# Polynomial model predictions
y_PolyPred = predict(poly_reg, newdata = data.frame(ind_var = 137,
                                                    ind_var2 = 137^2,
                                                    ind_var3 = 137^3,
                                                    ind_var4 = 137^4))
