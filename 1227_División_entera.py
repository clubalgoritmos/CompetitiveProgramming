# https://jv.umsa.bo/oj/problem.php?id=1227
#  División entera
#  Enviar
#  Estado
#  Descripción
#    Escribir un programa que lea dos números naturales a y b, con b > 0, e imprimir el cociente d y el resto r, de dividir a entre b.Recuerde que, por definición, d y r deben ser números enteros, tal que 0 <= r < b y d * b + r = a.
#   Entrada
#    La entrada consiste de dos números enteros a, b > 0.
#   Salida
#    Imprimir una línea con la división d entera y el resto r de a dividido por b, separados por una espacio.
#   Ejemplo Entrada
#    32 6
#   Ejemplo Salida
#    5 2
#   Ayuda

A, B = map(int,input().split())
print(A//B, A%B)