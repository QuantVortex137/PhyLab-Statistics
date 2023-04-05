# Importar archivo csv
datos <- read.csv("ruta/al/archivo.csv")

# Crear histograma de la columna "datos"
hist(datos$columna, main="Distribución de los datos", xlab="Valores")

# Calcular media y desviación estándar
media <- mean(datos$columna)
desviacion <- sd(datos$columna)

# Crear vector de valores para la curva de distribución normal
valores <- seq(min(datos$columna), max(datos$columna), length=100)
curva <- dnorm(valores, mean=media, sd=desviacion)*length(datos$columna)

# Agregar curva de distribución normal al histograma
lines(valores, curva, col="blue", lwd=2)
