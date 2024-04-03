# https://jv.umsa.bo/oj/problem.php?id=1225
#  Máximo de tres números
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea tres números enteros separados por un espacio e imprima el máximo.
#   Entrada
#    La entrada consiste de una linea con tres números enteros separados por un espacio.
#   Salida
#   Ejemplo Entrada
#    22 44 -10
#   Ejemplo Salida
#    44
#   Ayuda

a,b,c = map(int, input().split())
print(max(a,b,c))