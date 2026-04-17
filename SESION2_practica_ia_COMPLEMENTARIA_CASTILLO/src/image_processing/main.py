import cv2
import matplotlib.pyplot as plt
from pathlib import Path
from image_processing.loader import cargar_imagen
from image_processing.transform import convertir_grises, ajustar_brillo

def main():
    # Ruta relativa a la raíz del proyecto
    ruta = Path("data/imagen_prueba.jpg")
    imagen = cargar_imagen(str(ruta))

    if imagen is None:
        print(f"Error: No se encontró la imagen en {ruta.absolute()}")
        return

    # OpenCV usa BGR, Matplotlib usa RGB
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    gris = convertir_grises(imagen)
    brillo = ajustar_brillo(gris, alpha=1.2, beta=30)

    # Mostrar resultados
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(imagen_rgb)
    plt.title("Original (Color)")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(gris, cmap="gray")
    plt.title("Escala de Grises")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(brillo, cmap="gray")
    plt.title("Brillo Ajustado")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()