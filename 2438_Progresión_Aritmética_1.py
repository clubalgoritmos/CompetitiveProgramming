# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=0
## https://jv.umsa.bo/oj/problem.php?id=2438
#  Progresión Aritmética 1
#  Enviar
#  Estado
#  Descripción
#    Considere la siguiente progresión aritmética: -7, -3, 1, 5, 9, 13, . . .En la posición 1 está el -7, en la posición 3 está el 1, en la posición 6 está el 13.El problema consiste en leer un número entero que corresponda a la posición e indicar el valor correspondiente a la progresión aritmética.
#   Entrada
#    Contiene un número n (1 ≤ n ≤ 500)
#   Salida
#    Imprima en una línea el valor correspondiente a la posición n en la progresión aritmética.
#   Ejemplo Entrada
#    6
#   Ejemplo Salida
#    13
#   Ayuda
N = int(input())
print(-7+4*(N-1))