# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=15
## https://jv.umsa.bo/oj/problem.php?id=2237
#  SOLO EVALUA
#  Enviar
#  Estado
#  Descripción
#    Evaluar la siguiente sumatoria
#    $\sum_{i=0}^{n-1} \frac{i+k}{2+i+k}$
#   Entrada
#    La entrada contiene multiples casos, por cada linea se tiene dos enteros N,K donde $(1 \leq N \leq 100)$ y $(1 \leq K \leq 100)$
#   Salida
#    Por cada caso de prueba mostrar la parte entera de la suma total redondeada hacia arriba.
#   Ejemplo Entrada
#    10 42 1
#   Ejemplo Salida
#    81
#   Ayuda
#    4 / 6 = 0.66666666666666665 / 7 = 0.71428571428571436 / 8 = 0.757 / 9 = 0.77777777777777788 / 10 = 0.89 / 11 = 0.818181818181818210 / 12 = 0.833333333333333411 / 13 = 0.846153846153846112 / 14 = 0.857142857142857113 / 15 = 0.8666666666666667

    while True:
        try:
            N, K = map(int,input().split())
            print(int(sum((i+K)/(2+i+K) for i in range(N))+1))
        except EOFError:
            break