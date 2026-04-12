# https://jv.umsa.bo/oj/problem.php?id=1899
#  Series Reto 01
#  Enviar
#  Estado
#  Descripción
#    Se te pide que para un N dado generes las N elementos de la siguiente serie:
#    Se te pide que para un N dado generes las N elementos de la siguiente serie:
#    Se te pide que para un N dado generes las N elementos de la siguiente serie:
#    0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,...
#    0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,...
#    0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,...
#   Entrada
#    Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#    Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#    Se te dara un T (1 <= T <= 10) que son los numeros de casos, por cada caso se te dara un N (1 <= N <= 1000)
#   Salida
#    Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#    Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#    Por cada caso de prueba, tienes que escribir los N primeros numeros de la serie
#   Ejemplo Entrada
#    43541
#   Ejemplo Salida
#    0 0 1 0 0 1 1 2 0 0 1 1 0
#   Ayuda
#    Vea que al final de cada lpunea existe un espacio.

for _ in range(int(input())):
    for i in range(int(input())):
        print(i//2, end=" ")
    print()