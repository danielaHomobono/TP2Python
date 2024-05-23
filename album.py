

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

def crear_album(figus_total):
    return np.zeros(figus_total)

def comprar_paquete(figus_total, figus_paquete):
    return rd.sample(range(figus_total), figus_paquete)

def pegar_figus(album, paquete):
    album[paquete] = 1
    return album

def album_incompleto(album):
    return 0 in album

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        album = pegar_figus(album, paquete)
        paquetes += 1
    return paquetes

# Simulación
N = 100
figus_total = 860
figus_paquete = 5
rd.seed(123)
muestras = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(N)]
print(f"Se necesitan en promedio {np.mean(muestras)} paquetes para llenar el álbum.")

# para el histograma
sns.histplot(muestras, kde=False, bins=30)

# Agregar títulos y etiquetas
plt.title('Histograma de la cantidad de paquetes necesarios')
plt.xlabel('Cantidad de paquetes')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()
