import matplotlib.pyplot as plt

divisiones = [7, 2, 5, 11]
actividades = ['Dormir', 'Comer', 'Trabajar', 'Recreacion']
colores = ['red', 'purple', 'blue', 'orange']

plt.pie(divisiones, labels=actividades, colors=colores, startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')
plt.title('Gráficos Circular')
plt.show()