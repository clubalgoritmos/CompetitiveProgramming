# https://jv.umsa.bo/oj/problem.php?id=1259
#  Logaritmos
#  Enviar
#  Estado
#  Descripción
#    Su tarea es escribir un programa que calcule logaritmos en diferentes bases.
#   Entrada
#    Cada caso de prueba consiste en un par de números naturales ($a \geq 2$, $n \geq 1$)
#    La entrada termina cuando no hay más datos
#   Salida
#    Para cada par de numeros $a$ y $n$ imprimir $log_{a}n$ (La parte entera)
#   Ejemplo Entrada
#    2 82 92 152 163 610 110 1010 10010 1000
#   Ejemplo Salida
#    333410123
#   Ayuda

import math
while True:
    try:
        a,n = map(int,input().split())
        print(math.floor(math.log(n,a)))
    except EOFError:x
        break