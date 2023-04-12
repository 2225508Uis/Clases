"""Module providingFunction printing python version."""

import matplotlib.pyplot as plt
plt.matplotlib.use("Agg")
import os

# Datos de prueba
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [3, 6, 9, 12, 15]

fig,ax = plt.subplots()
ax.plot(x,y1)
fig.savefig("grafica.png")
os.system("cat grafica.png")
