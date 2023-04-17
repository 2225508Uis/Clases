#hacer una grafica con mathplotlib


import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y)
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Grafica de ejemplo')
plt.show()
