from numpy import *
from matplotlib.pyplot import *

productos = ["producto A", "producto B", "producto C"]
ventas = [125000, 530000, 650000]

bar(productos, ventas)
title("V E N T A S   T R I M E S T R A L E S")
xlabel("P R O D U C T O S")
ylabel("#   V E N T A S")
show()
