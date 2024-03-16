# https://jv.umsa.bo/oj/problem.php?id=1223
#  Suma de 3 números
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea tres números enteros separados por un espacio e imprima la suma.
#   Entrada
#    La entrada consiste de una linea con tres números enteros separados por un espacio.
#   Salida
#    La salida consiste de una línea con la suma de los tres números.
#   Ejemplo Entrada
#    22 44 -10
#   Ejemplo Salida
#    56
#   Ayuda

a,b,c = map(int, input().split())
print(a+b+c)