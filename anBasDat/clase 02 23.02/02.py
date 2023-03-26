from numpy import *

import random

numeros = []


while len(numeros) < 100:
    numero = random.randint(1, 100)
    if numero not in numeros:
        numeros.append(numero)

while True:
    total = len(numeros)
    print(total)
    break
