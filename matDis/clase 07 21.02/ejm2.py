
#para crear un conjunto vacio se usa set() porque si se usa () se generaa un diccionario


conjunto_vacio=set()

elementos = int(input("Digite cuantos elementos agregara al conjunto: "))

for posicion in range(elementos):
    datos=float(input("Dicte el numero que ba a agregar al conjunto: "))
    conjunto_vacio.add(datos)

print(conjunto_vacio)
conjunto_vacio.remove(2)



