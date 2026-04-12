# https://jv.umsa.bo/oj/problem.php?id=1284
#  Mezclar en base dos
#  Enviar
#  Estado
#  Descripción
#   Entrada
#    La entrada consiste de múltiples casos de prueba. Cada uno con el mismo número de bits entre 0 y 30.
#   Salida
#    Para cada caso de prueba escriba la mezcla de los dos números como se explicó.
#   Ejemplo Entrada
#    8 151 12 31000 600900000 1000000
#   Ejemplo Salida
#    11010101111101111010111001110000001111011110011010100011101001100000000000
#   Ayuda

import sys
for i in sys.stdin:
  a,b = map(int, i.split(" "))
  resultado = ""
  for i in range(max(len(bin(a)[2:]), len(bin(b)[2:]))):
      if i < len(bin(a)[2:]):
          resultado += bin(a)[2:][i]
      if i < len(bin(b)[2:]):
          resultado += bin(b)[2:][i] 
  print(resultado)