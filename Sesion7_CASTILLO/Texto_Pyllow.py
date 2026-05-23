from PIL import Image, ImageDraw, ImageFont 

img = Image.open(r"C:\Users\DOCENTE\Desktop\Sesion6_CASTILLO\marte.jpg")
dibujo = ImageDraw.Draw(img)

fuente = ImageFont.truetype("arial.ttf", 90)

dibujo.text((500, 500), "Sistemas Inteligentes - UCV", fill="white", font=fuente)

img.show()