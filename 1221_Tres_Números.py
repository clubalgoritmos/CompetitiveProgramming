# https://jv.umsa.bo/oj/problem.php?id=1221
#  Tres Números
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lee tres numeros enteros separados por un espacio y los imprima en una linea separados por un espacio en forma ordenada de menor a mayor.
#   Entrada
#    La entrada consiste de tres números enteros separados por un espacio.
#   Salida
#    La salida consiste de los números impresos de menor a mayor.
#   Ejemplo Entrada
#    3 1 2
#   Ejemplo Salida
#    1 2 3
#   Ayuda

print(*sorted(map(int,input().split())),)