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

# Suponiendo que se te dan las longitudes a, b, c, d
a,b,c,d = map(int,input().split())
# Calculando la longitud de X usando la ley del coseno
cosC = (a**2 + b**2 - c**2) / (2*a*b)
X = math.sqrt(c**2 + d**2 - 2*c*d*cosC)

print(f"{X:5}")
