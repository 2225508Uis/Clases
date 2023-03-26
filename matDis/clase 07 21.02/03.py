
electronica = {"TV", "computadora", "teléfono"}

ropa = {"camisa", "pantalón", "zapato"}

alimentos = {"manzana", "leche", "pan"}

producto_vendido = "Tv"

if producto_vendido in electronica:
    electronica.remove(producto_vendido)

elif producto_vendido in ropa:
    ropa.remove(producto_vendido)

elif producto_vendido in alimentos:
    alimentos.remove(producto_vendido)

else:
    print("producto no encontrado \n")

inventario_total = electronica.union(ropa, alimentos)
print("productos totales: ", inventario_total,"\n")

productos_comunes = electronica.intersection(ropa)
print("productos comunes entre elctronica y ropa: ", productos_comunes,"\n")

#esto solo funcina con conjuntos y diccionario, no con listas y etc.
