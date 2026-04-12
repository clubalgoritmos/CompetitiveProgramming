# https://jv.umsa.bo/oj/problem.php?id=1224
#  Maximo de dos números
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea dos números enteros separados por un espacio e imprima el mayor.
#   Entrada
#    La entrada consiste de una linea con dos números enteros separados por un espacio
#   Salida
#    La salida consiste de una línea que contiene el máximo de los números.
#   Ejemplo Entrada
#    22 44
#   Ejemplo Salida
#    44
#   Ayuda

a,b = map(int,input().split())
print(max(a,b))