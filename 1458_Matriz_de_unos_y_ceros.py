# https://jv.umsa.bo/oj/problem.php?id=1458
#  Matriz de unos y ceros
#  Enviar
#  Estado
#  Descripción
#    El problema es sencillo, para un $N$ (tamaño de la matriz) generar una matriz de este tipo:
#    $10101$
#    $01010$
#    Esta sería la matriz para $N = 5$.
#   Entrada
#    Se le dará un único número $N$ ($1 \leq N \leq 1000$) el tamaño de la matriz.
#   Salida
#    Generar una matriz como la descrita en la entrada.
#   Ejemplo Entrada
#    5
#   Ejemplo Salida
#    1010101010101010101010101
#   Ayuda

N = int(input())
M = [[(i+j) & 1 for i in range(N)] for j in range(1,N+1)]

for v in M:
    print(*v, sep="")