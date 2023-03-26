print("")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<inicio>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


num_1 = 50
num_2 = 50.2
num_3 = "50.3"

tupla = ("tengo", "hambre", "por", 56)

lista = ["lorem ipsum", "no", "tengo", "hambre"]

diccionario = {"dato1": 123, "dato2": 456}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# int y float
print(type(num_1))
print(type(num_2))
print(type(num_3+"\n"))


# tuplas => no se puede alterar
print(type(tupla))
print(tupla)
print(tupla[0]+"\n")


# listas
print(lista)
print(lista[0]+"\n")


# Diccionario => tiene llave y valor, la llave tiene que estar en comillas y cada pareja separaad por una ","
print(type(diccionario))
print(diccionario)
print(diccionario["dato1"])
print("")

VARIABLE = str(input("digite el valor de la variable: "))
print("la variable es: " + VARIABLE+"\n")


# potencia
num1 = float(input("digite la base: "))
num2 = float(input("digite la potencia: \n"))

resultado1 = num1**num2
resultado2 = pow(num1, num2)
print("el resultado con ** es: ")
print(resultado1)
print("")
print("el resultado con pow es: ")
print(resultado2)
print("")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<fin>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
