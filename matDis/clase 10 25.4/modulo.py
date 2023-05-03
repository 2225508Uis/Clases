from itertools import permutations
from itertools import combinations


class GeneradorPermucationes:
  def __init__(self, Parametro_letras, nmr) -> None:
    self.letras = Parametro_letras
    self.nmr = nmr

  def Imprimir(self):
    resultado_permutaciones = list(permutations(self.letras, self.nmr))
    print("numero de permutaciones: ", len(
        resultado_permutaciones), "agrupado de a: ", self.nmr)
    for i in resultado_permutaciones:
      print(list(i))


class GeneradorCombinaciones:
  def __init__(self, Parametro_letras, nmr) -> None:
    self.letras = Parametro_letras
    self.nmr = nmr

  def Imprimir(self):
    resultado_Combinaciones = list(combinations(self.letras, self.nmr))
    print("numero combinaciones: ", len(
        resultado_Combinaciones), "agrupado de a: ", self.nmr)
    for i in resultado_Combinaciones:
      print(list(i))
