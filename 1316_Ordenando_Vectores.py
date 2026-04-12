# https://jv.umsa.bo/oj/problem.php?id=1316
#  Ordenando Vectores
#  Enviar
#  Estado
#  Descripción
#    Dados dos arreglos de números enteros $A,B$ donde cada uno contiene ($1 \leq N \leq 100$) números.definimos la función $S=\sum_{i=0}^{i=N} a_i b_i$Se pide reordenar el arreglo $A$ de tal forma que la función $S$ de el valor mínimo.
#   Entrada
#    La entrada consiste de varios casos de prueba. Cada caso de prueba consiste de tres líneas. La primera línea tiene el número $N$ de elementos de los vectores $A,B$. La segunda línea tiene los elementos del vector $A$ separados por un espacio. La tercera línea los elementos del vector $B$ separados por un espacio.La entrada termina cuando no hay más datos.
#   Salida
#    En la salida escriba en una línea el valor mínimo de $S$.
#   Ejemplo Entrada
#    31 1 310 30 2051 1 1 6 02 7 8 3 195 15 100 31 39 0 0 3 2611 12 13 2 3 4 5 9 1
#   Ejemplo Salida
#    8018528
#   Ayuda

import sys
for i in sys.stdin:
  N = int(i)
  A = [int(x) for x in input().rstrip().split(" ")]
  B = [int(x) for x in input().rstrip().split(" ")]
  A.sort(reverse = True)
  B.sort()
  resultado = [a*b for a, b in zip(A, B)]
  print(sum(resultado))