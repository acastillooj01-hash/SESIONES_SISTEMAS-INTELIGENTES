import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen en escala de grises y mostrar
imagen = cv2.imread('imagen_prueba.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(imagen, cmap='gray')
plt.title('Escalas de Grises')
plt.axis('off')
plt.show()

# 2. Aplicar filtro gaussiano
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)
plt.imshow(imagen_suavizada, cmap='gray')
plt.title('Imagen Suavizada (Filtro Gaussiano)')
plt.axis('off')
plt.show()

# 3. Detección de bordes (Método de Canny)
bordes = cv2.Canny(imagen_suavizada, 50, 150)
plt.imshow(bordes, cmap='gray')
plt.title('Detección de Bordes (Canny)')
plt.axis('off')
plt.show()

# 4. Detección de esquinas (Detector de Harris)
imagen_color = cv2.imread('imagen_prueba.png')
imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)
esquinas = cv2.cornerHarris(np.float32(imagen), 2, 3, 0.04)
imagen_color[esquinas > 0.01 * esquinas.max()] = [255, 0, 0]
plt.imshow(imagen_color)
plt.title('Detección de Esquinas (Harris)')
plt.axis('off')
plt.show()

# 5. Detección de líneas y curvas (Transformada de Hough)
# Recargamos la imagen original a color para dibujar las líneas verdes sin las esquinas previas
imagen_lineas = cv2.imread('imagen_prueba.png')
imagen_lineas = cv2.cvtColor(imagen_lineas, cv2.COLOR_BGR2RGB)

lineas = cv2.HoughLinesP(bordes, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)

if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_lineas, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.imshow(imagen_lineas)
plt.title('Detección de Líneas (Hough)')
plt.axis('off')
plt.show()