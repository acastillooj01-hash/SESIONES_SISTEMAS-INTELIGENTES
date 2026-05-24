import numpy as np
import matplotlib.pyplot as plt
import cv2

def analizar_imagen(ruta_imagen, titulo):
   
    imagen = cv2.imread(ruta_imagen, 0)
    
    if imagen is None:
        print(f"Ups! No pude encontrar la imagen '{ruta_imagen}'. Revisa el nombre.")
        return

    # 1. Mostrar la imagen en escala de grises
    plt.imshow(imagen, cmap='gray')
    plt.title(f"{titulo} - Escala de Grises")
    plt.axis("off")
    plt.show()

    # 2. Obtener estadísticas básicas
    media = np.mean(imagen)
    maximo = np.max(imagen)
    minimo = np.min(imagen)

    print(f"\n--- Resultados Numéricos para {titulo} ---")
    print(f"Media: {media:.2f}") # El .2f es para que solo muestre 2 decimales
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")

    # 3. Visualizar distribución con gráfico de barras
    valores = [media, maximo, minimo]
    etiquetas = ['Media', 'Máximo', 'Mínimo']

    # Le pongo colores para que el gráfico se vea más bonito en tu informe
    colores = ['#4A90E2', '#E94B3C', '#50B432'] 
    
    plt.bar(etiquetas, valores, color=colores)
    plt.title(f"Estadísticas Básicas: {titulo}")
    plt.ylabel("Valor de los Píxeles (0 a 255)")
    plt.show()

# --- EJECUCIÓN DEL CÓDIGO ---
print("Iniciando el análisis de las imágenes...")

# Analizamos la primera imagen
analizar_imagen('imagen1.jpg', 'Imagen 1 (Clara)')

# Analizamos la segunda imagen
analizar_imagen('imagen2.jpg', 'Imagen 2 (Oscura)')

print("\n¡Análisis completado!")