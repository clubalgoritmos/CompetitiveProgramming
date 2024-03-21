# https://jv.umsa.bo/oj/problem.php?id=1900
#  Series Reto 02
#  Enviar
#  Estado
#  Descripción
#    Se te pide que para un N dado generes las N elementos de la siguiente serie:
#    Se te pide que para un N dado generes las N elementos de la siguiente serie:
#    Se te pide que para un N dado generes las N elementos de la siguiente serie:
#    0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, 21, 21, 34...
#    0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, 21, 21, 34...
#    0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, 21, 21, 34...
#   Entrada
#    Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#    Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#    Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#   Salida
#    Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#    Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#    Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#   Ejemplo Entrada
#    410671
#   Ejemplo Salida
#    0 0 1 1 1 1 2 2 3 3 0 0 1 1 1 1 0 0 1 1 1 1 20
#   Ayuda
fibo = [0, 0, 1, 1, 1, 1]
def fibonacci(n):
    if n < len(fibo):
        return fibo[:n]
    fibo.append(fibo[-2]+fibo[-4])
    return fibonacci(n)

for _ in range(int(input())):
    print(*fibonacci(int(input())), end=" ")
    print()