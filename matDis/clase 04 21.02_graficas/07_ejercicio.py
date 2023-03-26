from numpy import *
from matplotlib.pyplot import *

tiempo = ["año 1", "año 2", "año 3", "año 4", "año 5"]
demanda = [7, 9, 15, 10, 12]

media = mean(demanda)
desviacion = std(demanda)

titulo = "La media es: ("+str(media) + \
    ") La desviacion es: ("+str(desviacion)+")"

# -----------------salidas--------------------\
print("la media es: ")
print(media)
print("la desviacion es; ")
print(desviacion)
# -----------------salidas--------------------/

bar(tiempo, demanda)
title(titulo)
show()
