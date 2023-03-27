# R Machine Learning
# Part 1 - Pre-processing data

# Import datasets
dataset = read.csv('C:/Users/1107473901/Documents/Proyectos Software/R Studio/R Part 1 - Data pre-processing/Data1R.csv')

# Unknown "NA" data treatment
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x)mean(x, na.rm = TRUE)),
                        dataset$Salary)

# Categorical variables encoding
dataset$Country = factor(dataset$Country,
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0,1))

# Divide data in training and test sets
# Run this to install a package from the script: install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Values Escalating
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])

