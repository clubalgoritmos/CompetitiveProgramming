# https://jv.umsa.bo/oj/problem.php?id=1847
#  Clave Murcielago
#  Enviar
#  Estado
#  Descripción
#    La clave MURCIELAGO es una sencilla clave que como Boy Scout aprender debes. Es fácil de realizar por su ventaja de
#    cambiar las letras por símbolos numéricos, trabajando con la siguiente tabla de conversión:
#    M=0, U=1, R=2, C=3, I=4, E=5. L=6. A=7, G=8, O=9
#    De manera que si nuestro texto original fuera BOLIVIA
#    el resultado de la codificación sería: B964V47
#   Entrada
#    La entrada consiste en un entero N que es el número de casos de prueba, seguido de las N líneas que contiene una cadena escrita totalemente en letras mayúsculas.
#   Salida
#    Imprimir N líneas con las cadenas convertidas.
#   Ejemplo Entrada
#    3BOLIVIAUNIVERSITARIOENTRADA
#   Ejemplo Salida
#    B964V471N4V52S4T72495NT27D7
#   Ayuda

code = "MURCIELAGO"
for _ in range(int(input())):
  r = ""
  for c in input().upper():
    if c in code:
      r = r + str(code.find(c))
    else:
      r = r + c
  print(r)