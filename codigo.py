import numpy as np
numeros = np.random.chisquare(df=3,size=1000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=numeros, bins=30)
plt.title('Histograma de tiempos de servicio')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
plt.show()

#Se crea una grafica con una dstribución normal y una linea de densidad.
mu = 3
sigma = 0.5 
n = 1000

numeros = np.random.normal(mu, sigma, n)

# Graficar histograma
count, bins, ignored = plt.hist(x=numeros, bins=30, density=True, color='blue', alpha=0.7)

# Agregar línea de densidad de probabilidad
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='red')

plt.title('Histograma de tiempos de servicio (Distribución Normal)')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
plt.show()

r=1+2
