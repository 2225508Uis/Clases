from numpy import *
from matplotlib.pyplot import *

edades = random.normal(40, 10, 1000)


hist(edades, bins=20)
show()

media = mean(edades)
print("la media es ")
print(media)

estandar = std(edades)
print("la edad es")
print(estandar)
