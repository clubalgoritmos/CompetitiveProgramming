# https://jv.umsa.bo/oj/problem.php?id=1058
#  ordenando números
#  Enviar
#  Estado
#  Descripción
#    Te diré varios números, y quiero que los imprimas ordenados ascendentemente. (el menor se imprime primero, y el mayor se imprime último).
#   Entrada
#    En una línea, se te dará un número entero $1 \leq n \leq 50$ indicando la cantidad de casos de prueba. En la siguiente línea, se te dará un número entero $1 \leq a \leq 50$, indicando cuántos números existen en la lista de números que debes ``ordenar''.En la siguiente línea, y separados entre sí por un espacio, se te darán $a$ números enteros dentro del rango $[-10^3, 10^3]$
#   Salida
#    Por cada caso de entrada, debes imprimir una línea con los $a$ números enteros que se te dieron de entrada ordenados ascendentemente, imprime un espacio despues de cada numero y un salto de linea despues de imprimir todos los numeros con su respectivo espacio.
#   Ejemplo Entrada
#    3101 9 4 8 7 6 3 2 5 055 4 3 2 12100 1
#   Ejemplo Salida
#    0 1 2 3 4 5 6 7 8 91 2 3 4 51 100
#   Ayuda

for _ in range(int(input())):
    N = input()
    print(*sorted(map(int, input().split())))