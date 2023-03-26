
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *

ventas = {'producto A':75,'producto B':150,'producto C':50,'producto D':200,'producto E':125,'producto F':75,'producto G':100}

productos_con_alta_demanda = set()

for producto,i in ventas.items():
    if i > 100:
        productos_con_alta_demanda.add(producto)
        print(f"{producto} tuvo una demanda alta")
    elif i == 100:
        print(f"{producto} tuvo una demanda de exactamente 100 unidades")
    else:
        print(f"{producto} tuvo una demanda baja")



print(type(ventas))

productos = ventas.keys()
unidades_vendidas = ventas.values()

bar(productos,unidades_vendidas)
xlabel("productos")
ylabel("unidades vendidas")
title("Datos de ventas de los ultimos seis meses")
title("Datos de ventas de los ultimos seis meses")
show()
print("los siguientes productos tuvieron una demanda mayor a 100 unidades: ")

for producto in productos_con_alta_demanda:
    print(producto)
