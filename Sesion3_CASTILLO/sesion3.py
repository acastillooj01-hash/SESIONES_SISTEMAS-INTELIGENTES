import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('imagen_prueba.jpg', 0) 
img2 = cv2.imread('imagen_prueba2.jpg', 0) 

#  Calcular histogramas
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

# Visualización de Resultados 
plt.figure(figsize=(12, 8))

# Mostrar Imagen 1 y su Histograma
plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title("Imagen 1")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.plot(hist1, color='black')
plt.title("Histograma Imagen 1")
plt.xlabel("Nivel de Gris")
plt.ylabel("Frecuencia")

# Mostrar Imagen 2 y su Histograma
plt.subplot(2, 2, 3)
plt.imshow(img2, cmap='gray')
plt.title("Imagen 2")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.plot(hist2, color='black')
plt.title("Histograma Imagen 2")
plt.xlabel("Nivel de Gris")
plt.ylabel("Frecuencia")

plt.tight_layout()
plt.show()