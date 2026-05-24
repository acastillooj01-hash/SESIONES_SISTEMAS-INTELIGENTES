import os
from si_image_processing_lab.pipelines.image_processing.nodes import process_image

def test_process_image():
    # Asegurar que existan los directorios de prueba
    os.makedirs("data/01_raw", exist_ok=True)
    os.makedirs("data/03_primary", exist_ok=True)
    
    # Crear una imagen temporal para la prueba si no existe marte.jpg
    from PIL import Image
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save("data/01_raw/marte.jpg")

    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_output.jpg",
        90,
        "FIND_EDGES",
        "Test Watermark"
    )
    assert result is not None
    assert os.path.exists("data/03_primary/test_output.jpg")