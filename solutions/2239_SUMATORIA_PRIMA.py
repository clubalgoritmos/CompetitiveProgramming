# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=9
## https://jv.umsa.bo/oj/problem.php?id=2239
#  SUMATORIA PRIMA
#  Enviar
#  Estado
#  Descripción
#    Evaluar la suma de los primeros N numeros primos:$S = 2 - 3 + 5 - 7 + 11 - 13 + 17 - ...$
#   Entrada
#    La entrada consiste de un entero $N$ $(1 \leq N \leq 1700)$ el numero de terminos a evaluar en la sumatoria.
#   Salida
#    Imprime la sumatoria S mostrada en el enunciado.
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    4
#   Ayuda

def next_prime(n):
    while True:
        n += 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            return n

N = int(input())
last = 2
S = last
for _ in range(1, N):
    last = next_prime(last)
    S += last * (-1)**_
print(S)