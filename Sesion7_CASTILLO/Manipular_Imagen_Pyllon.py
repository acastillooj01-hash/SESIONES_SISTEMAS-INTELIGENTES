from PIL import Image

img = Image.open(r"C:\Users\DOCENTE\Desktop\Sesion6_CASTILLO\marte.jpg")
imgrotate = img.rotate(90)
imgrotate.show()