# https://jv.umsa.bo/oj/problem.php?id=1026
#  Tuncuña
#  Enviar
#  Estado
#  Descripción
#    Bob ve a su hermano menor Jack jungando Tunquña. El esta facinando con lo interesante del juego, y decidio jugarlo.  Se pintan una secuencia de cuadrados en el suelo con la ayuda de una tiza, y se le asigna un numero a cada cuadrado(1, 2, 3, 4, ...). Bob esta frente a esos cuadrados. A partir de aqui, el lanza una piedra al primer cuadrado, entonces Bob se mueve a ese cuadrado y recoge la piedra, entonces el vuelve a lanzar la piedra esta vez 2 cuadrados adelante, se mueve a ese cuadrado y recoge la piedra, vuelve a lanzar la piedra pero esta vez 3 cuadrados adelante y asi sucesivamente. ¿Cual es el objetivo del juego?. El objetivo es comprobar si es posible llegar al N-esimo cuadrado con el procedimiento descrito. Bob es un poco perezoso. El jugara solo si esta seguro que puede llegar al N-esimo cuadrado. Ayuda a Bob a decidir si jugara o no.
#   Entrada
#    La primera linea contiene un  numero entero T ($1 \leq T \leq 10^5$) que indica el numero de veces que Bob jugara el juego. Cada una de las T siguientes lineas contiene un unico entero N ($1 \leq N \leq 10^{18}$)que denota el N-esimo cuadrado.
#   Salida
#    La salida se compone de varias lineas(una linea por cada juego), siguiendo los siguientes criterios: Si Bob es capaz de llegar al N-esimo cuadrado, entonces imprima "Go On Bob"(sin comillas) seguido del numero de movimientos necesarios para llegar al N-esimo cuadrado, ambos separados por un espacio. Si Bob no es capaz de llegar al N-esimo cuadrado, imprima "Better Luck Next Time" (sin comillas).
#   Ejemplo Entrada
#    223
#   Ejemplo Salida
#    Better Luck Next TimeGo On Bob 2
#   Ayuda

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