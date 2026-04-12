# https://jv.umsa.bo/oj/problem.php?id=2481
#  Series de cubos
#  Enviar
#  Estado
#  Descripción
#    El problema es simple se te dará un n y debes generar hasta ese n que será un numero cubico y debes imprimir la serie de los números impares que se suman para obtener este número de la siguiente manera.
#   Entrada
#   Salida
#    La salida consta de la serie de números separados por un espacio que son los números que sumados forman el numero cubico.
#   Ejemplo Entrada
#    1827
#   Ejemplo Salida
#    1 3 5 7 9 11
#   Ayuda

import sys
for i in sys.stdin:
  N = int(i)
  n = int(N**(1/3))
  a = (N//n)
  if a%2==0:
    a = a-1
  else:
    a = a
  print(a)