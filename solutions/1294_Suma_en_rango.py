# https://jv.umsa.bo/oj/problem.php?id=1294
#  Suma en rango
#  Enviar
#  Estado
#  Descripción
#    Se tiene una lista de números y te piden hallar la suma de todos los numeros que estan entre las posiciones a y b (incluidos a y b). Se sabe que la suma no excede un numero entero.
#   Entrada
#   Salida
#    Por cada caso de prueba escrita en una linea la suma de los números que están entre a y b inclusive.
#   Ejemplo Entrada
#    37 1 31 2 3 4 5 6 7 10 8 99 8 7 6 5 4 3 2 1 -55 0 0-1 -3 5 3 1
#   Ejemplo Salida
#    9-4-1
#   Ayuda
#    almacene los numeros en un vector para que sea mas facil calcular los rangos

for _ in range(int(input())):
    N,i,j = map(int,input().split())
    A = list(map(int,input().split()))
    print(sum(A[i:j+1]))