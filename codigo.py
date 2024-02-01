import numpy as np
mu = 3
sigma = 0.5 
n=1000
numeros = np.random.chisquare(df=3,size=1000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=numeros, bins=30)
plt.title('Histograma de tiempos de servicio')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
plt.show()

