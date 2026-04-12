# https://jv.umsa.bo/oj/problem.php?id=1901
## https://jv.umsa.bo/oj/problem.php?id=1901
#  Series Reto 03
#  Enviar
#  Estado
#  Descripción
#    Se te pide que para un N y K dados generes los N elementos de la siguiente serie:
#    Se te pide que para un N y K dados generes los N elementos de la siguiente serie:
#    Se te pide que para un N y K dados generes los N elementos de la siguiente serie:
#    Por ejemplo si N = 10 y K = 2
#    Por ejemplo si N = 10 y K = 2
#    Por ejemplo si N = 10 y K = 2
#    1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15
#    1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15
#    1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15
#   Entrada
#    La entrada consiste de T casos (1 <= T <= 100)
#    La entrada consiste de T casos (1 <= T <= 100)
#    La entrada consiste de T casos (1 <= T <= 100)
#    Por cada caso de prueba se te dara un N y K, (1 <= K <= N <= 1000)
#    Por cada caso de prueba se te dara un N y K, (1 <= K <= N <= 1000)
#    Por cada caso de prueba se te dara un N y K, (1 <= K <= N <= 1000)
#   Salida
#    Por cada caso de prueba debes imprimir N numeros, deacuerdo a K
#    Por cada caso de prueba debes imprimir N numeros, deacuerdo a K
#    Por cada caso de prueba debes imprimir N numeros, deacuerdo a K
#   Ejemplo Entrada
#    29 110 3
#   Ejemplo Salida
#    1 3 5 7 9 11 13 15 17 1 1 1 3 3 3 5 5 5 7
#   Ayuda
#    Si N = 10 y K = 3
#    Si N = 10 y K = 3
#    Si N = 10 y K = 3
#    Salida:
#    Salida:
#    Salida:
#    1 1 1 3 3 3 5 5 5 7
#    1 1 1 3 3 3 5 5 5 7
#    1 1 1 3 3 3 5 5 5 7

for _ in range(int(input())):
    N, K = map(int, input().split())
    count = 0
    i = 1
    while count < N:
        for _ in range(K):
            if count >= N:
                break
            print(i, end=" ")
            count += 1
        i += 2
    print()