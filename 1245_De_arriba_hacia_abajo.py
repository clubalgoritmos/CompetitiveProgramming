# Solucion
# https://jv.umsa.bo/oj/problem.php?id=1245
#  De arriba hacia abajo
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea dos números X y Y luego imprima todos los números desde el mayor hasta el menor de ambos.
#   Entrada
#    La entrada consiste en dos numero enteros X, Y.
#   Salida
#    En la salida escriba los números que se encuentran entre X y Y cada uno en una linea y en forma descendente.
#   Ejemplo Entrada
#    3 7
#   Ejemplo Salida
#    76543
#   Ayuda

A,B = map(int,input().split())
for i in range(max(A,B),min(A,B)-1,-1):
    print(i)