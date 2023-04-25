# Multiple Linear Regression

dataset = read.csv('dataset.csv')

# Categorical data encoding
dataset$column_categorical = factor(dataset$column_categorical,
                         levels = c("cat_1", "cat_2", "cat_3"),
                         labels = c(1, 2, 3))

# Divide data in training and testing sets
library(caTools)
set.seed(123)
split = sample.split(dataset$dependentvar_column, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Adjust multiple linear regression to training set
regression = lm(formula = dependentvar_column ~ .,# columnvar_1 + columnvar_2 + columnvar_3 + ... + columnvar_n
                data = training_set)

summary(regression)

# Predict data with testing_set
y_pred = predict(regression, newdata = testing_set)

# Manual backwards elimination
SL = 0.05
regression = lm(formula = dependentvar_column ~ columnvar_1 + columnvar_2 + columnvar_3 + columnvar_4,
                data = dataset)
summary(regression)

regression = lm(formula = dependentvar_column ~ columnvar_1 + columnvar_2 + columnvar_3,
                data = dataset)
summary(regression)

regression = lm(formula = dependentvar_column ~ columnvar_1 + columnvar_2,
                data = dataset)
summary(regression)

regression = lm(formula = dependentvar_column ~ columnvar_1,
                data = dataset)
summary(regression)

# For installing ElemStatLearn: install.packages("https://cran.r-project.org/src/contrib/Archive/ElemStatLearn/ElemStatLearn_2015.6.26.2.tar.gz",repos=NULL, type="source")
library(ElemStatLearn)
