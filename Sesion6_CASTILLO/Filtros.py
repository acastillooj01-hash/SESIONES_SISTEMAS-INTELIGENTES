from PIL import Image, ImageFilter

img = Image.open(r"C:\Users\DOCENTE\Desktop\Sesion6_CASTILLO\marte.jpg")
f = img.filter(ImageFilter.EMBOSS)
f.show()