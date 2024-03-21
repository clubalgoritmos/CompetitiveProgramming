# https://jv.umsa.bo/oj/problem.php?id=1432
## https://jv.umsa.bo/oj/problem.php?id=1432
#  K-sumatoria
#  Enviar
#  Estado
#  Descripción
#    Se te pide que cálcules la sumatoria de los primeros X múltiplos de K, módulo M.
#    Se te pide que cálcules la sumatoria de los primeros X múltiplos de K, módulo M.
#    Se te pide que cálcules la sumatoria de los primeros X múltiplos de K, módulo M.
#    Por ejemplo para $X = 3$, $K = 6$, $M = 1000$, los primeros $3$ multiplos de K son: $6$, $12$ y $18$ que suman $36$ modulo $1000$ es $36$
#    Por ejemplo para $X = 3$, $K = 6$, $M = 1000$, los primeros $3$ multiplos de K son:
#    Por ejemplo para $X = 3$, $K = 6$, $M = 1000$, los primeros $3$ multiplos de K son:
#    $6$, $12$ y $18$ que suman $36$ modulo $1000$ es $36$
#    $6$, $12$ y $18$ que suman $36$ modulo $1000$ es $36$
#   Entrada
#    Se te darán $3$ números X (1 <= X <= 10000), K (1 <= K <= 100) y M (1 <= M <= 1000).
#    Se te darán $3$ números X (1 <= X <= 10000), K (1 <= K <= 100) y M (1 <= M <= 1000).
#    Se te darán $3$ números X (1 <= X <= 10000), K (1 <= K <= 100) y M (1 <= M <= 1000).
#   Salida
#    Imprimir el resultado de la sumatoria módulo M.
#    Imprimir el resultado de la sumatoria módulo M.
#    Imprimir el resultado de la sumatoria módulo M.
#   Ejemplo Entrada
#    3 6 1000
#   Ejemplo Salida
#    36
#   Ayuda

X,K,M = map(int,input().split())
S = 0
for i in range(1,X+1):
    S+=(K*i%M)
print(S%M)