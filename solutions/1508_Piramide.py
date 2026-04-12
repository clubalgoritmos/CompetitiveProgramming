# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=3
## https://jv.umsa.bo/oj/problem.php?id=1508
#  Piramide
#  Estado
#  Descripción
#    Hallar la suma de la piramide de numeros.
#    $$ 2 ^ 0 $$
#    $$ 2 ^ 1, 2 ^ 1 $$
#    $$ 2 ^ 2, 2 ^ 2, 2 ^ 2 $$
#    $$ \ldots $$
#    $$ 2 ^n, 2 ^ n, 2 ^ n, \dots, 2 ^n, 2 ^ n, 2 ^ n $$
#   Entrada
#    La entrada contiene una o mas lineas de texto, cada linea contiene un numero positivo $(0 \leq n \leq 10^{12})$.
#   Salida
#    Imprimir la suma de la piramide modulo 1000000007.
#   Ejemplo Entrada
#    01234
#   Ejemplo Salida
#    151749129
#   Ayuda
MOD = 10**9 + 7

def piramides(n):
    suma = 1
    for i in range(1, n+1):
        suma = (suma + (2**i)*(i+1)) % MOD
    return suma

while True:
    try:
        n = int(input())
        print(piramides(n))
    except EOFError:
        break