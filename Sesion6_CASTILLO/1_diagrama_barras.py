import numpy as np
import matplotlib.pyplot as plt

x1 = [2, 3, 4]
y1 = [3, 5, 6]
x2 = [5, 6, 8]
y2 = [4, 4, 3]

plt.bar(x1, y1, label='Línea 1', color='blue')
plt.bar(x2, y2, label='Línea 2', color='green')

plt.title('Diagrama de Barras')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.show()