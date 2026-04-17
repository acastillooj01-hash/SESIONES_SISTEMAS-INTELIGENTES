import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
imagen = cv2.imread('image\imagen_prueba.png')

# Verificar si la imagen cargó
if imagen is None:
    print("Error: No se encontró la imagen")
    exit()

# Convertir de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Mostrar imagen original
plt.imshow(imagen_rgb)
plt.title("Imagen Original")
plt.axis("off")
plt.show()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

plt.imshow(gris, cmap='gray')
plt.title("Imagen en Escala de Grises")
plt.axis("off")
plt.show()

# Ajustar brillo
brillo = cv2.convertScaleAbs(gris, alpha=1.2, beta=30)

plt.imshow(brillo, cmap='gray')
plt.title("Imagen con Brillo Ajustado")
plt.axis("off")
plt.show()