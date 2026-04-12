# https://jv.umsa.bo/oj/problem.php?id=1291
#  Lectura3
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#    Por cada caso de prueba escrita en una linea la suma de los números.
#   Ejemplo Entrada
#    1 2 3 4 09 8 7 6 5 4 3 2 1 -5 0-1 -3 5 3 1 0
#   Ejemplo Salida
#    10405
#   Ayuda

import sys
for line in sys.stdin:
    print(sum(map(int, line.split())))