# https://jv.umsa.bo/oj/problem.php?id=2538
#  La Plaza Murillo
#  Enviar
#  Estado
#  Descripción
#    La Plaza Murillo, en la ciudad de La Paz, tiene una forma rectangular con el tamaño de N×M metros. Con motivo del aniversario de la ciudad, se decidió pavimentar la Plaza con losas cuadradas de granito especial. Cada losa tiene el tamaño A × A.
#    ¿Cuál es el menor número de losas necesarias para pavimentar la plaza? Se permite cubrir una superficie más grande que la Plaza Murillo, pero la Plaza tiene que ser cubierta en su totalidad. No está permitido romper las losas. Los lados de las losas deben ser paralelos a los lados del Cuadrado.
#   Entrada
#    La entrada contiene tres números enteros positivos en la primera línea: N,M y A (1≤N,M,A≤109).
#   Salida
#    Escriba el número necesario de losas.
#   Ejemplo Entrada
#    6 6 4
#   Ejemplo Salida
#    4
#   Ayuda

from math import ceil
n, m, a = (int(x) for x in input().split(' '))
s = ceil(n/a) * ceil(m/a)
print(s)