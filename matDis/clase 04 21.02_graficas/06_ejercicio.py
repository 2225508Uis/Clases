from numpy import *
from matplotlib.pyplot import *

tiempo_de_espera = random.normal(10, 5, 10)
print(tiempo_de_espera)
hist(tiempo_de_espera, bins=10)
show()
