# Import dataset
dataset = read.csv('dataset.csv')

# Unknown "NA" data treatment
dataset$X_column = ifelse(is.na(dataset$X_column),
                     ave(dataset$X_column, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$X_column)
dataset$Y_column = ifelse(is.na(dataset$Y_column),
                        ave(dataset$Y_column, FUN = function(x)mean(x, na.rm = TRUE)),
                        dataset$Y_column)

# Categorical variables encoding
dataset$Z_column = factor(dataset$Z_column,
                         levels = c("catdata_1", "catdata_2", "catdata_3"),
                         labels = c(1, 2, 3))
dataset$W_column = factor(dataset$W_column,
                           levels = c("No", "Yes"),
                           labels = c(0,1)) # Categorical data examples

# Divide data in training and testing sets
# Run this to install a package from the script: install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$X_column, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Values Escalating
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3]) # You must change the values
