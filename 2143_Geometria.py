# https://jv.umsa.bo/oj/problem.php?id=2143
#  Geometria
#  Enviar
#  Estado
#  Descripción
#    La tarea de
#    geometría
#    que le han dado un grafico y consiste en hallar la distancia de X.
#    Como la cantidad de ejercicios es muy larga tienes que hacer un programa para calcular X.
#    La entrada de datos consiste en la distancia de la rectas (a,b,c,d). Los ángulos marcados con 90 son rectos.
#   Entrada
#    La entrada consiste de un caso de prueba. Cada caso de prueba que contiene cuatro números enteros (a,b,c,d) menores a 10.000.
#   Salida
#    Por cada caso de prueba escriba una linea con el valor de X con 2 decimales.
#   Ejemplo Entrada
#    3 4 3 4
#   Ejemplo Salida
#    8.00
#   Ayuda
import math

a,b,c,d = map(int,input().split())
#A^2 = B^2 + Z^2
z = math.sqrt(abs(math.pow(a,2)-math.pow(b,2)))
x = math.sqrt(math.pow(c+z,2)+math.pow(d,2))
print(x)