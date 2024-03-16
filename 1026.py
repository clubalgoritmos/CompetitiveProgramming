import math
import sys

# Leer todas las entradas a la vez
inputs = map(int, sys.stdin.read().split())

# Saltar el número de casos de prueba
next(inputs)

# Procesar cada caso de prueba
outputs = []
for n in inputs:
    i = (-1 + math.sqrt(1 + 8*n))/2
    if i == int(i):
        outputs.append(f"Go On Bob {int(i)}")
    else:
        outputs.append("Better Luck Next Time")

# Imprimir todas las salidas a la vez
print('\n'.join(outputs))