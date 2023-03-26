from numpy import *
from matplotlib.pyplot import *

datos = random.randint(0, 100, size=1000)
print(type(datos))
boxplot(datos)
show()
