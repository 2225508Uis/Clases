

concierto = set()
conferencia = set()

NConcierto = int(input("cuantas personas asistieron al concierto: "))

for i in range(NConcierto):
  persona = str(input("nombre: "))
  concierto.add(persona)
print("\n")

NConferencia = int(input("cuantas personas asistieron a la conferencia: "))

for i in range(NConferencia):
  persona = str(input("nombre: "))
  conferencia.add(persona)
print("\n")

print("listado asistencia a ambos eventos:\n",concierto.intersection(conferencia),"\n")

print("listado concierto:")
print(concierto)
print("\n")

print("listado conferencia:")
print(conferencia)
print("\n")

""" a=True
while a:
  val = input("bucar? y/n: ")
  if val == "y":
    b=True
    while b:
      val2 = input("lista: concierto=1/conferencia=2: ")
      if val2 == "1":
        busqueda = str(input("buscar nombre: "))
        for i in concierto:
          if i==busqueda:
            print("se encontro:",i)
            b=False

      elif val2 == "2":
        ""
      else:
        print("input invalido\n")
  elif val == "n":
    break
  else:
    print("input invalido\n") """
