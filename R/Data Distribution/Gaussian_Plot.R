# Import data from csv
data <- read.csv("dataset.csv")

# Create histogram for data
hist(data$column, main="Data Distribution", xlab="Values")

# Calculate mean and standard deviation
mu <- mean(data$column)
sigma <- sd(data$column)

# Crear vector of values for the normal distribution curve
values <- seq(min(data$column), max(data$column), length=100)
curve <- dnorm(values, mean=mu, sd=sigma)*length(data$column)

# Add the normal distribution curve to the histogram
lines(values, curve, col="blue", lwd=2)
