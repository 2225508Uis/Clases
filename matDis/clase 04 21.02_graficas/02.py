from numpy import *
from matplotlib.pyplot import *

productos = ["producto A", "producto B", "producto C"]
ventas = [125000, 530000, 650000]

meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL"]

gastos = [250000, 560000, 52000, 690000]

pie(gastos, labels=meses, autopct="%1.3f%%")
title("G A S T O S   M E N S U A L E S")

show()
