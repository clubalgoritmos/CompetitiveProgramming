# https://jv.umsa.bo/oj/problem.php?id=2020
#  DULCE ANDREA
#  Enviar
#  Estado
#  Descripción
#   Entrada
#    La entrada contendra únicamente un número entero X (2 <= X <= 10^9)
#   Salida
#    La salida debe contener un número entero que representa las formas que tiene Andrea para comer sus X dulces
#   Ejemplo Entrada
#    12
#   Ejemplo Salida
#    6
#   Ayuda
import math

X = int(input())
contador = 0
i = 1
while i <= math.sqrt(X):
    if X % i == 0:
        if X / i == i:  # Si los factores son iguales, cuéntalos solo una vez
            contador += 1
        else:  # Si los factores son diferentes, cuéntalos dos veces
            contador += 2
    i += 1
print(contador)