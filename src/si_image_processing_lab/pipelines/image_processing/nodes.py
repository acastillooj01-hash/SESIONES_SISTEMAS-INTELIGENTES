from PIL import Image, ImageFilter, ImageDraw

def process_image(
    input_path: str, 
    output_path: str, 
    rotation_angle: int, 
    filter_name: str, 
    watermark_text: str
) -> str:
    # 1. Abrir la imagen original
    image = Image.open(input_path)
    
    # 2. Rotación dinámica (Reto)
    rotated = image.rotate(rotation_angle)
    
    # 3. Filtro dinámico FIND_EDGES (Reto)
    if filter_name == "FIND_EDGES":
        filtered = rotated.filter(ImageFilter.FIND_EDGES)
    else:
        filtered = rotated.filter(ImageFilter.EMBOSS)
        
    # 4. Marca de agua personalizada (Reto)
    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), watermark_text, fill="white")
    
    # 5. Guardar el resultado
    filtered.save(output_path)
    return output_path