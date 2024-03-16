# https://jv.umsa.bo/oj/problem.php?id=1300
#  Igual al Ultimo
#  Enviar
#  Estado
#  Descripción
#    Escribir un programa que lea una secuencia no vacía de números enteros, y imprime cuántosde ellos son iguales al último numero.
#   Entrada
#    La entrada consiste de múltiples secuencias. Cada secuencia comienza con un numero natural que indica la longitud de la secuencia. Termina cuando no hay más secuencias.
#   Salida
#    Imprima, para cada secuencia el numero de elementos igual al ultimo.
#   Ejemplo Entrada
#    102 2 1 1 3 5 3 5 3 3103 1 1 4 1 1 5 2 2 3105 5 2 2 4 2 2 5 2 5
#   Ejemplo Salida
#    424
#   Ayuda

while True:
    try:
        N = int(input())
        A = list(map(int,input().split()))
        print(A.count(A[-1]))
    except EOFError:
        break