import numpy as np
import sys
import os

# Esto ayuda a que el test encuentre la carpeta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from image_processing.transform import ajustar_brillo, convertir_grises

def test_convertir_grises_dimensiones():
    imagen = np.zeros((10, 10, 3), dtype=np.uint8)
    resultado = convertir_grises(imagen)
    assert resultado.ndim == 2

def test_ajustar_brillo_dimensiones():
    imagen = np.zeros((10, 10), dtype=np.uint8)
    resultado = ajustar_brillo(imagen, alpha=1.2, beta=30)
    assert resultado.shape == (10, 10)
