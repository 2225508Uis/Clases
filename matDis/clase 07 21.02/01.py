from numpy import *
from matplotlib.pyplot import *




agua = array([10,20,30,40,50,60,70,80,90,100])
produccion = array([100,200,400,600,800,1000,1100,1200,1300,1400])

scatter(agua,produccion)
scatter(agua,produccion)
xlabel("Cantidad De agua aplicada")
ylabel("Produccion de los cultivos")
show()

if produccion.max() == produccion[-1]:
  print("No se puede determinar la cantidad optima de agua")
else:
  cantidad_optima = agua[argmax(produccion)]
  print("La cantidad óptima de agua a aplicar es de",cantidad_optima,"litros")
