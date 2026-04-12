# https://jv.umsa.bo/oj/problem.php?id=1434
#  Números capicúa
#  Enviar
#  Estado
#  Descripción
#    Se dice que un número es capicúa cuando puede ser leído de la misma forma de izquierda a derecha, que de derecha a izquierda por ejemplo 1001 es un número capicúa, ya que 1001 al revés es también 1001 y 123 no es porque 123 al revés es 321.
#    Se pide realizar un programa para ver si un número es capicúa o no.
#   Entrada
#    La entrada consiste de un único número entero grande N (1 <= N <= 10¹⁸) .
#   Salida
#    Imprimir la letra 'S' (sin las comillas) si el número es capicúa y 'N' en caso de que no lo sea.
#   Ejemplo Entrada
#    1001
#   Ejemplo Salida
#    S
#   Ayuda
#    Ejemplo 2:
#    Entrada:
#    123
#    Salida:
#    N

N=input()
if(N[::-1]==N):
    print("S")
else:
    print("N")