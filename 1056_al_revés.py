# https://jv.umsa.bo/oj/problem.php?id=1056
#  al revés
#  Enviar
#  Estado
#  Descripción
#    Te diré una serie de números, y quiero que los imprimas al revés de como te los dije.
#   Entrada
#    En una línea, se te dará un número entero $1 \leq n \leq 10^5$ indicando la cantidad de casos de prueba. En la siguiente línea, se te dará un número entero $1 \leq a \leq 10^3$, indicando cuántos números existen en la lista de números que debes ``voltear''.En la siguiente línea, y separados entre sí por un espacio, se te darán $a$ números enteros dentro del rango $[-10^3, 10^3]$
#   Salida
#    Por cada caso de entrada, debes imprimir una línea con los $a$ números enteros que se te dieron de entrada, separados entre sí por un espacio, en el orden inverso en el que te fueron dados.
#   Ejemplo Entrada
#    351 3 2 5 7110068 3 0 1 -4 9
#   Ejemplo Salida
#    7 5 2 3 1 100 9 -4 1 0 3 8
#   Ayuda

for _ in range(int(input())):
    n = input()
    A = list(map(int,input().split()))
    A.reverse()
    for a in A:
        print(a,end=" ")
    print()