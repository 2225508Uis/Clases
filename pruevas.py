"""Module providingFunction printing python version."""

import matplotlib.pyplot as plt


# Datos de prueba
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [3, 6, 9, 12, 15]

# Creación de la gráfica
plt.plot(x, y1, label='Línea 1')
plt.plot(x, y2, label='Línea 2')

# Título y etiquetas del eje
plt.title('Gráfica con dos líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Leyenda
plt.legend()

# Mostrar gráfica
plt.show()
